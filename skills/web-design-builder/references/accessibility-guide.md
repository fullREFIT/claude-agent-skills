# Accessibility Guide

Comprehensive WCAG 2.2 Level AA compliance reference for web design generation.


## WCAG 2.2 Requirements Summary

### Perceivable

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 1.1.1 Non-text Content | A | All non-text content has text alternative |
| 1.3.1 Info and Relationships | A | Structure conveyed through semantics, not just visually |
| 1.3.4 Orientation | AA | Content not restricted to single orientation |
| 1.4.1 Use of Color | A | Color not sole means of conveying information |
| 1.4.3 Contrast (Minimum) | AA | Text: 4.5:1, Large text: 3:1 |
| 1.4.4 Resize Text | AA | Text resizable to 200% without loss |
| 1.4.10 Reflow | AA | Content reflows at 320px width (no horizontal scroll) |
| 1.4.11 Non-text Contrast | AA | UI components and graphics: 3:1 |
| 1.4.12 Text Spacing | AA | Adjustable text spacing without loss |
| 1.4.13 Content on Hover/Focus | AA | Dismissable, hoverable, persistent |

### Operable

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 2.1.1 Keyboard | A | All functionality keyboard accessible |
| 2.1.2 No Keyboard Trap | A | Focus can always be moved away |
| 2.4.1 Bypass Blocks | A | Skip navigation links |
| 2.4.2 Page Titled | A | Descriptive `<title>` |
| 2.4.3 Focus Order | A | Logical focus sequence |
| 2.4.6 Headings and Labels | AA | Descriptive headings and labels |
| 2.4.7 Focus Visible | AA | Focus indicator visible |
| 2.4.11 Focus Not Obscured | AA | Focused element not fully hidden (WCAG 2.2) |
| 2.5.7 Dragging Movements | AA | Dragging has non-dragging alternative (WCAG 2.2) |
| 2.5.8 Target Size (Minimum) | AA | Touch targets at least 24x24px (WCAG 2.2) |

### Understandable

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 3.1.1 Language of Page | A | `lang` attribute on `<html>` |
| 3.2.1 On Focus | A | No unexpected changes on focus |
| 3.3.1 Error Identification | A | Errors described in text |
| 3.3.2 Labels or Instructions | A | Labels for user input |
| 3.3.7 Redundant Entry | A | Don't re-ask for already provided info (WCAG 2.2) |
| 3.3.8 Accessible Authentication | AA | No cognitive function test for auth (WCAG 2.2) |

### Robust

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 4.1.2 Name, Role, Value | A | All UI components have accessible name and role |
| 4.1.3 Status Messages | AA | Status messages announced via `role` or `aria-live` |


## ARIA Patterns

### When to Use ARIA

**First rule of ARIA:** Don't use ARIA if native HTML provides the semantics. Prefer:
- `<button>` over `<div role="button">`
- `<nav>` over `<div role="navigation">`
- `<dialog>` over `<div role="dialog">`
- `<details>/<summary>` over custom accordions

### Common ARIA Patterns

**Live regions for dynamic content:**
```html
<!-- Polite: announced when user is idle -->
<div aria-live="polite" aria-atomic="true">
  Search results updated: 42 results found.
</div>

<!-- Assertive: announced immediately (use sparingly) -->
<div aria-live="assertive" role="alert">
  Error: Form submission failed.
</div>
```

**Tabs:**
```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">Profile</button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2" tabindex="-1">Security</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Profile content -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Security content -->
</div>
```

**Tab keyboard behavior:**
- Arrow keys move between tabs
- Tab key moves focus into the panel
- Home/End move to first/last tab

```javascript
tablist.addEventListener('keydown', (e) => {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const index = tabs.indexOf(e.target);

  let newIndex;
  if (e.key === 'ArrowRight') newIndex = (index + 1) % tabs.length;
  else if (e.key === 'ArrowLeft') newIndex = (index - 1 + tabs.length) % tabs.length;
  else if (e.key === 'Home') newIndex = 0;
  else if (e.key === 'End') newIndex = tabs.length - 1;
  else return;

  e.preventDefault();
  activateTab(tabs[newIndex]);
});
```

**Disclosure (show/hide):**
```html
<button aria-expanded="false" aria-controls="content-1">
  Show more
</button>
<div id="content-1" hidden>
  Additional content here.
</div>
```

**Accessible tooltips:**
```html
<button aria-describedby="tooltip-1">
  Settings
</button>
<div id="tooltip-1" role="tooltip" hidden>
  Configure your account preferences
</div>
```


## Accessible Forms

### Complete Form Pattern

```html
<form novalidate>
  <!-- Group related fields -->
  <fieldset>
    <legend>Contact Information</legend>

    <div class="form-field">
      <label for="name">
        Full Name <span aria-label="required">*</span>
      </label>
      <input
        type="text"
        id="name"
        name="name"
        required
        aria-required="true"
        aria-describedby="name-error"
        autocomplete="name"
      />
      <span id="name-error" class="error" role="alert" hidden>
        Please enter your full name
      </span>
    </div>

    <div class="form-field">
      <label for="email">
        Email <span aria-label="required">*</span>
      </label>
      <input
        type="email"
        id="email"
        name="email"
        required
        aria-required="true"
        aria-describedby="email-hint email-error"
        autocomplete="email"
      />
      <span id="email-hint" class="hint">
        We'll never share your email.
      </span>
      <span id="email-error" class="error" role="alert" hidden>
        Please enter a valid email address
      </span>
    </div>
  </fieldset>

  <button type="submit">Submit</button>
</form>
```

### Form Validation JavaScript

```javascript
function validateForm(form) {
  let isValid = true;
  let firstInvalid = null;

  // Clear previous errors
  form.querySelectorAll('.error').forEach(el => el.hidden = true);
  form.querySelectorAll('[aria-invalid]').forEach(el => el.removeAttribute('aria-invalid'));

  // Validate each required field
  form.querySelectorAll('[required]').forEach(field => {
    const errorEl = document.getElementById(field.getAttribute('aria-describedby')?.split(' ').find(id => id.includes('error')));

    if (!field.value.trim() || (field.type === 'email' && !isValidEmail(field.value))) {
      field.setAttribute('aria-invalid', 'true');
      if (errorEl) errorEl.hidden = false;
      isValid = false;
      if (!firstInvalid) firstInvalid = field;
    }
  });

  // Focus first invalid field
  if (firstInvalid) firstInvalid.focus();

  return isValid;
}
```


## Color Contrast

### Minimum Ratios

| Content Type | Level AA | Level AAA |
|-------------|----------|-----------|
| Normal text (< 24px / < 18.5px bold) | 4.5:1 | 7:1 |
| Large text (≥ 24px / ≥ 18.5px bold) | 3:1 | 4.5:1 |
| UI components and graphical objects | 3:1 | 3:1 |
| Focus indicators | 3:1 | 3:1 |

### Safe Color Combinations

**On white (#FFFFFF):**
- Black (#000000) — 21:1
- Dark gray (#374151) — 10.3:1
- Blue (#1D4ED8) — 7.1:1
- Red (#B91C1C) — 5.9:1
- Green (#047857) — 5.4:1

**On dark (#111827):**
- White (#FFFFFF) — 18.1:1
- Light gray (#D1D5DB) — 10.7:1
- Light blue (#93C5FD) — 7.2:1


## Focus Management

### Focus Indicator Styles

```css
/* Remove default only if replacing with better indicator */
:focus { outline: none; }

/* Custom focus indicator — 3:1 contrast minimum */
:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

/* Focus within for composite widgets */
.widget:focus-within {
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.3);
}
```

### Focus Trapping for Modals

```javascript
function trapFocus(element) {
  const focusable = element.querySelectorAll(
    'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  element.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;

    if (e.shiftKey) {
      if (document.activeElement === first) {
        e.preventDefault();
        last.focus();
      }
    } else {
      if (document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });

  first?.focus();
}
```


## Motion and Reduced Motion

```css
/* Default animations */
.animated {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

/* Remove non-essential motion */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```


## Testing Methodology

### Automated Testing

Tools to recommend to users for ongoing testing:
- **axe DevTools** — Browser extension for automated WCAG checking
- **Lighthouse** — Built into Chrome DevTools
- **WAVE** — Web Accessibility Evaluation Tool

### Manual Testing Checklist

1. Navigate entire page using only keyboard (Tab, Enter, Escape, Arrow keys)
2. Verify all focus indicators are visible
3. Test with browser zoom at 200%
4. Test with text spacing overrides
5. Test in forced colors mode (Windows High Contrast)
6. Verify all images have meaningful alt text
7. Check heading hierarchy (no skipped levels)
8. Test forms with invalid input
9. Verify error messages are announced by screen readers
