# Initial Audit Report Template

Deliver as a markdown artifact after completing the Phase 2 audit.

---

```markdown
# Gmail Inbox Audit Report

**Account:** [user@domain.com]
**Date:** [YYYY-MM-DD]
**Period Analyzed:** [N] months sent mail, [N] days inbox
**Messages Analyzed:** [N] sent, [N] inbox

---

## Executive Summary

Your inbox receives ~[N] messages per week. Of those:
- **[N]% require your attention** (Tier 1-2 senders, actionable content)
- **[N]% are informational** (receipts, confirmations, valuable newsletters)
- **[N]% are noise** (marketing, cold outreach, dead subscriptions)

**Estimated time recoverable:** [N] minutes/week by eliminating noise.

---

## Sender Registry

### Tier 1 — Inner Circle ([N] senders)
| Sender | Domain | Sent (6mo) | Last Contact | Relationship |
|--------|--------|------------|-------------|-------------|
| [name] | [domain] | [N] | [date] | [Client/Partner/etc.] |

### Tier 2 — Active Network ([N] senders)
| Sender | Domain | Sent (6mo) | Last Contact | Relationship |
|--------|--------|------------|-------------|-------------|
| [name] | [domain] | [N] | [date] | [Vendor/Colleague/etc.] |

### Tier 3 — Peripheral
[N] senders, 1-4 messages in last 12 months. Notable: [any worth mentioning]

### Tier 4 — Top Noise Sources
| Sender | Domain | Inbound (30d) | Category | Recommendation |
|--------|--------|--------------|----------|---------------|
| [sender] | [domain] | [N] msgs | Marketing | Unsubscribe + Pre-Delete |

---

## Email Category Breakdown

| Category | Volume (30d) | % of Inbox | Recommended Action |
|----------|-------------|------------|-------------------|
| Personal/Client | [N] | [N]% | Keep |
| Transactional | [N] | [N]% | Label: 🏷-Receipts, archive |
| Valuable Newsletters | [N] | [N]% | Keep |
| Noise Newsletters | [N] | [N]% | Unsubscribe + Pre-Delete |
| Notifications | [N] | [N]% | Label: 🏷-Noise/Notify, archive |
| Marketing/Sales | [N] | [N]% | Pre-Delete |
| Cold Outreach | [N] | [N]% | Pre-Delete |
| Unknown | [N] | [N]% | 📥-Review/Maybe |

---

## Current Label Audit

| Existing Label | Recommendation |
|---------------|---------------|
| [label name] | [Keep / Rename / Merge / Remove] |

### New Labels to Create
[List any from the label architecture not yet created]

---

## 🟢 Immediate Actions

### 1. Batch Pre-Delete — Noise Marketing
Search query (paste into Gmail):
```
from:([sender1] OR [sender2] OR [sender3]) in:inbox
```
→ Select all → Apply label "📥-Review/Delete"

### 2. Batch Pre-Delete — Cold Outreach
```
from:([sender1] OR [sender2]) in:inbox
```
→ Select all → Apply label "🏷-Noise/Sales" → Apply "📥-Review/Delete"

### 3. Unsubscribe from Top [N] Noise Sources
| Sender | Email | Frequency | How to Unsubscribe |
|--------|-------|-----------|--------------------|
| [name] | [email] | Daily | [link or instructions] |

### 4. Label Your Active Notifications
```
from:(noreply@github.com OR notifications@[service].com) in:inbox
```
→ Select all → Apply label "🏷-Noise/Notify" → Archive

### 5. Turn Off Email Notifications for Services You Check Directly
[List services like Slack, GitHub, etc. where email notifications duplicate
what you already see in-app]

---

## Signal System Quick Reference

| Action in Gmail | What It Teaches the AI |
|----------------|----------------------|
| Apply ✅-Keep | "Stop flagging this as noise" |
| Apply ❌-Kill | "Delete this and everything like it" |
| Apply ⏸-Pause | "Defer, don't delete" |
| Star a message | "This sender matters more" |
| Reply to someone | "Active relationship" |
| Apply 🏷-VIP | "Always Tier 1" |

---

## Next Session

Schedule your first **Weekly Triage** in 7 days. By then:
- Labels will be created
- Pre-Delete will have initial noise staged
- Signal System will have 7 days of data
- Classifications will be more refined

**Say:** "Triage my inbox"
```

---

## Notes for the Agent

- Replace all `[placeholders]` with actual data
- Sort Tier 4 noise by descending volume
- Merge overlapping existing labels with new recommendations
- Keep report under 3,000 words — summarize Tier 3+ rather than listing
- If sent-mail volume is low, note reduced confidence in tier assignments
- Always end with the specific next action and timeframe
- Include copy-pasteable Gmail search queries for every batch action
