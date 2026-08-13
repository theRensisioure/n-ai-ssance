---
name: durable-land
description: >
  Land capture files into a stamped durable directory with MANIFEST.json and
  INDEX.md. Default is COPY (originals stay). Use when the user types
  /durable-land, "land this capture", "durable archive land", or needs
  copy-first provenance without chat-governance archives.
---

# `/durable-land` — copy-first stamped land

## Run

```bash
python skills/durable-land/scripts/durable_land.py path/to/file.png
python skills/durable-land/scripts/durable_land.py --from-inbox
# move only when explicitly requested:
python skills/durable-land/scripts/durable_land.py file.bin --move
```

Env:

- `SSFS_DURABLE_ROOT` — default `~/jwrangle/durable-archive/lands`  
- `SSFS_CAPTURE_INBOX` — default `~/test-write`  

## Contract

- **Copy by default**  
- `--move` only when user says move  
- Each land: `files/` + `MANIFEST.json` + `INDEX.md`  
- Not chat-diff archives; not “AI memory”  

## Sterile

Do not commit landed personal captures into the SSFS git repo.
