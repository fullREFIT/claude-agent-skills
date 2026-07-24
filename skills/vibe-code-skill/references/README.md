# Vibe Coding Orchestrator - Reference Documents

This directory contains comprehensive reference materials for autonomous AI-driven development using Claude Code.

## Quick Navigation

### Core Philosophy & Workflows
**File:** `../agentic-custom-instructions/vibe-coding-custom-instructions-v2-part1.md`

**Topics:**
- The Autonomous Development Paradigm (vs. semi-autonomous)
- The `&` prefix command for background task execution
- Environment setup (Git, GitHub, Vercel, Supabase, CLAUDE.md)
- Launching autonomous background tasks (single and parallel)
- Teleporting sessions between cloud and local
- Mobile development workflows via Claude Mobile
- Review and merge workflows
- When to use cloud vs. local execution

**Use when:** Setting up projects, understanding autonomous workflows, launching first tasks

### Production Patterns & Implementation
**File:** `../agentic-custom-instructions/vibe-coding-custom-instructions-v2-part2.md`

**Topics:**
- Project foundation (dependencies, setup)
- Complete Supabase integration (client setup, database schemas, RLS, TypeScript types)
- Authentication implementation (utilities, hooks, middleware, components)
- n8n webhook integration (utilities, workflows, retry logic)
- Next.js API routes (CRUD patterns, validation with zod, dynamic routes)
- Component architecture patterns
- Data fetching strategies

**Use when:** Implementing specific features, need code examples, database design, API patterns

### Task Templates & Best Practices
**File:** `../agentic-custom-instructions/vibe-coding-custom-instructions-v2-part3.md`

**Topics:**
- 5 autonomous task specification templates:
  1. Complete Feature Build
  2. UI Page/Component
  3. API Integration
  4. Database Schema & Migration
  5. Refactoring/Cleanup
- 3 real-world examples (e-commerce catalog, real-time chat, analytics dashboard)
- Complete QA checklist (40+ checkpoints)
- Troubleshooting guide (task stuck, code errors, wrong files, deployment issues)
- Git workflow patterns
- Security best practices
- Cost optimization strategies

**Use when:** Creating task specifications, QA validation, troubleshooting, production readiness

## Conceptual Understanding

### What is Vibe Coding?
**File:** `../docs/what-is-vibe-coding_012126.md`

Brief conceptual introduction to vibe coding paradigm, history, typical products built, and how tools fit together. Great starting point for newcomers.

### 2026 Development Landscape
**File:** `../docs/vibe-coding-application-architect-guide-jan-2026.md`

Comprehensive 1,900+ line guide covering:
- Vibe coding spectrum (pure vibe, professional review, hybrid)
- 2026 productivity realities and expectations
- Complete AI model ecosystem (Claude 4.5 family, GPT-5.2-Codex, Cursor Composer)
- Modern development platforms (Claude Code, Cursor, Windsurf, Replit, Lovable, Bolt.new)
- Strategic tool selection framework
- Context management and optimization
- Security & quality standards
- Common pitfalls and solutions
- Advanced topics (multi-agent orchestration, prompt injection, MCP)
- Getting started roadmap

**Use when:** Strategic decisions, tool selection, understanding ecosystem, production planning

### Project Builder Instructions
**File:** `../docs/vibe-coding-project-builder-custom-instructions.md`

Operational modes, implementation patterns, and detailed code examples.

## Usage Recommendations

### For Beginners
1. Start with `what-is-vibe-coding_012126.md` for conceptual foundation
2. Read Part 1 (v2-part1.md) for setup and basic workflows
3. Try launching first autonomous task with examples from Part 1
4. Reference Part 2 for specific implementation patterns as needed

### For Intermediate Users
1. Skip to Part 2 for production patterns
2. Use Part 3 templates for task specifications
3. Reference QA checklist before merging
4. Consult troubleshooting guide when issues arise

### For Advanced Users
1. Reference specific sections as needed
2. Use templates as starting points, customize for your stack
3. Study real-world examples in Part 3 for complex features
4. Review architect guide for tool selection and optimization

## Code Examples Available

All reference documents include copy-paste ready code for:

### Supabase Integration
- Client setup with TypeScript type generation
- Database schema with RLS policies
- Triggers and functions
- Complete authentication system

### Next.js Patterns
- API routes with zod validation
- Dynamic routes
- Middleware for protected routes
- Server and client components

### Component Patterns
- Feature-based directory structure
- Reusable UI components (Button, Input, Form)
- Auth components (LoginForm, SignupForm)
- Dashboard layouts

### Workflow Automation
- n8n webhook utilities
- Email workflows (welcome, password reset, digest)
- User onboarding automation
- Analytics event tracking

### Testing & Quality
- Vitest setup
- API route testing patterns
- Component testing with React Testing Library
- QA checklists

## Key Principles Across All Documents

1. **Autonomy First:** Tasks should run for hours without interruption
2. **Specificity Wins:** Detailed specs prevent stalls and errors
3. **Parallel Scale:** Launch 5-10 tasks simultaneously for maximum velocity
4. **Mobile Native:** Complete workflows possible from phone
5. **Review Critically:** Always review auth, payments, security code
6. **Test Before Merge:** npm run build must pass before commit
7. **Progressive Disclosure:** Start simple, add complexity as mastery grows

## Document Interconnections

- **Part 1** establishes workflows → **Part 2** provides implementation patterns → **Part 3** gives templates and troubleshooting
- **Architect Guide** gives strategic overview → **Parts 1-3** provide tactical execution
- **What is Vibe Coding** gives context → **All other docs** assume understanding

## Updates & Versioning

- **Current Version:** 2.0 (January 2026)
- **Last Updated:** January 21, 2026
- **Review Cadence:** Quarterly (next review April 2026)

These documents reflect January 2026 state of Claude Code, Supabase, Vercel, and related tools. Features, APIs, and best practices evolve; verify current capabilities when implementing.

---

**Note:** All documents are designed for progressive disclosure. Start at your knowledge level and go deeper as needed. The skill will reference specific sections based on your requests.
