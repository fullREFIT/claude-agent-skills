# Done Means guide

**Live guide:** https://done-means-guide.vercel.app

This is a scrolling public landing page for the Done Means Agent Skill, built with the full/REFIT workbench landing-page pattern. The older report renderer is preserved under `deck-runtime/` as an implementation reference.

## Contents

- `done-means-guide-report.json`: the original structured report content
- `site/`: the live landing page source and Vite build
- `deck-runtime/`: the earlier presentation renderer, retained for reference

## Local preview

From `site/`:

```bash
npm install
npm run validate
npm test
npm run typecheck
npm run build
npm run dev
```

The guide is source-backed by the public Done Means skill and the Agent Skills specification. It contains no private project data or credentials.
