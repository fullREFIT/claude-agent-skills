---
name: docx
description: "Word document (.docx) creation, editing, and analysis with support for tracked changes, comments, and formatting preservation. Use when Claude needs to work with .docx files for creating new documents, modifying or editing content, working with tracked changes, adding comments, or any other Word document tasks. MANDATORY TRIGGERS: Word, .docx, document creation, tracked changes, comments, redlining, letter, memo, formal report, resume, contract."
---

# DOCX Creation, Editing, and Analysis

## Overview

Create, edit, or analyze Word documents (.docx). A .docx file is a ZIP archive containing XML files (Office Open XML format) and resources.

## Creating New Documents

To create new .docx documents from scratch using JavaScript, read [`../docx-js.md`](../docx-js.md) for the complete tutorial covering:

- Text formatting, styles, professional typography
- Proper lists (never use Unicode bullets — always use numbering config with `LevelFormat.BULLET`)
- Tables with borders, shading, and proper widths
- Links, table of contents, navigation
- Images, headers/footers, page setup
- Page breaks and multi-section documents

**Critical rules from the tutorial:**
- Never use `\n` for line breaks — always use separate Paragraph elements
- Always use `ShadingType.CLEAR` for table cell shading (never SOLID)
- Always specify `type` parameter for ImageRun ("png", "jpg", etc.)
- Set both `columnWidths` array AND individual cell widths for tables
- Use `LevelFormat.BULLET` constant, not the string "bullet"
- PageBreak must always be inside a Paragraph wrapper

## Editing Existing Documents

To edit existing .docx files using OOXML manipulation, read [`../ooxml.md`](../ooxml.md) for:

- Schema compliance and XML validation rules
- Document content patterns (headings, lists, tables, layout, images, links)
- The Document Python class for tracked changes and comments
- Image insertion with proper dimensions and relationships
- Hyperlink creation (internal and external)

### Editing Workflow

1. Unpack the document: `python ooxml/scripts/unpack.py <office_file> <output_dir>`
2. Edit XML files (primarily `word/document.xml`)
3. **CRITICAL**: Validate after each edit: `python ooxml/scripts/validate.py <dir> --original <file>`
4. Pack the final document: `python ooxml/scripts/pack.py <input_directory> <office_file>`

## Analyzing Documents

### Text Extraction

```bash
python -m markitdown document.docx
```

### Structure Inspection

Unpack and examine the XML structure:

| File | Purpose |
|------|---------|
| `word/document.xml` | Main document content |
| `word/styles.xml` | Style definitions |
| `word/numbering.xml` | List definitions |
| `word/comments.xml` | Comments |
| `word/settings.xml` | Document settings |
| `word/_rels/document.xml.rels` | Relationships |

## When to Choose DOCX over Markdown

- Tracked changes or formal review workflows required
- Precise print layout control needed
- Specific Word template must be used
- Document will be edited collaboratively in Microsoft Word
- Formal business correspondence (letters on letterhead, contracts)
- Resume or CV that must be in Word format

For general reports, documentation, and artifacts, prefer Markdown (see parent skill).

## Dependencies

- **docx** (npm): `npm install -g docx` — JavaScript document creation
- **markitdown**: `pip install markitdown` — Text extraction
- **defusedxml**: `pip install defusedxml` — Secure XML parsing
- **Pillow**: `pip install Pillow` — Image handling for insertion
