# Sent Mail Forensics — Sender Tier Classification Workflow

The most reliable signal for who matters is **who you email**. Inbound volume
is noise — outbound volume is intent. This workflow analyzes sent mail to build
a Sender Registry with tier classifications.

---

## Phase 1: Identify the User's Email Address

Call `Gmail:gmail_get_profile` to get the authenticated user's email address.
Store this for distinguishing sent-from vs. sent-to in search results.

---

## Phase 2: High-Volume Recipient Discovery

### Query Sequence

```
# Last 30 days — deep scan (read every message)
in:sent newer_than:30d

# Last 6 months — medium scan (sample every 3rd message)
in:sent newer_than:180d

# Last 12 months — light scan (unique recipients only)
in:sent newer_than:365d
```

Use `maxResults: 500` and paginate with `pageToken` if needed.

### Extraction Process

For each returned message:
1. Read via `Gmail:gmail_read_message`
2. Extract `To`, `CC`, `BCC` headers
3. Parse email addresses
4. Record: recipient address, date sent, subject, thread ID

### Aggregation

Build a recipient frequency table:

| Recipient | Msgs (12mo) | Msgs (6mo) | Msgs (30d) | Last Contact | Avg Thread Depth |
|-----------|-------------|------------|------------|-------------|-----------------|

**Thread depth** = total messages in threads where you replied.
Sample 5-10 representative threads per recipient via `Gmail:gmail_read_thread`.

---

## Phase 3: Tier Assignment

### Tier 1 — Inner Circle

**Criteria (meet ANY):**
- 5+ sent messages in last 30 days
- 15+ sent messages in last 6 months
- Average thread depth > 3
- User applied 🏷-VIP label

### Tier 2 — Active Network

**Criteria (meet ANY):**
- 1-4 sent messages in last 30 days
- 5-14 sent messages in last 6 months
- At least 1 sent message in last 90 days
- Average thread depth 1.5-3

### Tier 3 — Peripheral

**Criteria (meet ANY):**
- 1-4 sent messages in last 12 months
- No sent messages in last 90 days
- Average thread depth < 1.5
- Single-reply threads only

### Tier 4 — Unknown / Never Contacted

**Criteria:**
- Zero sent messages to this sender, ever
- Inbound-only relationship

---

## Phase 4: Cross-Reference with Inbound

After building the outbound table, cross-reference with inbound:

```
in:inbox newer_than:30d
```

For each inbound sender:
1. If in recipient table → tier already assigned
2. If not → Tier 4 (inbound-only)

### Upgrading Tier 4 Senders

Flag as "Tier 4 — Review" (not auto-noise) if:
- From a domain you've emailed other people at (colleague of a contact)
- Clearly transactional for a service you use
- Reply to something you initiated elsewhere (support tickets)

---

## Phase 5: Build the Sender Registry

Output as structured data for the Inbox Profile:

```markdown
### Tier 1 — Inner Circle ([N] senders)
| Sender | Domain | Sent (6mo) | Last Contact | Thread Depth | Relationship |
|--------|--------|------------|-------------|-------------|-------------|

### Tier 2 — Active Network ([N] senders)
| Sender | Domain | Sent (6mo) | Last Contact | Thread Depth | Relationship |
|--------|--------|------------|-------------|-------------|-------------|

### Tier 3 — Peripheral
[N] senders with 1-4 messages in last 12 months. Notable: [any worth mentioning]

### Tier 4 — Unknown
Top 20 Tier 4 senders by inbound volume:
| Sender | Domain | Inbound (30d) | Has Unsubscribe | Category |
|--------|--------|--------------|-----------------|----------|
```

Present Tier 1 and 2 candidates to the user for confirmation before recording.

---

## Phase 6: Domain-Level Patterns

After individual analysis, consolidate by domain:

```
from:@example.com
```

**Rules:**
- 3+ people from same domain at Tier 1-2 → domain itself is Tier 2
- Domain only sends automated messages → classify the domain as a whole
- Marketing infrastructure domains → Tier 4 by default (see noise-domain-registry.md)

---

## Sampling Strategy

| Timeframe | Strategy | Estimated Calls |
|-----------|----------|-----------------|
| 30-day | Read every sent message (up to 500) | 20-50 |
| 6-month | Sample every 3rd message | 15-30 |
| 12-month | Search for unique recipients only | 5-10 |
| Thread depth | Sample 5 threads per recipient max | 20-40 |

**Total: 60-120 calls** depending on inbox size.

If 10,000+ sent messages in 12 months, notify user that the audit will be
thorough but time-intensive. Offer to limit scope to 6 months.
