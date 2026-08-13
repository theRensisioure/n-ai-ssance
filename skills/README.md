# skills/

Naissance pack. Install into Grok skills home (copy each folder):

Install into Grok skills home (copy each folder):

```text
%USERPROFILE%\.grok\skills\     (Windows cmd)
$env:USERPROFILE\.grok\skills\  (PowerShell)
~/.grok/skills/                 (Unix)
```

| Skill | Slash | Script |
|-------|-------|--------|
| session-map | `/session-map` | `session-map/scripts/session_map.py` |
| reconstruct | `/reconstruct` | `reconstruct/scripts/reconstruct.py` |
| scan-sessions | `/scan-sessions` | `scan-sessions/scripts/scan_sessions.py` |
| intent | `/intent` | `intent/scripts/intent.py` |
| durable-land | `/durable-land` | `durable-land/scripts/durable_land.py` |

Shared lib: `_lib/ssfs_common.py` (must sit next to skill folders as `skills/_lib` in the pack; when installing, copy `_lib` into `~/.grok/skills/_lib` **or** keep pack layout and run scripts from the clone).

## Install helper

From pack root:

```bash
python skills/install_to_grok.py
```

## PowerShell note

`%USERPROFILE%` does **not** expand in PowerShell. Use:

```powershell
python "$env:USERPROFILE\jwrangle\tools\on-plan-path.py" "C:\dev\ssfs\docs\FOR-READERS.md"
# or
python "C:\Users\<you>\jwrangle\tools\on-plan-path.py" "C:\dev\ssfs\README.md"
```
