---
name: gmail-inbox-command
description: >-
  Gmail inbox management system using the Gmail MCP connector. Conducts forensic
  sent-email analysis to classify senders into 4 importance tiers, identifies noise
  (subscriptions, sales, cold outreach, notifications), and maintains organized label
  taxonomy. Operates in phases: setup, forensic audit, classification, triage, training.
  Uses a companion Inbox Profile document for persistent state across sessions. Never
  deletes without staging in Pre-Delete review label first. Teaches the user a 3-label
  feedback signal system (Keep/Kill/Pause) to refine classifications. Includes upgrade
  path to n8n or custom MCP for write automation. MANDATORY TRIGGERS: inbox management,
  email triage, email cleanup, Gmail organize, inbox zero, email audit, unsubscribe,
  email noise, email signal, email classification, VIP contacts, sent email analysis,
  email habits, inbox overwhelm, sender classification, email subscriptions, clean my
  email, sort my inbox, email priorities, gmail labels.
---

# Gmail Inbox Command — V2

AI-powered inbox management that learns who matters, identifies noise, and produces
actionable triage recommendations. Built on the principle: **analyze first, act
never — until trained and confirmed.**

## Table of Contents

1. [Architecture & Constraints](#architecture--constraints)
2. [Phase 1: Initial Setup](#phase-1-initial-setup)
3. [Phase 2: Forensic Sent-Mail Audit](#phase-2-forensic-sent-mail-audit)
4. [Phase 3: Full Inbox Classification](#phase-3-full-inbox-classification)
5. [Phase 4: Ongoing Triage Sessions](#phase-4-ongoing-triage-sessions)
6. [Phase 5: Training & Feedback Loop](#phase-5-training--feedback-loop)
7. [Sender Tier Model](#sender-tier-model)
8. [Email Category Taxonomy](#email-category-taxonomy)
9. [Classification Rules](#classification-rules)
10. [Label Architecture](#label-architecture)
11. [User Interaction Protocol](#user-interaction-protocol)
12. [Safety Guardrails](#safety-guardrails)
13. [Upgrade Path](#upgrade-path)
14. [Reference Files](#reference-files)

---

## Architecture & Constraints

```
┌─────────────────────────────────────────────────┐
│  SKILL (this file)                               │
│  Procedures: setup, audit, classify, triage,     │
│  train. Classification rules, tier model.        │
├─────────────────────────────────────────────────┤
│  PROJECT KNOWLEDGE (Inbox Profile doc)           │
│  Persistent state: VIPs, rules, label map,       │
│  noise domains, audit history, user overrides     │
├─────────────────────────────────────────────────┤
│  GMAIL MCP CONNECTOR                             │
│  Runtime: search, read, draft, list labels       │
├─────────────────────────────────────────────────┤
│  USER (manual execution layer)                   │
│  Creates labels, applies labels, deletes,        │
│  archives, provides feedback via signal labels    │
├─────────────────────────────────────────────────┤
│  UPGRADE PATH (optional)                         │
│  inbox_cleaner.py / n8n / custom MCP for writes  │
└─────────────────────────────────────────────────┘
```

### Gmail MCP Connector — Actual Capabilities

| Tool | Function | Use In This Skill |
|------|----------|-------------------|
| `Gmail:gmail_search_messages` | Search with Gmail query syntax, up to 500 results | Forensics, triage, noise detection, signal reads |
| `Gmail:gmail_read_message` | Read full message content and headers | Classification, sender analysis |
| `Gmail:gmail_read_thread` | Read full conversation threads | Relationship depth analysis |
| `Gmail:gmail_list_labels` | List all existing labels and IDs | Audit current organization |
| `Gmail:gmail_create_draft` | Create email drafts | Unsubscribe requests, draft replies |
| `Gmail:gmail_list_drafts` | List existing drafts | Check pending drafts |
| `Gmail:gmail_get_profile` | Get account info | Identify user's email address |

### What It Cannot Do (Critical)

The connector documentation references `gmail_modify_thread` but **this tool does
not exist in the current connector.** Confirmed by tool registry search. This means:

- **No** label application or removal
- **No** label creation
- **No** deletion, archiving, or mark-as-read
- **No** message modification of any kind

All write operations are manual (user executes in Gmail) or automated via the
upgrade path (inbox_cleaner.py script, n8n workflows, or custom MCP server).

---

## Phase 1: Initial Setup

**One-time. ~15 minutes of user action.**

### Step 1: Verify Gmail connector

Call `Gmail:gmail_get_profile` to confirm the connector is active. If it fails,
instruct the user: Settings → Connectors → Gmail → toggle ON for chat.

### Step 2: Guide label creation

Present this checklist. The user creates these labels manually in Gmail
(Settings → Labels → Create new label):

**Review labels (triage staging):**
```
📥-Review              ← Messages needing your decision
📥-Review/Delete       ← Pre-Delete holding pen (14-day minimum)
📥-Review/Unsub        ← Subscriptions to evaluate
📥-Review/Maybe        ← Uncertain — needs a second look
```

**Classification labels:**
```
🏷-VIP                 ← People who matter (override: never classified as noise)
🏷-Noise/Sales         ← Cold outreach, pitches, vendor spam
🏷-Noise/Marketing     ← Newsletters, promotions, drip campaigns
🏷-Noise/Notify        ← Automated notifications (GitHub, Jira, etc.)
🏷-Noise/Social        ← Social media notifications
🏷-Receipts            ← Purchase confirmations, invoices
```

**Feedback signal labels (the training system):**
```
✅-Keep                ← "I want this — stop flagging it as noise"
❌-Kill                ← "Delete this and everything like it"
⏸-Pause               ← "Not now but don't delete — revisit later"
```

**Naming rationale:** Emoji prefixes group labels visually in Gmail's sidebar.
Sublabels nest under parents. The 📥-Review/Delete label is the Pre-Delete
holding pen — nothing gets permanently deleted until the user confirms.

Check the user's existing labels via `Gmail:gmail_list_labels` and note any
that overlap with this structure. Suggest merging rather than duplicating.

### Step 3: Initialize Inbox Profile

The companion **Inbox Profile** document stores all persistent state. If the
Project doesn't yet have one, instruct the user to create a Google Doc from
the template in `references/inbox-profile-template.md` and add it as
Project Knowledge.

### Step 4: Confirm readiness

Verify with the user: all labels created, Inbox Profile exists. Record the
setup completion date.

---

## Phase 2: Forensic Sent-Mail Audit

**One-time. ~15-25 minutes. Heavy tool usage (60-120+ API calls).**

Read `references/sent-mail-forensics.md` for the complete methodology.

### Summary of the forensic process:

1. Get user's email via `gmail_get_profile`
2. Search sent mail in bands: 30-day deep scan, 6-month medium scan
3. Extract recipients, count per-recipient frequency, sample thread depth
4. Score contacts into 4 tiers (see Sender Tier Model below)
5. Cross-reference with inbound — anyone who emails you but you've never
   emailed back is Tier 4 (Unknown)
6. Identify organizational and partner domains
7. Present VIP candidate list for user confirmation
8. Record confirmed Sender Registry in the Inbox Profile document

### Output: Sender Registry + Audit Report

Produce the full audit report as a markdown artifact. Use the template in
`references/audit-report-template.md`. The report includes:

- Sender Registry (Tier 1-2 listed individually, 3-4 summarized)
- Email category breakdown with volume percentages
- Current label audit with recommendations
- Top 20 noise sources with unsubscribe recommendations
- Immediate action items with copy-pasteable Gmail search queries
- Signal System quick reference

Instruct the user to update the Inbox Profile with the confirmed VIP list
and domain classifications.

---

## Phase 3: Full Inbox Classification

**First comprehensive scan. After the audit.**

### Step 1: Search inbox

Use `gmail_search_messages` with `in:inbox` to retrieve messages. Work in
batches of 20-30. Start with the last 30 days.

### Step 2: Classify each message

Apply the Classification Rules (below) in priority order. Read full messages
with `gmail_read_message` when headers alone are insufficient.

### Step 3: Generate classification report

Three buckets:

**🔴 Act Now** — VIP messages, time-sensitive items needing response.
Include sender, subject, urgency reason.

**🟡 Your Call** — Ambiguous messages with evidence and confidence rating.
The user decides.

**🟢 Recommended Actions** — Grouped by action:
- Archive these (noise, notifications, receipts already reviewed)
- Apply Pre-Delete label to these (confirmed noise)
- Unsubscribe from these (high-volume noise you never opened)
- Include copy-pasteable Gmail search queries for batch operations

Example batch query:
```
from:(noreply@github.com) in:inbox
→ Select all → Apply label "🏷-Noise/Notify" → Archive
```

### Step 4: Guide user through actions

Walk the user through applying labels to each group. One group at a time.

### Step 5: First Pre-Delete review

After the user has labeled 📥-Review/Delete messages, review contents together.
Confirm each item. Establish the pattern: **nothing leaves Pre-Delete without
explicit human confirmation.**

---

## Phase 4: Ongoing Triage Sessions

**Recurring. 5-15 minutes. Weekly or as needed.**

### Triage protocol

1. **Read signal data first** (check for training feedback):
   ```
   label:✅-Keep          ← User marked as wrongly classified noise
   label:❌-Kill          ← User wants this sender killed
   label:⏸-Pause         ← User wants to defer, not delete
   is:starred newer_than:7d   ← Importance signals
   in:sent newer_than:7d      ← Who they're actively emailing
   in:trash newer_than:7d     ← What they deleted directly
   ```

2. **Process any feedback** before classifying new mail (see Phase 5).

3. **Search recent inbox:** `in:inbox newer_than:7d` (or 1d, 3d based on cadence).

4. **Quick-classify:** Apply Classification Rules. For recognized patterns, classify
   immediately. For ambiguous, flag as 📥-Review/Maybe.

5. **Produce triage report** (three buckets — same format as Phase 3):
   - 🔴 Act Now
   - 🟡 Your Call
   - 🟢 Recommended Actions (with search queries for batch operations)

6. **Pre-Delete review reminder:** Check `label:📥-Review/Delete older_than:14d`.
   If items exist, remind user to review and bulk-delete.

7. **Draft replies if requested:** Use `gmail_create_draft` for messages needing
   response.

8. **Update Inbox Profile:** Note new senders, pattern changes, rule refinements.

### Triage cadence recommendations

| Inbox volume | Recommended frequency | Session target |
|-------------|----------------------|----------------|
| <50/day | 2-3x per week | 5 min |
| 50-150/day | Daily | 10 min |
| 150+/day | Twice daily | 15 min |

### Progressive disclosure

- **Sessions 1-5:** Walk through everything. Explain labels. Show examples.
  Full reasoning for every classification.
- **Sessions 6+:** Expert mode. Terse output. Just the three buckets. Only
  flag exceptions and new patterns.

---

## Phase 5: Training & Feedback Loop

### The 3-label feedback system

The user teaches the AI by applying these labels to messages between sessions:

| Label | Meaning | Skill Response |
|-------|---------|----------------|
| **✅-Keep** | "I want this — stop flagging as noise" | Add sender/domain to allowlist in Inbox Profile |
| **❌-Kill** | "Delete this and everything like it" | Add to blocklist, search for similar, stage all in Pre-Delete |
| **⏸-Pause** | "Not now but don't delete" | Skip in future triage, revisit monthly |

### Training protocol

1. **Check feedback labels** at the start of every triage session
2. **Process corrections:** Extract the pattern (sender, domain, subject keywords)
   and update classification rules in the Inbox Profile
3. **Track accuracy:** Record corrections / total classified per session
4. **Suggest refinements:** "Based on your last 3 corrections, I'd suggest adding
   [domain] to the noise blocklist. Agree?"

### Implicit signals (read automatically)

| User Action in Gmail | What It Tells the AI |
|---------------------|---------------------|
| Star a message | Sender matters more than expected |
| Reply to someone | Active relationship — at least Tier 2 |
| Apply 🏷-VIP label | Always Tier 1, absolute override |
| Trash directly | Obvious noise — higher confidence |
| Archive without reading | Low priority |

### Teaching the user

When onboarding, explain the system in plain language:

> **Your job is simple: when I get it wrong, slap a label on it.**
>
> See something I flagged as noise but you actually want? → Apply ✅-Keep
> See something in your inbox that should have been caught? → Apply ❌-Kill
> Something you want to deal with later but not lose? → Apply ⏸-Pause
>
> Next time we triage, I'll learn from your corrections.

---

## Sender Tier Model

Every sender is classified into one of four tiers based on sent-mail forensics:

| Tier | Name | Signal | Examples |
|------|------|--------|----------|
| **1** | Inner Circle | 5+ sent messages/month, multi-reply threads, personal tone | Active clients, close collaborators, family |
| **2** | Active Network | 1-4 sent/month, occasional threads, professional tone | Vendors you work with, professional contacts |
| **3** | Peripheral | 1-4 sent/year, single-reply threads, transactional | Old colleagues, one-time contacts |
| **4** | Unknown | Zero sent mail to this sender ever, inbound-only | Marketing, cold outreach, subscriptions, notifications |

See `references/sent-mail-forensics.md` for the complete tier assignment methodology.

---

## Email Category Taxonomy

| Category | Detection Signals | Default Action |
|----------|-------------------|----------------|
| **Personal/Client** | Tier 1-2, conversational tone, no unsubscribe | Keep in Inbox |
| **Transactional** | Order confirmations, receipts, invoices | Label: 🏷-Receipts, archive |
| **Newsletter-Valuable** | Has unsubscribe link, but user has opened/replied/starred or ✅-Keep | Keep |
| **Newsletter-Noise** | Has unsubscribe link, never opened, high frequency | 📥-Review/Delete + Unsubscribe |
| **Notification** | Automated system emails, noreply senders | Label: 🏷-Noise/Notify, archive |
| **Marketing/Sales** | Cold outreach, promotional, sales cadence | 📥-Review/Delete |
| **Social** | Social platform notifications | Label: 🏷-Noise/Social, archive |
| **Subscription-Service** | SaaS notifications from tools you pay for | Label per vendor, archive |
| **Spam-Adjacent** | Not in spam folder but clearly unsolicited | 📥-Review/Delete |
| **Unknown** | Cannot confidently classify | 📥-Review/Maybe |

---

## Classification Rules

Apply in priority order. First match wins.

### Priority 1: VIP Override
Sender on VIP list (any tier in Inbox Profile) → **Always surface.** Never
classify as noise. VIP status is an absolute override.

### Priority 2: User Overrides
Sender/domain on allowlist (from ✅-Keep) → Keep.
Sender/domain on blocklist (from ❌-Kill) → Pre-Delete.

### Priority 3: Pattern Matching
Apply detection patterns from `references/noise-detection-patterns.md` and
domain checks from `references/noise-domain-registry.md`.

**Sales/Cold Outreach:** Tier 4 sender + subject contains "quick question",
"following up", "partnership" + calendar booking links + from known sales
platform domains.

**Subscription/Marketing:** Has List-Unsubscribe header + from noreply/newsletter/
marketing sender patterns + body contains "unsubscribe" + consistent cadence.

**Notifications:** From known notification domains + subject patterns like
"[Repo] Pull request", "New comment on" + typically no reply expected.

**Social:** From facebook/twitter/linkedin/instagram notification addresses.

**Receipts:** From known e-commerce/payment domains + order/receipt/invoice
keywords.

### Priority 4: Ambiguous
No pattern match, unknown sender → 📥-Review/Maybe. Flag for user decision.
Include evidence and confidence rating.

### Priority 5: Default
Known sender, non-VIP, non-noise → Leave in inbox, no label.

---

## Label Architecture

### Complete label map

```
📥-Review                    ← Messages needing user decision
├── 📥-Review/Delete         ← Pre-Delete holding pen (14-day minimum)
├── 📥-Review/Unsub          ← Subscriptions to evaluate
└── 📥-Review/Maybe          ← Uncertain, needs second look

🏷-VIP                       ← Tier 1 override: always important
🏷-Noise/Sales               ← Cold outreach, pitches
🏷-Noise/Marketing           ← Newsletters, promotions
🏷-Noise/Notify              ← Automated notifications
🏷-Noise/Social              ← Social media notifications
🏷-Receipts                  ← Transactions, invoices

✅-Keep                      ← Feedback: stop flagging as noise
❌-Kill                      ← Feedback: delete and learn
⏸-Pause                     ← Feedback: defer, don't delete
```

### Pre-Delete Protocol

1. Skill recommends messages for 📥-Review/Delete
2. User applies the label in Gmail
3. Messages sit for **minimum 14 days**
4. Each triage session reminds user to review items older than 14 days
5. User bulk-selects and deletes confirmed items
6. Any mis-classified items get ✅-Keep label → removed from Pre-Delete

---

## User Interaction Protocol

### Session invocations

| User Says | Skill Does |
|-----------|-----------|
| "Set up inbox management" | Phase 1 — guided setup |
| "Audit my sent mail" / "Who do I email?" | Phase 2 — forensic analysis |
| "Full inbox scan" / "Classify my inbox" | Phase 3 — comprehensive classification |
| "Triage my inbox" | Phase 4 — quick recent-mail triage |
| "Train on my feedback" | Phase 5 — process feedback labels |
| "Show my VIP list" | Display current tiers from Inbox Profile |
| "Inbox status" | Summary: count, unread, noise estimate, days since last triage |
| "Pre-Delete review" | List 📥-Review/Delete contents for confirmation |
| "Unsubscribe review" | List 📥-Review/Unsub with recommendations |
| "Investigate [sender]" | Deep dive on one sender: all sent/received, tier, category |
| "Noise sweep" | Bulk noise identification across entire inbox |

---

## Safety Guardrails

1. **Never instruct deletion directly.** Always stage in 📥-Review/Delete first.
2. **VIP is absolute.** Never auto-classify VIP contacts as noise, even if they
   trigger noise patterns. Flag as anomaly for user review instead.
3. **Preserve ambiguity.** Low confidence → 📥-Review/Maybe, not a guess.
   False negatives (missing important mail) are worse than false positives.
4. **Every classification includes reasoning.** The user always knows WHY.
5. **14-day Pre-Delete retention.** Minimum hold before permanent deletion.
6. **Audit trail.** Every session records: date, messages scanned, classifications,
   corrections. Stored in Inbox Profile.
7. **Graceful degradation.** If Gmail connector fails mid-session, save progress
   and provide a manual pickup point.
8. **First 3 sessions are recommendation-only.** Even with write tools available
   via upgrade path, no automated actions until trust is established.

---

## Upgrade Path

The skill works today with read-only tools. Write capabilities can be added
progressively.

### Level 1: Current (Read + Recommend)
Fully functional. User manually applies labels, archives, deletes per reports.

### Level 2: Python Script (inbox_cleaner.py)
If the user has an existing Python script with Gmail OAuth2 and `gmail.modify`
scope, the skill can produce classification JSON that the script executes.
See `references/upgrade-path.md` for script integration specs.

### Level 3: n8n Automation Bridge
Build n8n workflows exposing Gmail API write operations as endpoints.
See `references/upgrade-path.md` for workflow specifications.

### Level 4: Custom Gmail MCP Server
Full read/write MCP server for Claude Desktop/Code.

### Level 5: Official Gmail MCP Write Tools
When Anthropic ships `gmail_modify_thread` and related tools.

---

## Reference Files

| File | Purpose | When to Load |
|------|---------|-------------|
| `references/sent-mail-forensics.md` | Complete forensic analysis workflow | Phase 2 (Audit), Sender Investigation |
| `references/noise-detection-patterns.md` | Header analysis, content patterns, confidence levels | Every triage and classification |
| `references/noise-domain-registry.md` | Seed list of ~150 known noise domains by category | Every triage (quick reference) |
| `references/inbox-profile-template.md` | Starter template for Inbox Profile doc | Phase 1 (Setup) |
| `references/audit-report-template.md` | Structured output template for audit report | Phase 2 (Audit) |
| `references/gmail-search-queries.md` | Pre-built query library for all session types | Every session |
| `references/upgrade-path.md` | Script integration, n8n workflows, custom MCP specs | When adding write automation |

---

*Gmail Inbox Command v2.0 — March 2026*
*Requires: Gmail MCP Connector (Anthropic built-in)*
*Persistence: Inbox Profile document as Project Knowledge*
*Optional: inbox_cleaner.py, n8n, or custom MCP for write operations*
*Conformant to agentskills.io open standard (December 2025)*
