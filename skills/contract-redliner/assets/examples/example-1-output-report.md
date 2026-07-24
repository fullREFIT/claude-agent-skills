# Risk Report: CloudMetrics SaaS Agreement

## Executive Summary

**Risk Level: Medium.** The contract contains two red flags (unlimited liability for Acme and broad data usage rights for CloudMetrics) and three yellow flags (60-day auto-renewal notice, one-sided indemnification scope, and aggressive audit rights). The remaining terms are standard and match the playbook. Recommend negotiating the red flags before signing.

---

## Contract Metadata

- **Parties:** Acme Corp (Customer), CloudMetrics Inc. (Vendor)
- **Type:** SaaS Software License Agreement
- **Term:** 12 months, auto-renewal
- **Value:** $48,000/year ($4,000/month, 50 seats)
- **Effective Date:** April 1, 2026

---

## Green Flags

| Clause | Section | Assessment |
|--------|---------|------------|
| Mutual NDA / Confidentiality | Section 7 | Standard mutual confidentiality with 2-year survival. Matches playbook. |
| Payment Terms | Section 4.2 | Net 30, monthly invoicing. Matches playbook preference. |
| Governing Law | Section 12.1 | Delaware. Matches playbook (Acme's incorporation state). |
| Force Majeure | Section 11 | Standard mutual clause. Matches playbook. |
| Termination for Cause | Section 9.1 | 30-day cure period, mutual. Matches playbook. |
| Dispute Resolution | Section 12.2 | Negotiation > mediation > litigation in Delaware. Matches playbook. |
| Assignment Restrictions | Section 12.5 | Mutual consent required. Matches playbook. |
| Customer Data Ownership | Section 5.1 | Customer retains all rights. Matches playbook. |
| Data Security | Section 5.2 | Reasonable safeguards. Standard, acceptable. |
| Exclusion of Consequential Damages | Section 10.3 | Mutual exclusion. Standard, acceptable. |

---

## Yellow Flags

| Clause | Section | Deviation | Suggested Edit |
|--------|---------|-----------|---------------|
| Auto-Renewal Notice Period | Section 3.2 | Requires 60-day notice to opt out. Playbook prefers 30 days. | "Either party may elect not to renew by providing thirty (30) days' written notice prior to the end of the then-current term." |
| Indemnification Scope | Section 8.1-8.2 | Imbalanced. Vendor indemnifies for IP claims only. Customer indemnifies for "any and all claims arising from use." Customer's scope is much broader. | "Each party shall indemnify the other against third-party claims arising from (a) its own breach of this Agreement, (b) its negligent or wrongful acts, or (c) its violation of applicable law." |
| Audit Rights | Section 6.3 | Vendor can audit "at any time" with only 5 business days' notice. Playbook: once per year, 30 days' notice. | "Vendor may audit Customer's compliance with usage terms no more than once per twelve (12) month period, upon thirty (30) days' prior written notice, during normal business hours." |

---

## Red Flags

| Clause | Section | Risk | Suggested Edit | Escalation |
|--------|---------|------|---------------|------------|
| Customer Liability - No Cap | Section 10.2 | Acme has UNLIMITED liability. Vendor's liability is capped at 12 months' fees. This is a significant imbalance — Acme's exposure is uncapped while Vendor's is limited. | "Neither party's aggregate liability under this Agreement shall exceed the total fees paid or payable by Customer during the twelve (12) month period immediately preceding the event giving rise to the claim." (Make the cap mutual.) | General Counsel — Immediate. Do not sign without a mutual cap. |
| Broad Data Usage Rights | Section 5.3 | Vendor may use Customer Data "in anonymized, aggregated form for any business purpose including product improvement and benchmarking." This gives Vendor broad rights to Acme's operational data, even if anonymized. Risk: competitive intelligence leakage, regulatory exposure if anonymization is inadequate. | "Vendor shall not use Customer Data for any purpose other than performing the Services under this Agreement. Any use of anonymized or aggregated Customer Data requires Customer's prior written consent and shall be subject to Vendor's privacy policy." | General Counsel + Privacy Officer — Before signing. |

---

## Missing Clauses

| Expected Clause | Why It Matters |
|----------------|---------------|
| Data Processing Agreement (DPA) | No DPA referenced or attached. If Acme's data includes personal information (employee data, customer data), a DPA is required for GDPR/CCPA compliance. Playbook requires DPA when personal data is involved. |
| SLA with Service Credits | No uptime commitment or service credits defined. For a $48K/year SaaS platform, playbook expects 99.9% uptime SLA with monthly service credits for downtime. |
| Termination for Convenience | Contract only allows termination for cause (Section 9.1). Playbook expects mutual termination for convenience with 30 days' notice. Without this, Acme is locked in for the full term even if the service is not meeting needs. |

---

## Escalation Matrix

| Flag | Expertise Needed | Priority |
|------|-----------------|----------|
| Unlimited liability for Acme (Section 10.2) | General Counsel | Immediate — do not sign without a mutual liability cap |
| Broad data usage rights (Section 5.3) | General Counsel + Privacy Officer | Before signing — assess sensitivity of data being uploaded |
| Missing DPA | Privacy Officer | Before signing if any personal data will be processed |
| Missing SLA | VP Operations / IT | Before signing — negotiate uptime commitment |

---

## Summary Recommendation

**Do not sign as-is.**

1. **Must fix (red flags):** Negotiate mutual liability cap and restrict data usage rights. These are non-negotiable per the playbook.

2. **Should fix (yellow flags):** Reduce auto-renewal notice to 30 days, balance indemnification scope, and limit audit frequency. These are standard negotiation points.

3. **Should add (missing clauses):** Request DPA, SLA with service credits, and termination for convenience clause.

4. **Acceptable as-is (green flags):** Payment terms, confidentiality, governing law, force majeure, termination for cause, dispute resolution, and data ownership are all standard.

With the red flag corrections and the addition of the three missing clauses, this becomes a signable agreement. The yellow flag negotiations are desirable but could be accepted if the vendor pushes back, provided the red flags are resolved.
