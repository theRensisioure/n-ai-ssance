---
name: session-map
description: >
  Build a session MAP (identity, copy-ready relay, user spine, paths, find/open)
  without dumping the full chat transcript. Use when the user types /session-map,
  "map this session", "session handoff", "map not chat", or needs orientation of a
  Grok/Claude session path for a human or agent. Sister to Artifact Scanner
  session-map preview; works without the suite server.
---

# `/session-map` — map, not chat dump

## Job

Given a **session directory** (or `chat_history.jsonl` / `prompt_history.jsonl` path), produce a short markdown **map**: agent · sid · cwd · **relay** · user spine · paths · find/open. Do **not** paste the full transcript into chat.

## Run

```bash
python skills/session-map/scripts/session_map.py "<session-or-history-path>"
```

From a clone of this pack (or after install into `~/.grok/skills/session-map/`):

```bash
python "%USERPROFILE%\.grok\skills\session-map\scripts\session_map.py" "<path>"
```

If no path given: ask once for the session path, or run `/scan-sessions` first.

## Agent procedure (if script unavailable)

1. Resolve session root (dir containing history/summary).  
2. Prefer `summary.json` title → else first substantive user line → never lead with raw uuid.  
3. Extract **user** turns only into a short spine (cap ~24).  
4. Collect edit paths from hunk metadata if present — not whole jsonl dump.  
5. Emit Relay one-liner + sections above.  
6. Point at raw transcript path with “do not open unless you must.”

## Sterile

Never commit live maps with personal paths into the SSFS repo. Local run output stays local.
