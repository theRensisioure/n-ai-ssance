# MAP · Zychs/ssfs skill pack vs Zychs/sesefus product docs (no monorepo)

## Unit path
docs/arrays/maps/extra-map-03.md

## Map
- **Approach:** Explicit multi-repo ring law (skills vs product vs optional host)
- **Audience:** Maintainers, agents, and readers who confuse sibling projects
- **Intent spine:** SSFS is portable scanner-shaped skills; Sesefus is a separate product with its own docs and tree—not one monorepo.
- **Salience:** wrong merge kills both stories; name the fence every handoff
- **Ring:**
  - **Zychs/ssfs** — skill pack + sterile docs + optional thin scripts; works without suite UI
  - **Sesefus** — separate product (own code, docs, concerns); not required to use SSFS
  - **Artifact Scanner** — optional rich host; provenance of ideas, not a required install for SSFS

## Keep
- PRODUCT.md one-sentence lock: skills for underbuilt skill community, not suite rehost, not sesefus monorepo
- Out-of-pack list: board host chrome, sesefus product code (journal, alarms, will-sieve, etc.), encryption/card rack/outer products
- Docs that teach handoff/map/land without importing sesefus UI or domain modules
- Provenance note: ideas distilled from scanner behaviors; implementation lives as skills, not as a fork of either product tree
- Separate install stories: skills → Grok skills home; sesefus → its own product path (never collapsed here)

## Toss
- Monorepo “convenience” that drops sesefus or scanner trees into ssfs
- Doc claims that SSFS solves sesefus product problems or replaces the scanner host
- Requiring sesefus install, journal features, or suite flip/zip to use session-map / reconstruct / land
- Cross-copying product docs wholesale into ssfs arrays (link concepts; do not merge trees)
- Treating private remotes as permission to blend personal product boards into the skill pack

## Smoke test
1. Names ssfs vs sesefus as separate surfaces; states no monorepo
2. Scanner appears only as optional host / idea provenance, not dependency for pack use
3. No absolute user-home paths; no session dumps; no keys; no legal/journal
4. Reader can answer: “Do I need sesefus to run SSFS skills?” → No
5. Out-of-pack items match PRODUCT.md spirit (suite chrome + sesefus product code stay out)

## Next commit
- Keep README / PRODUCT / FOR-READERS aligned on ring law wording
- Skill bodies (D2+) must not import sesefus modules or scanner serve host
- Arrays stay inside ssfs docs only; do not vendor sibling product trees

## Salience weight
High — boundary failure is the main architectural thrash risk for the pack

## Version role
Foundation (repo identity fence for skill-community backbone)
