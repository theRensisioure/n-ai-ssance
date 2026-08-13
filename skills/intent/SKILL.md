---
name: intent
description: >
  Goal fence for a session: outcome · surface · fence (3-Q). Show existing
  intent/interview.md or write a packet. Use when the user types /intent,
  "goal packet", "3-Q", "fence this session", thrash multi-goals, or no intent
  packet exists before expanding scope.
---

# `/intent` — outcome · surface · fence

## Run

```bash
# print template
python skills/intent/scripts/intent.py --print-template

# show packet if present
python skills/intent/scripts/intent.py "<session-dir>"

# write packet
python skills/intent/scripts/intent.py "<session-dir>" --write \
  --outcome "…" --surface "…" --fence "…" --spine "…"
```

## Agent procedure

If missing packet and user is thrashing: ask **one** of the three axes per turn (or offer ≤5 seeds), then `--write`. Do not invent personal life content.

## Packet path

`<session>/intent/interview.md`
