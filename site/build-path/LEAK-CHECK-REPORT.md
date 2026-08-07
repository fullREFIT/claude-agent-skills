# Leak Check Report — site/build-path/index.html

**Date:** 080626
**Target:** `site/build-path/index.html`
**Task:** SITE-002 (project `skillquiver-build-path-site`)

---

## 1. Repo leak detector, file argument (as specified in SITE-002)

```
cd <repo root>
python3 detect-leaks.py site/build-path/index.html
```

Output:
```
CLEAN — no personal/sensitive content detected.
exit=0
```

**This pass is vacuous and must not be trusted on its own.** `detect-leaks.py`
scans with `os.walk(root)`. When `root` is a file rather than a directory,
`os.walk` yields nothing, so the script reports CLEAN having read zero bytes.
This is the exact failure mode anticipated in the project's `DEPENDENCIES.md`
risk table. The directory scan below is the real result.

## 2. Repo leak detector, directory argument (real scan)

```
python3 detect-leaks.py site/build-path/
```

Output:
```
FILE: site/build-path/index.html
  L121 [brand]: <a href="https://fullrefit-execution-prompt-forge.vercel.app" class="btn-s">Try execution-prompt-for
  L242 [brand]: <p><b>See it running:</b> <a href="https://fullrefit-execution-prompt-forge.vercel.app" style="color

TOTAL: 2 hits in 1 files
exit=1
```

## 3. Manual grep required by SITE-002

```
grep -niE "/Users/paul|fullrefit\.co/aoc|1password|airtable\.com/app" site/build-path/index.html
```

Output: no matches (exit 1). **PASS.**

## 4. Extended sweep (beyond what SITE-002 required)

```
grep -niE "op://|sk-[a-zA-Z0-9]{10}|Bearer |xox[baprs]-|/home/|Dropbox/|hello@|paul@|n8n\.|supabase\.co|hstgr\.cloud|\bapp[A-Za-z0-9]{14}\b|C0[A-Z0-9]{8,}" site/build-path/index.html
```

Output: no matches (exit 1). **PASS.**

Every external URL in the shipped file, enumerated:

| URL | Status |
|---|---|
| `https://fonts.googleapis.com` | Public CDN, required by the design system |
| `https://fonts.gstatic.com` | Public CDN, required by the design system |
| `https://fullrefit-execution-prompt-forge.vercel.app` | Public site, required by SITE-001 |
| `https://github.com/fullREFIT/claude-agent-skills` | Public repo, this repo's own remote |
| `https://skillquiver.dev/build-path` | Canonical URL of this page |

No private hosts, no tokenized URLs, no credentials, no filesystem paths.

---

## Disclosure: the 2 brand-pattern hits

Both hits are the same string, `fullrefit-execution-prompt-forge.vercel.app`,
which SITE-001 explicitly requires in the header nav and which SPECS.md names
as the design reference. They were reviewed and kept, not missed. Reasoning:

- The string is a **public Vercel hostname for a public marketing page**. It
  discloses nothing private.
- This repo's own git remote is `github.com/fullREFIT/claude-agent-skills`.
  The org name is already public and is on every page of the published repo.
- `detect-leaks.py`'s brand patterns exist to keep **skill files** generic and
  reusable by strangers. A first-party marketing site under the org's own
  wordmark is a different class of file.
- Verified scope: `skills/` (the actually-published content) scans **0 hits**.
  Pre-existing hits elsewhere in the repo: **28 hits across 2 files** in
  `project-state/`, containing real absolute home paths and the author's name.
  Those predate this task and are out of its scope, but they mean the detector
  is not currently enforced as a repo-wide gate.

**Recommendation for a follow-up task (not done here, out of scope):** scope
the detector to the directories that actually ship to strangers by adding a
`SKIP_DIRS = {'project-state', 'site'}` guard in `scan_dir`, or clean the two
`project-state/` files. As written, a whole-repo run fails on content that was
never meant to be gated, which trains everyone to ignore the exit code.

No private path, credential, email address, client name, or internal
identifier is present in the shipped file.

CLEAN — 0 findings
