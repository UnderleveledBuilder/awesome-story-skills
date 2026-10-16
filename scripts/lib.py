"""数据加载、校验和 GitHub API 访问。只依赖标准库（Python 3.11+）。"""

from __future__ import annotations

import datetime as dt
import http.client
import json
import os
import re
import subprocess
import sys
import time
import tomllib
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
META_PATH = DATA / "meta.json"

REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SKILL_FIELDS = {
    "required": {"repo", "desc", "group", "methods", "format", "lang"},
    "optional": {"name", "agents", "install", "tier", "note", "checked", "desc_en", "note_en"},
}
TIERS = {"featured", "listed"}
DESC_MAX = 80
DESC_EN_MAX = 260


def load_toml(name: str) -> dict:
    with open(DATA / name, "rb") as f:
        return tomllib.load(f)


def load_meta() -> dict:
    if not META_PATH.exists():
        return {"fetched_at": None, "repos": {}}
    return json.loads(META_PATH.read_text(encoding="utf-8"))


def save_meta(meta: dict) -> None:
    META_PATH.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def load_all() -> tuple[dict, list[dict], list[dict], list[dict]]:
    taxonomy = load_toml("taxonomy.toml")
    skills = load_toml("skills.toml").get("skills", [])
    packs = load_toml("packs.toml").get("packs", [])
    ignored = load_toml("ignore.toml").get("ignored", [])
    return taxonomy, skills, packs, ignored


def validate(taxonomy: dict, skills: list[dict], packs: list[dict], ignored: list[dict]) -> list[str]:
    errors: list[str] = []
    seen: dict[str, int] = {}
    allowed = SKILL_FIELDS["required"] | SKILL_FIELDS["optional"]

    for i, s in enumerate(skills, 1):
        where = f"skills.toml 第 {i} 条（{s.get('repo', '?')}）"
        missing = SKILL_FIELDS["required"] - s.keys()
        if missing:
            errors.append(f"{where}: 缺少字段 {sorted(missing)}")
        unknown = s.keys() - allowed
        if unknown:
            errors.append(f"{where}: 未知字段 {sorted(unknown)}")

        repo = s.get("repo", "")
        if not REPO_RE.match(repo):
            errors.append(f"{where}: repo 应为 owner/name 格式")
        key = repo.lower()
        if key in seen:
            errors.append(f"{where}: 与第 {seen[key]} 条重复")
        seen[key] = i

        if len(s.get("desc", "")) > DESC_MAX:
            errors.append(f"{where}: desc 超过 {DESC_MAX} 字（当前 {len(s['desc'])}）")
        if len(s.get("desc_en", "")) > DESC_EN_MAX:
            errors.append(f"{where}: desc_en 超过 {DESC_EN_MAX} 个字符（当前 {len(s['desc_en'])}）")
        if s.get("group") not in taxonomy["groups"]:
            errors.append(f"{where}: group '{s.get('group')}' 不在 taxonomy.groups 里")
        methods = s.get("methods", [])
        if not methods:
            errors.append(f"{where}: methods 不能为空")
        for mt in methods:
            if mt not in taxonomy["methods"]:
                errors.append(f"{where}: method '{mt}' 不在 taxonomy.methods 里")
        if s.get("format") not in taxonomy["formats"]:
            errors.append(f"{where}: format '{s.get('format')}' 不在 taxonomy.formats 里")
        if s.get("lang") not in taxonomy["langs"]:
            errors.append(f"{where}: lang '{s.get('lang')}' 不在 taxonomy.langs 里")
        for ag in s.get("agents", []):
            if ag not in taxonomy["agents"]:
                errors.append(f"{where}: agent '{ag}' 不在 taxonomy.agents 里")
        if s.get("tier", "listed") not in TIERS:
            errors.append(f"{where}: tier 只能是 {sorted(TIERS)}")
        if "checked" in s and not isinstance(s["checked"], dt.date):
            errors.append(f"{where}: checked 应写成 TOML 日期，如 2026-10-12（不加引号）")

    for p in packs:
        for repo in p.get("repos", []):
            if repo.lower() not in seen:
                errors.append(f"packs.toml「{p.get('name')}」: {repo} 未在 skills.toml 收录")

    for ig in ignored:
        if ig.get("repo", "").lower() in seen:
            errors.append(f"ignore.toml: {ig['repo']} 同时出现在 skills.toml 里")
        if not ig.get("reason"):
            errors.append(f"ignore.toml: {ig.get('repo')} 缺少 reason")

    return errors


def load_valid() -> tuple[dict, list[dict], list[dict], list[dict]]:
    data = load_all()
    errors = validate(*data)
    if errors:
        print("数据校验失败：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    return data


# ───────────────────────── GitHub API ─────────────────────────

class NotFound(Exception):
    pass


def github_token() -> str | None:
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


_TOKEN = github_token()


def gh_get(path: str) -> dict:
    url = path if path.startswith("https://") else f"https://api.github.com/{path.lstrip('/')}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-story-skills",
        **({"Authorization": f"Bearer {_TOKEN}"} if _TOKEN else {}),
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (404, 409, 451):  # 409：空仓库没有 git tree
                raise NotFound(path) from e
            if e.code == 403 and e.headers.get("X-RateLimit-Remaining") == "0":
                reset = dt.datetime.fromtimestamp(int(e.headers.get("X-RateLimit-Reset", "0")))
                sys.exit(f"GitHub API 配额用完，{reset:%H:%M} 重置。设置 GITHUB_TOKEN 或登录 gh 可提高配额。")
            if e.code < 500 or attempt == 2:
                raise
        except (OSError, http.client.HTTPException):
            # 网络抖动（SSL 断开、超时、响应体没读完）：几百个仓库刷一遍时难免遇到，重试两次
            if attempt == 2:
                raise
        time.sleep(2 * (attempt + 1))


def has_token() -> bool:
    return _TOKEN is not None
