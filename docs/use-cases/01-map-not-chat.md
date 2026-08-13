# Use case · Map, not chat dump

## Situation (synthetic)

Alex has three open agent sessions about **example-app** auth.  
River asks: “Where did we leave the login bug?”  
Alex’s instinct is to paste a 400-line transcript into chat.

## Approach

Treat the session as a **map**:

- Identity (agent, project, when)  
- **Relay** (copy-ready one-liner for a human)  
- User spine (what Alex actually asked, tabbed)  
- Paths touched  
- Find/open pointers  

No full `chat_history` dump into the working thread.

## Benefit

- River gets a **usable handoff in under a minute**  
- Alex keeps context window for the next decision, not archaeology  
- Meaning stays in the **title/spine**, not a sliced id  

## If skipped

The next agent re-derives the same history from raw jsonl, burns tokens, and still misses the one decision Alex already made.
