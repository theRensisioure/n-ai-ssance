#!/usr/bin/env python3
"""session-map CLI — map, not chat dump. Exit 0 prints markdown map to stdout."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# pack-local lib
_LIB = Path(__file__).resolve().parents[2] / "_lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from ssfs_common import (  # noqa: E402
    clip,
    grok_user_spine,
    meaning_title,
    paths_from_hunks,
    paths_from_text_blobs,
    read_json,
    session_dir_for,
)


def build_map(raw: str) -> tuple[bool, str]:
    p = Path(raw).expanduser()
    if not p.exists():
        return False, f"error: not found: {p}"
    sess = session_dir_for(p)
    hist = sess / "chat_history.jsonl"
    prompt = sess / "prompt_history.jsonl"
    summary = read_json(sess / "summary.json") if (sess / "summary.json").is_file() else {}

    spine: list[str] = []
    if hist.is_file():
        spine = grok_user_spine(hist)
    elif prompt.is_file():
        # prompt_history is often user-only lines
        spine = grok_user_spine(prompt)

    if not hist.is_file() and not prompt.is_file() and not summary:
        # accept synthetic fixture dir
        spine_md = sess / "spine.md"
        if spine_md.is_file():
            spine = [
                ln.lstrip("0123456789. ").strip()
                for ln in spine_md.read_text(encoding="utf-8", errors="replace").splitlines()
                if ln.strip() and not ln.startswith("#")
            ]
        title_f = sess / "summary-line.txt"
        title = (
            title_f.read_text(encoding="utf-8", errors="replace").strip()
            if title_f.is_file()
            else meaning_title(sess, spine, summary)
        )
        paths: list[str] = []
        pf = sess / "paths.txt"
        if pf.is_file():
            paths = [
                ln.strip()
                for ln in pf.read_text(encoding="utf-8", errors="replace").splitlines()
                if ln.strip()
            ]
        agent = "synthetic"
        sid = sess.name
        cwd = ""
        msgs = len(spine)
        model = "—"
        source = "fixture"
    elif hist.is_file() or prompt.is_file() or summary:
        info = summary.get("info") or {}
        sid = str(info.get("id") or sess.name)
        cwd = str(info.get("cwd") or "")
        title = meaning_title(sess, spine, summary)
        msgs = int(summary.get("num_chat_messages") or summary.get("num_messages") or 0) or len(
            spine
        )
        model = str(summary.get("current_model_id") or summary.get("agent_name") or "—")
        agent = "grok"
        source = "grok"
        paths = paths_from_hunks(sess)
        if not paths and hist.is_file():
            # light path harvest from spine only (not full dump)
            for s in spine:
                paths_from_text_blobs(paths, s)
    else:
        return False, f"error: not a session-shaped path: {p}"

    last_asks = spine[-2:] if spine else []
    relay_bits = [title]
    if last_asks:
        relay_bits.append("Last: " + " · ".join(clip(a, 100) for a in last_asks))
    if cwd:
        relay_bits.append("cwd: " + cwd)
    relay = " — ".join(relay_bits)

    lines = [
        f"# Session map · {title}",
        "",
        f"- **agent:** {agent}",
        f"- **sid:** `{sid}`",
        f"- **cwd:** `{cwd or '—'}`",
        f"- **msgs (approx):** {msgs}",
        f"- **model:** {model}",
        f"- **source:** {source}",
        "",
        "## Relay (copy-ready)",
        "",
        relay,
        "",
        "## User spine",
        "",
    ]
    if spine:
        for s in spine:
            lines.append(f"- {s}")
    else:
        lines.append("- (no clear user turns extracted)")

    lines.extend(["", "## Paths touched", ""])
    if paths:
        for fp in paths[:40]:
            lines.append(f"- `{fp}`")
    else:
        lines.append("- (none found — chat-only or metadata missing)")

    raw_hint = str(hist if hist.is_file() else (prompt if prompt.is_file() else sess))
    lines.extend(
        [
            "",
            "## Find / open",
            "",
            f"- **session root:** `{sess}`",
            f"- **raw transcript (do not open unless you must):** `{raw_hint}`",
            "",
            "## Contract",
            "",
            "This is a **map**, not a chat dump. Full transcript stays on disk.",
            "",
        ]
    )
    # intent packet if present
    intent_md = sess / "intent" / "interview.md"
    if intent_md.is_file():
        lines.extend(["## Intent packet", "", f"- present: `{intent_md}`", ""])
        try:
            body = intent_md.read_text(encoding="utf-8", errors="replace").strip().splitlines()
            for ln in body[:30]:
                lines.append(ln)
            lines.append("")
        except OSError:
            pass

    return True, "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="SSFS session-map — map, not chat dump")
    ap.add_argument("path", help="session directory or chat_history/prompt_history path")
    args = ap.parse_args()
    ok, out = build_map(args.path)
    print(out)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
