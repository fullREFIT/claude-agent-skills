# Gmail Search Query Library

Pre-built queries for all session types. Use with `Gmail:gmail_search_messages`
and include in triage reports as copy-pasteable strings for the user.

---

## Session Start — Signal System Checks

Run these at the start of every triage/training session:

```
label:✅-Keep                    # User marked: stop flagging as noise
label:❌-Kill                    # User marked: delete and learn
label:⏸-Pause                   # User marked: defer, don't delete
is:starred newer_than:7d         # Recently starred (importance signal)
in:sent newer_than:7d            # Who they've been emailing
in:trash newer_than:7d           # What they deleted directly
```

---

## Sent Mail Analysis

```
in:sent newer_than:30d           # Last 30 days (deep scan)
in:sent newer_than:180d          # Last 6 months (medium scan)
in:sent newer_than:365d          # Last 12 months (light scan)
in:sent to:[email]               # Sent to specific person
in:sent to:@[domain.com]         # Sent to domain
```

---

## Inbox Triage

```
in:inbox newer_than:1d           # Last 24 hours
in:inbox newer_than:3d           # Last 3 days
in:inbox newer_than:7d           # Last week
in:inbox is:unread               # All unread
in:inbox is:unread newer_than:3d # Recent unread
category:primary newer_than:7d   # Primary tab only
category:promotions newer_than:7d # Marketing noise
category:updates newer_than:7d   # Notifications
```

---

## Noise Detection

```
# Subscription/newsletter indicators
in:inbox unsubscribe                              # Has unsubscribe link
in:inbox from:noreply                             # From noreply addresses
in:inbox from:newsletter                          # From newsletter addresses
in:inbox from:marketing                           # From marketing addresses
in:inbox from:info@                               # From info@ addresses
in:inbox from:hello@                              # From hello@ addresses

# Broad noise sweep
in:inbox (unsubscribe OR "opt out" OR "email preferences") -from:@[your-domain]

# Sales/cold outreach
in:inbox "quick question" -from:@[your-domain]
in:inbox "following up" -from:@[your-domain] -is:sent
in:inbox calendly.com
in:inbox hubspot
in:inbox "book a time"
in:inbox "schedule a call"

# Notification sources
in:inbox from:notifications@github.com
in:inbox from:noreply@github.com
in:inbox from:no-reply@
in:inbox "has been updated"
in:inbox "new comment"
in:inbox "mentioned you"

# Social media
in:inbox from:facebookmail.com
in:inbox from:linkedin.com
in:inbox from:twitter.com OR from:x.com

# Receipts
in:inbox "order confirmation"
in:inbox "your receipt"
in:inbox "payment received"
in:inbox "invoice"
```

---

## Sender Investigation

```
from:[sender@domain.com]                    # All mail from sender
from:@[domain.com]                          # All from domain
in:sent to:[sender@domain.com]              # Your replies to them
{from:[sender] to:[sender]}                 # All threads with sender
from:[sender@domain.com] newer_than:30d     # Volume check (30d)
```

---

## Batch Operations (for triage reports)

```
# Find all from a specific domain
from:@[domain.com] in:inbox

# Multi-sender batch (for applying one label to several)
from:([sender1] OR [sender2] OR [sender3]) in:inbox

# Old inbox messages (archive candidates)
in:inbox older_than:30d
in:inbox older_than:90d

# Large messages (storage cleanup)
in:inbox larger:10M
in:inbox has:attachment older_than:1y larger:5M
```

---

## Pre-Delete Management

```
label:📥-Review/Delete                      # All staged for deletion
label:📥-Review/Delete older_than:14d       # Ready for permanent delete
label:📥-Review/Delete newer_than:14d       # Still in review period
label:📥-Review/Unsub                       # Subscriptions to evaluate
label:📥-Review/Maybe                       # Uncertain items
```

---

## Feedback Label Checks

```
label:✅-Keep                               # User corrections: keep these
label:❌-Kill                               # User corrections: kill these
label:⏸-Pause                              # User corrections: defer these
```

**Note:** Gmail search with emoji-prefixed custom labels may require clicking
the label in Gmail sidebar instead. If search doesn't return results, instruct
the user to click the label and report what's there.

---

## Query Syntax Quick Reference

| Operator | Example |
|----------|---------|
| `from:` | `from:alice@example.com` |
| `to:` | `to:bob@example.com` |
| `subject:` | `subject:invoice` |
| `in:` | `in:sent`, `in:inbox`, `in:trash` |
| `is:` | `is:unread`, `is:starred` |
| `has:` | `has:attachment`, `has:unsubscribe` |
| `label:` | `label:📥-Review/Delete` |
| `category:` | `category:promotions` |
| `newer_than:` | `newer_than:7d`, `newer_than:30d` |
| `older_than:` | `older_than:14d` |
| `after:` / `before:` | `after:2026/01/01` |
| `larger:` / `smaller:` | `larger:5M` |
| `OR` | `from:a@x.com OR from:b@x.com` |
| `-` (exclude) | `-from:noreply@example.com` |
| `{ }` (group OR) | `{from:a@x.com from:b@x.com}` |
| `" "` (exact) | `"meeting agenda"` |
