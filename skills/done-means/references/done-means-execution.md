# Done Means execution

Use this after an audit has produced and verified a roadmap. The objective is to complete outstanding tasks in dependency order until every finish-line condition passes or a real blocker remains.

## Preflight

1. Confirm the project path exists and is not empty.
2. Read the finish-line source.
3. Read the current roadmap and backend records.
4. Preserve existing status values and declare filesystem coverage.

Stop before mutation if any required source cannot be read.

## Task loop

Select the first task that is not complete, has cleared dependencies, traces to a finish-line condition, and has enough evidence to act.

Classify it:

- `READY`: safe and authorized to execute.
- `BLOCKED`: a decision, credential, dependency, or external system prevents execution.
- `STALE`: cited evidence conflicts with the live project.
- `DONE`: acceptance criteria already pass, so verify and preserve the result.

For each READY task:

1. Recheck every cited path or live reference.
2. Execute the smallest change that satisfies `Done when`.
3. Preserve unrelated agent work and inspect current files before overwriting.
4. Avoid generic cleanup or infrastructure.
5. Do not publish, send, deploy, delete, or change credentials without approval.
6. Verify the actual outcome, not just command success.
7. Update the existing task record with current status and evidence.

When blocked, record the exact blocker, owner, clearing action, and evidence. Continue with independent tasks when possible.

## Completion gate

Recheck every finish-line condition independently. If one fails, update or create only the corresponding BROKEN, MISSING, or REQUIRED task. Do not manufacture a generic backlog.

## Final report

Return:

- Status: Complete, Partially complete, Blocked, or Unresolved.
- Result: what changed and which conditions pass.
- Verification: commands, live reads, URLs, and artifact checks.
- Residual work: every remaining task, owner, blocker, and clearing action.
- Next action: one action, one owner, and the first command or UI step.
