---
name: reconstruct
description: >
  Re-member a jwrangle day board from disk (active queue/slot, carry, closed,
  parked) with work names first — not a streamed old chat mind. Use when the
  user types /reconstruct, "reconstruct the day", "what was on my board",
  "re-member today", or needs interrupt recovery without the suite rails card.
---

# `/reconstruct` — day from disk

## Run

```bash
python skills/reconstruct/scripts/reconstruct.py
python skills/reconstruct/scripts/reconstruct.py --day Wed2612th
python skills/reconstruct/scripts/reconstruct.py --save
```

Env: `SSFS_JWRANGLE_DAYS` overrides `~/jwrangle/days`.

## Contract

- Re-read `day.md` every time  
- Lead with **active queue + active slot** work names  
- `--save` writes a **new** `RECONSTRUCT-ssfs-*.md` — never overwrite  

## Not

Not a full chat replay. Not board UI.
