"""抓取收录仓库的 GitHub 元数据写入 data/meta.json，并报告改名、失效、归档和久未更新的项目。

用法：
  python3 scripts/refresh.py                  # 刷新全部
  python3 scripts/refresh.py --only a/b c/d   # 只刷新指定仓库（新增条目时用）
  python3 scripts/refresh.py --fix-renames    # 仓库改名时，同步改写 data/*.toml 里的旧名字
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys

from lib import DATA, NotFound, gh_get, has_token, load_meta, load_valid, save_meta

STALE_DAYS = 180


def count_skills(full_name: str, branch: str) -> tuple[int, bool]:
    """统计仓库里的 SKILL.md。同名 skill 的多份副本只算一次。"""
    try:
        tree = gh_get(f"repos/{full_name}/git/trees/{branch}?recursive=1")
    except NotFound:  # 空仓库
        return 0, False
    names = set()
    for item in tree.get("tree", []):
        path = item["path"]
        if item["type"] == "blob" and path.rsplit("/", 1)[-1].lower() == "skill.md":
            parent = path.rsplit("/", 1)[0] if "/" in path else ""
            names.add(parent.rsplit("/", 1)[-1])
    return len(names), bool(tree.get("truncated"))


def fetch(repo: str) -> dict:
    info = gh_get(f"repos/{repo}")
    n, truncated = count_skills(info["full_name"], info["default_branch"])
    license_id = (info.get("license") or {}).get("spdx_id")
    return {
        "full_name": info["full_name"],
        "stars": info["stargazers_count"],
        "forks": info["forks_count"],
        "pushed_at": info["pushed_at"][:10],
        "license": None if license_id in (None, "NOASSERTION") else license_id,
        "archived": info["archived"],
        "description": info.get("description") or "",
        "skill_count": n,
        "skill_count_truncated": truncated,
        "status": "ok",
    }


def fix_renames(pairs: list[tuple[str, str]], meta: dict) -> None:
    for name in ("skills.toml", "packs.toml"):
        path = DATA / name
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            text = text.replace(f'"{old}"', f'"{new}"')
        path.write_text(text, encoding="utf-8")
    for old, new in pairs:
        meta["repos"][new] = meta["repos"].pop(old)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="+", metavar="OWNER/REPO", help="只刷新这些仓库")
    ap.add_argument("--fix-renames", action="store_true", help="把改名后的新仓库名写回 data/*.toml")
    args = ap.parse_args()

    _, skills, _, _ = load_valid()
    meta = load_meta()
    repos = [s["repo"] for s in skills]

    if args.only:
        wanted = {r.lower() for r in args.only}
        unknown = wanted - {r.lower() for r in repos}
        if unknown:
            sys.exit(f"不在 skills.toml 里：{', '.join(sorted(unknown))}")
        repos = [r for r in repos if r.lower() in wanted]
    else:
        # 删除已从 skills.toml 移除的条目
        meta["repos"] = {k: v for k, v in meta["repos"].items() if k in repos}

    if not has_token():
        print("提示：未检测到 GITHUB_TOKEN 或 gh 登录，匿名配额每小时 60 次。", file=sys.stderr)

    today = dt.date.today()
    renamed, missing, archived, stale = [], [], [], []

    for repo in repos:
        try:
            m = fetch(repo)
        except NotFound:
            meta["repos"][repo] = {**meta["repos"].get(repo, {}), "status": "missing"}
            missing.append(repo)
            print(f"  ✗ {repo}  失效（404）")
            continue
        # first_seen：第一次抓到这个仓库的日期，用于「本周新增」；首批种子数据没有这个字段
        prev = meta["repos"].get(repo)
        first_seen = prev.get("first_seen") if prev is not None else today.isoformat()
        if first_seen:
            m["first_seen"] = first_seen
        meta["repos"][repo] = m
        print(f"  ✓ {repo}  ★{m['stars']}  skills:{m['skill_count']}  {m['pushed_at']}")

        if m["full_name"] != repo:
            renamed.append((repo, m["full_name"]))
        if m["archived"]:
            archived.append(repo)
        if (today - dt.date.fromisoformat(m["pushed_at"])).days > STALE_DAYS:
            stale.append(f"{repo}（{m['pushed_at']}）")

    if args.fix_renames and renamed:
        fix_renames(renamed, meta)

    if not args.only or not meta.get("fetched_at"):
        meta["fetched_at"] = today.isoformat()
    save_meta(meta)

    print(f"\n已刷新 {len(repos)} 个仓库 → {DATA / 'meta.json'}")
    report = [
        ("改名", [f"{a} → {b}" for a, b in renamed],
         "已同步改写 data/*.toml" if args.fix_renames else "加 --fix-renames 可自动改写 data/*.toml"),
        ("失效", missing, "确认后从 skills.toml 移除，或移到 ignore.toml"),
        ("已归档", archived, "考虑降级或移除"),
        (f"超过 {STALE_DAYS} 天未更新", stale, "README 中会标 💤"),
    ]
    for title, items, hint in report:
        if items:
            print(f"\n{title}（{len(items)}）— {hint}")
            for it in items:
                print(f"  - {it}")


if __name__ == "__main__":
    main()
