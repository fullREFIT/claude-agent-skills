# Build Path — Source Material to Executed Work

**skillquiver.dev/build-path**

A chain of four Claude skills. Each one turns raw material into something more useful than what came before it, and hands its result to the next.

---

## What this solves

Most AI instructions fail in one of two ways. Either they're too vague and the agent guesses wrong, or they're too long and duplicate a plan that already exists somewhere else — creating two versions of the truth that quietly drift apart. Build Path is four skills that catch both failures at different points in the pipeline: turning a transcript into something verified, turning verified knowledge into standing instructions, and turning any situation into a request that's exactly as long as it needs to be.

---

## The chain

```
source material (a transcript, a doc, a recording)
        │
        ▼
  triage — decides whether this even needs routing,
           or can be finished right now
        │
        ▼
  transcript-superguide — turns the source into verified
           knowledge: a guide, a checked resource list,
           and a record of what was actually confirmed
        │
        ▼
  project-instructions-forge — turns that verified
           knowledge into a working Claude Project:
           steps with clear stopping points, not a
           summary of the topic
        │
        ▼
  execution-prompt-forge — turns any single situation
           into a request sized correctly: sometimes
           one line, sometimes a full multi-step plan
        │
        ▼
      executed work
```

**The rule that keeps it from turning into a pile:** each skill does exactly one job, and hands a real, checked result to the next one. Nothing re-does work the step before it already finished.

---

## The four skills

### triage
Looks at what you're asking for and figures out if it can just be done right now, or if it genuinely needs to be handed off somewhere else first. Most requests don't need a hand-off. This is the skill that decides.

### transcript-superguide
Takes a transcript — a video, a recording, a talk — and turns it into something better than watching the original: a written guide with the shaky claims checked against real sources, a resource list where every link and price has actually been verified, and an honest note about what the transcript doesn't tell you.

**What it checks before trusting the source:**
- **Is the evidence actually finished?** If a video says "part one of four" and nothing has been proven yet, the guide says so plainly instead of writing it up like a settled method.
- **Is a sponsor's product being taught as if it were the only way to do this?** If so, the guide separates the method from the product, so you get the actual technique instead of an ad in disguise.
- **Does this touch something regulated** — money, contact information, health, hiring? If so, that gets its own clearly marked section instead of getting lost in the excitement of a cool idea.

### project-instructions-forge
Takes a verified guide and turns it into instructions a Claude Project can actually run — not a summary of the topic, but a real workflow: numbered steps, a clear point where each step is genuinely finished, and rules for when something's gone wrong. Two quick tests keep it honest:
- **Swap test:** if you could drop in a totally different subject and the steps would still make sense, they weren't specific enough. Start over.
- **Verb test:** every step should start with something a person actually does. A step that starts with a noun is a topic heading pretending to be an instruction.

### execution-prompt-forge
Takes any single situation — a task, a request, a job — and writes it up in exactly the size it needs. If the plan already exists in a file somewhere, this writes one line pointing to it. If it's a brand-new, multi-step, high-stakes job, it writes the full thing, broken into checkpoints. It always starts at the smallest option and only goes bigger when there's a real, nameable reason — never just because the task feels important.

---

## Try it

1. Download `execution-prompt-forge` and add it to your Claude tools folder.
2. Type a request the way you normally would.
3. It tells you how big a request it decided to write, and why — then hands you the finished version.

No account. No sign-up. Free.

---

*Part of the Build Path collection. Chain: triage → transcript-superguide → project-instructions-forge → execution-prompt-forge.*
