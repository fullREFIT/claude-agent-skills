# Contract Redliner — Quick Start

**Time to set up:** 15 minutes (one-time playbook creation), then 5 minutes per contract review
**What you need:** Contract text + your legal playbook

---

## What This Skill Does

Compares contracts against your company's legal playbook and produces a risk report with green/yellow/red flags and specific edit suggestions. Does not replace your lawyer — catches risks before the lawyer needs to get involved.

---

## First-Time Setup (15 Minutes)

1. **Open** `assets/playbook-template.md`
2. **Fill in** your company's standard acceptable terms, hard stops, and negotiable terms
3. **Have your legal counsel or CEO review** the completed playbook
4. **Save** the playbook — you will reuse it for every contract review

---

## Reviewing a Contract (5 Minutes)

1. **Open Claude** (or ChatGPT)
2. **Paste** the contract-review-prompt from `scripts/contract-review-prompt.txt`
3. **Paste** your playbook
4. **Paste** the contract text
5. **Run it** — you get a risk report with flags and suggested edits
6. **Handle** green/yellow flags internally; escalate red flags to legal

---

## Folder Contents

```
contract-redliner.skill/
  SKILL.md                                Full framework + risk taxonomy + example
  README.md                               This file
  assets/
    playbook-template.md                  Fill-in playbook template
    risk-taxonomy.md                      Green/Yellow/Red definitions + examples
    sample-playbook.md                    Complete example playbook for reference
    examples/
      example-1-saas-contract.txt         Sample SaaS contract
      example-1-playbook.md               Playbook used for the review
      example-1-output-report.md          Generated risk report
  scripts/
    contract-review-prompt.txt            The reusable prompt (copy-paste into Claude)
```

---

## Risk Levels

- **Green:** Matches your playbook. No action needed.
- **Yellow:** Deviates from your playbook. Negotiate using the suggested edit language.
- **Red:** Real risk. Escalate to your lawyer with the risk report attached.

---

## Important

This skill is a review tool, not legal advice. Always involve qualified legal counsel for contracts with significant financial exposure, complex IP terms, or regulatory compliance requirements.
