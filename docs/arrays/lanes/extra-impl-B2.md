# EXTRA-IMPL-B2 · dual-track sterile gate

## Strategy name
Sterile gate before dual-track ship

## Lane
B — Sterile compliance & fixtures

## MVP one-liner (SSFS dual-track docs)
Treat dual-track doc ship as a **gate**: public + author files land together only after sterile-check and a short “no potent residue” self-audit.

## Acceptance checklist
- [ ] Diff touches only allowed surfaces under `docs/`, `fixtures/`, `PRODUCT.md`, `README.md`, `STERILE.md`, `scripts/`
- [ ] No session jsonl, no real third-party names, no keys
- [ ] Dual-track pair (use-case or FOR-READERS + socratic series leaf) reviewed as a set
- [ ] `docs/collection/MANIFEST.md` still matches what is in-pack vs out
- [ ] `python scripts/sterile-check.py` exit 0

## Risks
- Gate becomes ceremony; people skip when remote is private
- MANIFEST drifts from tree (listed in-pack but missing, or present but unlisted)
- Compliance focus delays skill bodies while only docs move
