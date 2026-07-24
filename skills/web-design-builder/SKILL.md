---
name: web-design-builder
description: "Create and refactor production-ready HTML5/CSS/JavaScript web designs from specifications or descriptions. Generates complete, accessible, responsive web designs using modern CSS (container queries, nesting, view transitions), semantic HTML5, and optional framework integration (Tailwind CSS, Alpine.js, React, HTMX). Includes automatic Playwright MCP verification for accessibility and functionality testing when available. Output is static HTML/CSS/JS files — no build pipeline or deployment. MANDATORY TRIGGERS: HTML mockup, HTML prototype, web mockup, web design, HTML page, static HTML, responsive HTML, CSS design, web interface design, WCAG, accessible website, refactor HTML, form design, HTML dashboard, web prototype, accessibility audit."
metadata:
  version: "2.0.0"
  user-invocable: "true"
---
# Web Design Builder

Generate professional, accessible, production-ready web designs from specifications or natural language descriptions. Designs follow WCAG 2.2 Level AA standards, use modern CSS and semantic HTML5, and support automatic verification via Playwright MCP.


## Table of Contents

1. [Core Workflow](#core-workflow)
2. [Requirements Gathering](#phase-1-requirements-gathering)
3. [Design Generation](#phase-2-design-generation)
4. [Verification](#phase-3-verification)
5. [Iteration](#phase-4-iteration)
6. [Framework Selection](#framework-selection)
7. [Bundled Resources](#bundled-resources)


## Core Workflow

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  1. Requirements │───▶│  2. Generate     │───▶│  3. Verify       │───▶│  4. Iterate      │
│  Gather scope,   │    │  HTML/CSS/JS     │    │  A11y, visual,   │    │  Fix issues,     │
│  framework, a11y │    │  with a11y built │    │  responsive      │    │  re-verify       │
│                  │    │  in from start   │    │  (if Playwright) │    │  deliver final   │
└──────────────────┘    └──────────────────┘    └──────────────────┘    └──────────────────┘
```


## Phase 1: Requirements Gathering

Before generating, clarify these with the user:

| Category | Questions | Default |
|----------|-----------|---------|
| **Design type** | Landing page, dashboard, form, portfolio, SaaS app? | Landing page |
| **Framework** | Vanilla, Tailwind CSS, React, Alpine.js, HTMX? | Vanilla HTML/CSS/JS |
| **Content** | User-provided copy or placeholder content? | Placeholder |
| **Brand** | Colors, fonts, design system? | Professional defaults |
| **Responsive** | Mobile-first? Target breakpoints? | Mobile-first, 3 breakpoints |
| **Accessibility** | WCAG level (A, AA, AAA)? | AA |
| **Interactivity** | Forms, modals, animations, dark mode? | Based on design type |

### Check Playwright MCP

Before starting, check if Playwright MCP tools are available (e.g., `mcp__playwright__browser_navigate`). If available, inform the user that automatic verification will run. If not, skip Phase 3 and provide manual testing guidance.


## Phase 2: Design Generation

### HTML Structure Requirements

Every generated design must include:

- **Semantic elements**: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- **Skip link**: `<a href="#main-content" class="skip-link">Skip to main content</a>`
- **Heading hierarchy**: Logical `h1` through `h6` (one `h1` per page)
- **ARIA landmarks**: `role` attributes only where semantic elements are insufficient
- **Accessible forms**: `<label>` + `for`/`id` pairing, `aria-required`, `aria-describedby` for errors
- **Image alt text**: Descriptive `alt` on all `<img>` elements
- **Language attribute**: `lang="en"` on `<html>`
- **Viewport meta**: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

### CSS Architecture

Use modern CSS features with sensible defaults:

```css
/* Custom properties for theming */
:root {
  --color-primary: #4F46E5;
  --color-primary-hover: #4338CA;
  --color-text: #1F2937;
  --color-text-muted: #6B7280;
  --color-bg: #FFFFFF;
  --color-bg-alt: #F9FAFB;
  --color-border: #E5E7EB;
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --spacing: 1rem;
  --radius: 0.5rem;
}

/* Modern reset */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font-sans); line-height: 1.6; color: var(--color-text); }

/* Fluid typography */
h1 { font-size: clamp(2rem, 5vw, 3.5rem); }

/* Responsive container */
.container { max-width: 1200px; margin-inline: auto; padding-inline: var(--spacing); }

/* Skip link */
.skip-link {
  position: absolute; top: -40px; left: 0;
  background: var(--color-primary); color: white; padding: 8px 16px;
  z-index: 100; text-decoration: none;
}
.skip-link:focus { top: 0; }

/* Focus indicator (3:1 contrast minimum) */
:focus-visible { outline: 3px solid var(--color-primary); outline-offset: 2px; }

/* Respect motion preferences */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

### Modern CSS Features to Use

| Feature | Use Case | Example |
|---------|----------|---------|
| **CSS Nesting** | Component scoping | `.card { & h3 { ... } &:hover { ... } }` |
| **Container queries** | Component-level responsive | `@container (min-width: 400px) { ... }` |
| **`:has()` selector** | Parent selection | `form:has(:invalid) .submit { opacity: 0.5; }` |
| **`clamp()`** | Fluid sizing | `font-size: clamp(1rem, 2vw, 1.5rem);` |
| **`color-mix()`** | Dynamic color variants | `color-mix(in srgb, var(--primary) 80%, black)` |
| **Logical properties** | RTL-ready | `margin-inline`, `padding-block` |

For detailed patterns and code examples, read [`references/design-patterns.md`](references/design-patterns.md).

### JavaScript Guidelines

- Use progressive enhancement — pages must work without JS
- Use `'use strict'` in all scripts
- Add keyboard support for all interactive elements
- Use `aria-expanded`, `aria-controls`, `aria-hidden` for dynamic UI
- Wrap in IIFE or use module pattern to avoid globals
- Handle errors gracefully with user-visible feedback

### File Output Structure

```
project-name/
├── index.html          ← Single-file for mockups (CSS/JS inline)
├── styles.css          ← Separate CSS for production builds
├── script.js           ← Separate JS for production builds
└── assets/
    ├── images/         ← Image assets
    └── fonts/          ← Custom fonts (if needed)
```

For mockups and prototypes, prefer single-file HTML with inline CSS/JS. For production builds, separate files.

### Design Templates

Ready-to-use starter templates are available for common design types. Read [`references/design-templates.md`](references/design-templates.md) for:
- SaaS landing page
- Contact form
- Admin dashboard
- Portfolio page
- E-commerce product page


## Phase 3: Verification

**Only execute if Playwright MCP is available.** If not, provide the manual testing checklist from [`assets/manual-testing-checklist.md`](assets/manual-testing-checklist.md).

### Verification Steps

1. **Load design** — Navigate to the saved HTML file
2. **Accessibility audit** — Run automated a11y scan, check contrast, heading hierarchy, ARIA
3. **Responsive screenshots** — Capture at 375px (mobile), 768px (tablet), 1440px (desktop)
4. **Keyboard navigation** — Tab through all interactive elements, verify focus indicators
5. **Form testing** — Submit with valid/invalid data, verify error messages
6. **JavaScript testing** — Check console for errors, test interactive components

For detailed Playwright MCP commands and verification procedures, read [`references/verification-guide.md`](references/verification-guide.md).

### Verification Report

After testing, generate a report using the template in [`assets/verification-report-template.md`](assets/verification-report-template.md). The report covers:
- Accessibility compliance (pass/warn/fail)
- Responsive layout results
- Functionality test outcomes
- Performance observations
- Prioritized fix recommendations


## Phase 4: Iteration

1. **Fix critical issues** first — accessibility violations, broken functionality
2. **Apply improvements** — performance optimizations, visual refinements
3. **Re-verify** if Playwright MCP is available
4. **Deliver final files** with documentation and deployment notes


## Framework Selection

| Framework | Best For | Size | Build Step | Recommendation |
|-----------|----------|------|------------|----------------|
| **Vanilla HTML/CSS/JS** | Simple sites, fastest load | 0KB | No | Default for static content |
| **Tailwind CSS** (CDN) | Rapid prototyping, utility-first | ~300KB CDN | No | Recommended for mockups |
| **Alpine.js** | Lightweight interactivity | ~15KB | No | Best for progressive enhancement |
| **HTMX** | Server-driven interactivity | ~14KB | No | Best for form-heavy sites |
| **React** (CDN) | Complex SPAs | ~140KB CDN | No* | Only for complex interactivity |

*CDN versions work without build steps. Production React requires a build pipeline.

For framework-specific setup, patterns, and code examples, read [`references/framework-guide.md`](references/framework-guide.md).


## Accessibility Checklist

Every design must pass these checks before delivery:

- [ ] Skip link present and functional
- [ ] One `h1`, logical heading hierarchy
- [ ] All images have `alt` text
- [ ] Color contrast 4.5:1 for text, 3:1 for large text
- [ ] Focus indicators visible (3:1 contrast)
- [ ] All form inputs have associated `<label>` elements
- [ ] Error messages use `role="alert"` and `aria-describedby`
- [ ] Interactive elements keyboard-accessible (Tab, Enter, Escape)
- [ ] No keyboard traps
- [ ] `prefers-reduced-motion` respected
- [ ] `lang` attribute on `<html>`

For comprehensive accessibility guidance, read [`references/accessibility-guide.md`](references/accessibility-guide.md).


## Deliverables

Provide the user with:

1. **Design files** — Complete HTML/CSS/JS, ready to open in a browser
2. **Verification report** — If Playwright MCP was available
3. **Customization notes** — How to change colors, content, layout
4. **Next steps** — Deployment options, further improvements, production considerations


## Bundled Resources

| File | Purpose |
|------|---------|
| [`references/design-patterns.md`](references/design-patterns.md) | Modern CSS patterns, responsive layouts, dark mode, animations |
| [`references/design-templates.md`](references/design-templates.md) | Starter HTML templates for landing pages, dashboards, forms |
| [`references/accessibility-guide.md`](references/accessibility-guide.md) | WCAG 2.2 compliance, ARIA patterns, testing methodology |
| [`references/framework-guide.md`](references/framework-guide.md) | Tailwind CSS, Alpine.js, HTMX, React setup and patterns |
| [`references/verification-guide.md`](references/verification-guide.md) | Playwright MCP commands, automated testing procedures |
| [`assets/verification-report-template.md`](assets/verification-report-template.md) | Template for design verification reports |
| [`assets/manual-testing-checklist.md`](assets/manual-testing-checklist.md) | Manual testing checklist when Playwright MCP is unavailable |
| [`scripts/validate_html.py`](scripts/validate_html.py) | HTML structure and accessibility validation script |


---
*Web Design Builder v2.0 — February 2026*
*Conformant to agentskills.io open standard (December 2025)*
