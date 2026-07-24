---
name: contract-redliner
description: "Review contracts against a company legal playbook and produce a structured risk report with green, yellow, and red flags before legal review. Use when uploading vendor agreements, SaaS subscriptions, service contracts, or NDAs for pre-legal risk triage. Builds a reusable playbook template once, then applies it to every subsequent contract. MANDATORY TRIGGERS: contract review, redline, contract risk, legal review, NDA, vendor agreement, SaaS contract, service agreement."
license: MIT
---

# Contract Redliner

**Catch contract risks before lawyers do.**

Your team signs contracts regularly — vendor agreements, SaaS subscriptions, service contracts, NDAs. Some get reviewed by a lawyer. Most do not. The ones that do not get reviewed are the ones that create problems six months later when you discover an auto-renewal clause, an unlimited liability provision, or an IP assignment you did not intend.

This skill does not replace your lawyer. It replaces the silence before the lawyer sees it. Upload a contract and your company's legal playbook, and get a risk report that identifies green flags (acceptable), yellow flags (worth discussing), and red flags (escalate immediately). The report includes specific language suggestions for yellow and red items so your team can negotiate before legal gets involved.

---

## How It Works

### Step 1: Build Your Playbook

A legal playbook defines what your company accepts, rejects, and negotiates in contracts. It is the standard your contracts are measured against. Without a playbook, every contract review is ad hoc — different people make different calls on the same terms.

This skill includes a playbook template you fill in once. After that, every contract gets reviewed against the same standard.

### Step 2: Upload Contract + Playbook

Paste both the contract text and your playbook into the prompt. The AI compares every clause in the contract against your playbook's rules.

### Step 3: Get a Risk Report

The output is a structured risk report with:
- Executive summary (1-2 sentences: overall risk level)
- Green flags (terms that match your playbook)
- Yellow flags (deviations worth discussing, with suggested edits)
- Red flags (risks that need lawyer review, with escalation guidance)
- Suggested edit language for every yellow and red item
- Escalation matrix (which red flags need which expertise)

---

## Risk Taxonomy

### Green — Acceptable

Terms that match your playbook. No action needed. These confirm the contract uses standard, acceptable language.

**Examples:**
- Mutual NDA with standard 2-year term
- Standard confidentiality clause matching your playbook language
- Payment terms within your acceptable range (Net 30)
- Governing law in your preferred jurisdiction
- Standard force majeure clause

### Yellow — Deviates, Worth Discussing

Terms that differ from your playbook but are not deal-breakers. These are negotiation points. The report includes specific language suggestions to bring them closer to your standard.

**Examples:**
- Payment terms are Net 60 instead of your standard Net 30
- Indemnification is one-sided but limited in scope
- Auto-renewal with 60-day notice instead of your preferred 30-day
- Limitation of liability set at 2x contract value instead of your standard 1x
- Non-compete clause that is broader than your standard
- Data retention period longer than your policy

### Red — Real Risk, Escalate

Terms that create genuine legal or financial exposure. These require lawyer review before signing. The report explains the risk in plain language and suggests what to ask for.

**Examples:**
- Unlimited liability cap (no cap on damages)
- Broad IP assignment (vendor retains rights to your custom work)
- Unilateral termination without cause by the other party
- Non-mutual indemnification with unlimited scope
- Governing law in a jurisdiction where you have no presence
- Mandatory arbitration in an unfavorable location
- Data ownership clause that gives vendor rights to your data
- Automatic price escalation with no cap
- Broad audit rights without reasonable notice

---

## Playbook Template

Fill in this template once for your company. Update it as your legal standards evolve.

### Company Legal Playbook

**Company Name:** [Your company]
**Last Updated:** [Date]
**Approved By:** [Legal counsel or CEO]

---

#### 1. Standard Acceptable Terms (We Never Negotiate These)

These terms are fine as-is in any contract:

| Term | Our Standard | Notes |
|------|-------------|-------|
| Mutual NDA | Standard mutual, 2-3 year term | Accept any mutual NDA |
| Confidentiality | Mutual obligations, reasonable scope | Standard in most contracts |
| Payment terms | Net 30 | Preferred; Net 15 also acceptable |
| Governing law | [Your state] | Preferred jurisdiction |
| Termination notice | 30 days written notice | For either party |
| Force majeure | Standard mutual clause | Accept as written |
| Dispute resolution | Mediation first, then litigation | Preferred over arbitration |

---

#### 2. Unacceptable Terms (Hard Stops)

Reject these terms or escalate to legal immediately:

| Term | Why It Is Unacceptable | Action |
|------|----------------------|--------|
| Unlimited liability | Unlimited exposure to damages | Require a cap (standard: 1x annual contract value) |
| Broad IP assignment | Gives the other party rights to our work product | Require narrow IP terms specific to deliverables |
| Unilateral termination | Other party can terminate without cause, we cannot | Require mutual termination rights |
| Non-mutual indemnification | We indemnify them but they do not indemnify us | Require mutual indemnification |
| Data ownership by vendor | Vendor claims rights to our data | Our data remains ours, always |
| Mandatory arbitration in [unfavorable jurisdiction] | Removes our ability to litigate locally | Require local jurisdiction or mutual agreement on venue |

---

#### 3. Negotiable Terms (Case-by-Case)

These terms are acceptable in some situations but should be reviewed:

| Term | Our Preference | When to Accept Alternatives |
|------|---------------|---------------------------|
| Payment terms | Net 30 | Net 45-60 acceptable for large vendors with leverage |
| Liability cap | 1x annual contract value | 2x acceptable for critical services |
| Auto-renewal | 30-day opt-out notice | 60-day notice acceptable if terms are otherwise favorable |
| Non-compete | Narrow scope, 12 months | Broader scope acceptable if compensation justifies it |
| SLA credits | Monthly service credits | Quarterly credits acceptable for lower-value contracts |
| Insurance requirements | Standard commercial coverage | Higher limits acceptable for high-risk engagements |

---

#### 4. Escalation Rules

| Situation | Escalate To | Response Time |
|-----------|------------|---------------|
| Any red flag | General Counsel or outside counsel | Within 2 business days |
| Contract value over [threshold] | CFO + Legal | Before signing |
| Non-standard IP terms | Legal (IP specialist) | Within 3 business days |
| Data processing terms (GDPR, CCPA) | Legal + Privacy Officer | Within 2 business days |
| Employment-related terms | HR + Legal | Within 2 business days |

---

#### 5. Standard Language (Our Preferred Terms)

**Limitation of Liability:**
"Neither party's aggregate liability under this Agreement shall exceed the total fees paid or payable by [Client] to [Vendor] during the twelve (12) month period preceding the claim."

**Termination for Convenience:**
"Either party may terminate this Agreement upon thirty (30) days' written notice to the other party."

**IP Ownership:**
"All work product created specifically for [Client] under this Agreement shall be owned by [Client] upon full payment. [Vendor] retains ownership of pre-existing materials and general knowledge."

**Data Ownership:**
"[Client] retains all rights, title, and interest in and to [Client] Data. [Vendor] shall not use [Client] Data for any purpose other than performing services under this Agreement."

---

## Risk Report Structure

The contract-review-prompt produces a report in this format:

### Executive Summary
1-2 sentences. Overall risk level (Low / Medium / High). Key concern if applicable.

### Contract Metadata
- Parties
- Contract type
- Term / duration
- Total value (if stated)
- Effective date

### Green Flags
| Clause | Section | Assessment |
|--------|---------|------------|
| [Clause name] | [Section reference] | Matches playbook — acceptable |

### Yellow Flags
| Clause | Section | Deviation | Suggested Edit |
|--------|---------|-----------|---------------|
| [Clause name] | [Section ref] | [How it differs from playbook] | [Specific language to propose] |

### Red Flags
| Clause | Section | Risk | Suggested Edit | Escalation |
|--------|---------|------|---------------|------------|
| [Clause name] | [Section ref] | [Plain-language risk explanation] | [Specific language to propose] | [Who to involve] |

### Escalation Matrix
| Flag | Expertise Needed | Priority |
|------|-----------------|----------|
| [Red flag] | [Legal / IP / Privacy / Finance] | [Immediate / Within 2 days / Before signing] |

### Missing Clauses
Clauses your playbook expects but that are absent from the contract:
- [Expected clause] — [Why it matters]

### Summary Recommendation
[Sign as-is / Negotiate yellow flags / Escalate red flags before proceeding / Do not sign without legal review]

---

## Example: SaaS Vendor Contract Review

### Sample Playbook (Used for This Review)

See `assets/sample-playbook.md` for the complete playbook used in this example.

### Contract Under Review

**Type:** SaaS Software License Agreement
**Parties:** Acme Corp (Customer) and CloudMetrics Inc. (Vendor)
**Term:** 12 months with auto-renewal
**Value:** $48,000/year ($4,000/month, 50 seats)

See `assets/examples/example-1-saas-contract.txt` for the full contract text.

### Generated Risk Report

**Executive Summary:**
Medium risk. The contract contains two red flags (unlimited liability for Acme and broad data usage rights for CloudMetrics) and three yellow flags (60-day auto-renewal notice, one-sided indemnification scope, and aggressive audit rights). The remaining terms are standard and match the playbook. Recommend negotiating the red flags before signing.

**Contract Metadata:**
- Parties: Acme Corp (Customer), CloudMetrics Inc. (Vendor)
- Type: SaaS Software License Agreement
- Term: 12 months, auto-renewal
- Value: $48,000/year
- Effective Date: April 1, 2026

**Green Flags:**

| Clause | Section | Assessment |
|--------|---------|------------|
| Mutual NDA | Section 7 | Standard mutual confidentiality, 2-year survival. Matches playbook. |
| Payment Terms | Section 4.1 | Net 30, monthly invoicing. Matches playbook. |
| Governing Law | Section 12 | Delaware. Acceptable jurisdiction per playbook. |
| Force Majeure | Section 11 | Standard mutual clause. Matches playbook. |
| Termination for Cause | Section 9.1 | 30-day cure period, mutual. Matches playbook. |

**Yellow Flags:**

| Clause | Section | Deviation | Suggested Edit |
|--------|---------|-----------|---------------|
| Auto-Renewal Notice | Section 3.2 | Requires 60-day notice to opt out. Playbook prefers 30 days. | "Either party may elect not to renew by providing thirty (30) days' written notice prior to the end of the then-current term." |
| Indemnification Scope | Section 8.2 | CloudMetrics indemnifies Acme for IP claims only. Acme indemnifies CloudMetrics for "any and all claims arising from Acme's use." Scope imbalance. | "Each party shall indemnify the other against third-party claims arising from its own breach of this Agreement or negligent acts." |
| Audit Rights | Section 6.3 | CloudMetrics can audit Acme's usage "at any time upon 5 business days' notice." Playbook prefers 30 days' notice and once per year. | "Vendor may audit Customer's compliance with usage terms no more than once per twelve-month period, upon thirty (30) days' written notice." |

**Red Flags:**

| Clause | Section | Risk | Suggested Edit | Escalation |
|--------|---------|------|---------------|------------|
| Liability Cap | Section 10.1 | No liability cap for Acme. CloudMetrics' liability is capped at 12 months' fees. Acme has unlimited exposure. | "Neither party's aggregate liability shall exceed the total fees paid or payable during the twelve (12) month period preceding the claim." | General Counsel — Immediate |
| Data Usage Rights | Section 5.3 | "CloudMetrics may use Customer Data in anonymized, aggregated form for any business purpose including product improvement and benchmarking." This gives CloudMetrics broad rights to Acme's operational data. | "Vendor shall not use Customer Data for any purpose other than providing the Services. Any use of anonymized data requires Customer's prior written consent." | General Counsel + Privacy Officer — Before signing |

**Missing Clauses:**
- **Data Processing Agreement (DPA):** No DPA referenced or attached. If Acme's data includes personal information (employee data, customer data), a DPA is required for GDPR/CCPA compliance.
- **SLA with Service Credits:** No uptime commitment or service credits defined. Playbook expects 99.9% uptime SLA with monthly service credits.
- **Termination for Convenience:** Contract only allows termination for cause. Playbook expects mutual termination for convenience with 30 days' notice.

**Escalation Matrix:**

| Flag | Expertise Needed | Priority |
|------|-----------------|----------|
| Unlimited liability for Acme | General Counsel | Immediate — do not sign without a mutual cap |
| Broad data usage rights | General Counsel + Privacy Officer | Before signing — assess data sensitivity |
| Missing DPA | Privacy Officer | Before signing if personal data is involved |

**Summary Recommendation:**
Do not sign as-is. Negotiate the two red flags (liability cap and data usage rights) and request a DPA. The three yellow flags are standard negotiation points that can be addressed in parallel. The green flags indicate the rest of the contract is reasonable. With the red flag corrections, this is a signable agreement.

---

## How to Implement

### Step 1: Build Your Playbook
Use the playbook template in `assets/playbook-template.md`. Fill in your company's standards. Have your legal counsel or CEO review and approve it.

### Step 2: Review a Contract
1. Open Claude
2. Paste the contract-review-prompt from `scripts/contract-review-prompt.txt`
3. Paste your playbook
4. Paste the contract text
5. Run it
6. Review the risk report
7. For green and yellow flags, your team can handle negotiations
8. For red flags, forward the report to legal with the specific concerns highlighted

### Step 3: Negotiate
Use the suggested edit language as starting points for negotiation. The suggested edits are designed to be reasonable — they protect your interests without being adversarial.

### Step 4: Iterate
If the other party sends a revised contract, run it through the prompt again with the same playbook to verify the changes were made correctly.

---

## Important Disclaimer

This skill is a review tool, not legal advice. It identifies common contract risks based on your playbook and standard business law principles. It does not replace qualified legal counsel. Always have a lawyer review contracts involving:
- Significant financial exposure
- Complex IP arrangements
- Employment or contractor classifications
- Regulatory compliance requirements
- International jurisdictions you are unfamiliar with
- Any term you do not fully understand
