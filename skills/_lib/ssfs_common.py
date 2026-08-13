"""Shared helpers for SSFS skill CLIs. Portable; no suite host required."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Iterator

# Generic env overrides — never bake a personal home into the pack.
GROK_SESSIONS = Path(
    os.environ.get("SSFS_GROK_SESSIONS")
    or os.environ.get("GROK_SESSIONS")
    or (Path.home() / ".grok" / "sessions")
)
JWRANGLE_DAYS = Path(
    os.environ.get("SSFS_JWRANGLE_DAYS")
    or os.environ.get("JWRANGLE_DAYS")
    or (Path.home() / "jwrangle" / "days")
)
DURABLE_ROOT = Path(
    os.environ.get("SSFS_DURABLE_ROOT")
    or (Path.home() / "jwrangle" / "durable-archive" / "lands")
)
CAPTURE_INBOX = Path(
    os.environ.get("SSFS_CAPTURE_INBOX")
    or (Path.home() / "test-write")
)

_PATH_RE = re.compile(
    r"(?P<p>(?:[A-Za-z]:\\|\\\\|~/|\./|\.\./|/)"
    r"[^\s\"'<>|*?]{3,220})"
)
_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.I,
)


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return {}


def iter_jsonl(path: Path, limit: int = 5000) -> Iterator[dict[str, Any]]:
    if not path.is_file():
        return
    n = 0
    try:
        with path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue
                n += 1
                if n >= limit:
                    break
    except OSError:
        return


def clip(s: str, n: int = 160) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    if len(s) <= n:
        return s
    return s[: n - 1] + "…"


def session_dir_for(path: Path) -> Path:
    p = path.resolve()
    if p.is_file():
        # Grok: chat_history.jsonl lives in session dir
        if p.name in (
            "chat_history.jsonl",
            "prompt_history.jsonl",
            "summary.json",
            "plan.md",
        ):
            return p.parent
        return p.parent
    return p


def grok_user_spine(hist: Path, max_items: int = 24) -> list[str]:
    spine: list[str] = []
    for row in iter_jsonl(hist, limit=8000):
        role = (row.get("role") or row.get("type") or "").lower()
        if role not in ("user", "human"):
            # Grok sometimes nests
            msg = row.get("message") or {}
            role = (msg.get("role") or "").lower()
            content = msg.get("content") if isinstance(msg, dict) else None
        else:
            content = row.get("content")
        if role not in ("user", "human"):
            continue
        text = _content_to_text(content if content is not None else row.get("content"))
        if not text:
            continue
        if text.startswith("<system") or text.startswith("System:"):
            continue
        # weak session plumbing
        if text.strip() in ("/clear", "/resume", "/add-dir") or text.startswith(
            "/add-dir"
        ):
            continue
        spine.append(clip(text, 200))
        if len(spine) >= max_items:
            break
    return spine


def _content_to_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(str(block.get("text") or ""))
                elif "text" in block:
                    parts.append(str(block.get("text") or ""))
        return "\n".join(parts).strip()
    if isinstance(content, dict):
        return str(content.get("text") or content.get("content") or "").strip()
    return str(content).strip()


def paths_from_text_blobs(paths: list[str], text: str) -> None:
    for m in _PATH_RE.finditer(text or ""):
        p = m.group("p").rstrip(".,);:]}")
        if len(p) < 4:
            continue
        if p not in paths:
            paths.append(p)
        if len(paths) >= 40:
            return


def paths_from_hunks(sess: Path) -> list[str]:
    out: list[str] = []
    hunk = sess / "hunk_records.jsonl"
    for row in iter_jsonl(hunk, limit=2000):
        for key in ("path", "file", "filepath", "target"):
            v = row.get(key)
            if isinstance(v, str) and v and v not in out:
                out.append(v)
        if len(out) >= 40:
            break
    return out


def meaning_title(sess: Path, spine: list[str], summary: dict[str, Any]) -> str:
    for key in ("generated_title", "session_summary", "title", "summary"):
        v = summary.get(key)
        if isinstance(v, str) and v.strip() and not _UUID_RE.match(v.strip()):
            return clip(v.strip(), 120)
    info = summary.get("info") or {}
    if isinstance(info, dict):
        for key in ("title", "name"):
            v = info.get(key)
            if isinstance(v, str) and v.strip() and not _UUID_RE.match(v.strip()):
                return clip(v.strip(), 120)
    # first substantive user line
    for line in spine:
        if len(line) > 12 and not line.startswith("/"):
            return clip(line, 120)
    if spine:
        return clip(spine[0], 120)
    name = sess.name
    if _UUID_RE.match(name) or len(name) > 20:
        return f"session · {name[:8]}… (no prompt yet)"
    return name


def decode_cwd_from_folder(name: str) -> str:
    # Grok encodes cwd as C%3A%5CUsers%5C...
    try:
        from urllib.parse import unquote

        return unquote(name).replace("/", "\\") if "%3" in name or "%5" in name else name
    except Exception:
        return name
