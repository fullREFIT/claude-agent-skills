---
name: done-means
description: "Audit a live project against explicit DONE MEANS conditions, derive only evidence-backed BROKEN, MISSING, or REQUIRED work, sequence dependencies, and verify the finish line. Use when auditing project completion, defining a finish line, building an evidence-backed roadmap, or executing a Done Means review. MANDATORY TRIGGERS: done means, completion audit, project audit, finish line, remaining tasks, evidence-backed roadmap, project completion."
license: MIT
compatibility: Portable Agent Skills format. Requires filesystem access and either a project-specified task backend or the bundled local Markdown fallback.
---

# Done Means

Turn an ambiguous project status into a checkable finish line and an ordered list of remaining work. Read the live project before forming an opinion. Treat prior reports, task records, and documentation as claims that require current evidence.

## Workflow

1. Read `references/done-means-protocol.md` before auditing.
2. Read `references/done-means-execution.md` before executing an existing roadmap.
3. Confirm the project path, finish-line source, and tracking backend.
4. Define three to six independently verifiable DONE MEANS conditions.
5. Derive only evidence-backed `BROKEN`, `MISSING`, or `REQUIRED` tasks.
6. Sequence tasks by dependency and split work that cannot be independently verified.
7. Write or reconcile the roadmap in the project-specified backend. Preserve existing status values.
8. Read the records back and verify counts, links, and task fields.
9. Execute only when the user explicitly asks for execution. Otherwise return the verified roadmap and first action.

## Backend boundary

The skill must not invent a backend. Use the backend explicitly named by the project or user. Supported patterns include a project task tracker, an API adapter documented by the project, or the bundled local Markdown fallback. When no backend is named, stop before mutations and ask for one, or use the local fallback only when the user asks for a file-based roadmap.

The public package contains no account IDs, private URLs, credentials, or client-specific schemas. Backend-specific fields belong in a project adapter or the local fallback file.

## Non-negotiable evidence rules

- `BROKEN` requires a failure you observed.
- `MISSING` requires a referenced but absent file, route, variable, function, or surface.
- `REQUIRED` requires a finish-line condition that needs work with no existing implementation reference.
- Every task needs a path, line, command, error, or explicit absence citation.
- Never add generic cleanup, tests, refactoring, or documentation unless a finish-line condition or observed failure requires it.
- Never claim completion because a file was written or a command exited zero. Verify the outcome independently.

## Execution boundary

Do not publish, send, deploy, delete, rotate credentials, create credentials, or make legally or financially consequential changes without the required approval. Safe local inspection, reversible edits, validation, and focused tests are allowed when the user has asked for execution.

## Wrong output

- A generic checklist that could describe any project
- A roadmap with tasks that do not trace to DONE MEANS
- Evidence that restates the finding instead of locating it
- A new backend or project-specific table invented by the agent
- Overwriting an existing task status without a current read
- Calling completion from a README, prior report, or command success alone
- Stopping at a plan when explicitly authorized safe execution remains

## Bundled resources

Read `references/done-means-protocol.md` for the audit contract and backend boundary.

Read `references/done-means-execution.md` for dependency-ordered execution and completion verification.

Read `assets/short-launch-prompts.md` for compact launch prompts.
