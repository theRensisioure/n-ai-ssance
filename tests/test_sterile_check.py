"""Drive the real sterile-check entry point — no reimplementation."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "sterile-check.py"


def test_sterile_check_exits_zero_on_pack():
    assert SCRIPT.is_file(), "sterile-check.py must exist"
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr or proc.stdout
    assert "OK" in proc.stdout


def test_docs_backbone_files_exist():
    required = [
        ROOT / "docs" / "FOR-READERS.md",
        ROOT / "docs" / "use-cases" / "01-map-not-chat.md",
        ROOT / "docs" / "socratic" / "SERIES-01-map.md",
        ROOT / "docs" / "collection" / "MANIFEST.md",
        ROOT / "docs" / "arrays" / "INDEX.md",
        ROOT / "fixtures" / "synthetic-session" / "spine.md",
    ]
    missing = [str(p) for p in required if not p.is_file()]
    assert not missing, f"missing backbone files: {missing}"


def test_array_quantity_liberal():
    arrays = ROOT / "docs" / "arrays"
    files = list(arrays.rglob("*.md"))
    assert len(files) >= 50, f"expected liberal array volume, got {len(files)}"


def test_use_cases_are_synthetic():
    text = (ROOT / "docs" / "use-cases" / "01-map-not-chat.md").read_text(
        encoding="utf-8"
    )
    assert "Alex" in text and "example-app" in text
    assert "chat_history.jsonl" not in text or "No full" in text
