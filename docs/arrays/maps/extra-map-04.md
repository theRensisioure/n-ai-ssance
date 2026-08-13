# MAP · session-map skill teaching path

## Unit path
docs/arrays/maps/extra-map-04.md

## Map
- **Skill name:** session-map (`/session-map` when D2 ships)
- **What this is:** Docs-only **teaching path** for the skill — how an author or agent learns to teach map-not-chat without writing skill code yet
- **Not this:** SKILL.md body, live session readers, suite board preview
- **Intent spine:** Handoff without transcript — identity, relay, user spine, paths, open pointers
- **Synthetic ground:** Alex has three example-app auth sessions; River asks where the login bug left off
- **Doc chain (ordered):**
  1. PRODUCT.md row for map-not-chat / session-map
  2. docs/use-cases/01-map-not-chat.md (situation → approach → benefit)
  3. docs/socratic/SERIES-01-map.md (P1–P5, done-when)
  4. fixtures/synthetic-session/ (summary-line, spine, paths — fake only)
  5. docs/arrays unit maps for map-not-chat × audiences (implementer, verifier, reader)
  6. prompt pack prompt-map-not-chat-01…08 when drilling phrasing
- **Learner outcomes:**
  - Can state benefit in one concrete story (not feature laundry)
  - Can refuse a full chat_history paste when a map would serve
  - Can name meaning-first title vs id slice as title law
- **Ring law:** Skill must work without Artifact Scanner host; teaching never assumes `:8765`

## Keep
- Sterile Alex / River / example-app scenarios only
- Relay as copy-ready one-liner for a human first; spine second
- Paths as relative or pattern placeholders (`~/.grok/sessions/<id>/`)
- Link use-case ↔ socratic ↔ PRODUCT shipping order (D2)
- Benefit-first: token cost, handoff speed, meaning in title

## Toss
- Live jsonl / prompt_history / events dumps
- Real home absolute paths or real session ids
- Suite flip/zip/UI chrome as required for the lesson
- Perfect schema debates before one synthetic handoff succeeds
- Implementing skills/session-map/ in this map’s job (docs path only)

## Smoke test
1. File exists under docs/arrays/maps/ with this name
2. Mentions teaching path for session-map / map-not-chat, not suite UI
3. No absolute user-home paths; no secrets; no live transcript excerpts
4. Reader can walk the doc chain without opening a real session
5. Synthetic fixture names only (Alex, River, example-app)
6. `python scripts/sterile-check.py` still green after add

## Next commit
- Keep teaching path aligned when D2 SKILL.md lands (do not invent code here)
- Ensure use-case 01 + SERIES-01 remain the story spine
- Optional: one sterile “before map / after map” example block in FOR-READERS if missing
- Do not grow this into skill runtime

## Salience
High — first skill in shipping order (D2); load-bearing community move is handoff without dump. Teaching path is the bridge while skills/ is still documentation spine only.

## Version role
Extra map · skill teaching path (session-map). Complements unit-map-not-chat__* audience maps. Foundation for D2 author/implementer onboarding; not a product feature surface.
