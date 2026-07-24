# Noise Domain Registry — Seed List

Known domains that generate noise email. Validate against the user's actual
communication patterns during the initial audit. The user's overrides (✅-Keep,
❌-Kill) always take precedence over this list.

---

## Sales Outreach Platforms

Domains that send email on behalf of salespeople. Receiving from these almost
always indicates unsolicited outreach.

```
outreach.io         apollo.io          salesloft.com
lemlist.com         mailshake.com      woodpecker.co
reply.io            gmass.co           mixmax.com
yesware.com         snov.io            hunter.io
lusha.com           zoominfo.com       seamless.ai
instantly.ai
```

---

## Email Service Providers / Marketing Infrastructure

Sending infrastructure for marketing and newsletter content.

```
sendgrid.net        sendgrid.com       mailchimp.com
mc-email.com        mailgun.org        mailgun.net
amazonses.com       awsapps.com        constantcontact.com
campaign-monitor.com hubspot.com       hubspotemail.com
hs-email.com        marketo.com        pardot.com
intercom-mail.com   intercom.io        drip.com
convertkit.com      substack.com       beehiiv.com
buttondown.email    ghost.io           revue.email
klaviyo.com         klaviyomail.com    activecampaign.com
postmarkapp.com     customer.io
```

---

## Social Media Notifications

```
facebookmail.com    linkedin.com       e.linkedin.com
twitter.com         x.com              instagram.com
tiktok.com          pinterest.com      reddit.com
quora.com           medium.com         tumblr.com
```

---

## Developer / SaaS Notifications

```
# Version control
github.com          gitlab.com         bitbucket.org

# Project management
jira.atlassian.com  linear.app         asana.com
monday.com          trello.com         notion.so
clickup.com

# CI/CD and infrastructure
circleci.com        travis-ci.com      vercel.com
netlify.com         heroku.com         render.com
railway.app         fly.io

# Monitoring
sentry.io           datadog.com        pagerduty.com
statuspage.io       opsgenie.com

# Cloud providers
amazonaws.com       azure.com          cloudflare.com
digitalocean.com
```

**Important:** These domains send notifications (noise) but also messages from
real people (important). Use sender address patterns (noreply@, notifications@),
not just domain, for classification.

---

## E-commerce / Receipts

```
# Shipping
ups.com             fedex.com          usps.com
dhl.com

# Payments
paypal.com          stripe.com         square.com
venmo.com           cash.app           zelle.com

# Major retailers
amazon.com          walmart.com        target.com
bestbuy.com         apple.com
```

---

## Usage Rules

1. **Never blindly blocklist everything here.** Validate against sent mail and VIP list.
2. **Domain vs sender matters.** `github.com` sends both noise and real messages.
3. **User overrides always win.** ✅-Keep from a noise domain → respect it.
4. **Update during triage** as new patterns emerge.
5. **Substack/Beehiiv exception:** May contain valuable newsletters. Check user signals.
