#!/usr/bin/env python3
"""durable-land — copy-only stamped land + MANIFEST (default). Move only with --move."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

_LIB = Path(__file__).resolve().parents[2] / "_lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from ssfs_common import CAPTURE_INBOX, DURABLE_ROOT  # noqa: E402


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="SSFS durable-land")
    ap.add_argument(
        "src",
        nargs="*",
        help="files/dirs to land (default: nothing — use --from-inbox)",
    )
    ap.add_argument(
        "--from-inbox",
        action="store_true",
        help=f"land all files under capture inbox ({CAPTURE_INBOX})",
    )
    ap.add_argument("--root", default=str(DURABLE_ROOT), help="lands root")
    ap.add_argument(
        "--move",
        action="store_true",
        help="MOVE instead of copy (dangerous; off by default)",
    )
    ap.add_argument("--stamp", default=None, help="optional stamp id")
    args = ap.parse_args()

    root = Path(args.root).expanduser()
    sources: list[Path] = []
    if args.from_inbox:
        inbox = CAPTURE_INBOX.expanduser()
        if inbox.is_dir():
            sources.extend([p for p in inbox.iterdir() if p.is_file()])
    for s in args.src:
        sources.append(Path(s).expanduser())

    if not sources:
        print("error: no sources — pass paths or --from-inbox", file=sys.stderr)
        return 1

    missing = [str(s) for s in sources if not s.exists()]
    if missing:
        print("error: missing: " + ", ".join(missing), file=sys.stderr)
        return 1

    stamp = args.stamp or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    land = root / stamp
    files_dir = land / "files"
    files_dir.mkdir(parents=True, exist_ok=False)

    entries = []
    for src in sources:
        dest = files_dir / src.name
        if dest.exists():
            dest = files_dir / f"{src.stem}-{stamp}{src.suffix}"
        if args.move:
            shutil.move(str(src), str(dest))
            action = "move"
        else:
            if src.is_dir():
                shutil.copytree(src, dest)
            else:
                shutil.copy2(src, dest)
            action = "copy"
        digest = sha256_file(dest) if dest.is_file() else None
        entries.append(
            {
                "name": dest.name,
                "source": str(src),
                "action": action,
                "sha256": digest,
                "bytes": dest.stat().st_size if dest.is_file() else None,
            }
        )

    manifest = {
        "stamp": stamp,
        "created": datetime.now(timezone.utc).isoformat(),
        "default_action": "move" if args.move else "copy",
        "entries": entries,
    }
    (land / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    index_lines = [
        f"# Land {stamp}",
        "",
        f"- **root:** `{land}`",
        f"- **action:** {'MOVE' if args.move else 'COPY (default)'}",
        "",
        "## Files",
        "",
    ]
    for e in entries:
        index_lines.append(f"- `{e['name']}` · {e['action']} · {e.get('bytes')} bytes")
    index_lines.append("")
    (land / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    print(f"# durable-land · {stamp}")
    print(f"- **path:** `{land}`")
    print(f"- **action:** {'move' if args.move else 'copy'}")
    print(f"- **files:** {len(entries)}")
    for e in entries:
        print(f"  - `{e['name']}`")
    print(f"- **MANIFEST:** `{land / 'MANIFEST.json'}`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
