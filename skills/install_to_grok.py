#!/usr/bin/env python3
"""Copy n-ai-ssance skills + _lib into ~/.grok/skills/.

Env: N_AI_SSANCE_GROK_SKILLS, then NAISSANCE_GROK_SKILLS, then SSFS_GROK_SKILLS, then ~/.grok/skills.
"""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent
DEST = Path(
    os.environ.get("N_AI_SSANCE_GROK_SKILLS")
    or os.environ.get("NAISSANCE_GROK_SKILLS")
    or os.environ.get("SSFS_GROK_SKILLS")
    or (Path.home() / ".grok" / "skills")
)
SKILLS = ("session-map", "reconstruct", "scan-sessions", "intent", "durable-land")


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    # shared lib
    lib_src = PACK / "_lib"
    lib_dst = DEST / "_lib"
    if lib_dst.exists():
        shutil.rmtree(lib_dst)
    shutil.copytree(lib_src, lib_dst)
    print(f"copied _lib → {lib_dst}")

    for name in SKILLS:
        src = PACK / name
        if not src.is_dir():
            print(f"skip missing {name}", file=sys.stderr)
            continue
        dst = DEST / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        # point scripts at DEST/_lib: they already use parents[2]/_lib from skill/scripts
        # skill/scripts -> skill -> skills-root; parents[2] is skills root. Good when installed flat under .grok/skills
        print(f"copied {name} → {dst}")
    print("done. Try: python session-map/scripts/session_map.py <path>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
