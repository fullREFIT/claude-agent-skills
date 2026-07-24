# Design Patterns Reference

Modern CSS and HTML patterns for web design generation. Use these patterns when building designs.

## Responsive Layout Patterns

### Mobile-First Breakpoints

```css
/* Base: mobile (< 640px) */
.container { padding: 1rem; }

/* Small: tablets (≥ 640px) */
@media (min-width: 640px) {
  .container { padding: 1.5rem; max-width: 640px; margin-inline: auto; }
}

/* Medium: small desktops (≥ 768px) */
@media (min-width: 768px) {
  .container { max-width: 768px; }
}

/* Large: desktops (≥ 1024px) */
@media (min-width: 1024px) {
  .container { padding: 2rem; max-width: 1024px; }
}

/* X-Large: wide screens (≥ 1280px) */
@media (min-width: 1280px) {
  .container { max-width: 1200px; }
}
```

### CSS Grid Layouts

**Auto-fit responsive grid (no media queries):**
```css
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: 1.5rem;
}
```

**Sidebar layout:**
```css
.sidebar-layout {
  display: grid;
  grid-template-columns: minmax(200px, 250px) 1fr;
  gap: 2rem;
}

@media (max-width: 768px) {
  .sidebar-layout { grid-template-columns: 1fr; }
}
```

**Holy grail layout:**
```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "nav    main   aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

header { grid-area: header; }
nav    { grid-area: nav; }
main   { grid-area: main; }
aside  { grid-area: aside; }
footer { grid-area: footer; }
```

### Container Queries

Component-level responsive design — components respond to their container, not the viewport:

```css
/* Define containment context */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Component responds to container width */
.card {
  display: grid;
  gap: 1rem;
}

@container card (min-width: 400px) {
  .card {
    grid-template-columns: 200px 1fr;
  }
}

@container card (min-width: 700px) {
  .card {
    grid-template-columns: 300px 1fr;
    gap: 2rem;
  }
}
```

### Flexbox Patterns

**Centered content:**
```css
.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
```

**Space-between navigation:**
```css
.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  flex-wrap: wrap;
  gap: 1rem;
}
```

**Equal-height cards:**
```css
.card-row {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.card-row > * {
  flex: 1 1 300px;
  display: flex;
  flex-direction: column;
}

.card-row .card-body { flex: 1; }
```


## Modern CSS Features

### CSS Nesting

```css
.card {
  background: white;
  border-radius: var(--radius);
  padding: 1.5rem;

  & h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }

  & p {
    color: var(--color-text-muted);
  }

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  &.featured {
    border: 2px solid var(--color-primary);
  }
}
```

### :has() Selector

```css
/* Style parent based on child state */
.form-group:has(:invalid) {
  border-color: #DC2626;
}

/* Style label when input is focused */
label:has(+ input:focus) {
  color: var(--color-primary);
}

/* Card with image gets different layout */
.card:has(img) {
  grid-template-rows: 200px 1fr;
}

/* Nav with many items switches to hamburger */
nav:has(> ul > li:nth-child(6)) {
  .nav-links { display: none; }
  .mobile-toggle { display: block; }
}
```

### color-mix()

```css
:root {
  --primary: #4F46E5;
  --primary-hover: color-mix(in srgb, var(--primary) 85%, black);
  --primary-light: color-mix(in srgb, var(--primary) 20%, white);
  --primary-subtle: color-mix(in srgb, var(--primary) 10%, white);
}
```

### Logical Properties

Use logical properties for RTL language support:

```css
/* Instead of margin-left/right, use: */
.element {
  margin-inline: auto;      /* left + right */
  padding-block: 1rem;      /* top + bottom */
  border-inline-start: 3px solid var(--primary);  /* left in LTR, right in RTL */
  text-align: start;        /* left in LTR, right in RTL */
}
```

### Scroll-Driven Animations

```css
/* Progress bar that fills as user scrolls */
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: var(--color-primary);
  transform-origin: left;
  animation: grow-progress linear;
  animation-timeline: scroll();
}

@keyframes grow-progress {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```


## Dark Mode

### CSS-Only Dark Mode

```css
:root {
  --color-text: #1F2937;
  --color-bg: #FFFFFF;
  --color-bg-alt: #F9FAFB;
  --color-border: #E5E7EB;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #F3F4F6;
    --color-bg: #111827;
    --color-bg-alt: #1F2937;
    --color-border: #374151;
  }
}
```

### Toggle-Based Dark Mode

```css
/* Light theme (default) */
[data-theme="light"] {
  --color-text: #1F2937;
  --color-bg: #FFFFFF;
}

/* Dark theme */
[data-theme="dark"] {
  --color-text: #F3F4F6;
  --color-bg: #111827;
}
```

```javascript
function toggleTheme() {
  const html = document.documentElement;
  const current = html.getAttribute('data-theme') || 'light';
  const next = current === 'light' ? 'dark' : 'light';
  html.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
}

// Apply saved preference on load
const saved = localStorage.getItem('theme') ||
  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
document.documentElement.setAttribute('data-theme', saved);
```


## Typography

### Fluid Typography Scale

```css
:root {
  --text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem);
  --text-sm: clamp(0.875rem, 0.8rem + 0.35vw, 1rem);
  --text-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --text-lg: clamp(1.125rem, 1rem + 0.6vw, 1.25rem);
  --text-xl: clamp(1.25rem, 1rem + 1.2vw, 1.75rem);
  --text-2xl: clamp(1.5rem, 1.1rem + 2vw, 2.5rem);
  --text-3xl: clamp(2rem, 1.2rem + 3.5vw, 3.5rem);
}
```

### System Font Stack

```css
/* Sans-serif (default) */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Monospace */
font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, monospace;

/* Serif */
font-family: 'Georgia', 'Times New Roman', serif;
```


## Component Patterns

### Accessible Button

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: var(--radius);
  font: inherit;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.2s, box-shadow 0.2s;
}

.btn:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

.btn-primary {
  background: var(--color-primary);
  color: white;
}

.btn-primary:hover { background: var(--color-primary-hover); }
```

### Card Component

```css
.card {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  overflow: hidden;
  transition: box-shadow 0.2s;

  & img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  & .card-body {
    padding: 1.5rem;
  }

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }
}
```

### Modal/Dialog (Native HTML)

```html
<button onclick="document.getElementById('my-dialog').showModal()">
  Open Dialog
</button>

<dialog id="my-dialog">
  <form method="dialog">
    <h2>Dialog Title</h2>
    <p>Dialog content here.</p>
    <button value="cancel">Cancel</button>
    <button value="confirm">Confirm</button>
  </form>
</dialog>
```

```css
dialog {
  border: none;
  border-radius: var(--radius);
  padding: 2rem;
  max-width: min(90vw, 500px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
}

dialog::backdrop {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
}
```

### Accordion (Native HTML)

```html
<details>
  <summary>Section title</summary>
  <div class="details-content">
    <p>Collapsible content here.</p>
  </div>
</details>
```

```css
details {
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 1rem;
}

summary {
  cursor: pointer;
  font-weight: 600;
  list-style: none;
}

summary::before {
  content: '▸';
  display: inline-block;
  margin-right: 0.5rem;
  transition: transform 0.2s;
}

details[open] summary::before {
  transform: rotate(90deg);
}

.details-content {
  padding-top: 1rem;
}
```


## Animation Patterns

### Transitions

```css
/* Smooth hover effects */
.interactive {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.interactive:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

### Entrance Animations

```css
@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.animate-in {
  animation: fade-in 0.3s ease-out;
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  .animate-in { animation: none; }
}
```


## Performance Patterns

### Image Optimization

```html
<!-- Responsive images with srcset -->
<img
  src="image-800.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw, (max-width: 1024px) 50vw, 33vw"
  alt="Description"
  loading="lazy"
  decoding="async"
  width="800"
  height="600"
/>

<!-- Modern format with fallback -->
<picture>
  <source srcset="image.avif" type="image/avif" />
  <source srcset="image.webp" type="image/webp" />
  <img src="image.jpg" alt="Description" loading="lazy" width="800" height="600" />
</picture>
```

### Critical CSS

For above-the-fold content, inline critical CSS in `<style>` and defer the rest:

```html
<head>
  <!-- Critical CSS inline -->
  <style>
    /* Only styles needed for above-the-fold content */
  </style>

  <!-- Non-critical CSS deferred -->
  <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="styles.css"></noscript>
</head>
```

### Font Loading

```css
/* Use font-display: swap for fast text rendering */
@font-face {
  font-family: 'Custom Font';
  src: url('font.woff2') format('woff2');
  font-display: swap;
}
```

```html
<!-- Preload critical fonts -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin />
```
