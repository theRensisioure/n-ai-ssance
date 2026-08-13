#!/usr/bin/env python3
"""intent — show or write a 3-Q goal packet (outcome · surface · fence)."""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path


TEMPLATE = """# intent interview

status: open
updated: {ts}

## Spine
{spine}

## 3-Q

### Q1 · Outcome
What exists when this is done?

{outcome}

### Q2 · Surface
Where does it live (repo, skill, doc, path)?

{surface}

### Q3 · Fence
What is explicitly out of scope?

{fence}
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="SSFS intent fence packet")
    ap.add_argument(
        "session",
        nargs="?",
        default=None,
        help="session directory (writes intent/interview.md under it)",
    )
    ap.add_argument("--outcome", default="")
    ap.add_argument("--surface", default="")
    ap.add_argument("--fence", default="")
    ap.add_argument("--spine", default="")
    ap.add_argument(
        "--print-template",
        action="store_true",
        help="print empty 3-Q template to stdout (no write)",
    )
    ap.add_argument(
        "--write",
        action="store_true",
        help="write packet (requires session dir + answers)",
    )
    args = ap.parse_args()

    if args.print_template or (not args.session and not args.write):
        print(
            TEMPLATE.format(
                ts=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
                spine="_(one sentence)_",
                outcome="_(fill)_",
                surface="_(fill)_",
                fence="_(fill)_",
            )
        )
        print(
            "\n_Fill outcome · surface · fence, then:_ "
            "`python intent.py <session-dir> --write --outcome '…' --surface '…' --fence '…'`",
            file=sys.stderr,
        )
        return 0

    sess = Path(args.session).expanduser()
    if not sess.is_dir():
        print(f"error: not a directory: {sess}", file=sys.stderr)
        return 1

    packet = sess / "intent" / "interview.md"
    if packet.is_file() and not args.write:
        print(f"# Intent · present\n\n- **path:** `{packet}`\n")
        print(packet.read_text(encoding="utf-8", errors="replace"))
        return 0

    if not args.write:
        print("# Intent · missing\n")
        print("No `intent/interview.md`. Run 3-Q:\n")
        print("1. **Outcome** — what exists when done?")
        print("2. **Surface** — where does it live?")
        print("3. **Fence** — what is out?")
        print(f"\nThen write with `--write` into `{sess / 'intent'}`.")
        return 0

    if not (args.outcome and args.surface and args.fence):
        print(
            "error: --write needs --outcome, --surface, and --fence",
            file=sys.stderr,
        )
        return 1

    spine = args.spine or args.outcome.strip().split("\n")[0][:160]
    text = TEMPLATE.format(
        ts=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        spine=spine,
        outcome=args.outcome.strip(),
        surface=args.surface.strip(),
        fence=args.fence.strip(),
    )
    packet.parent.mkdir(parents=True, exist_ok=True)
    packet.write_text(text, encoding="utf-8")
    print(f"wrote `{packet}`")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
