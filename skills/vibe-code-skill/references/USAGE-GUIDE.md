# How to Use the Vibe Coding Orchestrator Skill

This guide explains how to effectively use the Vibe Coding Orchestrator skill in your Claude Projects.

## What This Skill Does

The Vibe Coding Orchestrator skill transforms Claude into an expert autonomous development partner. It helps you:

1. **Design autonomous tasks** that run independently in the cloud for hours
2. **Launch parallel development workflows** (5-10 features simultaneously)
3. **Build production applications** using Next.js, Supabase, and Vercel
4. **Develop from mobile** using Claude Mobile's background task execution
5. **Review and optimize** autonomous development workflows

## Installation

1. **Add to Claude Project:**
   - Copy the entire `vibe-code-skill` folder to your Claude Project's knowledge base
   - Or add the skill folder path to your project's skill directory

2. **Verify Installation:**
   - In your Claude Project, ask: "Do you have the vibe-coding-orchestrator skill?"
   - Claude should confirm and describe its capabilities

## Triggering the Skill

The skill activates automatically when you mention:
- "autonomous development" or "background tasks"
- "vibe coding" or "AI-driven development"
- Claude Code's `&` prefix or launching tasks
- "teleport sessions" or cloud-to-local workflows
- Building applications with Claude Code
- Parallel session orchestration
- Mobile development workflows
- Supabase + Next.js + Vercel stack

## Usage Patterns

### Pattern 1: Project Planning (Strategic Mode)

**When:** Starting a new project or planning a feature

**Example Prompts:**
```
"I want to build a SaaS for [description]. How should I structure this as autonomous tasks?"

"What's the best way to parallelize development of authentication, dashboard, and blog features?"

"Help me design the branching strategy for autonomous Claude Code development."
```

**What to Expect:**
- Claude breaks down your project into parallelizable tasks
- Recommendations for tech stack and architecture
- Clarifying questions about requirements
- Stays in strategic mode until you're ready to build

### Pattern 2: Environment Setup (First Time)

**When:** Setting up a new project for autonomous development

**Example Prompts:**
```
"Walk me through setting up my first autonomous development project."

"How do I configure Git, GitHub, and Vercel for Claude Code workflows?"

"I need to create a CLAUDE.md file for my project. What should it contain?"
```

**What to Expect:**
- Step-by-step setup instructions
- Configuration examples
- Best practices for CLAUDE.md
- Environment variable setup

### Pattern 3: Launching Autonomous Tasks (Implementation Mode)

**When:** Ready to build features autonomously

**Example Prompts:**
```
"Create a complete autonomous task specification for user authentication using Supabase."

"I need 5 parallel tasks for building: landing page, dashboard, blog, admin panel, and email automation."

"Generate the & command to build a real-time chat feature with Supabase Realtime."
```

**What to Expect:**
- Complete task specifications with `&` prefix
- Detailed requirements (database, API, UI, tests)
- Quality criteria and git workflow
- Explanation of what will happen during execution

### Pattern 4: Getting Code Patterns

**When:** Need implementation examples

**Example Prompts:**
```
"Show me the Supabase client setup with TypeScript types."

"I need a Next.js API route with zod validation."

"How do I implement n8n webhook integration with retry logic?"
```

**What to Expect:**
- Copy-paste ready code examples
- Full implementation with error handling
- TypeScript types included
- Best practices explained

### Pattern 5: Troubleshooting

**When:** Something went wrong with autonomous task

**Example Prompts:**
```
"My autonomous task got stuck. How do I diagnose and fix it?"

"The Vercel deployment failed with [error]. How do I fix this?"

"Claude modified the wrong files. How do I prevent this?"
```

**What to Expect:**
- Diagnostic steps
- Specific fix strategies
- Prevention recommendations
- New task specification if needed

### Pattern 6: Mobile Workflows

**When:** Developing from phone

**Example Prompts:**
```
"How do I launch autonomous tasks from Claude Mobile?"

"Walk me through a complete mobile development workflow."

"How do I review and merge code from my phone?"
```

**What to Expect:**
- Mobile-specific workflows
- Monitoring strategies
- Testing on mobile device
- PR creation from phone

## Skill Modes

### Strategic Mode (Default)
Claude helps you **plan and design** autonomous workflows.

**Indicators you're in this mode:**
- Claude asks clarifying questions
- Suggests multiple approaches
- Explains trade-offs
- Challenges vague specifications

**How to stay here:**
- Ask "how to" questions
- Request recommendations
- Discuss architecture
- Explore options

### Implementation Mode (Explicit Trigger)
Claude provides **concrete task specifications and code**.

**How to switch:**
- Say "Launch the background tasks"
- Say "Start autonomous development"
- Say "Execute the plan"
- Say "Give me the & command"

**Indicators you're in this mode:**
- Claude provides `&` prefixed task specifications
- Detailed implementation requirements
- Copy-paste ready code
- Git workflow instructions

## Example Conversation Flow

### Complete Feature Development

**You:** "I want to build a blog system with CRUD operations for my Next.js app."

**Claude (Strategic):** *Asks clarifying questions about data model, user permissions, features needed*

**You:** "Posts should have title, content, author. Only authenticated users can create. Anyone can read published posts."

**Claude (Strategic):** *Proposes architecture, suggests breaking into 2 tasks: database + API, then UI*

**You:** "That sounds good. Let's build it."

**Claude (Implementation):** *Provides complete `&` task specification including:*
- Database schema with RLS policies
- API routes with validation
- UI components
- Quality criteria
- Git workflow

**You:** *Runs the & command in Claude Code CLI*

**Claude:** *Task runs autonomously for 2-3 hours, completes, pushes to GitHub*

**You (later):** "The task completed but there's a TypeScript error in the API route."

**Claude (Troubleshooting):** *Provides debugging task specification to fix the specific error*

## Best Practices

### 1. Be Specific When Ready to Build
❌ **Bad:** "Build authentication"
✅ **Good:** "I need authentication with email/password using Supabase, including login form, signup form, protected routes, and password reset"

### 2. Use Strategic Mode for Planning
Don't jump straight to implementation. Let Claude help you:
- Break down complex features
- Identify dependencies
- Plan parallel execution
- Design proper architecture

### 3. Trust the Quality Checklists
Claude's task specifications include quality criteria. These are based on production best practices:
- TypeScript strict mode
- Error handling
- Loading states
- Mobile responsive
- Test before commit

### 4. Review Critical Code
Even with autonomous tasks, **always review:**
- Authentication/authorization
- Payment processing
- Database RLS policies
- API security
- User data handling

### 5. Start Simple, Scale Gradually
- **First task:** Single feature (landing page)
- **Second task:** Feature with database (blog posts)
- **Third task:** Two parallel tasks
- **Eventually:** 5-10 parallel tasks

### 6. Use Mobile Workflow
Once comfortable:
- Launch tasks from Claude Mobile during commute
- Monitor progress during day
- Review and merge from phone
- Never touch laptop for development

## Common Mistakes

### Mistake 1: Vague Task Specifications
**Problem:** "Build a dashboard"
**Fix:** Specify exact components, data sources, interactions

### Mistake 2: Skipping Environment Setup
**Problem:** Launching autonomous tasks without Git/GitHub/Vercel configured
**Fix:** Follow Phase 1 setup instructions first

### Mistake 3: Not Creating CLAUDE.md
**Problem:** Task doesn't follow your coding standards
**Fix:** Create CLAUDE.md with project context and standards

### Mistake 4: Ignoring Quality Criteria
**Problem:** Task completes but code has errors
**Fix:** Include "test with npm run build" in task spec

### Mistake 5: Trying to Control Everything
**Problem:** Interrupting autonomous tasks constantly
**Fix:** Trust the process, specify well upfront, review at end

## Advanced Usage

### Parallel Feature Development
Launch 5-10 features simultaneously:
- Authentication system
- Landing page
- User dashboard
- Blog system
- Admin panel
- Email automation
- Analytics dashboard
- Settings page

Each runs independently. Merge foundation features (auth) first, then others.

### Teleport Sessions
Move between cloud and local:
1. Launch task in cloud with `&`
2. Task completes autonomously
3. Use `claude teleport [session-id]` locally
4. Continue with full context preserved

### Multi-Environment Workflows
- `main` branch → Production (Vercel)
- `staging` branch → Staging environment
- `feature/*` branches → Preview deployments

Each environment has separate database and config.

## Getting Help

### Within the Skill
Ask Claude:
- "Show me examples of autonomous task specifications"
- "What's in the reference documents?"
- "How do I troubleshoot [specific issue]?"

### Reference Documents
The skill bundles comprehensive documentation:
- **Part 1:** Workflows and setup (1,250 lines)
- **Part 2:** Production patterns (1,150 lines)
- **Part 3:** Templates and troubleshooting (700+ lines)

Claude will reference these automatically as needed.

## Success Metrics

**You're using this skill effectively when:**
- ✅ You launch tasks that run for 2+ hours without issues
- ✅ You're developing 5-10 features in parallel
- ✅ Your autonomous tasks complete without modification
- ✅ You're building from mobile during commute
- ✅ You're shipping features 5-10x faster
- ✅ Your code passes TypeScript/ESLint without errors
- ✅ Vercel deployments succeed automatically

**You need more practice when:**
- ❌ Tasks get stuck frequently
- ❌ You're constantly interrupting autonomous execution
- ❌ Code has errors after completion
- ❌ You're afraid to launch tasks without supervision
- ❌ You're not using parallel execution
- ❌ You're still doing everything on laptop

## Next Steps

1. **Read the overview:** Ask Claude to summarize vibe coding
2. **Set up first project:** Follow Phase 1 environment setup
3. **Launch first task:** Start with simple feature (landing page)
4. **Review completed work:** Test preview, review code
5. **Scale to parallel:** Launch 2-3 tasks simultaneously
6. **Go mobile:** Try launching from Claude Mobile
7. **Master patterns:** Reference Part 2 for advanced implementations

## Updates

This skill is versioned and updated quarterly:
- **Current Version:** 1.0.0 (January 2026)
- **Next Review:** April 2026

Features and best practices evolve with Claude Code updates. The skill incorporates the latest patterns as of January 2026.

---

**Ready to start?** Ask Claude: "I want to learn vibe coding. Where should I begin?"
