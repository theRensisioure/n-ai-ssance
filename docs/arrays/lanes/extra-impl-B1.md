# EXTRA-IMPL-B1 · fixture-bound examples

## Strategy name
Examples only from synthetic fixtures

## Lane
B — Sterile compliance & fixtures

## MVP one-liner (SSFS dual-track docs)
Dual-track teaching may cite **only** `fixtures/synthetic-session/` (and hand-written Alex/River style names) so public and author tracks never need a real session dump.

## Acceptance checklist
- [ ] Any example session shape points at `fixtures/synthetic-session/` or stays fully invented
- [ ] No absolute user-home paths; only patterns (`~/.grok/sessions/<id>/` as pattern, not a dump)
- [ ] `python scripts/sterile-check.py` exit 0 after edits
- [ ] STERILE.md “never commit” list still covered by check script
- [ ] Author Socratic prompts do not ask the reader to paste live transcripts into the repo

## Risks
- Fixture too thin to prove the approach; temptation to “just once” paste a real path
- Synthetic names reused inconsistently across use-cases and fixtures
- Authors treat sterile-check as a substitute for judgment on borderline redaction
