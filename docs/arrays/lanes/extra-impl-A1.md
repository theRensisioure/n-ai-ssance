# EXTRA-IMPL-A1 · dual-track voice fence

## Strategy name
Voice fence at the doc header

## Lane
A — Docs clarity & dual-track separation

## MVP one-liner (SSFS dual-track docs)
Every dual-track surface opens with a one-line **track label** (author-Socratic vs public-reader) so the two voices never blend mid-file.

## Acceptance checklist
- [ ] `docs/socratic/` files declare author-track only at the top
- [ ] `docs/FOR-READERS.md` and `docs/use-cases/` stay public-track (calm, no inquiry voice)
- [ ] `docs/INDEX.md` lists both tracks with distinct roles
- [ ] No suite UI, no live session paste, synthetic names only
- [ ] Paths in examples are repo-relative or generic patterns (`~/.grok/skills/`, `fixtures/synthetic-session/`)

## Risks
- Headers alone fail if body prose still mixes inquiry and public framing
- Track labels become boilerplate and get ignored without a smoke read of one pair
- Over-splitting one idea into two files when a single public page plus optional Socratic series is enough
