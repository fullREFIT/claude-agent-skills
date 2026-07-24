# Gmail Inbox Command V2 — Setup & Usage Guide

---

## Part 1: What You Need

### Required
- **Claude Pro/Max account** with a Claude Project
- **Gmail MCP connector** enabled (Settings → Connectors → Gmail → ON)
- **15 minutes** to create labels in Gmail

### Optional (for write automation later)
- `inbox_cleaner.py` script with Gmail OAuth2 credentials
- n8n instance with Gmail OAuth2 configured

---

## Part 2: Installation (10 minutes)

### Step 1: Create a New Claude Project

Go to claude.ai → Projects → Create Project. Name it "Gmail Inbox Command"
or whatever you prefer.

### Step 2: Upload the Skill Files

Upload all 8 files from the zip as **Project Knowledge**:

```
SKILL.md                                ← Main skill (the brain)
references/sent-mail-forensics.md       ← Sent mail analysis methodology
references/noise-detection-patterns.md  ← Header/content classification signals
references/noise-domain-registry.md     ← ~150 known noise domains
references/inbox-profile-template.md    ← Persistent state template
references/audit-report-template.md     ← Audit output template
references/gmail-search-queries.md      ← Pre-built query library
references/upgrade-path.md             ← Script/n8n/MCP write automation specs
```

Claude.ai flattens the folder structure — that's fine. The filenames are
distinct enough that Claude will find the right reference when needed.

### Step 3: Create the Inbox Profile Document

1. Open Google Docs → Create new document
2. Copy the entire contents of `inbox-profile-template.md` into it
3. Name it "Inbox Profile"
4. Add this Google Doc as Project Knowledge in the same project

This document is your persistent memory. Claude reads it every session
and you update it with results after each triage.

### Step 4: Verify Gmail Connector

Open a conversation in the project and say:

```
Check if my Gmail connector is working — get my profile.
```

If it returns your email address, you're set. If it fails: Settings →
Connectors → Gmail → toggle ON.

---

## Part 3: The Execution Sequence

### Session 1: Setup + Audit (30-40 minutes)

**Paste this prompt:**

```
Run Gmail Inbox Command Phase 1 (Setup) and Phase 2 (Audit).

SETUP:
1. Get my Gmail profile
2. List my current labels
3. Tell me which labels from the skill's architecture I need to create,
   accounting for labels I already have

AUDIT (after I confirm labels are created):
4. Run Sent Mail Forensics — search my sent mail from the last 6 months.
   Build a sender tier classification:
   - Tier 1 (Inner Circle): 5+ sent/month or deep thread engagement
   - Tier 2 (Active Network): 1-4 sent/month, active contacts
   - Tier 3 (Peripheral): 1-4 sent/year
   - Tier 4 (Unknown): Never emailed, inbound-only

5. Scan my inbox from the last 30 days. Categorize every sender using
   the 10-category taxonomy.

6. Produce the full Audit Report as a markdown artifact with:
   - Sender Registry (Tier 1-2 individually, 3-4 summarized)
   - Category breakdown with volume percentages
   - Top 20 noise sources
   - Copy-pasteable Gmail search queries for batch labeling
   - Unsubscribe recommendations
   - Immediate action items

Refer to sent-mail-forensics, noise-detection-patterns, noise-domain-registry,
audit-report-template, and gmail-search-queries references.
```

**What happens:**
- Claude guides you through label creation first
- Then runs 60-120+ Gmail API calls analyzing your sent mail and inbox
- Produces an audit report with your personalized Sender Registry
- Gives you batch Gmail search queries to label and Pre-Delete noise

**After the session:**
1. Create any remaining labels in Gmail
2. Copy the Sender Registry into your Inbox Profile Google Doc
3. Execute the batch actions from the report (apply labels, Pre-Delete noise)
4. Unsubscribe from the top offenders
5. Star any messages the audit misclassified

### Session 2: First Triage (7 days later, 10-15 minutes)

**Paste this prompt:**

```
Triage my inbox.

1. Check for signal data:
   - Search for ✅-Keep, ❌-Kill, ⏸-Pause feedback labels
   - Check starred messages from last 7 days
   - Check my sent mail from last 7 days

2. Process any feedback corrections before classifying new mail

3. Search inbox for messages from the last 7 days

4. Classify each sender against the Sender Registry in my Inbox Profile

5. Produce a triage report with three buckets:
   🔴 Act Now — VIP/time-sensitive messages needing response
   🟡 Your Call — Ambiguous, with evidence and confidence rating
   🟢 Recommended Actions — grouped by action with Gmail search queries

6. Check Pre-Delete for items older than 14 days

7. Flag any new senders not in the registry
```

### Session 3+: Ongoing Triage

After the first two sessions, you can use shorter prompts:

```
Triage my inbox
```

or

```
Triage my inbox — last 3 days, expert mode
```

Claude will read the SKILL.md and know what to do.

### Other Session Types

| What You Want | What to Say |
|--------------|------------|
| Deep dive on a sender | "Investigate sender@domain.com" |
| Find all noise in inbox | "Run a noise sweep" |
| Process your feedback labels | "Train on my feedback" |
| See your VIP list | "Show my VIP list" |
| Review Pre-Delete | "Pre-Delete review — show items older than 14 days" |
| Review subscriptions | "Unsubscribe review" |
| Get inbox stats | "Inbox status" |

---

## Part 4: The Feedback System (How to Train the AI)

This is the most important habit. Between sessions, when you see emails
in Gmail that were classified wrong, apply one of these labels:

| Label | When to Use | What Happens Next Session |
|-------|------------|--------------------------|
| **✅-Keep** | AI flagged as noise, but you want it | Sender added to allowlist |
| **❌-Kill** | Noise that wasn't caught | Sender added to blocklist, similar found and staged |
| **⏸-Pause** | Not ready to deal with, but don't delete | Skipped in future triage, revisited monthly |

**You don't need to be perfect.** Even 2-3 corrections per week make the
system significantly more accurate over time.

---

## Part 5: When to Add the Python Script

### Don't touch the script until:
1. You've completed the audit (Session 1)
2. You've run at least 2 triage sessions (Sessions 2-3)
3. You trust the classification model

### When you're ready (Session 4+):

Open a conversation in this project or a Claude Code session and say:

```
I've completed 3+ sessions with Gmail Inbox Command and trust the
classifications. Here's my audit report and Inbox Profile:
[paste or upload both]

And here's my inbox_cleaner.py:
[upload the script]

Upgrade the script to:
1. Replace binary classification with the 4-tier sender model
2. Add the 10-category taxonomy
3. Add --apply-labels (uses batchModify to apply Gmail labels)
4. Add --pre-delete (applies 📥-Review/Delete label)
5. Add --create-labels (creates the full label architecture)
6. Add sender_registry.json for persistent tier/category storage
7. Keep existing --fetch, --classify, --review, --mark-read working
```

---

## Part 6: Updating the Inbox Profile

After every session, Claude will tell you what to update in the Inbox Profile.
The updates are usually:

- New senders added to Tier 1-2 lists
- Domains added to allowlist or blocklist
- Classification rules refined
- Session log entry with accuracy stats

**Open your Google Doc, paste the updates, save.** Claude reads it next session.

This is friction, and it matters. The Inbox Profile is the AI's memory.
If you skip updating it, the next session starts from stale data.

---

## Part 7: File Reference

| File | What It Does |
|------|-------------|
| **SKILL.md** | Master skill: phases, rules, tiers, taxonomy, safety |
| **sent-mail-forensics.md** | How to analyze outbound email for sender importance |
| **noise-detection-patterns.md** | Header signatures, content signals, confidence levels |
| **noise-domain-registry.md** | ~150 known noise domains organized by category |
| **inbox-profile-template.md** | Template for the persistent Inbox Profile Google Doc |
| **audit-report-template.md** | Output template for the initial audit |
| **gmail-search-queries.md** | Pre-built Gmail query library for all sessions |
| **upgrade-path.md** | Script integration, n8n workflows, custom MCP specs |

---

## Quick Start (If You Just Want to Get Going)

1. Create a Claude Project
2. Upload all 8 files as Project Knowledge
3. Create Inbox Profile Google Doc from template, add as Project Knowledge
4. Open a conversation and paste the Session 1 prompt from Part 3
5. Follow Claude's instructions

That's it. Everything else is in the skill.
