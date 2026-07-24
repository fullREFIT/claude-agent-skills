# Upgrade Path — Write Operations for Gmail Inbox Command

The skill works today with read-only Gmail MCP tools. This document covers
how to add write capabilities progressively.

---

## Level 2: Python Script Integration (inbox_cleaner.py)

If you have a Python script with Gmail OAuth2 and `gmail.modify` scope,
the skill can produce classifications that the script executes.

### What the Script Needs

The existing `inbox_cleaner.py` already has:
- Gmail OAuth2 authentication with `gmail.modify` scope
- `batchModify` for marking messages read (removing UNREAD label)
- Claude API integration for classification
- Fetch → Classify → Review → Execute pipeline

### Recommended Upgrades

After running the Phase 2 audit and confirming the classification model works,
upgrade the script to add:

1. **`--apply-labels`** — Takes classified JSON, applies Gmail labels via
   `batchModify` with `addLabelIds`

2. **`--pre-delete`** — Applies the 📥-Review/Delete label instead of just
   marking as read

3. **`--create-labels`** — Creates the full label architecture via Gmail API
   `labels.create` endpoint

4. **`--forensics`** — Runs sent-mail analysis, outputs `sender_registry.json`

5. **`sender_registry.json`** — Persistent file storing tier/category assignments
   so known senders aren't re-classified every run

### Classification Model Upgrade

Replace the binary "important/not_important" with:

```python
CLASSIFICATION_SCHEMA = {
    "tier": 1-4,           # Sender tier from registry
    "category": str,        # From the 10-category taxonomy
    "confidence": "high|medium|low",
    "action": str,          # "keep|archive|pre_delete|review"
    "label": str,           # Gmail label to apply
    "reason": str           # Classification reasoning
}
```

### Automation

```bash
# Weekly cron job
0 8 * * 1 cd /path/to/project && \
  python inbox_cleaner.py --fetch && \
  python inbox_cleaner.py --classify && \
  python inbox_cleaner.py --review && \
  python inbox_cleaner.py --apply-labels
```

---

## Level 3: n8n Automation Bridge

Build n8n workflows exposing Gmail API write operations as HTTP endpoints.

### Required Workflows

**Workflow 1: Apply Label**
- Trigger: Webhook (POST)
- Input: `{ "threadId": "...", "labelIds": ["Label_ID"], "action": "add" }`
- Node: Gmail → Add Label
- Output: success/failure

**Workflow 2: Archive Thread**
- Input: `{ "threadId": "..." }`
- Node: Gmail → Remove Label "INBOX"

**Workflow 3: Create Label**
- Input: `{ "labelName": "📥-Review/Delete" }`
- Node: HTTP Request → `POST gmail/v1/users/me/labels`

**Workflow 4: Batch Label**
- Input: `{ "threadIds": [...], "addLabelIds": [...], "removeLabelIds": [...] }`
- Node: HTTP Request → `POST gmail/v1/users/me/messages/batchModify`

**Workflow 5: Move to Trash**
- Input: `{ "threadId": "..." }`
- Node: Gmail → Move to Trash
- Safety: Only callable from Pre-Delete review flow

### Gmail OAuth2 Scopes for n8n

| Scope | Purpose |
|-------|---------|
| `gmail.modify` | Apply/remove labels, archive |
| `gmail.labels` | Create, update, delete labels |
| `https://mail.google.com/` | Full access (trash/delete) |

### Connecting n8n to Claude

If n8n MCP connector is available:
```
n8n:execute_workflow
  workflowId: "workflow-id"
  inputs: { type: "webhook", webhookData: { body: { ... } } }
```

---

## Level 4: Custom Gmail MCP Server

For Claude Desktop or Claude Code. Build a dedicated MCP server with
full read/write capabilities.

**Recommended base:** `ArtyMcLabin/Gmail-MCP-Server` (actively maintained,
includes modify_labels, delete, archive, attachment download).

**Key tools to expose:**
- `gmail_modify_labels` — Add/remove labels from messages
- `gmail_create_label` — Create new labels
- `gmail_archive` — Remove from inbox
- `gmail_trash` — Move to trash
- `gmail_batch_modify` — Bulk label/archive operations

---

## Level 5: Official Gmail MCP Write Tools

The Gmail connector documentation already references `gmail_modify_thread`
in the `gmail_list_labels` description. This suggests Anthropic plans to
add it. When available, the skill's recommendations become one-click actions.

---

## Safety Guardrails (All Levels)

Regardless of write capability level:

1. **Never auto-delete.** Trash requires explicit user confirmation.
2. **Pre-Delete is always the staging area.** Automated labeling can mark
   as Pre-Delete, but deletion is user-initiated.
3. **Batch operations are logged.** Record thread IDs affected for rollback.
4. **Tier 1-2 excluded from automation.** Only Tier 3-4 messages can be
   auto-labeled. Tier 1-2 always require manual review.
5. **First 3 sessions are recommendation-only.** No automated actions until
   trust is established, even with write tools available.
