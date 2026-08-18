# Done Means audit protocol

Produce one complete, ordered, evidence-backed list of every remaining task between the live project state and its DONE MEANS conditions. Write it to the backend named by the project. Do not create a competing system.

## Step 0: Confirm the operating surface

Before auditing, confirm:

1. The project path exists and is not empty.
2. The finish-line source is readable.
3. The named task backend is reachable, if the project uses one.
4. The output location and mutation permission are clear.

If no backend is named, use the local fallback only when the user requests a file-based roadmap. Otherwise stop before mutations and ask for the smallest missing decision.

## Step 1: Read the project

Read in this order:

1. README, contribution docs, docs, and root Markdown files.
2. AGENTS.md, CLAUDE.md, or other project instructions.
3. Manifests and lockfiles.
4. Configuration and environment names only. Never expose secret values.
5. Source entry points and the modules they reach.
6. Tests and verification scripts.
7. TODO, FIXME, HACK, and XXX comments.
8. Git status, recent commits, and active branches.
9. Existing task or issue records when the project names them.

Run the commands the project identifies as proof. Record actual outputs and errors. Declare which directories were read, sampled, or skipped.

## Step 2: Define the finish line

Restate DONE MEANS as three to six conditions that an independent observer can check without asking for interpretation. Good conditions name a command, URL, route, file, behavior, or recorded result. Avoid terms such as polished, production ready, or works correctly without a check.

Every task must trace to at least one condition. Drop tasks that do not.

## Step 3: Derive findings

Every finding has exactly one source:

- **BROKEN**: something exists and failed. Cite the command and error.
- **MISSING**: something is referenced but absent. Cite the reference and absence.
- **REQUIRED**: a finish-line condition needs work with no implementation reference. Cite the condition.

Do not add generic best practices. Split work that cannot be independently verified.

## Step 4: Record fields

Each task must include:

| Field | Rule |
| --- | --- |
| Task ID | `T01`, `T02`, in dependency order |
| Task | Specific imperative action |
| Type | Build, Fix, Verify, Decide, Config, Content, or Deploy |
| Why needed | Ties the task to a finish-line condition |
| Evidence | Path and line, command and error, or explicit absence |
| Source | BROKEN, MISSING, or REQUIRED |
| Done when | Testable assertion |
| Depends on | Task IDs or none |
| Effort | <1h, 1-4h, 1-2d, or >2d |
| Risk | Blocker, Degraded, or Cosmetic |
| Confidence | Verified, Inferred, or Assumed with a settling action |
| Phase | Dependency-ordered phase number |

## Step 5: Sequence

Group tasks into phases named for outcomes. Phase 0 contains blockers. State the critical path and the single first task.

## Step 6: Write and verify

Use the existing project backend and its schema. Read current records before mutation. Match existing tasks by stable identity, add only missing tasks, and preserve user-owned statuses. Read the records back and verify counts, links, and every newly written task.

For the local fallback, write a Markdown file containing the finish-line conditions, coverage statement, task table, phases, critical path, and verification evidence. The file is a record, not proof. Re-run the checks before calling a condition met.

## Halt conditions

Stop before mutation when the project path, finish-line source, required backend, or output permission cannot be verified. Report the exact blocker, owner, and cheapest unblocker.

A project can be complete. If every condition passes with current evidence, report that finding and do not manufacture a backlog.
