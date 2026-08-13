# n-ai-ssance

A **public Grok skill library**. MIT.

Five portable skills for people who work with coding agents and keep losing the thread: map a session (do not dump the chat), scan what you have, reconstruct a day from disk, fence intent, land a capture with a manifest.

No API keys. No network. No desktop suite required.

**License:** [MIT](LICENSE).  
**Public home:** [theRensisioure/n-ai-ssance](https://github.com/theRensisioure/n-ai-ssance).  
**Copied from** private `Zychs/ssfs` (scanner-shaped skills). Original stays. See [SOURCE.md](SOURCE.md).  
**Not** private `Zychs/naissance` (a different, closed prompt vault).

## Skills

| Slash | Job |
|-------|-----|
| `/session-map` | Map a session — not a chat dump |
| `/scan-sessions` | List sessions without a board server |
| `/reconstruct` | Re-member a day from files on disk |
| `/intent` | Outcome · surface · fence packet |
| `/durable-land` | Copy-first stamped land + MANIFEST |

## Install (Grok)

1. Clone this repo (or copy `skills/`).
2. Run:

```text
python skills/install_to_grok.py
```

That copies each skill plus `_lib` into `%USERPROFILE%\.grok\skills\` (Windows) or `~/.grok/skills/` (macOS / Linux). Override with `NAISSANCE_GROK_SKILLS` (or `SSFS_GROK_SKILLS`).

3. Smoke: `/session-map` · `/scan-sessions` · `/reconstruct` · `/intent` · `/durable-land`

## What this is not

- Not Artifact Scanner’s window (`board.html`, `:8765`, suite flip/zip)
- Not Circadia (the Zig alarm daemon — **not done**)
- Not Sesefus (the voice journal)
- Not AyTree (version control for dyslexics)
- Not a claim to solve every workflow

Those are **siblings**. Skills work without them.

## Breadcrumbs to the paid / richer hosts

n-ai-ssance is the free public trail. When a skill is not enough, the host is:

- **Artifact Scanner** — Windows finder. Maps sessions in a native window. Nearly done. [Zychs/artifact-scanner](https://github.com/Zychs/artifact-scanner)
- **Circadia** — keeps time. Scheduler wired. Product not finished. No public GitHub remote yet; do not pretend it shipped
- **Sesefus** — voice journal. [Zychs/sesefus](https://github.com/Zychs/sesefus)
- **AyTree** — version control for dyslexics. [Zychs/AyTree](https://github.com/Zychs/AyTree)

Do not swallow them into one app. Do not require them to use these skills. Marketing lives on the [portfolio Instruments page](https://zychs.github.io/pages/instruments.html) and [MARKETING.md](https://github.com/Zychs/zychs.github.io) (local tree if Pages is not live).

## Sterile (hard law)

No live sessions, keys, journal audio, or real home-path dumps.  
`python scripts/sterile-check.py` must exit 0 before push.  
[STERILE.md](STERILE.md).

## Docs

- Calm overview: [docs/FOR-READERS.md](docs/FOR-READERS.md)
- Product lock: [PRODUCT.md](PRODUCT.md)
- Use cases (synthetic): [docs/use-cases/](docs/use-cases/)
