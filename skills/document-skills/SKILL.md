---
name: document-skills
description: "Universal document creation, editing, conversion, and analysis across all major formats. Handles Markdown (.md) for rendered artifacts, reports, README files, and documentation. Routes to specialized sub-skills for PDF (.pdf), PowerPoint (.pptx), and Word (.docx). Also covers CSV/TSV data export. Use when producing any formatted document, creating rendered text artifacts, generating reports, writing documentation, exporting data, or converting between formats. MANDATORY TRIGGERS: document, markdown, .md, artifact, report, README, CSV, memo, documentation, notes, guide, letter, export."
---

# Document Skills

Unified document creation, editing, and conversion across all major formats. Choose the right format, then follow format-specific guidance below.

## Table of Contents

1. [Format Selection Guide](#format-selection-guide)
2. [Markdown Documents](#markdown-documents)
3. [CSV and Structured Data](#csv-and-structured-data)
4. [PDF Documents](#pdf-documents)
5. [PowerPoint Presentations](#powerpoint-presentations)
6. [Word Documents](#word-documents)
7. [Format Conversion](#format-conversion)
8. [Quality Checklist](#quality-checklist)

---

## Format Selection Guide

| If the user needs... | Format | Why |
|---------------------|--------|-----|
| A rendered, formatted artifact | **Markdown** | Native artifact format, renders beautifully |
| A report, analysis, or write-up | **Markdown** | Fast, flexible, universal readability |
| README, CONTRIBUTING, docs | **Markdown** | GitHub/GitLab standard |
| Meeting notes, project plans | **Markdown** | Lightweight, version-control friendly |
| Blog post, article, guide | **Markdown** | Works with all static site generators |
| Structured data export | **CSV/TSV** | Universal spreadsheet import |
| Printed/shared formal document | **PDF** | Fixed layout, universal viewing |
| Form filling | **PDF** | See `pdf/forms.md` |
| Slide deck, presentation | **PPTX** | Full visual control, animations |
| Formal document with tracked changes | **DOCX** | Word compatibility, review workflows |
| Letter, resume, or template-based doc | **DOCX** | Professional formatting, print-ready |

**Default to Markdown** when the user says "create a document," "write a report," or "make an artifact" without specifying a format. Markdown is the fastest to produce, easiest to read, and renders directly in Claude's artifact window.

---

## Markdown Documents

Markdown is the primary format for rendered text artifacts, documentation, reports, and any formatted text output. Use as the default unless a specific office format is required.

### When to Use Markdown

- **Artifacts** — Any request for a formatted, rendered document in Claude's interface
- **Documentation** — README files, guides, tutorials, API docs, changelogs
- **Reports** — Analyses, summaries, research findings, meeting notes
- **Content** — Blog posts, articles, newsletters for static site generators
- **Planning** — Project plans, specifications, decision records
- **Knowledge bases** — SOPs, playbooks, reference materials

### Document Structure Patterns

**Short document (<50 lines):**

```markdown
# Title

Brief introduction paragraph.

## Key Points

- Point one with explanation
- Point two with explanation
- Point three with explanation

## Conclusion

Summary and next steps.
```

**Long document (50+ lines) — always include a table of contents:**

```markdown
# Document Title

Brief description of purpose and audience.

## Table of Contents

1. [Section One](#section-one)
2. [Section Two](#section-two)
3. [Section Three](#section-three)

---

## Section One

Content organized with sub-headings, lists, and tables as needed.

## Section Two

Content...
```

**Report format:**

```markdown
# Report Title

**Date:** YYYY-MM-DD
**Author:** Name
**Status:** Draft | Final

## Executive Summary

2-3 sentences capturing key findings and recommendations.

## Background

Context the reader needs.

## Findings

### Finding 1: Title
Details, evidence, data.

### Finding 2: Title
Details, evidence, data.

## Recommendations

| Priority | Action | Owner | Timeline |
|----------|--------|-------|----------|
| High | Action item | Name | Date |
| Medium | Action item | Name | Date |

## Appendix

Supporting data, methodology notes, references.
```

### Professional Formatting Techniques

**Visual hierarchy** — Use heading levels consistently:
- `#` for document title (one per document)
- `##` for major sections
- `###` for subsections
- `####` sparingly, for sub-subsections only

**Emphasis for scannability:**
- **Bold** for key terms, important callouts, and action items
- *Italic* for titles of works, technical terms, and subtle emphasis
- `Code` for file names, commands, variable names, and literal values

**Tables** — Use for structured comparisons, not for layout:

```markdown
| Feature | Free Plan | Pro Plan |
|---------|-----------|----------|
| Users   | 5         | Unlimited|
| Storage | 1 GB      | 100 GB   |
```

**Code blocks** — Always specify the language for syntax highlighting:

````markdown
```python
def hello():
    print("Hello, World!")
```
````

**Task lists** — For actionable checklists:

```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

**Blockquotes** — For callouts and important notes:

```markdown
> **Note:** Important consideration that readers should not overlook.
```

**Horizontal rules** — Use `---` to separate major sections visually.

### Advanced Features

For detailed coverage of advanced Markdown features, read [`markdown/reference.md`](markdown/reference.md) which covers:
- **Mermaid diagrams** — Flowcharts, sequence diagrams, Gantt charts, ER diagrams
- **LaTeX math** — Inline `$E=mc^2$` and block equations
- **YAML frontmatter** — Metadata for static sites, skills, and structured documents
- **Footnotes** — Academic and technical references
- **Admonitions/callouts** — GitHub alert boxes (`> [!NOTE]`, `> [!WARNING]`)
- **Platform rendering reference** — What works where (GitHub, GitLab, Obsidian, Claude artifacts, VS Code)
- **Document templates** — Ready-to-use structures for reports, READMEs, meeting notes, API docs, changelogs

### Artifact-Specific Guidance

When creating rendered Markdown artifacts in Claude's interface:

1. **Use clean structure** — Headings, lists, and tables render beautifully
2. **Include a title** — Start with `# Title` for visual clarity
3. **Keep it self-contained** — Don't reference external files the user can't see
4. **Use tables for data** — They render as formatted tables in the artifact window
5. **Code blocks render with syntax highlighting** — Always specify the language
6. **Mermaid diagrams render** — Use fenced code blocks with `mermaid` language tag
7. **Math renders** — Use `$inline$` and `$$block$$` LaTeX notation
8. **Avoid raw HTML** — Stick to standard Markdown for best rendering

### Anti-Patterns

- Do NOT create Markdown when the user explicitly asks for PDF, DOCX, or PPTX
- Do NOT use HTML tables when Markdown tables suffice
- Do NOT skip heading levels (e.g., jump from `##` to `####`)
- Do NOT use excessive emphasis (bold AND italic AND caps simultaneously)
- Do NOT create walls of text without visual breaks (lists, headings, horizontal rules)

---

## CSV and Structured Data

Use CSV/TSV for tabular data export, spreadsheet import, or data interchange.

### When to Use CSV

- Exporting data for spreadsheet analysis
- Data interchange between systems
- Tabular reports intended for further processing
- Any structured data the user will import elsewhere

### CSV Formatting Rules

```csv
"Header One","Header Two","Header Three"
"Value with, comma","Simple value","123"
"Value with ""quotes""","Another value","456"
```

- **Always quote fields** containing commas, quotes, or newlines
- **Escape quotes** by doubling: `"He said ""hello"""`
- **Use UTF-8 encoding** for international characters
- **Include a header row** unless explicitly told not to
- **Consistent column count** across all rows
- **No trailing commas** at end of rows

### TSV Alternative

Use TSV (tab-separated values) when data frequently contains commas:

```
Header One	Header Two	Header Three
Value one	Value two	123
```

---

## PDF Documents

For PDF creation, manipulation, text extraction, form filling, and analysis, use the separate `pdf` skill which handles:
- Text and table extraction (pypdf, pdfplumber)
- PDF creation (reportlab)
- Merging, splitting, rotating
- OCR for scanned documents
- Password protection and watermarks
- Form filling (fillable and non-fillable)

---

## PowerPoint Presentations

For creating, editing, and analyzing presentations, use the separate `pptx` skill which handles:
- Creating presentations from scratch (html2pptx workflow)
- Editing existing presentations (OOXML manipulation)
- Creating from templates (rearrange + replace workflow)
- Thumbnail generation and visual validation
- Design principles and color palette selection

---

## Word Documents

For creating and editing Word documents (.docx):

### Creating New DOCX Files

Read [`docx-js.md`](docx-js.md) for the complete JavaScript docx library tutorial covering:
- Text formatting, styles, professional typography
- Proper lists (never use Unicode bullets — always use numbering config with `LevelFormat.BULLET`)
- Tables with borders, shading, and proper widths
- Links, table of contents, navigation
- Images, headers/footers, page setup

**Critical rules:**
- Never use `\n` for line breaks — always use separate Paragraph elements
- Always use `ShadingType.CLEAR` for table cell shading (never SOLID)
- Always specify `type` parameter for ImageRun ("png", "jpg", etc.)
- Set both `columnWidths` array AND individual cell widths for tables

### Editing Existing DOCX Files

Read [`ooxml.md`](ooxml.md) for Office Open XML manipulation covering:
- Schema compliance and XML validation rules
- Document content patterns (headings, lists, tables, layout, images, links)
- The Document Python class for tracked changes and comments
- Image insertion with proper dimensions and relationships

### When to Choose DOCX over Markdown

- Tracked changes or formal review workflows required
- Precise print layout control needed
- Specific Word template must be used
- Document will be edited collaboratively in Microsoft Word
- Formal business correspondence (letters on letterhead, contracts)

---

## Format Conversion

### Markdown to Other Formats (Pandoc)

```bash
# Markdown to DOCX
pandoc input.md -o output.docx

# Markdown to PDF (requires LaTeX)
pandoc input.md -o output.pdf

# Markdown to HTML
pandoc input.md -o output.html --standalone

# Markdown to PPTX (slide breaks on ## headings)
pandoc input.md -o output.pptx

# With custom reference doc styling
pandoc input.md -o output.docx --reference-doc=template.docx
```

### Other Formats to Markdown (markitdown)

```bash
# Convert any document to Markdown for analysis
python -m markitdown document.docx
python -m markitdown presentation.pptx
python -m markitdown spreadsheet.xlsx
```

### Direct Conversion Between Office Formats

```bash
# LibreOffice command-line conversion
soffice --headless --convert-to pdf document.docx
soffice --headless --convert-to docx document.pdf
soffice --headless --convert-to pdf presentation.pptx
```

---

## Quality Checklist

### All Formats
- [ ] Correct format chosen for the use case
- [ ] Document has a clear title and structure
- [ ] Content is complete and accurate
- [ ] No placeholder text remaining
- [ ] Consistent formatting throughout

### Markdown
- [ ] Heading hierarchy is correct (no skipped levels)
- [ ] Table of contents included for documents >50 lines
- [ ] Code blocks specify language for syntax highlighting
- [ ] Tables are properly aligned
- [ ] Links are valid and descriptive
- [ ] No unnecessary raw HTML
- [ ] Renders correctly in target platform

### CSV
- [ ] Header row present
- [ ] Fields with special characters are properly quoted
- [ ] Consistent column count across all rows
- [ ] UTF-8 encoding

### Office Formats (PDF/PPTX/DOCX)
- [ ] Sub-skill quality checklist completed
- [ ] Visual validation performed where applicable
- [ ] File opens correctly in target application
