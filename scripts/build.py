"""根据 data/ 和 templates/ 生成 README.md 和 METHODS.md（按创作方法的完整索引）。

用法：
  python3 scripts/build.py              # 生成 README.md 和 METHODS.md
  python3 scripts/build.py --check      # 生成结果与数据不一致时以退出码 1 结束（CI 用）
  python3 scripts/build.py --validate   # 只校验数据
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys

from lib import ROOT, load_meta, load_valid

README = ROOT / "README.md"
METHODS = ROOT / "METHODS.md"
TEMPLATES = ROOT / "templates"
STALE_DAYS = 180
NEW_DAYS = 7        # 「本周新增」：first_seen 在 fetched_at 前 NEW_DAYS 天以内

FORMAT_BADGE = {"prompts": "📝 提示词", "harness": "⚙️ 框架", "app": "🧩 应用", "research": "🎓 研究"}
LANG_LABEL = {"zh": "中文", "en": "英文", "ja": "日文", "ko": "韩文", "multi": "多语言"}
# 方法索引里，每个方法下按形态分三行
FORMAT_FAMILIES = (("skill · 提示词", {"skill", "prompts"}), ("框架 · 应用", {"harness", "app"}), ("研究代码", {"research"}))


def gh_url(repo: str) -> str:
    return f"https://github.com/{repo}"


def display_name(s: dict) -> str:
    return s.get("name") or s["repo"].split("/", 1)[1]


def fmt_stars(n: int | None) -> str:
    if n is None:
        return "—"
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def sort_key(s: dict, meta: dict):
    stars = meta.get(s["repo"], {}).get("stars", -1)
    return (s.get("tier") != "featured", -stars, display_name(s).lower())


def status_mark(m: dict, ref: dt.date | None) -> str:
    if m.get("status") == "missing":
        return " ⚠️"
    if m.get("archived"):
        return " 📦"
    if ref and m.get("pushed_at") and (ref - dt.date.fromisoformat(m["pushed_at"])).days > STALE_DAYS:
        return " 💤"
    return ""


def name_line(s: dict, m: dict, ref: dt.date | None) -> str:
    star = "🌟 " if s.get("tier") == "featured" else ""
    return f"{star}**[{display_name(s)}]({gh_url(s['repo'])})** · ★ {fmt_stars(m.get('stars'))}"


def meta_line(s: dict, m: dict, ref: dt.date | None) -> str:
    sub = [f"更新于 {m.get('pushed_at') or '—'}{status_mark(m, ref)}"]
    if s["format"] in FORMAT_BADGE:
        sub.append(FORMAT_BADGE[s["format"]])
    sub.append(LANG_LABEL[s["lang"]])
    if m.get("skill_count", 0) > 1:
        sub.append(f"{m['skill_count']}{'+' if m.get('skill_count_truncated') else ''} 个 skill")
    if m.get("license"):
        sub.append(m["license"])
    return " · ".join(sub)


def desc_block(s: dict, method_text: str, meta: str) -> str:
    text = cell(s["desc"]) + f"<br><sub>方法：{method_text}</sub><br><sub>{meta}</sub>"
    if s.get("note"):
        text += f"<br><sub>💡 {cell(s['note'])}</sub>"
    return text


def install_cmd(s: dict) -> str | None:
    if s.get("install"):
        return s["install"]
    if s["format"] == "skill":
        return f"npx skills add {s['repo']}"
    return None


def by_stars(items, meta: dict) -> list[dict]:
    return sorted(items, key=lambda s: -meta.get(s["repo"], {}).get("stars", -1))


def render_packs(packs: list[dict], by_repo: dict) -> list[str]:
    out = [
        '<a id="packs"></a>',
        "## 推荐组合",
        "",
        "> 初版组合依据仓库说明搭配，尚未实测，实测后会更新。",
        "",
    ]
    for p in packs:
        links = " → ".join(
            f"[{display_name(by_repo[r.lower()])}]({gh_url(by_repo[r.lower()]['repo'])})" for r in p["repos"]
        )
        out += [f"- **{p['name']}**：{p['goal']}", f"  - 组合：{links}", f"  - 思路：{p['why']}"]
    return out + [""]


def render_group(key: str, group: dict, items: list[dict], meta: dict, ref: dt.date | None, taxonomy: dict) -> list[str]:
    methods = taxonomy["methods"]
    out = [f'<a id="group-{key}"></a>', f"### {group['label']}", ""]
    if group.get("intro"):
        out += [group["intro"], ""]
    families = [(name, [s for s in items if s["format"] in formats]) for name, formats in FORMAT_FAMILIES]
    families = [(name, fam) for name, fam in families if fam]
    for name, fam in families:
        if len(families) > 1:
            out += [f"#### {name}（{len(fam)}）", ""]
        for s in fam:
            m = meta.get(s["repo"], {})
            method_text = " · ".join(mt["short"] for k, mt in methods.items() if k in s["methods"])
            out += [f"- {name_line(s, m, ref)}<br>{desc_block(s, method_text, meta_line(s, m, ref))}", ""]

    cmds = [(display_name(s), install_cmd(s)) for s in items if install_cmd(s)]
    if cmds:
        out += ["", "<details><summary>安装命令</summary>", "", "```bash",
                "# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准"]
        for name, cmd in cmds:
            out += [f"# {name}", cmd]
        out += ["```", "", "</details>"]
    return out + [""]


def new_entries(skills: list[dict], meta: dict, ref: dt.date | None) -> list[dict]:
    if ref is None:
        return []
    def age(s):
        seen = meta.get(s["repo"], {}).get("first_seen")
        return (ref - dt.date.fromisoformat(seen)).days if seen else None
    hits = [s for s in skills if (a := age(s)) is not None and 0 <= a < NEW_DAYS]
    return sorted(hits, key=lambda s: (age(s), -meta.get(s["repo"], {}).get("stars", -1)))


def render_new(items: list[dict], meta: dict) -> list[str]:
    out = ['<a id="new"></a>', "## 本周新增", ""]
    if not items:
        return out + ["本周暂无新增。发现好项目欢迎[推荐](../../issues/new?template=submit-skill.yml)。", ""]
    out += [f"近 {NEW_DAYS} 天新收录 {len(items)} 个：", ""]
    for s in items:
        stars = meta.get(s["repo"], {}).get("stars")
        star = f" ★{fmt_stars(stars)}" if stars is not None else ""
        out.append(f"- [{display_name(s)}]({gh_url(s['repo'])}){star}：{cell(s['desc'])}")
    return out + [""]


def render_featured(items: list[dict], groups: dict, meta: dict) -> list[str]:
    if not items:
        return []
    out = ['<a id="featured"></a>', "## 精选：从这里开始", "",
           "每种故事类型里方法最扎实、最有代表性的项目，第一次来可以先看这些。", ""]
    for s in items:
        stars = meta.get(s["repo"], {}).get("stars")
        star = f" ★{fmt_stars(stars)}" if stars is not None else ""
        out.append(f"- [{display_name(s)}]({gh_url(s['repo'])}){star} · {groups[s['group']]['label']}：{cell(s['desc'])}")
    return out + [""]


def links(items) -> str:
    return " · ".join(f"[{display_name(s)}]({gh_url(s['repo'])})" for s in items)


def render_index(anchor: str, title: str, intro: str, labels: dict[str, str], field: str,
                 skills: list[dict], meta: dict, split: bool = False) -> list[str]:
    """split=True 时每项按形态拆成 skill · 提示词 / 框架 · 应用 / 研究代码三行。"""
    out = [f'<a id="{anchor}"></a>', f"## {title}", "", intro, ""]
    for key, label in labels.items():
        hits = by_stars((s for s in skills if key in s.get(field, [])), meta)
        if not hits:
            continue
        out.append(f'<a id="method-{key}"></a>')
        if not split:
            out += [f"**{label}**（{len(hits)}）：{links(hits)}", ""]
            continue
        out += [f"**{label}**（{len(hits)}）", ""]
        for name, formats in FORMAT_FAMILIES:
            items = [s for s in hits if s["format"] in formats]
            if items:
                out.append(f"- {name}（{len(items)}）：{links(items)}")
        out += [""]
    return out


def render(taxonomy: dict, skills: list[dict], packs: list[dict], meta_all: dict) -> str:
    meta = meta_all.get("repos", {})
    ref = dt.date.fromisoformat(meta_all["fetched_at"]) if meta_all.get("fetched_at") else None
    groups = taxonomy["groups"]
    by_repo = {s["repo"].lower(): s for s in skills}
    grouped = {k: sorted((s for s in skills if s["group"] == k), key=lambda s: sort_key(s, meta)) for k in groups}
    indexed = [s for s in skills if groups[s["group"]].get("indexed", True)]

    header = (TEMPLATES / "header.md").read_text(encoding="utf-8")
    header = (header.replace("{{count}}", str(len(indexed)))
                    .replace("{{skills}}", str(sum(s["format"] in ("skill", "prompts") for s in skills)))
                    .replace("{{tools}}", str(sum(s["format"] in ("harness", "app") for s in skills)))
                    .replace("{{research}}", str(sum(s["format"] == "research" for s in skills)))
                    .replace("{{updated}}", meta_all.get("fetched_at") or "—"))

    new = new_entries(skills, meta, ref)
    featured = [s for k in groups for s in grouped[k] if s.get("tier") == "featured"]
    toc = ["## 目录", "", f"- [本周新增](#new)（{len(new)}）"]
    toc += [f"- [精选：从这里开始](#featured)（{len(featured)}）"] if featured else []
    toc += ["- [推荐组合](#packs)"] if packs else []
    toc += ["- [按故事类型](#by-group)"]
    toc += [f"  - [{g['label']}](#group-{k})（{len(grouped[k])}）" for k, g in groups.items() if grouped[k]]
    toc += ["- [按创作方法查找](#by-method)", "- [相关资源](#resources)", "- [收录徽章](#badge)", ""]

    body = ['<a id="by-group"></a>', "## 按故事类型", ""]
    for k, g in groups.items():
        if grouped[k]:
            body += render_group(k, g, grouped[k], meta, ref, taxonomy)

    # 方法索引篇幅大，单独生成 METHODS.md，README 只放各方法的入口
    method_labels = {k: mt["label"] for k, mt in taxonomy["methods"].items()}
    method_links = ['<a id="by-method"></a>', "## 按创作方法查找", "",
                    f"同一种方法在不同项目里怎么落地，完整索引见 [{METHODS.name}]({METHODS.name})：", ""]
    for k, label in method_labels.items():
        n = sum(k in s["methods"] for s in indexed)
        if n:
            method_links.append(f"- [{label}]({METHODS.name}#method-{k})（{n}）")
    gen_note = "<!-- 本文件由 scripts/build.py 生成，请勿手改。要改内容请编辑 data/ 或 templates/ 后重新生成。 -->"
    readme = [
        gen_note,
        "",
        header.rstrip(),
        "",
        *toc,
        *render_new(new, meta),
        *render_featured(featured, groups, meta),
        *(render_packs(packs, by_repo) if packs else []),
        *body,
        *method_links,
        "",
        (TEMPLATES / "footer.md").read_text(encoding="utf-8").rstrip(),
        "",
    ]
    index = render_index("by-method", "按创作方法查找",
                         "同一种方法在不同项目里怎么落地：每个方法下按 skill、框架和应用、研究代码分开，各自按星数排序。"
                         "项目简介见 [README](README.md)。",
                         method_labels, "methods", indexed, meta, split=True)
    methods = [gen_note, "", *index]
    return "\n".join(readme), "\n".join(methods).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="只检查 README.md 是否最新")
    ap.add_argument("--validate", action="store_true", help="只校验数据")
    args = ap.parse_args()

    taxonomy, skills, packs, _ = load_valid()
    if args.validate:
        print(f"数据校验通过：{len(skills)} 个项目，{len(packs)} 个组合。")
        return

    meta_all = load_meta()
    unfetched = [s["repo"] for s in skills if s["repo"] not in meta_all.get("repos", {})]
    if unfetched:
        print(f"提示：{len(unfetched)} 个仓库还没有元数据，先运行 scripts/refresh.py --only {' '.join(unfetched)}",
              file=sys.stderr)

    outputs = dict(zip((README, METHODS), render(taxonomy, skills, packs, meta_all)))
    if args.check:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            sys.exit(f"{'、'.join(stale)} 不是最新的，请运行 python3 scripts/build.py")
        print("README.md 和 METHODS.md 已是最新。")
        return
    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
    print(f"已生成 README.md 和 METHODS.md：{len(skills)} 个项目。")


if __name__ == "__main__":
    main()
