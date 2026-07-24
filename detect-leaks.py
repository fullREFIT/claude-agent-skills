#!/usr/bin/env python3
"""
detect-leaks.py — scan a directory tree for personal/sensitive content.

Returns exit code 0 if clean, 1 if any hits found.
Usage: python3 detect-leaks.py <dir>
"""

import os, re, sys

PATTERNS = [
    # Author name
    (r'\bpaul\b', 'author-name'),
    (r'\bPaul\b', 'author-name'),
    (r'\bChambers\b', 'author-name'),
    # Brand
    (r'\bfullrefit\b', 'brand'),
    (r'\bFullRefit\b', 'brand'),
    (r'\bfullREFIT\b', 'brand'),
    (r'\bfull refit\b', 'brand'),
    (r'\bFull Refit\b', 'brand'),
    # Email addresses
    (r'paul@', 'email'),
    (r'\w+@fullrefit\.com', 'email'),
    # Absolute home paths
    (r'/Users/paul/', 'abs-path'),
    (r'/home/paul/', 'abs-path'),
    # Airtable IDs
    (r'\bapp[A-Za-z0-9]{14}\b', 'airtable-base'),
    (r'\btbl[A-Za-z0-9]{14}\b', 'airtable-table'),
    (r'\bfld[A-Za-z0-9]{14}\b', 'airtable-field'),
    (r'\bviw[A-Za-z0-9]{14}\b', 'airtable-view'),
    # Slack channel IDs
    (r'\bC0[A-Z0-9]{8,}\b', 'slack-channel'),
    (r'\bT0[A-Z0-9]{8,}\b', 'slack-workspace'),
    # Short-link / personal domains
    (r'fullrefit\.com', 'personal-domain'),
    (r'4refit\.com', 'short-link'),
    (r'bit\.ly/[A-Za-z0-9]+', 'short-link'),
    # Dropbox paths
    (r'Dropbox/', 'dropbox-path'),
    # n8n cloud hostname (private instance)
    (r'n8n\.fullrefit\.com', 'n8n-host'),
    (r'n8n\.io/workflows/\d+', 'n8n-workflow-id'),
    # Client names (add more as discovered)
    (r'\bproofeditor\.ai\b', 'client-tool'),  # Note: proof tool URL - OK if public
]

# Patterns that are OK to leave in (public services, generic examples)
ALLOWLIST = [
    r'proofeditor\.ai',  # public product
    r'1password\.com',   # public product
    r'github\.com',      # public
    r'anthropic\.com',   # public
]

def should_skip(path):
    basename = os.path.basename(path)
    return basename.startswith('.') or basename == 'detect-leaks.py'

def scan_file(filepath):
    hits = []
    try:
        text = open(filepath, encoding='utf-8', errors='ignore').read()
    except Exception:
        return hits
    for line_num, line in enumerate(text.splitlines(), 1):
        for pattern, label in PATTERNS:
            if re.search(pattern, line):
                # Check allowlist
                allowed = any(re.search(a, line) for a in ALLOWLIST)
                if not allowed:
                    hits.append((line_num, label, line.strip()[:100]))
    return hits

def scan_dir(root):
    all_hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden dirs
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for fname in filenames:
            if should_skip(fname):
                continue
            fpath = os.path.join(dirpath, fname)
            hits = scan_file(fpath)
            if hits:
                all_hits.append((fpath, hits))
    return all_hits

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <dir>", file=sys.stderr)
        sys.exit(1)
    root = sys.argv[1]
    results = scan_dir(root)
    if not results:
        print("CLEAN — no personal/sensitive content detected.")
        sys.exit(0)
    else:
        for fpath, hits in results:
            print(f"\nFILE: {fpath}")
            for line_num, label, snippet in hits:
                print(f"  L{line_num} [{label}]: {snippet}")
        print(f"\nTOTAL: {sum(len(h) for _,h in results)} hits in {len(results)} files")
        sys.exit(1)
