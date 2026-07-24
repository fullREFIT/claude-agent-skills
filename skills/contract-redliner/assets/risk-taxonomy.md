# Risk Taxonomy

Definitions and examples for the three risk levels used in contract review.

---

## Green — Acceptable

**Definition:** The contract term matches your playbook's standard. No action needed. These confirmations are included in the report so you can verify that important protections are present.

**When a term is Green:**
- The language matches or is substantially similar to your playbook's standard
- The term is mutual (applies equally to both parties)
- The term falls within your acceptable range for negotiable items
- The term is a standard industry practice that your playbook accepts

**Examples:**
| Term | Why It Is Green |
|------|----------------|
| Mutual NDA, 2-year term | Standard mutual confidentiality |
| Net 30 payment terms | Matches playbook preference |
| 30-day termination notice, mutual | Both parties have equal rights |
| Delaware governing law | Acceptable jurisdiction per playbook |
| Standard force majeure | Mutual, standard scope |
| Mutual indemnification for breach | Balanced, reasonable scope |

---

## Yellow — Deviates, Worth Discussing

**Definition:** The term differs from your playbook but is not a deal-breaker. It represents a negotiation opportunity. The risk report includes specific language to propose.

**When a term is Yellow:**
- The term is within the "negotiable" range of your playbook
- The deviation creates a minor imbalance but limited exposure
- The term could be improved but is not unreasonable
- Standard negotiation would likely resolve it
- The risk is manageable even if the term stays as written

**Examples:**
| Term | Deviation | Risk Level |
|------|-----------|------------|
| Net 60 payment (playbook: Net 30) | Cash flow impact, but manageable | Low financial risk |
| 60-day auto-renewal notice (playbook: 30) | Less flexibility, but workable | Low operational risk |
| Liability cap at 2x contract value (playbook: 1x) | Higher exposure, but bounded | Medium financial risk |
| One-sided audit rights with 5-day notice | Inconvenient, not dangerous | Low operational risk |
| Non-compete: 18 months (playbook: 12) | Broader restriction | Medium business risk |
| SLA: 99.5% uptime (playbook: 99.9%) | Lower reliability commitment | Medium operational risk |

**How to handle Yellow flags:**
1. Read the suggested edit in the risk report
2. Decide if negotiation is worth the effort (consider contract value and relationship)
3. If negotiating: propose the suggested edit language
4. If accepting: document the deviation and the reasoning

---

## Red — Real Risk, Escalate

**Definition:** The term creates genuine legal, financial, or operational exposure. Escalate to legal counsel before signing. These are not negotiation points for non-lawyers — they require qualified legal review.

**When a term is Red:**
- The term is on your playbook's "hard stop" list
- The term creates unlimited or disproportionate liability
- The term transfers IP rights you did not intend to give up
- The term gives the other party unilateral power you cannot match
- The term involves regulatory compliance (GDPR, CCPA, HIPAA)
- The term is unusual or absent from standard contracts (could indicate bad faith)
- The financial exposure is significant relative to the contract value

**Examples:**
| Term | Risk | Exposure |
|------|------|----------|
| No liability cap for your company | Unlimited financial exposure | Could exceed contract value many times over |
| Vendor owns all custom deliverables | Loss of IP you paid to create | Permanent, irreversible |
| Unilateral termination by vendor only | Vendor can exit, you cannot | Operational dependence without protection |
| Vendor can use your data for "any purpose" | Privacy, competitive, and regulatory risk | Unquantifiable |
| Mandatory arbitration in foreign jurisdiction | Cannot litigate locally | Costly, inconvenient, potentially unfair |
| Automatic 20% price escalation annually | Uncapped cost increase | Compounds to 2.5x in 5 years |
| Non-mutual indemnification, unlimited scope | You bear all third-party claim risk | Potentially catastrophic |

**How to handle Red flags:**
1. Stop the review and flag immediately
2. Forward the risk report to legal counsel with the red flags highlighted
3. Do not negotiate red flags yourself unless you have legal training
4. Do not sign until red flags are resolved
5. If the other party refuses to modify red flag terms, consider walking away

---

## Classification Decision Tree

```
Is the term on your playbook's "hard stop" list?
  YES → RED
  NO → Continue

Does the term create unlimited or disproportionate liability?
  YES → RED
  NO → Continue

Does the term involve IP rights, data ownership, or regulatory compliance?
  YES → Is the term standard and mutual?
    YES → GREEN
    NO → RED (escalate to legal)

Does the term match your playbook's standard?
  YES → GREEN
  NO → Continue

Is the deviation within your playbook's "negotiable" range?
  YES → YELLOW
  NO → RED
```
