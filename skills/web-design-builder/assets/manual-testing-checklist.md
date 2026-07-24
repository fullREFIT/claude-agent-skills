# Manual Testing Checklist

Use this checklist when Playwright MCP is not available for automated verification.


## Keyboard Navigation

- [ ] Tab through entire page — all interactive elements receive focus
- [ ] Focus indicators are clearly visible on every element
- [ ] Tab order follows logical reading order
- [ ] Enter/Space activates buttons and links
- [ ] Escape closes modals, dropdowns, and popups
- [ ] No keyboard traps (can always Tab away from any element)
- [ ] Skip link works (visible on focus, jumps to main content)


## Visual Inspection

- [ ] Open in browser and review layout
- [ ] Resize browser to mobile width (~375px) — layout adapts, no horizontal scroll
- [ ] Resize to tablet width (~768px) — layout adapts
- [ ] Zoom to 200% — content reflows, no overlap or clipping
- [ ] Text is readable at all sizes
- [ ] Images load and display correctly
- [ ] Colors and spacing match design intent


## Accessibility Quick Checks

- [ ] Open browser DevTools → Accessibility panel → check for violations
- [ ] Right-click images → verify `alt` text is present and descriptive
- [ ] Check heading hierarchy (DevTools → Elements → search for `<h`)
- [ ] Verify form inputs have `<label>` elements
- [ ] Check color contrast using browser DevTools or online checker
- [ ] Test with OS high contrast mode (if available)


## Form Testing (if applicable)

- [ ] Submit empty form — error messages appear
- [ ] Error messages are clear and specific
- [ ] Fill valid data and submit — success state appears
- [ ] Tab through form fields — focus order is logical
- [ ] Required fields are indicated visually AND with `aria-required`


## Browser Testing

Test in at least two browsers:

- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (if on macOS)


## Mobile Testing

If possible, test on an actual mobile device or use browser DevTools device emulation:

- [ ] Touch targets are at least 44x44px
- [ ] Navigation is usable on mobile
- [ ] Forms are easy to fill on mobile keyboard
- [ ] No content hidden behind mobile browser chrome


## Performance Quick Check

- [ ] Page loads within 3 seconds
- [ ] No visible layout shifts during load
- [ ] Images are appropriately sized (not loading 2000px images for thumbnails)
- [ ] Open DevTools → Console → check for JavaScript errors


## Online Tools

For more thorough testing, recommend these free tools:

| Tool | URL | Purpose |
|------|-----|---------|
| axe DevTools | Chrome extension | Automated accessibility audit |
| WAVE | wave.webaim.org | Visual accessibility checker |
| Lighthouse | Chrome DevTools | Performance + accessibility audit |
| WebAIM Contrast Checker | webaim.org/resources/contrastchecker | Color contrast verification |
| HTML Validator | validator.w3.org | HTML structure validation |
