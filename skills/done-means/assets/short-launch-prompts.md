# Short launch prompts

## Audit

```text
Run a Done Means audit for this project.

Project name: <PROJECT NAME>
Project path: <ABSOLUTE PROJECT PATH>
Finish-line source: <PATH OR URL>
Roadmap backend: <NAMED BACKEND OR LOCAL MARKDOWN FILE>

Read the live project first. Define 3 to 6 independently verifiable DONE MEANS conditions. Derive only evidence-backed BROKEN, MISSING, or REQUIRED tasks. Preserve existing task statuses. Verify the roadmap records and report coverage, counts, critical path, first task, and blockers.

Stop if the project path, finish-line source, or required backend cannot be verified. Do not pad the list or invent evidence.
```

## Execute

```text
Execute the verified Done Means roadmap for this project until every condition passes or a real blocker remains.

Project name: <PROJECT NAME>
Project path: <ABSOLUTE PROJECT PATH>
Finish-line source: <PATH OR URL>
Roadmap backend: <NAMED BACKEND OR LOCAL MARKDOWN FILE>

Read current records first, preserve statuses, execute in dependency order, verify each acceptance condition, and update the existing records with evidence. Do not create a competing roadmap system. Stop only for a real approval, credential, access, safety, or external-system boundary.

Finish with Status, Result, Verification, Residual work, and Next action.
```
