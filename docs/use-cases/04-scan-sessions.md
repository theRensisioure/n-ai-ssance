# Use case · Scan sessions (no board server)

## Situation (synthetic)

Alex is on a laptop without the desktop suite running.  
Needs: “which Grok sessions touched **example-app** this week?”  
No `:8765`, no WebView host.

## Approach

**Scan** known session roots on disk (Grok / Claude / Cursor layouts as available):

- List path, project, **meaning-first title** (not id slice)  
- Optional filter by project name or recency  

Agent procedure + local paths only.

## Benefit

- Inventory works in pure CLI/agent environments  
- Community users get scanner-shaped behavior **without** installing a suite  
- Titles stay human-readable for handoff  

## If skipped

Alex opens the newest chat by habit; the real decision thread stays buried under a uuid.
