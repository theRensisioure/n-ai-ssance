# Working with agent sessions without losing the thread

**n-ai-ssance** is a public Grok skill library (MIT) — a small set of practices for people who use coding agents heavily and need **reliable handoff, recovery, and scope control**. It draws on ideas proven in local session-finding tools, but it does **not** require a desktop suite, a local web server, or a particular product install. The skills work without Artifact Scanner, Circadia, Sesefus, or AyTree. Those are sibling products; this page is the free trail.

This page is the calm overview. For product boundaries, see [PRODUCT.md](../PRODUCT.md). For install, see [README.md](../README.md).

## The problem in plain terms

Agent work produces large transcripts and many session folders. When the next person (or the next agent, or future you) needs context, pasting everything is expensive and noisy. Closing a chat can feel like losing the day. Starting without a written goal invites thrash. Captures land in temporary folders and disappear.

None of that requires a new ideology. It requires a few **disciplined procedures**.

## Five approaches

### 1. Prefer a session map over a transcript dump

A useful handoff includes who/what/when, a short relay line a human can paste, the user’s actual requests in order, and paths worth opening. It does not include the full message log.

**Benefit:** Faster orientation, lower token cost, fewer repeated mistakes.

### 2. Reconstruct the day from files on disk

Treat day boards, pins, and artifacts as the durable record. A new session should re-read those files rather than pretend to continue an old process in memory.

**Benefit:** Recovery after interrupt without depending on a single live chat.

### 3. Fence intent before expanding scope

When no goal packet exists, answer three things: desired outcome, where it lives, and what is out of scope. Write that down for the session.

**Benefit:** Less dual-tracking; clearer “no” for detours.

### 4. Scan sessions as an inventory

List recent sessions with readable titles and project hints from local paths—no board UI required.

**Benefit:** Find the right thread without launching a suite or guessing by recency alone.

### 5. Land captures with copy-first provenance

Move important files into a stamped directory with a small manifest. Default to copy so originals remain.

**Benefit:** Demo and review assets stay findable; accidents stay recoverable.

## How to use this repository

- **Skills** (as they ship) install into your Grok skills directory.  
- **Use cases** under `docs/use-cases/` show synthetic scenarios (no real personal data).  
- **Author inquiry prompts** under `docs/socratic/` are optional deep work for maintainers; they are not required to use the skills.  
- **Sterile policy** (`STERILE.md`) keeps the repository free of secrets, transcripts, and personal dumps—even while private.

## What this project is not

It is not a replacement for your editor, not a hosted “AI memory,” and not a merge of unrelated products. It does not claim to solve every workflow problem. It aims to make a few high-leverage session habits **portable and teachable**.

When you want the window, the timekeeper, the journal, or the tree — that is a sibling, not this pack. See the root README breadcrumbs.

## Further reading

- [docs/INDEX.md](INDEX.md) — documentation map  
- [docs/use-cases/](use-cases/) — concrete scenarios  
- [STERILE.md](../STERILE.md) — contribution safety  
