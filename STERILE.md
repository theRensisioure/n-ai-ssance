# STERILE — what must never land in this repo

**Law:** n-ai-ssance is a **public community skill pack**. Every commit and every push must be free of **potent / sensitive / personal** data. Public remote is **especially** not permission to dump life into git.

Agents (including Grok) **must refuse** to `git add` / `commit` / `push` material that fails this list. Prefer failing the step over “just this once.”

## Never commit

### Secrets
- API keys, tokens (`gho_`, `ghp_`, `sk-`, Bearer, OAuth), passwords, `.env*`, private keys, cookies, session cookies  
- Cloud credentials, webhook secrets, license keys  

### Identity & personal
- Real full names of third parties, medical/BA journal content, legal matter, therapy notes  
- Phone numbers, street addresses, government IDs, financial account numbers  
- Personal email dumps, Gmail Takeout, chat takeouts  

### Session / agent residue (the main trap)
- Live or archived **session directories** (`chat_history.jsonl`, `prompt_history.jsonl`, `events.jsonl`, `hunk_records.jsonl`, compaction dumps)  
- Full or large transcript excerpts that are not **synthetic fixtures**  
- Real absolute paths that identify a specific person’s home beyond **generic** install placeholders (`%USERPROFILE%`, `~`, `$HOME`)  
  - Bad: a full Windows/mac/Linux home path that names a real account  
  - OK: `%USERPROFILE%\.grok\skills\`, `~/.grok/sessions/<id>/` as a **pattern**, not a dump of their tree  
- Screenshots of live boards with real titles/paths  
- `confirmations.csv`, durable-archive **lands** with real captures, jwrangle day boards with private notes  

### Product bleed
- Entire Artifact Scanner or Sesefus trees  
- Binary blobs, wav/mp3 journals, proprietary datasets  

## Allowed

- Skill procedures (`SKILL.md`) with **generic** path conventions  
- Synthetic / redacted fixtures under `fixtures/` (obviously fake names, no real secrets)  
- Docs that teach map-not-chat **without** pasting real sessions  
- MIT license, changelogs of **code/docs** changes only  

## Before every push

1. Run `python scripts/sterile-check.py` (exit 0 required).  
2. `git status` + `git diff --cached` — no session files, no user-home absolutes, no keys.  
3. If unsure: **do not push**. Ask.  

## Fixtures rule

If a skill needs an example session for tests:

- Hand-written tiny JSONL under `fixtures/synthetic-session/`  
- Characters named `Alex` / `River`, project `example-app`  
- No real sid, no real repo paths, no real third-party names  

## Agent standing order

When implementing SSFS deltas: write only under `C:\dev\ssfs` (or the clone).  
**Do not** copy from `jwrangle/days`, live `~/.grok/sessions`, legal archives, or journal takes into this repo.  
Quote PRODUCT.md / STERILE.md; do not re-home personal boards here.
