# Claude Agent Skills — Public Collection

A curated set of agent skills for Claude Code, Claude Desktop, and any [agentskills.io](https://agentskills.io)-compatible platform. Each skill is a self-contained SKILL.md file with optional bundled references, scripts, and assets.

## Install

**Claude Code / Claude Desktop:**
```
~/.claude/skills/<skill-name>/
```

**Codex:**
```
~/.codex/skills/<skill-name>/
```

**Cursor:**
```
~/.cursor/skills/<skill-name>/
```

Clone or download a skill folder and place it in the appropriate directory for your platform. Each skill activates when its MANDATORY TRIGGERS appear in a prompt.

## Skills

| Skill | Description |
|-------|-------------|
| [1pw-env](skills/1pw-env/) | 1Password credential management for development environments — sync secrets to `~/.env.mcp` via `op` CLI |
| [claude-md-forge](skills/claude-md-forge/) | Distill source material (docs, transcripts, codebases) into optimized CLAUDE.md / AGENTS.md files |
| [claude-release-guide](skills/claude-release-guide/) | Convert source material about a Claude product release into a verified, teaching-grade implementation guide |
| [contract-redliner](skills/contract-redliner/) | Pre-legal contract risk review against a company playbook — flags green, yellow, and red issues before legal sees it |
| [document-skills](skills/document-skills/) | Universal document creation and conversion across Markdown, PDF, PPTX, and DOCX formats |
| [gamma-claude-skill](skills/gamma-claude-skill/) | Optimize and produce content specifically for the Gamma.app presentation platform |
| [github-repo-setup](skills/github-repo-setup/) | Universal GitHub repository setup — README, .gitignore, branch protection, CI scaffolding |
| [gmail-inbox-command](skills/gmail-inbox-command/) | Forensic Gmail inbox audit and ongoing management using the Gmail MCP connector |
| [gpt-5-6-relay](skills/gpt-5-6-relay/) | Route tasks to GPT-5.6 threads (Sol/Terra/Luna tiers) via API relay |
| [instagram-carousel-forge](skills/instagram-carousel-forge/) | Produce Instagram carousel PNG sets from any content input |
| [interactive-checklist-skill](skills/interactive-checklist-skill/) | Build interactive HTML checklists with progress tracking, completion states, and export |
| [linkedin-carousel-forge](skills/linkedin-carousel-forge/) | Produce LinkedIn carousel PDFs and infographic PDFs from content input — configure brand tokens in `config.example.md` |
| [logo-designer](skills/logo-designer/) | AI-assisted logo concept and prompt generation using professional design studio methodologies |
| [loop-goal-triage](skills/loop-goal-triage/) | Triage any task to the right execution method: plain prompt, /goal, /loop, dynamic workflow, or Routine |
| [plan-execute-router](skills/plan-execute-router/) | Split plan and execute phases to different Claude tiers for cost optimization |
| [project-doc-refresh](skills/project-doc-refresh/) | Three-phase audit → research → diff workflow to keep project documentation current |
| [project-orchestrator](skills/project-orchestrator/) | Decompose projects into routed task plans across Claude Cowork, Claude Code, Cursor, Warp.dev, n8n, and other AI tools |
| [skill-architect](skills/skill-architect/) | Create, audit, improve, and package agent skills following the agentskills.io open standard |
| [skill-creator](skills/skill-creator/) | Step-by-step guide for creating new agent skills from scratch |
| [skill-translate](skills/skill-translate/) | Port skills across platforms (Claude Code ↔ Codex ↔ Cursor ↔ deepagents) |
| [slack-gif-creator](skills/slack-gif-creator/) | Create animated GIFs and emoji animations optimized for Slack size constraints |
| [sop-generator](skills/sop-generator/) | Generate structured Standard Operating Procedures from process descriptions |
| [tiktok-carousel-forge](skills/tiktok-carousel-forge/) | Produce TikTok vertical carousel PNG sets — configure brand tokens in `config.example.md` |
| [trafilatura-research](skills/trafilatura-research/) | Web content extraction and research using Trafilatura and related scraping tools |
| [vibe-code-skill](skills/vibe-code-skill/) | Vibe-coding workflow guidance for rapid AI-assisted software prototyping |
| [web-app-builder](skills/web-app-builder/) | Generate self-contained HTML/CSS/JS web apps and interactive tools from specifications |
| [web-design-builder](skills/web-design-builder/) | Build production-quality web pages with modern CSS, accessibility, and framework guidance |
| [youtube-screen-share-forge](skills/youtube-screen-share-forge/) | Produce branded full-screen HTML presentation slides for YouTube screen sharing via Ecamm Live — configure brand tokens in `config.example.md` |

## Configuring brand tokens

Skills that produce branded visual outputs (carousel forges, screen-share forge) include a `config.example.md` with placeholder brand values. Copy it to `config.md` and fill in your colors, wordmark, tagline, and CTA URLs before use.

## License

MIT — see [LICENSE](LICENSE). Exception: `skills/slack-gif-creator/` is Apache 2.0.
