# Collection manifest — what enters the pack vs stays out

**Purpose:** One list of documentation sources for the SSFS GitHub backbone.  
**Rule:** Only **sterile-safe** material is copied or paraphrased into this repo. See root [STERILE.md](../../STERILE.md).

## In pack (ship / already present)

| Surface | Path | Role |
|---------|------|------|
| Product lock | `PRODUCT.md` | One-sentence claim + ring law |
| Public README | `README.md` | Install + what/not |
| Sterile law | `STERILE.md` | Push ban list |
| Sterile check | `scripts/sterile-check.py` | Gate before commit |
| Use cases (synthetic) | `docs/use-cases/` | Benefit scenarios per approach |
| Author Socratic series | `docs/socratic/` | In-depth prompts for author-style inquiry |
| Professional framing | `docs/FOR-READERS.md` | Calm generalized README analogue |
| Collection index | `docs/collection/MANIFEST.md` | This file |
| Docs hub | `docs/INDEX.md` | Navigation |
| Agent-array volume | `docs/arrays/` | Map / lane / prompt units (liberal quantity) |
| Synthetic fixtures | `fixtures/synthetic-session/` | Fake session shape only |
| Skills tree notes | `skills/README.md` | Shipping order for skills |

## Referenced for shape only (not copied verbatim)

| Source | Why read | Why not dump |
|--------|----------|--------------|
| Artifact Scanner SEED/CHANGELOG (local) | Approach truth: map-not-chat, reconstruct, durable land | Product suite UI; machine-specific paths |
| Sesefus `docs/CANON.md` status vocabulary | Honest WIRED/STUB/DEAD framing culture | Product binary status ≠ SSFS skills |
| Sesefus public README tone | Calm product prose | Different product; no monorepo merge |
| Author product-essay Socratic *form* | Mirror, concrete, seeds ≤5 | Personal essay answers stay private |

## Explicitly out (never pack)

- Live `~/.grok/sessions/**`, Claude/Cursor project dumps  
- jwrangle `days/**`, confirmations, legal/Takeout, journal audio  
- Real home absolute paths, keys, `.env`  
- Full Sesefus monorepo / Artifact Scanner tree  
- Private essay answer dumps with potent life detail  

## Relationship: Sesefus docs vs this repo

Sesefus product documentation remains on **`Zychs/sesefus`**.  
This repo (**`Zychs/ssfs`**) holds the **skill-community backbone**: sterilized approaches, dual-track teaching (author Socratic + public framing), and future skill bodies.  
It is not a rebrand of Sesefus and not a paste of CANON.

## Collection actions taken this pass

1. Authored sterile use-cases + dual-track docs in-tree.  
2. Generated multi-unit agent arrays under `docs/arrays/`.  
3. No session files or personal boards imported.
