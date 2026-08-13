# n-ai-ssance

**v1.0** · [MIT](LICENSE) · [CI](https://github.com/theRensisioure/n-ai-ssance/actions)

A public Grok skill library for people who work with coding agents and lose the thread.

It gives you five portable procedures: map a session instead of dumping the chat, list what you have, reconstruct a day from files on disk, write a goal fence, and land a capture with a manifest.

No API keys. No network calls. No desktop suite.

## Why

Agent work leaves large transcripts and many session folders. Pasting everything is expensive. Closing a chat can feel like losing the day. Starting without a written goal invites thrash. Temporary captures disappear.

n-ai-ssance is those habits as installable Grok skills.

## Skills

- `/session-map` — identity, a copy-ready relay line, user spine, paths. Not a transcript.
- `/scan-sessions` — inventory of local Grok, Claude, and Cursor sessions. No board server.
- `/reconstruct` — re-read a day from files on disk. Nothing is streamed or cached.
- `/intent` — write outcome, surface, and fence before the work grows.
- `/durable-land` — copy first into a stamped folder with `MANIFEST.json` and `INDEX.md`.

## Install

Requires Python 3 and a Grok skills directory.

```bash
git clone https://github.com/theRensisioure/n-ai-ssance.git
cd n-ai-ssance
python skills/install_to_grok.py
```

This copies each skill plus `_lib` into:

- Windows: `%USERPROFILE%\.grok\skills\`
- macOS / Linux: `~/.grok/skills/`

Override the destination with `N_AI_SSANCE_GROK_SKILLS`.

Then, in Grok: `/session-map` · `/scan-sessions` · `/reconstruct` · `/intent` · `/durable-land`

You can also run the scripts under `skills/*/scripts/` without installing.

## Verify

```bash
python scripts/sterile-check.py
python -m pytest tests -q
```

CI on `main` runs the same checks.

## What this is not

n-ai-ssance is not a session host, not a voice journal, not an alarm daemon, and not an editor. It does not replace Artifact Scanner, Circadia, Sesefus, or AyTree. Those are separate products. The skills work without them.

It is not a hosted memory service. It does not claim to solve every workflow.

## Related products

When a skill is not enough, these are the sibling hosts — optional, not required:

- [Artifact Scanner](https://github.com/Zychs/artifact-scanner) — native Windows finder. Maps sessions in a window. Nearly done.
- Circadia — local timekeeper. Scheduler exists; the product is not finished. No public repository yet.
- [Sesefus](https://github.com/Zychs/sesefus) — voice journal.
- [AyTree](https://github.com/Zychs/AyTree) — version control for dyslexic readers.

## Documentation

- [docs/FOR-READERS.md](docs/FOR-READERS.md) — longer overview
- [docs/use-cases/](docs/use-cases/) — synthetic scenarios
- [PRODUCT.md](PRODUCT.md) — scope lock
- [STERILE.md](STERILE.md) — no secrets, transcripts, or personal dumps
- [docs/INDEX.md](docs/INDEX.md) — full map
- [wiki/Home.md](wiki/Home.md) — first wiki plate: *rain into order* (negentropic-matrix)

## Contribute

Keep the tree sterile. Run `python scripts/sterile-check.py` before every push. Do not commit live sessions, keys, journal audio, or real home-directory dumps.

## License

[MIT](LICENSE). Copyright theRensisioure and Zychs, 2026.

This public library is not the private prompt vault also historically named naissance.
