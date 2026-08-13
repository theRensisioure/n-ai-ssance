# Use case · Durable land (copy-only)

## Situation (synthetic)

Alex drops a screen recording and a notes file into a capture inbox for **example-app** demo prep.  
Needs a **stamped** place that survives cleanup scripts.  
Must not delete the originals by accident.

## Approach

**Durable land**:

- Copy into `lands/<stamp>/` with `MANIFEST` + index  
- Move only with an explicit flag (default copy)  
- Keep separate from chat-diff archives  

## Benefit

- Capture testing has a real sink without “AI archive” mystique  
- Provenance is boring and checkable  
- Mistakes are recoverable (originals remain)  

## If skipped

Demo assets live in Downloads forever, or vanish in a “cleanup” that nobody can reverse.
