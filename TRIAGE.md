# Skill Triage

One row per SKILL.md-bearing folder. Verdicts: PUBLISH, PUBLISH-AFTER-GENERALIZATION, PRIVATE, ARCHIVE, THIRD-PARTY, UNREAD.

## Detector baseline (updated after each batch)

```
CLEAN — no personal/sensitive content detected.
```
_(final pass: 31 skills published)_

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
| **theme-factory** | ARCHIVE | `license: Complete terms in LICENSE.txt` but LICENSE.txt is missing — same red flag as webapp-testing | — | — |
| **skill-architect** | PUBLISH-AFTER-GENERALIZATION | Original, thorough skill-creation guide; only issue was `license: "Proprietary"` | low | Changed license to MIT; Anthropic citation link is a reference, not upstream |
| **claude-code-project-orchistrator** | PUBLISH-AFTER-GENERALIZATION | Original multi-platform project orchestrator; no personal content; contained Perplexity research dev-artifact in references/ | low | Added license: MIT; excluded research doc from references/; published as `project-orchestrator` |
| **linkedin-carousel-forge** | PUBLISH-AFTER-GENERALIZATION | Solid LinkedIn carousel/infographic PDF skill; personal brand tokens, hashtags, CTA URL, and absolute path in 5 files | medium | Generalized brand refs; extracted brand tokens to config.example.md |
| **youtube-screen-share-forge-SKILL** | PUBLISH-AFTER-GENERALIZATION | Excellent Ecamm Live screen-share slide skill; personal name throughout SKILL.md and detail.md; private skill dependency; personal CTA; personal editorial gate | medium | Replaced personal refs with generic equivalents; added config.example.md |
| **yt-pipeline** | PRIVATE | Personal YouTube production pipeline inseparable from personal content system | — | — |
| **presentation-deck-builder** | PRIVATE | Requires private local project at personal absolute path | — | — |
| **smart-research-engine** | ARCHIVE | Requires bespoke Python MCP server at personal path; not usable standalone | — | — |
| **script-to-lead-magnet-skill** | PRIVATE | Personal brand workflow — personal YouTube channel + audience persona + design system | — | — |
| **lead-magnet-page-generator** | PRIVATE | Personal brand/domain dependency in description | — | — |
| **n8n-preflight** | PRIVATE | References personal n8n cloud instance | — | — |
| **linkedin-post-text** | PRIVATE | Private ICA persona, personal URL library, personal content numbering system | — | — |
| **content-idea-extraction** | PRIVATE | Personal content idea system with private output path | — | — |
| **editorial-discipline-content-audit-and-revise** | PRIVATE | Scoped entirely to personal content brand | — | — |
| **youtube-script-skill** | PRIVATE | Designed exclusively for author's YouTube channel | — | — |
| **qmd** | PRIVATE | Personal local search engine for private docs | — | — |
| **lead-attribution-cta** | PRIVATE | Personal UTM/CRM system with personal domain links | — | — |
| **full-content-audit** | PRIVATE | Personal content audit system | — | — |
| **brand-voice-engine** | PRIVATE | Personal brand voice engine by definition | — | — |
| **tracker-SOP-knowledgebase-skill_2** | PRIVATE | Personal product brand + private knowledge base | — | — |
| **content-package-spec** | PRIVATE | Personal content package spec with personal absolute path | — | — |
| **content-os-conductor** | PRIVATE | Personal content sprint system | — | — |
| **content-miner-60** | PRIVATE | Personal content sprint system | — | — |
| **fullrefit-revenue-generation-plan** | PRIVATE | Personal business planning system | — | — |
| **rev-content-1-triage** | PRIVATE | Personal Revenue Content Pipeline step 1 | — | — |
| **rev-content-2-produce** | PRIVATE | Personal Revenue Content Pipeline step 2 | — | — |
| **rev-content-3-advance** | PRIVATE | Personal Revenue Content Pipeline step 3 | — | — |

---

## Batch 6 (complete)

Skills initially assessed as PRIVATE but confirmed as author's original work and publishable after generalization. Also: 5 skills removed retroactively (not original work).

| Skill | Verdict | Reason | Effort | Notes |
|-------|---------|--------|--------|-------|
| **web-design-builder** | REMOVED | Initially published; confirmed third-party or not original work | — | Removed from public tree |
| **vibe-code-skill** | REMOVED | Initially published; confirmed not original work | — | Removed from public tree |
| **contract-redliner** | REMOVED | Initially published; confirmed not original work | — | Removed from public tree |
| **document-skills** | REMOVED | Initially published; confirmed not original work | — | Removed from public tree |
| **gmail-inbox-command** | REMOVED | Initially published; confirmed not original work | — | Removed from public tree |
| **prep-project** | PUBLISH-AFTER-GENERALIZATION | Original project→executor spec skill; personal paths, brand name, and personal email in reference examples | medium | Replaced all personal paths/names with `{OUTPUT_ROOT}` and generic placeholders across 3 reference templates |
| **vibe-coding-router** | PUBLISH-AFTER-GENERALIZATION | Original SDLC phase-routing skill; personal name, tool names (GStack, Hermes PWA), absolute paths throughout | medium | Replaced all personal refs with generic "you/your" and tool-agnostic descriptions |
| **clearpath** | PUBLISH-AFTER-GENERALIZATION | Original file/folder naming convention system; brand attribution in description and README | low | Removed "for [brand]" attribution; naming system (LF/SF/LIC/LI prefixes) published as-is |
| **proof-shortio-airtable** | PUBLISH-AFTER-GENERALIZATION | Original Proof + Short.io + Airtable automation; personal domain and Airtable IDs hardcoded in scripts | medium | Replaced all personal values with env var references (`${SHORT_IO_DOMAIN}`, `${AIRTABLE_BASE_ID}`, etc.) |
| **script-forge** | PUBLISH-AFTER-GENERALIZATION | Original YouTube script writing skill; personal brand name, audience persona name, personal path refs, personal editorial gate | medium | Replaced all personal brand/persona refs with generic creator/audience equivalents; abstracted paths |
| **deep-save** | PUBLISH-AFTER-GENERALIZATION | Original knowledge MCP extraction skill; personal name in description, personal paths, personal person-note example | low | Replaced personal name/path refs; kept Open Brain MCP name but marked as optional/pluggable dependency |
| **start-session** | PUBLISH-AFTER-GENERALIZATION | Original session-start skill; personal paths, personal tool ref (Proof as "cockpit"), ClaudeClaw internal name | low | Replaced personal paths; generalized Proof ref; removed ClaudeClaw; Open Brain kept as optional dependency |
| **signal-scanner** | PUBLISH-AFTER-GENERALIZATION | Original build-activity content scanner; deeply embedded in personal business context, 60+ personal paths, personal audience persona | high | Complete business-context rewrite using template placeholders; all paths genericized; audience persona structure kept, values replaced |
