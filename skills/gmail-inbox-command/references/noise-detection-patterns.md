# Noise Detection Patterns — Email Classification Signals

Pattern library for identifying email categories from message headers, content,
and sender behavior. Used during triage, classification, and sweep sessions.

---

## Header-Based Detection (High Confidence)

| Header | Value/Pattern | Classification |
|--------|--------------|---------------|
| `List-Unsubscribe` | Present | Subscription or newsletter |
| `Precedence` | `bulk` or `list` | Mass email |
| `X-Mailer` | Contains marketing platform name | Marketing/sales |
| `X-Campaign-ID` | Present | Marketing campaign |
| `X-MC-User` | Present | Mailchimp campaign |
| `X-SES-Outgoing` | Present | Amazon SES (bulk sender) |
| `Feedback-ID` | Present | Google-tracked bulk email |
| `X-PM-Message-Id` | Present | Postmark transactional |
| `X-SG-EID` | Present | SendGrid bulk email |

---

## Sender Address Patterns

These patterns indicate automated/noise email regardless of domain:

```
noreply@*          no-reply@*         donotreply@*
notifications@*    notification@*     alerts@*
updates@*          newsletter@*       marketing@*
promotions@*       digest@*           mailer@*
info@*             hello@*            team@*
support@* (when no active ticket)
billing@* (when not expecting invoice)
```

---

## Subject Line Patterns

### Sales/Cold Outreach (case-insensitive)
- "quick question", "following up", "checking in" (from Tier 4 senders)
- "partnership", "opportunity", "introduction", "connecting"
- "Re:" with no prior thread (fake reply threading)
- Contains emoji (from business senders — strong spam signal)

### Marketing/Promotional
- "% off", "discount", "deal", "offer", "promo"
- "limited time", "act now", "don't miss", "last chance"
- "free trial", "get started", "sign up"

### Newsletter
- Contains issue number, date, or "digest"
- "weekly roundup", "monthly update", "what's new"

### Notification
- "Your X is ready", "New activity on", "Reminder:"
- "Weekly summary", "has been updated", "new comment"
- "mentioned you", "invited you"

---

## Content-Based Detection

### Cold Outreach Body Signals
- Mentions "your company", "your website", "your team" (scraped context)
- Contains calendar link (Calendly, HubSpot, Chili Piper) in first email
- Visible personalization tokens: `{{first_name}}`, `Hi {name}`
- Under 150 words with a CTA
- From personal-looking email but with marketing infrastructure headers

### Marketing Body Signals
- Contains "unsubscribe" link (any language)
- Contains tracking pixels (1x1 images)
- Multiple external links to marketing pages
- HTML-heavy with minimal text content
- Footer contains physical mailing address (CAN-SPAM compliance = bulk sender)

---

## Volume-Based Classification

| Daily Volume from Sender | Classification |
|--------------------------|---------------|
| 3+ per day | Aggressive marketing or broken notification settings |
| 1 per day | Newsletter or daily digest |
| 3-5 per week | Active notification source |
| 1-2 per week | Weekly newsletter |
| 1-4 per month | Monthly newsletter or occasional update |
| < 1 per month | Infrequent (could be human or quarterly marketing) |

---

## Valuable vs. Noise Newsletter Distinction

- **Valuable:** User has starred, replied, opened, or applied ✅-Keep
- **Noise:** User has never interacted; sender is Tier 4; high frequency

**Exception:** Substack and Beehiiv newsletters may be valuable depending on
specific sender. Check user signal data before auto-classifying.

---

## Classification Confidence Levels

| Level | Meaning | Required Signals |
|-------|---------|-----------------|
| **High** | Recommend Pre-Delete with confidence | 3+ matching signals OR definitive header + Tier 4 |
| **Medium** | Suggest archive, flag for review | 2 matching signals OR behavioral pattern + Tier 3-4 |
| **Low** | Ask user during triage | 1 signal only, conflicting signals, or Tier 1-2 with noise patterns |

**Never auto-recommend Pre-Delete for Tier 1-2 senders.** If a VIP triggers
noise patterns, flag as anomaly: "Your Tier 1 contact is sending you marketing
emails — do you want newsletters from them or just direct messages?"
