# Skill Triage

One row per SKILL.md-bearing folder. Verdicts: PUBLISH, PUBLISH-AFTER-GENERALIZATION, PRIVATE, ARCHIVE, THIRD-PARTY, UNREAD.

## Detector baseline (updated after each batch)

```
CLEAN — no personal/sensitive content detected.
```
_(final pass: 28 skills published, 31 SKILL.md files including document-skills sub-skills)_

---

## Triage Table

| Skill | Verdict | Reason | Effort | Notes |
|-------|---------|--------|--------|-------|
| **claude-md-forge** | PUBLISH | Original, self-contained, no personal content; excellent methodology for distilling source material into CLAUDE.md/AGENTS.md | low | Changed license from Proprietary → MIT |
| **gpt-5-6-relay** | PUBLISH | Original, clean, portable; routes tasks across GPT-5.6 tier threads (Sol/Terra/Luna) | low | — |
| **plan-execute-router** | PUBLISH | Original, clean, portable; plan→execute cost-split with fit-check and multi-path executor routing | low | Changed license from Proprietary → MIT |
| **template-skill** | ARCHIVE | Stub file only — two-line placeholder with no method | low | Nothing to publish |
| **tiktok-carousel-forge** | PUBLISH-AFTER-GENERALIZATION | Solid Playwright-rendered carousel skill; brand wordmark and tagline were hardcoded in tt-reflow-rules.md | medium | Generalized: brand tokens extracted to config.example.md; "Carbon Forge" and private skill cross-references removed |
| **vibe-marketing** | THIRD-PARTY | Core methodology and reference files (including full transcript) are from James Dickerson / @boringmarketer YouTube content (https://www.youtube.com/watch?v=fVUlrpaWNxg) | — | Cannot republish without attribution and permission |
| **webapp-testing** | ARCHIVE | LICENSE.txt referenced in frontmatter but missing; referenced scripts (with_server.py, examples/) also missing — incomplete | — | `license: Complete terms in LICENSE.txt` suggests possible third-party origin |

---

## Batch 2 (complete)

| Skill | Verdict | Reason | Effort | Notes |
|-------|---------|--------|--------|-------|
| **deep-research-1** | ARCHIVE | `metadata: origin: ECC` indicates third-party origin; folder named with `-1` suffix but skill name is `deep-research` — appears to be a local copy, not an original; superseded by the currently installed `deep-research` skill | — | ECC unexplained; provenance uncertain → resolve toward not publishing |
| **project-doc-refresh** | PUBLISH | Original, complete three-phase audit→research→diff methodology; no personal content | low | — |
| **skill-creator** | PUBLISH-AFTER-GENERALIZATION | Original guide for creating skills; was deepagents-CLI specific; generalized Skill Location section to cover Claude Code, Codex, Cursor, deepagents | low | `compatibility: designed for deepagents-code` frontmatter left as informational note |
| **instagram-carousel-forge** | PUBLISH-AFTER-GENERALIZATION | Solid PNG-copy-and-caption skill; "Carbon Forge platform rules" and branded hashtag example were in references | low | Removed brand-specific hashtag example; updated `Carbon Forge` → generic references |
| **interactive-checklist-skill** | PUBLISH-AFTER-GENERALIZATION | Excellent HTML checklist builder; "Carbon Forge" and `full/REFIT` references in SKILL.md and design-tokens.md; also had wrong file structure (references at root not in `references/`) | medium | Fixed file structure; renamed design system section; updated design-tokens.md label |
| **loop-goal-triage** | PUBLISH-AFTER-GENERALIZATION | Strong execution-method triage skill; worked example had `fullrefit.co` domain and "Paul" personal name in one SKILL.md line | low | Replaced `fullrefit.co` → `example.com`; replaced "Paul" → "the user" |
| **start-session** | PRIVATE | Core functionality depends on Open Brain (private MCP), references private surfaces (Proof, ClaudeClaw); not portable without those systems | — | Methodology is sound but implementation is inseparable from private infrastructure |

---

## Batch 3 (complete)

| Skill | Verdict | Reason | Effort | Notes |
|-------|---------|--------|--------|-------|
| **web-app-builder** | PUBLISH-AFTER-GENERALIZATION | Solid markdown→HTML skill; "Carbon Forge" design system name throughout and "Paul Chambers" in a reference HTML example | medium | Renamed design system refs to "default design system (Carbon Forge)"; replaced `Paul Chambers` → `Your Name` in example |
| **gamma-claude-skill** | PUBLISH | Clean, portable Gamma.app optimization skill; no personal content | low | — |
| **last-chance-intel-recovery** | PRIVATE | Depends on Open Brain MCP and private save/ingest formats (db-brain-inbox, openbrain-thought-formats.md); implementation inseparable from private systems | — | The triage methodology is sound but unextractable |
| **sop-generator.skill** | PUBLISH-AFTER-GENERALIZATION | Good SOP generation skill; no personal content; but SKILL.md had no frontmatter and folder name had `.skill` suffix | low | Added valid frontmatter; renamed folder slug to `sop-generator` |
| **logo-designer** | PUBLISH | Original AI logo prompt generation skill using design studio methodologies; personal content was only in a PROJECT-HANDOFF.md dev artifact in references/ | low | Removed PROJECT-HANDOFF.md (development artifact, not part of the skill) |
| **deep-save-skill** | PRIVATE | Depends on Open Brain MCP; line in SKILL.md names Paul directly ("behavior Paul wants across LLMs"); implementation is tied to private knowledge management infrastructure | — | — |
| **github-repo-setup** | PUBLISH-AFTER-GENERALIZATION | Strong universal repo-setup skill; README had "Built for Paul Chambers / Full Refit" attribution line; license was "Proprietary" | low | Removed attribution; changed license to MIT |
| **proof** | THIRD-PARTY | `metadata: author: Proof / Every`; designed for proofeditor.ai (EveryInc product); upstream: github.com/EveryInc/ | — | MIT licensed by original authors; but this is their official skill, not ours to republish standalone |

---

## Batch 4 (complete)

| Skill | Verdict | Reason | Effort | Notes |
|-------|---------|--------|--------|-------|
| **claude-release-guide** | PUBLISH-AFTER-GENERALIZATION | Strong Claude release teaching skill; had "Paul teaches", "Full Refit / Carbon Forge voice", "Full Refit's ICP" in 3 places | low | Replaced all personal references with generic equivalents |
| **open-brain-archaeology** | PRIVATE | Explicitly depends on Open Brain MCP and Obsidian vault at personal path `/Users/paul/ObsidianVault/`; not portable without those systems | — | — |
| **trafilatura-research** | PUBLISH-AFTER-GENERALIZATION | Good web extraction skill; personal content was only install path examples in README | low | Replaced `/Users/paul/.codex/...` etc. with `~/.codex/...` etc. |
| **youtube-researcher** | THIRD-PARTY | README states "Source: https://github.com/rbrown101010/Rileys-Top-Skills/..." — this is Riley Brown's skill from their public collection | — | Cannot republish as if original |
| **skill-translate** | PUBLISH-AFTER-GENERALIZATION | Excellent cross-platform skill porting tool; personal content was only in Hermes path examples in references | low | Replaced `/Users/paul/hermes-agent/` → `~/.hermes-agent/` in references; SKILL.md was already clean |
| **1pw-env** | PUBLISH-AFTER-GENERALIZATION | Solid 1Password credential management workflow; personal vault names (Supabase fullREFIT CLI, n8n fullREFIT API Key), account name, and absolute paths in references | medium | Generalized vault entry names; replaced personal paths with placeholders |
| **story-miner** | PRIVATE | Depends on Open Brain MCP, chat-archaeology skill, personal content paths, Dropbox db-brain-inbox. "Paul Test" named in description. | — | — |
| **deep-save-skill** | PRIVATE | Depends on Open Brain MCP; directly names Paul; tied to private save/ingest infrastructure | — | _(dup of batch 3)_ |

---

## Batch 5 (complete)

| Skill | Verdict | Reason | Effort | Notes |
|-------|---------|--------|--------|-------|
| **slack-gif-creator** | PUBLISH | Original, Apache 2.0 LICENSE.txt present and intact; self-contained GIF/animation toolkit for Slack | low | — |
| **web-design-builder** | PUBLISH | Original, clean; all `@` hits are CSS/Alpine.js directives and npm packages, not personal email | low | — |
| **vibe-code-skill** | PUBLISH | MIT, clean, no personal content; portable vibe-coding workflow | low | — |
| **theme-factory** | ARCHIVE | `license: Complete terms in LICENSE.txt` but LICENSE.txt is missing — same red flag as webapp-testing | — | — |
| **clearpath** | PRIVATE | Description says "for full/REFIT"; the naming convention rules (LF/SF/LIC/LI prefixes) are the author's personal content production system — generalizing them out leaves a shell | — | — |
| **contract-redliner.skill** | PUBLISH-AFTER-GENERALIZATION | Original, solid pre-legal contract risk skill; SKILL.md had no frontmatter; folder name had `.skill` suffix | low | Added frontmatter; renamed folder to `contract-redliner` |
| **document-skills** | PUBLISH-AFTER-GENERALIZATION | Original router to docx/pptx/pdf sub-skills; pptx and pdf sub-SKILL.md files had `Proprietary. LICENSE.txt has complete terms` with no LICENSE.txt present | low | Fixed sub-skill license fields to MIT |
| **skill-architect** | PUBLISH-AFTER-GENERALIZATION | Original, thorough skill-creation guide; only issue was `license: "Proprietary"` | low | Changed license to MIT; Anthropic citation link is a reference, not upstream |
| **claude-code-project-orchistrator** | PUBLISH-AFTER-GENERALIZATION | Original multi-platform project orchestrator; no personal content; contained Perplexity research dev-artifact in references/ (ChrisWiles URL was a footnote citation); no license field | low | Added license: MIT; excluded research doc from references/; published as `project-orchestrator` |
| **Gmail-inbox-command-skill** | PUBLISH-AFTER-GENERALIZATION | Original Gmail forensic audit skill; 0 personal content hits; but reference files were at root level, not in references/ as SKILL.md expected | low | Moved files into references/; removed internal v2 subfolder; published as `gmail-inbox-command` |
| **linkedin-carousel-forge** | PUBLISH-AFTER-GENERALIZATION | Solid LinkedIn carousel/infographic PDF skill; "Carbon Forge" brand system, `#FullRefit` hashtags, `fullrefit.com/skool` CTA URL, and absolute path in 5 files | medium | Generalized brand refs; replaced hashtag → `#YourBrand`; extracted brand tokens to config.example.md; removed skill-ref dev artifact; renamed carbon-forge-slide-system.md → slide-system.md |
| **youtube-screen-share-forge-SKILL** | PUBLISH-AFTER-GENERALIZATION | Excellent Ecamm Live screen-share slide skill; "Paul" named throughout SKILL.md and detail.md; `fullrefit-brand-context` dependency; FULLREFIT.COM/SKOOL CTA; editorial-discipline-gate.md was entirely personal | medium | Replaced all "Paul" → "the presenter/creator"; removed private skill dependency; replaced CTA → configurable placeholder; rewrote editorial-discipline-gate.md as generic creator editorial guide; added config.example.md |
| **yt-pipeline** | PRIVATE | Description says "Full Refit YouTube production pipeline"; entire workflow (idea gate → video spec → production files) is tied to personal content production system | — | — |
| **presentation-deck-builder** | PRIVATE | Description embeds absolute path `/Users/paul/dev-4/1-fullREFIT/...` and "Carbon Forge brand/copy rules"; requires private local project | — | — |
| **smart-research-engine** | ARCHIVE | Requires bespoke Python MCP server at personal path; references include private chat recap and personal development artifacts; too tool-specific to be useful standalone | — | — |
| **script-to-lead-magnet-skill** | PRIVATE | Description hardcodes "Full Refit YouTube script", "ICA and Marcus alignment", "Carbon Forge brand requirements" — inseparable from personal brand workflow | — | — |
| **lead-magnet-page-generator** | PRIVATE | Description says "Carbon Forge design system (full/REFIT brand)" and "fullrefit.com page"; inseparable from personal brand | — | — |
| **n8n-preflight** | PRIVATE | Description references `fullrefit.app.n8n.cloud` (personal cloud instance); checks personal 1Password and n8n setup | — | — |
| **linkedin-post-text** | PRIVATE | Applies "Marcus test" (private ICA persona), "22-tool first-comment library" with fullrefit.com URLs, personal content numbering system (F##) | — | — |
| **content-idea-extraction** | PRIVATE | "Full Refit idea extraction", "ICA filter", writes to personal CONTENT-ASSET-MAP.md | — | — |
| **editorial-discipline-content-audit-and-revise** | PRIVATE | "full/REFIT content" scope, "Marcus test", Four-Module TOV OS — scoped entirely to author's content | — | — |
| **youtube-script-skill** | PRIVATE | Description says "Full/REFIT work only" — designed exclusively for the author's YouTube channel | — | — |
| **qmd** | PRIVATE | "Search Paul's local QMD pilot index" — personal local search engine for private docs | — | — |
| **script-forge** | PRIVATE | "Full Refit's content strategy", "full/REFIT Four-Module TOV OS" | — | — |
| **lead-attribution-cta** | PRIVATE | "full/REFIT single source of truth", fullrefit.co links, personal UTM/HeyReach/Apollo system | — | — |
| **vibe-coding-router** | PRIVATE | Description says "Use when Paul is building", references personal tools (GStack, Hermes Mobile PWA) | — | — |
| **proof-shortio-airtable** | PRIVATE | Integrates three private services (Proof, Short.io, Airtable) for fullrefit.co link workflow | — | — |
| **full-content-audit** | PRIVATE | "Full Refit content inventory", Four-Module TOV OS — personal content audit system | — | — |
| **brand-voice-engine** | PRIVATE | Explicitly "Paul Chambers' voice for full/REFIT" — by definition a personal brand voice engine | — | — |
| **tracker-SOP-knowledgebase-skill_2** | PRIVATE | "Tracker Products" (author's product brand), Nexus knowledge base | — | — |
| **content-package-spec** | PRIVATE | "full/REFIT content package", absolute path `/Users/paul/dev-4/task-orchestrator/` | — | — |
| **content-os-conductor** | PRIVATE | "full/REFIT 60-Day Content Sprint", Four-Module TOV OS, private sprint workspace | — | — |
| **content-miner-60** | PRIVATE | "60-day video sprint", Carbon Forge carousel PDFs — personal content sprint system | — | — |
| **fullrefit-revenue-generation-plan** | PRIVATE | Operates "full/REFIT revenue generation plan" — personal business planning system | — | — |
| **rev-content-1-triage** | PRIVATE | Step 1 of Revenue Content Pipeline; writes to personal Airtable Ideas table | — | — |
| **rev-content-2-produce** | PRIVATE | Step 2 of Revenue Content Pipeline; "full/REFIT content package", Carbon Forge | — | — |
| **rev-content-3-advance** | PRIVATE | Step 3 of Revenue Content Pipeline; mints n8n autoposter rows, Hermes-gated | — | — |
