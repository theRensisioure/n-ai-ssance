# MAP · Dual-track docs (author socratic vs public FOR-READERS)

## Unit path
docs/arrays/maps/extra-map-01.md

## Map
- **Approach:** Dual-track documentation
- **Audience:** Maintainers + public readers (split intentionally)
- **Intent spine:** Keep author inquiry separate from calm public framing so neither track poisons the other.
- **Salience:** which door for which reader; no forced deep work to install or use skills
- **Tracks:**
  - **Author / socratic** — `docs/socratic/`: prompts that pressure-test approaches; optional deep work for maintainers
  - **Public / FOR-READERS** — `docs/FOR-READERS.md` + use-cases: benefit-first overview; no inquiry homework required

## Keep
- Two doors with clear labels: “read to use” vs “read to author”
- FOR-READERS stays calm, short sentences, problem → five approaches → install pointer
- Socratic series stays optional; README in socratic states it is not required for skill use
- Use-cases as the shared middle: synthetic scenarios (Alex / River / example-app only when storytelling)
- Product lock and STERILE remain single SSOT; tracks do not fork product claims

## Toss
- Merging socratic prompts into the public overview as required reading
- Putting personal essay potency or live session residue into either track
- Suite UI / board host as a doc prerequisite
- One wall of text that tries to serve maintainer and adopter at once
- Treating dual-track as “two products” instead of two audiences for one pack

## Smoke test
1. File exists under docs/arrays/maps/ with prefix extra-map-
2. Mentions both socratic and FOR-READERS without conflating duties
3. No absolute user-home paths; no session dumps; no keys
4. Reader can answer: “I only want skills” → FOR-READERS + use-cases; “I maintain the pack” → socratic + PRODUCT
5. sterile-check would still pass on this unit alone

## Next commit
- Keep docs/INDEX.md pointing both tracks without burying either
- When a new approach ships: use-case (public-adjacent) first; socratic series update optional same wave
- Do not require socratic completion for skill install story

## Salience weight
High — pack readability and community onboarding hinge on not mixing tracks

## Version role
Foundation (doc architecture for skill-community backbone)
