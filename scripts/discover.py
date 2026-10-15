"""在 GitHub 搜索可能值得收录的新项目，输出 Markdown 候选清单。
已收录（skills.toml）和已忽略（ignore.toml）的仓库会被排除。搜索关键词在 taxonomy.toml 的 [discover] 里。

用法：
  python3 scripts/discover.py                          # 近 30 天有更新、至少 5 星
  python3 scripts/discover.py --days 90 --min-stars 10
  python3 scripts/discover.py --out candidates.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
import urllib.parse

from lib import NotFound, gh_get, load_valid
from refresh import count_skills

SEARCH_INTERVAL = 2.5  # 搜索接口限额 30 次/分钟


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=30, help="只看最近 N 天内有推送的仓库（默认 30）")
    ap.add_argument("--min-stars", type=int, default=5, help="最低星数（默认 5）")
    ap.add_argument("--out", help="写入文件，默认打印到终端")
    args = ap.parse_args()

    taxonomy, skills, _, ignored = load_valid()
    known = {s["repo"].lower() for s in skills} | {i["repo"].lower() for i in ignored}
    since = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()

    found: dict[str, dict] = {}
    queries = taxonomy["discover"]["queries"]
    for i, q in enumerate(queries):
        if i:
            time.sleep(SEARCH_INTERVAL)
        params = urllib.parse.urlencode({
            "q": f"{q} pushed:>={since} stars:>={args.min_stars}",
            "sort": "stars",
            "per_page": 50,
        })
        items = gh_get(f"search/repositories?{params}")["items"]
        print(f"  {q}: {len(items)}", file=sys.stderr)
        for it in items:
            key = it["full_name"].lower()
            if key in known:
                continue
            entry = found.setdefault(key, {"repo": it, "queries": []})
            entry["queries"].append(q)

    rows = sorted(found.values(), key=lambda e: -e["repo"]["stargazers_count"])
    lines = [
        f"# 候选项目（{dt.date.today().isoformat()}）",
        "",
        f"近 {args.days} 天有更新、至少 {args.min_stars} 星，已排除收录和忽略的仓库，共 {len(rows)} 个。",
        "收录：把条目加进 `data/skills.toml`；不收：加进 `data/ignore.toml` 并写明原因。",
        "",
        "| 仓库 | ★ | 最近推送 | SKILL.md | 简介 | 命中关键词 |",
        "|---|--:|---|--:|---|---|",
    ]
    for e in rows:
        r = e["repo"]
        try:
            n, truncated = count_skills(r["full_name"], r["default_branch"])
            skill_md = f"{n}{'+' if truncated else ''}"
        except NotFound:
            skill_md = "?"
        desc = (r.get("description") or "").replace("|", "\\|").replace("\n", " ")[:120]
        lines.append(
            f"| [{r['full_name']}]({r['html_url']}) | {r['stargazers_count']} | {r['pushed_at'][:10]} "
            f"| {skill_md} | {desc} | {'、'.join(e['queries'])} |"
        )
    text = "\n".join(lines) + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"已写入 {args.out}：{len(rows)} 个候选。", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
