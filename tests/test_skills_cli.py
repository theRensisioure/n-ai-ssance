"""Drive real SSFS skill CLIs — no reimplementation of map logic in tests."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "synthetic-session"
PY = sys.executable


def run(script: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        [PY, str(script), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_session_map_fixture():
    script = ROOT / "skills" / "session-map" / "scripts" / "session_map.py"
    proc = run(script, str(FIXTURE))
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout
    assert "Session map" in out
    assert "Relay" in out
    assert "example-app" in out
    assert "chat_history" not in out.lower() or "do not open" in out.lower()
    # must not dump huge transcript — fixture has no jsonl; spine short
    assert out.count("\n") < 80


def test_scan_sessions_runs():
    script = ROOT / "skills" / "scan-sessions" / "scripts" / "scan_sessions.py"
    proc = run(script, "--limit", "5")
    assert proc.returncode == 0, proc.stderr
    assert "scan-sessions" in proc.stdout


def test_intent_template_and_write():
    script = ROOT / "skills" / "intent" / "scripts" / "intent.py"
    proc = run(script, "--print-template")
    assert proc.returncode == 0
    assert "Outcome" in proc.stdout and "Fence" in proc.stdout
    with tempfile.TemporaryDirectory() as td:
        sess = Path(td)
        proc2 = run(
            script,
            str(sess),
            "--write",
            "--outcome",
            "ship map skill",
            "--surface",
            "ssfs skills/session-map",
            "--fence",
            "no suite UI",
            "--spine",
            "map skill ships",
        )
        assert proc2.returncode == 0, proc2.stderr
        packet = sess / "intent" / "interview.md"
        assert packet.is_file()
        body = packet.read_text(encoding="utf-8")
        assert "ship map skill" in body


def test_durable_land_copy_only():
    script = ROOT / "skills" / "durable-land" / "scripts" / "durable_land.py"
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        src = td_path / "note.txt"
        src.write_text("hello land\n", encoding="utf-8")
        root = td_path / "lands"
        proc = run(script, str(src), "--root", str(root), "--stamp", "TESTSTAMP")
        assert proc.returncode == 0, proc.stderr
        land = root / "TESTSTAMP"
        assert (land / "MANIFEST.json").is_file()
        assert (land / "INDEX.md").is_file()
        assert (land / "files" / "note.txt").is_file()
        # original remains (copy)
        assert src.is_file()
        man = json.loads((land / "MANIFEST.json").read_text(encoding="utf-8"))
        assert man["entries"][0]["action"] == "copy"


def test_reconstruct_script_exists_and_handles_missing_days():
    script = ROOT / "skills" / "reconstruct" / "scripts" / "reconstruct.py"
    with tempfile.TemporaryDirectory() as td:
        proc = run(script, "--days-root", td)
        # empty days root → exit 1
        assert proc.returncode == 1
        day = Path(td) / "Wed9901th"
        day.mkdir()
        (day / "day.md").write_text(
            "# day\n\n- **active queue:** demo-queue\n"
            "- **active slot:** demo-slot\n\n"
            "## Carry-forwards\n- keep demo\n\n"
            "## Closed today\n- closed item\n\n"
            "## Parked\n- parked item\n",
            encoding="utf-8",
        )
        proc2 = run(script, "--days-root", td, "--day", "Wed9901th")
        assert proc2.returncode == 0, proc2.stderr
        assert "demo-queue" in proc2.stdout
        assert "Reconstruct" in proc2.stdout
