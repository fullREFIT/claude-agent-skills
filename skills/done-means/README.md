# Done Means

Done Means is an Agent Skills package for turning project status into an evidence-backed finish line. It defines what must be true, identifies only observed or explicitly required work, sequences dependencies, and verifies the result.

## Install

Copy the `done-means` folder into the skill directory used by your agent platform:

```text
~/.claude/skills/done-means/
~/.codex/skills/done-means/
~/.cursor/skills/done-means/
```

The package follows the portable Agent Skills format. The bundled ZIP is ready for upload where ZIP skill installation is supported.

## First use

Provide:

- the project name and absolute path
- the source that defines the finish line
- the task backend, if one already exists
- whether to audit only or execute safe local work

Example:

```text
Run a Done Means audit for project `example-app` at `/path/to/example-app`.
Use `docs/launch-criteria.md` as the finish-line source. Write the roadmap to `docs/done-means-roadmap.md` and audit only.
```

## Package contents

- `SKILL.md`: trigger, workflow, evidence rules, and safety boundary
- `references/done-means-protocol.md`: audit and roadmap contract
- `references/done-means-execution.md`: execution and completion gate
- `assets/short-launch-prompts.md`: reusable audit and execution prompts
- `done-means.zip`: uploadable package

## License

MIT
