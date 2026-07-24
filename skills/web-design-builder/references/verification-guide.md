# Verification Guide

Playwright MCP commands and procedures for automated design verification.


## Prerequisites

Playwright MCP must be available in the Claude Code session. Check for tools matching `mcp__playwright__*` before attempting verification.

### If Playwright MCP Is Not Available

Inform the user and provide:
1. Installation instructions (below)
2. The manual testing checklist from `assets/manual-testing-checklist.md`
3. Continue with design generation — skip verification


## Installing Playwright MCP

### Option 1: Claude Code CLI

```bash
claude mcp add playwright -- npx @anthropic-ai/mcp-server-playwright
```

### Option 2: Manual Configuration

Add to Claude Code MCP settings:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-playwright"]
    }
  }
}
```

Restart Claude Code after configuration.


## Verification Procedure

### Step 1: Load the Design

Navigate to the saved HTML file:

```
mcp__playwright__browser_navigate({ url: "file:///path/to/design.html" })
```

### Step 2: Take Full-Page Screenshot

```
mcp__playwright__browser_screenshot()
```

Review the screenshot visually. Check for:
- Layout rendering correctly
- Text readable and properly sized
- Colors and spacing as intended
- No overflow or broken elements

### Step 3: Responsive Testing

Test at standard breakpoints:

**Mobile (375x667):**
```
mcp__playwright__browser_resize({ width: 375, height: 667 })
mcp__playwright__browser_screenshot()
```

**Tablet (768x1024):**
```
mcp__playwright__browser_resize({ width: 768, height: 1024 })
mcp__playwright__browser_screenshot()
```

**Desktop (1440x900):**
```
mcp__playwright__browser_resize({ width: 1440, height: 900 })
mcp__playwright__browser_screenshot()
```

At each breakpoint, verify:
- Layout adapts appropriately
- Navigation changes for mobile (hamburger menu)
- Images and cards reflow
- Text remains readable
- No horizontal scrolling

### Step 4: Accessibility Audit

Run the accessibility snapshot:

```
mcp__playwright__browser_snapshot()
```

Check the accessibility tree for:
- All interactive elements have accessible names
- Heading hierarchy is logical (h1 → h2 → h3)
- ARIA landmarks present (banner, navigation, main, contentinfo)
- Form inputs have associated labels
- Images have alt text
- Links have descriptive text (not "click here")

### Step 5: Keyboard Navigation Testing

Test keyboard navigation by simulating Tab key presses:

```
mcp__playwright__browser_press_key({ key: "Tab" })
mcp__playwright__browser_screenshot()
```

Repeat Tab presses to verify:
- Focus moves through all interactive elements
- Focus indicators are visible
- Focus order follows visual layout
- No elements are skipped
- No keyboard traps (can always Tab away)

Test specific interactions:
- **Enter/Space** on buttons and links
- **Escape** to close modals/dropdowns
- **Arrow keys** in tab lists, radio groups, select menus

### Step 6: Form Testing

If the design includes forms:

**Test empty submission:**
```
mcp__playwright__browser_click({ element: "Submit button" })
mcp__playwright__browser_screenshot()
```
Verify error messages appear with `role="alert"`.

**Test valid input:**
```
mcp__playwright__browser_click({ element: "Name input" })
mcp__playwright__browser_type({ text: "Test User" })
mcp__playwright__browser_click({ element: "Email input" })
mcp__playwright__browser_type({ text: "test@example.com" })
mcp__playwright__browser_click({ element: "Submit button" })
mcp__playwright__browser_screenshot()
```
Verify success state appears.

### Step 7: Interactive Component Testing

Test modals, dropdowns, accordions, tabs:

**Modal:**
```
mcp__playwright__browser_click({ element: "Open modal button" })
mcp__playwright__browser_screenshot()
```
Verify: modal opens, backdrop visible, focus moved into modal.

```
mcp__playwright__browser_press_key({ key: "Escape" })
mcp__playwright__browser_screenshot()
```
Verify: modal closes, focus returns to trigger button.

### Step 8: Console Error Check

```
mcp__playwright__browser_console_messages()
```

Check for JavaScript errors. Warnings about missing resources or deprecations are acceptable; actual errors must be fixed.


## Verification Report

After all tests, generate a report using the template at `assets/verification-report-template.md`.

### Result Categories

| Symbol | Meaning |
|--------|---------|
| ✅ PASS | Meets requirements |
| ⚠️ WARNING | Minor issue, non-blocking |
| ❌ FAIL | Must fix before delivery |

### Priority Levels

| Priority | Description | Action |
|----------|-------------|--------|
| **Critical** | Accessibility violation, broken functionality | Fix immediately |
| **High** | Visual issue, missing feature | Fix before delivery |
| **Medium** | Enhancement opportunity | Recommend to user |
| **Low** | Nice-to-have improvement | Note for future |


## Common Issues and Fixes

| Issue | Detection | Fix |
|-------|-----------|-----|
| Missing skip link | No skip link in accessibility tree | Add `<a href="#main" class="skip-link">` |
| No focus indicators | Tab through page, no visual change | Add `:focus-visible` styles |
| Missing form labels | Accessibility tree shows unlabeled inputs | Add `<label for="id">` |
| Low contrast text | Visual inspection of light gray text | Darken text to meet 4.5:1 |
| No alt text on images | Accessibility tree shows "image" without name | Add descriptive `alt` attribute |
| Keyboard trap | Can't Tab out of component | Fix tabindex and event handlers |
| Missing lang attribute | Accessibility tree root has no language | Add `lang="en"` to `<html>` |
| Horizontal scroll on mobile | Mobile screenshot shows overflow | Fix with `max-width: 100%` and `overflow-x: hidden` |
