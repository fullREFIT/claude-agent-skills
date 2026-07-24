# Private Triage Notes

This file documents every PRIVATE, ARCHIVE, and THIRD-PARTY decision made during the public release review. Kept here so future batches can reference the reasoning without re-reading source files.

---

## THIRD-PARTY (cannot republish as original)

| Skill | Reason |
|-------|--------|
| **vibe-marketing** | Core methodology and reference files (including full YouTube transcript) are from James Dickerson / @boringmarketer. Source: https://www.youtube.com/watch?v=fVUlrpaWNxg |
| **youtube-researcher** | README explicitly states "Source: https://github.com/rbrown101010/Rileys-Top-Skills/..." — this is Riley Brown's skill |
| **proof** | `metadata.author: Proof / Every`; designed for proofeditor.ai (EveryInc product); upstream: github.com/EveryInc/ |

---

## ARCHIVE (incomplete, broken, or no standalone value)

| Skill | Reason |
|-------|--------|
| **template-skill** | Stub file only — two-line placeholder with no method |
| **webapp-testing** | LICENSE.txt referenced in frontmatter but missing; scripts also missing — incomplete and suspect provenance |
| **deep-research-1** | `metadata: origin: ECC` — third-party origin uncertain; folder named with `-1` suffix, appears to be a local copy |
| **theme-factory** | `license: Complete terms in LICENSE.txt` but LICENSE.txt is missing — same pattern as webapp-testing |
| **smart-research-engine** | Requires bespoke Python MCP server at personal path `/Users/paul/dev-4/smart-research-engine`; references include private chat recap and personal development artifacts; not usable standalone |

---

## PRIVATE (inseparable from personal infrastructure or brand)

### Open Brain MCP dependency
These skills depend on Open Brain, a private Supabase-backed knowledge management system:

| Skill | Reason |
|-------|--------|
| **start-session** | Core functionality depends on Open Brain MCP; references private surfaces (Proof, ClaudeClaw) |
| **last-chance-intel-recovery** | Depends on Open Brain MCP and private save/ingest formats |
| **deep-save-skill** | Depends on Open Brain MCP; directly names Paul |
| **story-miner** | Depends on Open Brain MCP, chat-archaeology, personal content paths, Dropbox db-brain-inbox |
| **open-brain-archaeology** | Explicitly depends on Open Brain MCP and Obsidian vault at `/Users/paul/ObsidianVault/` |

### Personal brand / content production OS
These skills are tied to the full/REFIT Revenue Content Pipeline, Brand Voice Engine, or personal workflow:

| Skill | Reason |
|-------|--------|
| **brand-voice-engine** | Explicitly "Paul Chambers' voice for full/REFIT" — by definition a personal brand voice engine |
| **clearpath** | Description says "for full/REFIT"; naming convention rules (LF/SF/LIC/LI prefixes) are the personal content production system |
| **content-idea-extraction** | "Full Refit idea extraction", ICA filter, writes to personal CONTENT-ASSET-MAP.md |
| **content-miner-60** | "60-day video sprint", Carbon Forge carousel PDFs — personal content sprint system |
| **content-os-conductor** | "full/REFIT 60-Day Content Sprint", Four-Module TOV OS, private sprint workspace |
| **content-package-spec** | "full/REFIT content package", absolute path `/Users/paul/dev-4/task-orchestrator/` |
| **editorial-discipline-content-audit-and-revise** | "full/REFIT content" scope, Marcus test, Four-Module TOV OS — scoped entirely to author's content |
| **fullrefit-revenue-generation-plan** | Operates "full/REFIT revenue generation plan" — personal business planning system |
| **lead-attribution-cta** | "full/REFIT single source of truth", fullrefit.co links, personal UTM/HeyReach/Apollo system |
| **lead-magnet-page-generator** | "Carbon Forge design system (full/REFIT brand)", "fullrefit.com page" in description |
| **linkedin-post-text** | Marcus/ICA persona, 22-tool first-comment library with fullrefit.com URLs, personal F## content numbering |
| **n8n-preflight** | References `fullrefit.app.n8n.cloud` (personal cloud instance); checks personal 1Password and n8n setup |
| **presentation-deck-builder** | Embeds absolute path `/Users/paul/dev-4/1-fullREFIT/...` in description; requires private local project |
| **proof-shortio-airtable** | Integrates three private services (Proof, Short.io, Airtable) for fullrefit.co link workflow |
| **qmd** | "Search Paul's local QMD pilot index" — personal local search engine for private docs |
| **rev-content-1-triage** | Step 1 of Revenue Content Pipeline; writes to personal Airtable Ideas table |
| **rev-content-2-produce** | Step 2 of Revenue Content Pipeline; "full/REFIT content package", Carbon Forge |
| **rev-content-3-advance** | Step 3 of Revenue Content Pipeline; mints n8n autoposter rows, Hermes-gated |
| **script-forge** | "Full Refit's content strategy", "full/REFIT Four-Module TOV OS" |
| **script-to-lead-magnet-skill** | "Full Refit YouTube script", "ICA and Marcus alignment", "Carbon Forge brand requirements" in description |
| **tracker-SOP-knowledgebase-skill_2** | "Tracker Products" (author's product brand), Nexus knowledge base |
| **vibe-coding-router** | "Use when Paul is building", references personal tools (GStack, Hermes Mobile PWA) |
| **yt-pipeline** | "Full Refit YouTube production pipeline"; entire workflow tied to personal content production system |
| **youtube-script-skill** | Description says "Full/REFIT work only" — designed exclusively for the author's YouTube channel |
