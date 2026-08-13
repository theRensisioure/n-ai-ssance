#!/usr/bin/env python3
"""reconstruct — re-member a jwrangle day board from disk (meaning-first)."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

_LIB = Path(__file__).resolve().parents[2] / "_lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from ssfs_common import JWRANGLE_DAYS  # noqa: E402

_DAY_HUMAN = re.compile(r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\d{2,4}.+", re.I)
# **active queue:** val | **active queue / goal:** val | active queue: val
_ACTIVE_Q = re.compile(
    r"\*\*active queue(?:\s*/\s*goal)?:?\*\*:?\s*(.+)", re.I
)
_ACTIVE_SLOT = re.compile(r"\*\*active slot:?\*\*:?\s*(.+)", re.I)
_ACTIVE_Q_LOOSE = re.compile(r"active queue(?:\s*/\s*goal)?:?\s*(.+)", re.I)
_ACTIVE_SLOT_LOOSE = re.compile(r"active slot:?\s*(.+)", re.I)


def find_day_dir(days_root: Path, day: str | None) -> Path | None:
    if not days_root.is_dir():
        return None
    if day:
        # ISO or human
        direct = days_root / day
        if direct.is_dir() and (direct / "day.md").is_file():
            return direct
        for child in days_root.iterdir():
            if child.is_dir() and day.lower() in child.name.lower():
                if (child / "day.md").is_file():
                    return child
        return None
    # prefer today-ish human folders by mtime of day.md
    candidates: list[Path] = []
    for child in days_root.iterdir():
        dm = child / "day.md"
        if child.is_dir() and dm.is_file():
            candidates.append(child)
    if not candidates:
        return None

    def sk(p: Path) -> float:
        try:
            return (p / "day.md").stat().st_mtime
        except OSError:
            return 0.0

    candidates.sort(key=sk, reverse=True)
    return candidates[0]


def extract_section(md: str, heading: str) -> list[str]:
    lines = md.splitlines()
    out: list[str] = []
    capture = False
    for ln in lines:
        if ln.startswith("## "):
            if capture:
                break
            if heading.lower() in ln.lower():
                capture = True
            continue
        if capture:
            out.append(ln)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="SSFS reconstruct day from disk")
    ap.add_argument("--day", default=None, help="day folder name or substring")
    ap.add_argument("--days-root", default=str(JWRANGLE_DAYS))
    ap.add_argument(
        "--save",
        action="store_true",
        help="write RECONSTRUCT-<stamp>.md in the day folder (never overwrite)",
    )
    args = ap.parse_args()
    root = Path(args.days_root).expanduser()
    ddir = find_day_dir(root, args.day)
    if not ddir:
        print(f"error: no day board under `{root}`", file=sys.stderr)
        return 1
    day_md = (ddir / "day.md").read_text(encoding="utf-8", errors="replace")
    active_q = ""
    active_slot = ""
    for ln in day_md.splitlines():
        for rx in (_ACTIVE_Q, _ACTIVE_Q_LOOSE):
            m = rx.search(ln)
            if m:
                active_q = m.group(1).strip().strip("*").strip()
                break
        for rx in (_ACTIVE_SLOT, _ACTIVE_SLOT_LOOSE):
            m = rx.search(ln)
            if m:
                active_slot = m.group(1).strip().strip("*").strip()
                break

    carry = extract_section(day_md, "Carry")
    closed = extract_section(day_md, "Closed")
    parked = extract_section(day_md, "Parked")
    # queue table head lines
    queue_lines = []
    for ln in day_md.splitlines():
        if ln.strip().startswith("|") and (
            "active" in ln.lower() or "pending" in ln.lower() or "queue" in ln.lower()
        ):
            queue_lines.append(ln)

    stamp = date.today().isoformat().replace("-", "")
    lines = [
        f"# Reconstruct · {ddir.name}",
        "",
        f"- **day dir:** `{ddir}`",
        f"- **active queue:** {active_q or '—'}",
        f"- **active slot:** {active_slot or '—'}",
        "",
        "## Work names first",
        "",
        f"Head: **{active_q or 'unknown queue'}** · slot **{active_slot or 'unknown'}**",
        "",
        "## Day queue (raw rows)",
        "",
    ]
    if queue_lines:
        lines.extend(queue_lines[:20])
    else:
        lines.append("_No queue table rows parsed._")

    def add_block(title: str, body: list[str]) -> None:
        lines.extend(["", f"## {title}", ""])
        bullets = [b for b in body if b.strip().startswith("-") or b.strip().startswith("|")]
        if bullets:
            lines.extend(bullets[:30])
        else:
            # first non-empty
            kept = [b for b in body if b.strip()][:15]
            lines.extend(kept if kept else ["_empty_"])

    add_block("Carry-forwards", carry)
    add_block("Closed", closed)
    add_block("Parked", parked)
    lines.extend(
        [
            "",
            "## Contract",
            "",
            "Reconstruct **re-reads disk**. It does not stream an old chat mind.",
            "Board indices are secondary to work names.",
            "",
        ]
    )
    text = "\n".join(lines)
    print(text)
    if args.save:
        out = ddir / f"RECONSTRUCT-ssfs-{stamp}.md"
        # never overwrite: add counter
        n = 1
        while out.exists():
            out = ddir / f"RECONSTRUCT-ssfs-{stamp}-{n}.md"
            n += 1
        out.write_text(text, encoding="utf-8")
        print(f"\n_saved:_ `{out}`", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
