#!/usr/bin/env python3
"""scan-sessions — list local agent sessions without a board server."""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_LIB = Path(__file__).resolve().parents[2] / "_lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from ssfs_common import (  # noqa: E402
    GROK_SESSIONS,
    _UUID_RE,
    decode_cwd_from_folder,
    grok_user_spine,
    meaning_title,
    read_json,
)


def mtime_iso(p: Path) -> str:
    try:
        ts = p.stat().st_mtime
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except OSError:
        return "—"


def _looks_like_session_id(name: str) -> bool:
    # Grok native ids often uuid-shaped
    if _UUID_RE.match(name):
        return True
    # short hex / opaque id
    if len(name) >= 16 and all(c.isalnum() or c in "-_" for c in name):
        if not name.startswith("C%") and "%3A" not in name and "%5C" not in name:
            return True
    return False


def _is_session_dir(p: Path) -> bool:
    if not p.is_dir():
        return False
    if (p / "chat_history.jsonl").is_file():
        return True
    if (p / "summary.json").is_file() and (
        (p / "prompt_history.jsonl").is_file() or (p / "chat_history.jsonl").is_file()
    ):
        return True
    # uuid-like with any history
    if _looks_like_session_id(p.name) and (
        (p / "prompt_history.jsonl").is_file() or (p / "chat_history.jsonl").is_file()
    ):
        return True
    return False


def scan_grok(root: Path, limit: int, project: str | None) -> list[dict]:
    rows: list[dict] = []
    if not root.is_dir():
        return rows
    # Grok: ~/.grok/sessions/<encoded-cwd>/<session-id>/
    candidates: list[Path] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        # Prefer nested session ids under cwd folders
        nested = [sub for sub in child.iterdir() if sub.is_dir() and _is_session_dir(sub)]
        if nested:
            candidates.extend(nested)
            continue
        # Flat session dir at top (rare)
        if _is_session_dir(child) and _looks_like_session_id(child.name):
            candidates.append(child)
        # Do NOT treat encoded-cwd folders (C%3A%5C…) as sessions just because
        # they have a prompt_history.jsonl aggregate.

    def sort_key(p: Path) -> float:
        try:
            return p.stat().st_mtime
        except OSError:
            return 0.0

    candidates.sort(key=sort_key, reverse=True)

    for sess in candidates:
        summary = read_json(sess / "summary.json") if (sess / "summary.json").is_file() else {}
        hist = sess / "chat_history.jsonl"
        prompt = sess / "prompt_history.jsonl"
        spine = (
            grok_user_spine(hist if hist.is_file() else prompt)
            if (hist.is_file() or prompt.is_file())
            else []
        )
        title = meaning_title(sess, spine, summary)
        info = summary.get("info") or {}
        cwd = str(info.get("cwd") or "")
        if not cwd:
            cwd = decode_cwd_from_folder(sess.parent.name)
        if project:
            blob = f"{title} {cwd} {sess}".lower()
            if project.lower() not in blob:
                continue
        rows.append(
            {
                "agent": "grok",
                "title": title,
                "path": str(sess),
                "cwd": cwd,
                "mtime": mtime_iso(sess),
                "sid": str(info.get("id") or sess.name),
            }
        )
        if len(rows) >= limit:
            break
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description="SSFS scan-sessions")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--project", default=None, help="substring filter on title/cwd/path")
    ap.add_argument(
        "--root",
        default=str(GROK_SESSIONS),
        help="Grok sessions root (default: ~/.grok/sessions or SSFS_GROK_SESSIONS)",
    )
    args = ap.parse_args()
    root = Path(args.root).expanduser()
    rows = scan_grok(root, args.limit, args.project)
    print(f"# scan-sessions · {len(rows)} hit(s)")
    print(f"- **root:** `{root}`")
    print("")
    if not rows:
        print("_No sessions found. Set SSFS_GROK_SESSIONS if your root differs._")
        return 0
    for i, r in enumerate(rows, 1):
        print(f"## {i}. {r['title']}")
        print(f"- **agent:** {r['agent']}")
        print(f"- **sid:** `{r['sid']}`")
        print(f"- **cwd:** `{r['cwd'] or '—'}`")
        print(f"- **mtime:** {r['mtime']}")
        print(f"- **path:** `{r['path']}`")
        print("")
    print("_Titles are meaning-first when possible — not raw id slices._")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
