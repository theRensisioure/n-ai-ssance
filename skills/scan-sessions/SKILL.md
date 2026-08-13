---
name: scan-sessions
description: >
  List local Grok (and path-shaped) agent sessions with meaning-first titles,
  without starting Artifact Scanner or :8765. Use when the user types
  /scan-sessions, "list my sessions", "which chats touched X", "find session",
  or needs inventory before /session-map.
---

# `/scan-sessions` — inventory without a board server

## Run

```bash
python skills/scan-sessions/scripts/scan_sessions.py --limit 20
python skills/scan-sessions/scripts/scan_sessions.py --project example-app
```

Env: `SSFS_GROK_SESSIONS` overrides default `~/.grok/sessions`.

## Output

Numbered hits: **title** (meaning-first) · agent · sid · cwd · mtime · path.

## Next

Hand a path to `/session-map` for the full handoff map.
