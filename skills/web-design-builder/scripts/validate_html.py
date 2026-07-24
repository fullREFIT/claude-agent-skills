#!/usr/bin/env python3
"""
HTML Design Validator - Checks HTML files for common accessibility and structure issues.

Usage:
    python scripts/validate_html.py <path/to/file.html>
    python scripts/validate_html.py <path/to/directory>

Checks:
    - DOCTYPE declaration
    - lang attribute on <html>
    - viewport meta tag
    - Page title
    - Heading hierarchy (h1-h6)
    - Skip link presence
    - Image alt text
    - Form label associations
    - ARIA landmark usage
    - Focus indicator styles
    - prefers-reduced-motion media query
"""

import sys
import re
from pathlib import Path


def validate_html(content, filename=""):
    """Validate an HTML file for accessibility and structure issues."""
    issues = []
    warnings = []
    passes = []

    # DOCTYPE
    if re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE):
        passes.append("DOCTYPE declaration present")
    else:
        issues.append("Missing <!DOCTYPE html> declaration")

    # lang attribute
    if re.search(r'<html[^>]*\slang\s*=\s*["\'][a-z]', content, re.IGNORECASE):
        passes.append("lang attribute on <html>")
    else:
        issues.append("Missing lang attribute on <html> element")

    # Viewport meta
    if re.search(r'<meta[^>]*name\s*=\s*["\']viewport["\']', content, re.IGNORECASE):
        passes.append("Viewport meta tag present")
    else:
        issues.append("Missing viewport meta tag")

    # Page title
    title_match = re.search(r'<title[^>]*>(.+?)</title>', content, re.IGNORECASE | re.DOTALL)
    if title_match and title_match.group(1).strip():
        passes.append(f"Page title: \"{title_match.group(1).strip()[:50]}\"")
    else:
        issues.append("Missing or empty <title> element")

    # Heading hierarchy
    headings = re.findall(r'<(h[1-6])[^>]*>', content, re.IGNORECASE)
    h1_count = sum(1 for h in headings if h.lower() == 'h1')

    if h1_count == 1:
        passes.append("Single h1 element present")
    elif h1_count == 0:
        issues.append("No h1 element found")
    else:
        warnings.append(f"Multiple h1 elements found ({h1_count})")

    # Check heading level skips
    if headings:
        prev_level = 0
        for h in headings:
            level = int(h[1])
            if level > prev_level + 1 and prev_level > 0:
                warnings.append(f"Heading level skipped: h{prev_level} to h{level}")
            prev_level = level

    # Skip link
    if re.search(r'<a[^>]*href\s*=\s*["\']#(main|content|main-content)["\']', content, re.IGNORECASE):
        passes.append("Skip link present")
    elif re.search(r'skip.*(link|nav|content)', content, re.IGNORECASE):
        passes.append("Skip link present (class-based)")
    else:
        issues.append("Missing skip link (<a href=\"#main-content\">Skip to main content</a>)")

    # Image alt text
    images = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
    images_without_alt = [img for img in images if not re.search(r'\salt\s*=', img, re.IGNORECASE)]
    if images:
        if not images_without_alt:
            passes.append(f"All {len(images)} images have alt text")
        else:
            issues.append(f"{len(images_without_alt)} of {len(images)} images missing alt text")

    # Form labels
    inputs = re.findall(r'<input[^>]*>', content, re.IGNORECASE)
    visible_inputs = [inp for inp in inputs if not re.search(r'type\s*=\s*["\'](?:hidden|submit|button|reset)["\']', inp, re.IGNORECASE)]
    labeled_inputs = [inp for inp in visible_inputs if re.search(r'\sid\s*=', inp, re.IGNORECASE)]

    labels = re.findall(r'<label[^>]*\sfor\s*=\s*["\']([^"\']+)["\']', content, re.IGNORECASE)

    if visible_inputs:
        unlabeled = 0
        for inp in visible_inputs:
            id_match = re.search(r'\sid\s*=\s*["\']([^"\']+)["\']', inp, re.IGNORECASE)
            if id_match:
                if id_match.group(1) not in labels:
                    # Check if wrapped in <label>
                    if not re.search(r'<label[^>]*>.*?' + re.escape(inp) + r'.*?</label>', content, re.IGNORECASE | re.DOTALL):
                        unlabeled += 1
            else:
                # No id — check if wrapped in label
                if not re.search(r'<label[^>]*>.*?' + re.escape(inp[:30]) + r'.*?</label>', content, re.IGNORECASE | re.DOTALL):
                    unlabeled += 1

        if unlabeled == 0:
            passes.append("All form inputs have associated labels")
        else:
            issues.append(f"{unlabeled} form inputs missing associated <label>")

    # Semantic landmarks
    has_header = bool(re.search(r'<header[\s>]', content, re.IGNORECASE))
    has_main = bool(re.search(r'<main[\s>]', content, re.IGNORECASE))
    has_footer = bool(re.search(r'<footer[\s>]', content, re.IGNORECASE))
    has_nav = bool(re.search(r'<nav[\s>]', content, re.IGNORECASE))

    landmarks = []
    if has_header: landmarks.append("header")
    if has_nav: landmarks.append("nav")
    if has_main: landmarks.append("main")
    if has_footer: landmarks.append("footer")

    if has_main:
        passes.append(f"Semantic landmarks: {', '.join(landmarks)}")
    else:
        issues.append("Missing <main> landmark element")

    if not has_header:
        warnings.append("No <header> element found")
    if not has_nav:
        warnings.append("No <nav> element found")

    # Focus styles
    if re.search(r':focus-visible|:focus\b', content):
        passes.append("Focus styles defined")
    else:
        warnings.append("No :focus-visible or :focus styles found")

    # prefers-reduced-motion
    if re.search(r'prefers-reduced-motion', content):
        passes.append("prefers-reduced-motion media query present")
    else:
        warnings.append("No prefers-reduced-motion media query found")

    # aria-required on required inputs
    required_inputs = [inp for inp in inputs if re.search(r'\brequired\b', inp, re.IGNORECASE)]
    if required_inputs:
        aria_required = [inp for inp in required_inputs if re.search(r'aria-required', inp, re.IGNORECASE)]
        if len(aria_required) == len(required_inputs):
            passes.append("All required inputs have aria-required")
        else:
            warnings.append(f"{len(required_inputs) - len(aria_required)} required inputs missing aria-required")

    return issues, warnings, passes


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_html.py <path/to/file.html>")
        print("       python scripts/validate_html.py <path/to/directory>")
        sys.exit(1)

    target = Path(sys.argv[1])

    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.glob("**/*.html"))
        if not files:
            print(f"No HTML files found in {target}")
            sys.exit(1)
    else:
        print(f"Error: {target} not found")
        sys.exit(1)

    total_issues = 0
    total_warnings = 0

    for filepath in files:
        content = filepath.read_text(encoding='utf-8', errors='replace')
        issues, warnings, passes = validate_html(content, filepath.name)

        print(f"\n{'='*60}")
        print(f"  {filepath.name}")
        print(f"{'='*60}")

        if passes:
            for p in passes:
                print(f"  ✅ {p}")

        if warnings:
            print()
            for w in warnings:
                print(f"  ⚠️  {w}")

        if issues:
            print()
            for i in issues:
                print(f"  ❌ {i}")

        total_issues += len(issues)
        total_warnings += len(warnings)

        print()

    # Summary
    print(f"{'='*60}")
    if total_issues == 0:
        print(f"  ✅ All checks passed! ({total_warnings} warnings)")
        sys.exit(0)
    else:
        print(f"  ❌ {total_issues} issues found, {total_warnings} warnings")
        sys.exit(1)


if __name__ == "__main__":
    main()
