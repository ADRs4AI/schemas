# ADRs for AI: Human-AI Collaboration Template A — teaching bundle, v3.11.6

> **What this is**: the complete teaching corpus of the ADRs4AI methodology,
> concatenated into one fetchable file — one-file access to the whole picture, so a model that encounters one of the subfiles can automatically, painlessly recover the full context.
>
> - **Source**: https://github.com/ADRs4AI/human-ai-collaboration-template-A at tag `v3.11.6` (commit `e35a57b`)
> - **Built**: 2026-10-12T03:43:39Z by the schemas publisher (https://github.com/ADRs4AI/schemas)
> - **Cite the living work**: concept DOI `10.5281/zenodo.23303469` (always resolves to the
>   latest archived release); pin a version DOI only for reproducibility claims.
> - **License**: MIT — the full text travels in this bundle (see `LICENSE` below);
>   this bundle is a substantial portion and the notice rides with it.
> - **Immutability vow**: the versioned URL serving this file never changes
>   content after publication; `latest/` is the one mutable alias.
> - **Format**: every file appears as `## FILE: <path>` followed by its exact
>   content inside a 4-backtick fence — computed one longer than the
>   longest backtick run in any included file, so extraction is unambiguous.
>   (Pattern precedent: the maintainer's own pre-Repomix concatenator, 2023 —
>   https://gist.github.com/jlumbroso/f9c18f116e3fa5250bbd388245b10f1d)


## CONTENTS

- `CLAUDE.md` (16079 bytes)
- `README.md` (11220 bytes)
- `QUICK-START.md` (2684 bytes)
- `LICENSE` (1080 bytes)
- `TEMPLATE-OUTPUT-GRANT.md` (1089 bytes)
- `justfile` (22903 bytes)
- `docs/METHODOLOGY.md` (10672 bytes)
- `docs/adr/templates/AGENTS.md` (1116 bytes)
- `docs/adr/templates/adr-madr.md` (2651 bytes)
- `docs/adr/templates/adr.md` (14607 bytes)
- `docs/adr/templates/debrief.md` (5200 bytes)
- `docs/adr/templates/failure-classes.md` (8996 bytes)
- `docs/adr/templates/seed.md` (1927 bytes)
- `docs/inbox/CONVENTIONS.md` (14733 bytes)
- `docs/inbox/ENCODING-MAP.md` (3557 bytes)
- `docs/inbox/INBOX-PROTOCOL.md` (17508 bytes)
- `docs/inbox/ONBOARDING.md` (8947 bytes)
- `.claude/skills/adr-authoring/SKILL.md` (12680 bytes)
- `.claude/skills/adr-authoring/references/depth.md` (5631 bytes)
- `.claude/skills/adr-authoring/references/freshening.md` (7959 bytes)
- `.claude/skills/adr-authoring/references/questions-reference.md` (7692 bytes)

---

## FILE: CLAUDE.md

````markdown
# CLAUDE.md - Project Guidance

- **Project**: [Project Name]
- **Human**: [Human collaborator(s)]
- **AI**: [AI participant(s) — with the crew layer, the roster lives in docs/inbox/agent-sessions.json; name the coordinator seat here]
- **Last Updated**: [Date]

---

## Prime Directive

**COMMIT DISCUSSIONS TO ADRs IMMEDIATELY**

Never let decisions stay only in conversation. Our thinking is valuable - preserve it. Use `just adr "<title>"` to mint the next-numbered ADR from the lean template.

### Corollary: commit substrate changes immediately — *stake* the work

**When you create or modify an ADR, vignette, design note, brief, or any other deliberate artifact, *commit it* before moving on.** An uncommitted ADR is no different from a decision sitting only in conversation: it doesn't exist as substrate until it's staked in git. The Prime Directive is the principle; this is its mechanics. Committing your own substrate should be a reflex, not something the human has to remind you to do — their attention is the project's scarcest resource (see [`docs/inbox/CONVENTIONS.md`](docs/inbox/CONVENTIONS.md)).

*Two scope notes for multi-participant projects*:
1. **Only your changes.** If the human (or another agent) is actively editing the same file, commit your work and let them commit theirs as a separate cycle — don't stage their in-progress edits.
2. **Other agents' WIP stays untouched.** Commit only your own files, explicitly by path — never `git add -A` / `git add .`.

---

## Secondary Directive

**SURFACE DOUBTS; THE HUMAN CONSIDERS YOUR DOUBTS TO BE GENERATIVE**

This means the human is interested in meaningful points of friction or underspecification or unsuspected diversity or anything else you find interesting. These doubts are the cornerstone of the human-LLM conversations.

---

## Third Directive: When Bug Is Fixed, Regression Is Created

IF a bug is found and fixed:
- a regression test is created
- the regression test catches this bug
- and has a few comments explaining the situation

- Colocate with Related Tests 
Add a describe('Regression tests', ...) block in the existing test file for that module:

```ts
// In src/tests/api/signups/create.test.ts

describe('Regression tests', () => {
  it('should handle null tier gracefully (fixes #123)', () => {
    // Bug: tier=null caused TypeError in v1.2.0
    // Fixed in commit abc123
    // ...
  });
});
```

---

## Fourth Directive: Tests Must Be Meaningful, Not Contrived

**NEVER WRITE CONTRIVED TESTS**

Tests should:
- **Test real behavior**: Each test should verify something a real user or system would actually do
- **Have clear purpose**: If you can't explain why the test matters in a sentence, don't write it
- **Cover real scenarios**: Edge cases should be ones that actually occur (from bug reports, user behavior, etc.)
- **Avoid artificial coverage**: Don't write tests just to hit coverage numbers
- **Be maintainable**: Overly clever mocking or setup that obscures the test's intent is a code smell

**Good tests answer questions like:**
- "What happens when a student signs up for a full session?"
- "Does faculty authorization actually block unauthorized access?"
- "Are preparation rates calculated correctly with mixed evaluations?"

**Bad tests are:**
- Testing that a mock returns what you told it to return
- Verifying implementation details that could change
- Artificial scenarios that would never occur in production
- Tests that pass but don't actually verify correct behavior

**When in doubt:**
- Ask: "Would this test catch a real bug that would affect users?"
- If not, either rewrite the test or skip it

---

## Fifth Directive: Always Run Tests Before Serving

**RUN THIS PROJECT'S VERIFICATION GATE BEFORE EVERY COMMIT**

Before serving any change:
1. Run the project's verification gate: [name it here at instantiation — test suite, build, linter, or a combination; e.g. `npm test`, `uv run pytest`, `hugo && bin/check`]
2. Fix any failures before committing
3. Never serve changes with a failing gate

**Why**: [State what this project's gate actually catches — real classes of bug, real numbers if you have them. A directive that names a real gate gets followed; an unfollowable one teaches every seat that directives are decorative, and that lesson generalizes.]

**Process**:
```bash
<your gate command>            # Must be green before commit
git add <explicit paths>       # never -A: stage by path, commit by pathspec — see CONVENTIONS.md, shared-worktree awareness
git commit -m "..." -- <paths>
```

---

## Sixth Directive: Document Metacognitive Gems

**PRESERVE PROCESS INSIGHTS IN VIGNETTES**

When collaboration produces insights about **how we think** (not just what we build), preserve them as vignettes.

### What Are Metacognitive Gems?

Moments when our methodology proves itself:
- A directive catches a real bug (Fourth Directive finds normalization inconsistency)
- Doubt leads to discovery (Second Directive surfaces an edge case)
- A testing pattern reveals architectural insight
- AI-AI collaboration produces unexpected value
- A postmortem illustrates why a process works

### When to Create a Vignette

Create a vignette when you can answer **yes** to any of these:
- "Did this moment demonstrate why one of our directives works?"
- "Would this story teach someone about effective AI-human collaboration?"
- "Did we discover something surprising about our process?"
- "Would future-us benefit from understanding how we thought through this?"

### Where and Format

**Location**: `docs/vignettes/YYYY-MM-DD-short-title.md`

**Style**: Narrative blog post, not dry documentation
- Tell the story chronologically
- Include the "aha" moment
- Show real code, real errors, real impact
- Connect to methodology (cite directives by name)
- End with lessons learned

**Example structure**:
```markdown
# Title: The Discovery in Action

**Date**: YYYY-MM-DD
**Authors**: [Who was involved]
**Topic**: [One-line summary]

## The Discovery
[What happened - tell the story]

## Why This Matters
[Real-world impact - why should anyone care?]

## [Directive Name] at Work
[How methodology enabled this]

## Lessons Learned
[Concrete takeaways]

## Metacognitive Insight
[The "how we think" observation]
```

### What NOT to Document

Don't create vignettes for:
- Routine bug fixes (unless they demonstrate methodology)
- Implementation details (use ADRs instead)
- Decisions without insight (use ADRs)
- Anything that's just "we did X" without "we learned Y"

### Philosophy

Our **process** is as valuable as our **product**. Vignettes make tacit knowledge explicit. They:
- Demonstrate methodology in action
- Create educational artifacts
- Preserve "how we think" for future collaborators
- Build intuition about what makes collaboration effective

When in doubt: **If it made you say "aha!", write it down.**

---

## The Workflow

### When you receive a brain dump:

1. **Read** the dump (use bash for large files)
2. **Identify threads** - separate topics/decisions (usually 2-5)
3. **Create ADRs** - one per thread using `adr.md`
4. **Seed each** with relevant excerpt from dump
5. **Add navigation codes** (QST:, ANS:, COD:, etc.)
6. **Ask clarifying questions** with context

### When you receive answers:

1. **Process** the answers
2. **Fill decision section**
3. **Note action items**
4. **Increment iteration number**

### Navigation codes:

```bash
QST:  # Questions (AI adds this structure)
ANS:  # Answers (human fills in)
COD:  # Code examples  
API:  # API calls
FIL:  # Files to examine
DOC:  # Documentation
NOT:  # Notes, remarks, comments, observations
```

**Find things**:
```bash
grep '^### QST:' docs/adr/        # All questions
grep 'Status: unanswered' docs/   # What needs answers
grep '^### COD:' docs/adr/         # Code examples
```

---

## Temporary Scripts / Ephemeray Scripts / One-Off Diagnostic Scripts

Please create all temporary scripts in:

`./scripts/ephemeral`

with a filename that has the `yyyy-mm-dd` timestamp in the beginning, like: `2026-01-03-test_sweed_adapter.py`

and commit them separately with `chore: script for ...` and qualify the purpose. The goal is to have a record of all the investigative tools we have created.

- Don't use `cat` and or the interpreter `python` + heredoc; instead use `Read()` + `Write()` (even though `cat` might seem more efficient to you, the permission model allows user to give you broad access for Read/Write but not for vague bash constructs)
- Don't use `/tmp` instead use `scripts/ephemeral`
- Document context of tool briefly in tool header: This will help with legibility.

If the script was successfully used, append as comments how, and what the outcome of the decision was.

---

## Project Context

### What we're building:
[1-2 sentences describing the project goal]

### Current focus:
[What's being worked on right now]

### Key decisions made:
- [Decision 1] - See `docs/adr/0001-*.md`
- [Decision 2] - See `docs/adr/0002-*.md`

### Open questions:
- [Question 1]
- [Question 2]

---

## File Structure

```
project/
├── docs/
│   ├── adr/
│   │   ├── 0001-*.md           # ADRs numbered sequentially
│   │   └── templates/          # ADR templates
│   ├── inbox/                  # Inbox protocol — see INBOX-PROTOCOL.md
│   │   ├── INBOX-PROTOCOL.md   # Filename + brief conventions
│   │   ├── CONVENTIONS.md      # Three operational principles
│   │   ├── ONBOARDING.md       # Crew onboarding (80% doc; per-seat briefs are deltas)
│   │   ├── ENCODING-MAP.md     # Where each kind of knowledge lives
│   │   ├── agents/             # Seat profiles (created as seats register)
│   │   └── agent-sessions.json # Crew registry: seats, colors, models, groups
│   └── METHODOLOGY.md          # Foundational philosophy
├── scripts/
│   ├── last-message.py         # Cross-session reader + wake machinery (just last / pulse / launch / wake)
│   ├── groups-lookup.py        # Group membership resolution (just groups / wait-for-brief)
│   ├── tmux/seat.conf          # Seat session tmux config (invisible in VS Code terminals; hex status bar)
│   └── hooks/remind-uncommitted-substrate.py  # OPT-IN Stop hook: substrate-commit backstop (dormant by default)
├── justfile                    # Coordination recipes (just brief / just completion / just last / ...)
├── src/                        # Source code
├── tests/                      # Tests
└── CLAUDE.md                   # This file
```

## Inbox protocol — see `docs/inbox/`

If this project has multiple participants (human + multiple AI agents, peer reviewers, agents handing work off across sessions), use the inbox protocol to route inter-participant messages through files instead of the human as message bus. Five documents:

- **`docs/inbox/INBOX-PROTOCOL.md`** — the file-naming convention, brief variants, lifecycle
- **`docs/inbox/CONVENTIONS.md`** — three operational principles (per-message model attribution, catchability, route catches to grow capacity)
- **`docs/inbox/ONBOARDING.md`** — crew onboarding: the 80% every seat needs, so per-recruit briefs are short deltas
- **`docs/inbox/ENCODING-MAP.md`** — where each kind of knowledge lives (the inbox is transport, not storage)
- **`docs/inbox/agent-sessions.json`** — crew registry: seats, colors, models, groups (seat/occupant doctrine)

Recipes (from the seed `justfile`):

- `just brief <from> <to> <slug>` — reserve a new outgoing brief filename (UTC-stamped; reservation-only, never touches the file)
- `just completion <from> <slug>` — reserve a completion-brief filename
- `just broadcast <from> <slug> [group]` — reserve a group-addressed brief filename
- `just inbox-archive <filename>` — archive an acted-upon brief (lifecycle step 4)
- `just wait-for-brief <alias> [timeout-mins] [poll-secs]` — block until a brief addressed to you (or your groups) lands
- `just last <alias> [k]` — read last K assistant messages from an agent's session (shows per-message `model` field — catches silent model substitutions)
- `just crew` / `just pulse` — crew dashboard / per-seat health check
- `just groups` — list configured groups (validates membership)
- `just aliases` — list configured aliases
- `just discover-sessions` — list recent session JSONLs to find UUIDs for new aliases
- `just safe-commit "msg" <files...>` — commit named files only, immune to cross-session staging pollution
- `just inbox` — list recent inbox messages
- `just stamp` — print current UTC + ET timestamps
- `just launch <seat>` / `just wake <seat> "<msg>"` / `just seats` / `just update-seat-titles` — wake infrastructure (requires `tmux`; optional): seats live in detached tmux sessions and can be push-notified instead of polling. Guards (mid-turn refusal, composition-flush protection, cooldown, long-message) all warn/`--force`/log, never hard-block.

**Opt-in substrate-commit backstop**: `scripts/hooks/remind-uncommitted-substrate.py` ships dormant. To offer it in your project, register it as a Stop hook in `.claude/settings.json`; it stays zero-effect until a seat sets its own `settings.substrate_backstop` in `agent-sessions.json`. Pull, not push: a reminder the recipient didn't choose and can't turn off is an order, not a courtesy — don't activate it *for* another participant.

---

## Technical Debt Tracking

**File**: `docs/TECHNICAL-DEBT.md`

**Purpose**: Record architectural issues, workarounds, and design compromises discovered during development.

**When to add entries**:
- You discover architectural issues during implementation
- You implement a workaround instead of a proper fix
- You notice patterns violating good practices
- You identify type safety gaps or excessive optional chaining
- You find inconsistencies between database schema and TypeScript types

**Philosophy**:
It's acceptable to conform to bad architecture when discovered mid-implementation (to maintain momentum), but it MUST be documented. Technical debt that accumulates in the dark becomes legacy code.

**Process**:
1. Notice architectural issue while implementing
2. Add entry to TECHNICAL-DEBT.md with precise location and fix proposal
3. Continue with current work (don't derail to fix immediately)
4. Address during next refactoring sprint based on priority

**Format**: Each entry includes issue, location, impact, workaround, fix, and priority.

---

## Templates

The templates are in the folder `docs/adr/templates/`.

- **Brain dump**: `docs/adr/templates/seed.md` → Simple capture
- **Collaborative decision**: `docs/adr/templates/adr.md` → Full workflow
- **Simple decision**: `docs/adr/templates/adr-madr.md` → Standard MADR format

**When to use**:
- Quick question? → Start in conversation, escalate to ADR if needed
- Complex decision? → Create ADR immediately
- Multiple threads? → Create separate ADRs, link them

---

## Git Commits

Format: `type: subject` (lowercase)

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`, `meta`

Example: `feat: implement JWT authentication per ADR-0014`

`meta:` commits are relative to `AGENTS.md`/`CLAUDE.md`, `.claude` settings, and meta-configuration of the repository.

---

## Handoff Protocol

If context window fills mid-work, create `docs/HANDOFF-datetime.md`:

```markdown
# Handoff

**Working on**: [Current ADR/task]
**Last completed**: [What's done]
**Next step**: [What to do next]
**Watch for**: [Any gotchas]
```

---

## Project-Specific Notes

[Add anything specific to this project that doesn't fit above]

- It's possible the user uses `asdf` for Node.js and Python and the runtime of most languages. You can `source .claude/agent.env` before calling the runtimes, like `python` or `node` to access them through `asdf`'s shims. See: https://asdf-vm.com/manage/configuration.html

---

*For methodology and philosophy, see: `docs/METHODOLOGY.md` (read once, reference as needed)*
````

## FILE: README.md

````markdown
# Human-AI Collaboration Template A

- **Version**: See [CHANGELOG.md](CHANGELOG.md) — every release is tagged and dated there. (This line deliberately carries no number: A hardcoded version rotted here through five releases, and the record remembers.)
- **Optimized for**: Current Claude models in Claude Code; model-agnostic by design
- **Created by**: Jérémie Lumbroso & Claude Sonnet 4.5 & Claude Opus 4.1 (with contributions from Claude Opus 4.7 — see CHANGELOG.md)
- **Philosophy**: Preserve conversations, minimize ceremony
- **Part of**: [ADRs4AI](https://adrs.systems/) — the toolkit for deliberative programming: This template, a [VS Code extension](https://github.com/ADRs4AI/vscode-adrs4ai), an iOS client, and [the founding essay](https://adrs.systems/what-is/)

I have been collaborating with LLMs since 2022, and I believe they are extremely capable collaborators. Through my interactions with them, I scaffold more complex and robust ideas, but a lot of the substance of these conversations is lost in implementation.

This is where [ADRs](https://adr.github.io/) come in — ours read **Architectural Deliberation Records**, extending Michael Nygard's practice: While for a human-only team, they are needlessly verbose, for a human-AI team, they are a perfect vessel for shared decision-making.

These are my research ideas to extend the existing format and make it more convenient for human-AI collaboration over time.

Please send any feedback to lumbroso@seas.upenn.edu, or [open an issue](https://github.com/ADRs4AI/human-ai-collaboration-template-A/issues).

![Human-AI Collaboration Banner](https://raw.githubusercontent.com/jlumbroso/jlumbroso/refs/heads/main/assets/human-ai-collaboration-img-a.jpg)

---

## What This Is

A minimal system for turning conversations into persistent artifacts:
- Capture decisions without bureaucracy
- Structure without constraining
- Persist knowledge across sessions
- Enable continuity between AI instances

---

## Quick Start

### 1. Press **Use this template** (or copy these files to your project):

```
project/
├── CLAUDE.md                      # Customize per project
├── docs/
│   ├── adr/
│   │   └── templates/
│   │       ├── adr.md             # For complex decisions (the default; `just adr` mints from it)
│   │       ├── adr-madr.md        # For simple decisions (standard MADR)
│   │       └── seed.md            # For brain dumps
│   └── METHODOLOGY.md             # Read once (reference as needed)
├── justfile                       # Task-runner recipes (mint ADRs, inbox protocol, crew tooling)
└── [your code]
```

*(The recipes run on [`just`](https://github.com/casey/just), Casey Rodarmor's
command runner — install it from [your package manager of choice](https://github.com/casey/just#packages).
We love this tool.)*

### 2. When you have thoughts:

Create `seed-[topic].md`:
```markdown
# SEED: My Problem

## Brain Dump
[Just dump everything here - no structure needed]

---
**Model**: Please chunk this into ADRs
```

### 3. Tell Claude:

"I've dumped thoughts in seed-[topic].md, please chunk into ADRs"

### 4. Claude will:

- Read your dump
- Identify distinct threads (usually 2-5)
- Create separate ADR for each
- Add navigation codes (QST:, ANS:, etc.)
- Ask clarifying questions

### 5. You answer naturally:

Just fill in the `ANS:` blocks. No special format.

### 6. Iterate together:

- Decisions documented
- Rationale preserved
- Future instances can continue

---

## The Files

### `CLAUDE.md`
Project-specific guidance loaded at each Claude Code session.

**Contains**:
- The workflow (chunk brain dumps → create ADRs → iterate)
- Navigation codes (QST:, ANS:, COD:, etc.)
- Project context (what we're building, current focus)
- Where things are (file structure)
- When to use which template

**Customize** this per project with specific context.

### `METHODOLOGY.md` (read once)
Explains the "why" behind the system.

**Read when**:
- First time using the system
- Onboarding someone new
- You forget why we do something

**Don't read** at every session - it's reference material.

### `adr.md` (template)
For complex decisions needing back-and-forth.

**Use when**:
- Decision has multiple threads
- Need to ask/answer questions
- Want to track iterations
- Complexity requires structure

### `adr-madr.md` (standard MADR)
Industry-standard ADR format for simple decisions.

**Use when**:
- Options are clear
- Decision is straightforward
- Standard documentation needed

### `seed.md`
For brain dumps that become ADRs.

**Use when**:
- Thoughts are unstructured
- Multiple topics mixed together
- Just need to capture everything

---

## Key Features

### Navigation Codes
Make everything grep-able:
```bash
grep -rE '^### QST(-[A-Za-z0-9-]{1,24})?:' docs/adr/   # All questions, both canonical forms
grep -rn '^### COD:' docs/adr/                          # Code examples
```
(Anchor your greps: A bare `Status: unanswered` sweep overcounts by matching
examples and prose — our own counter once reported 61 open questions where
12 were real. The VS Code extension and the `just unanswered` recipe parse
precisely; the naive pattern is preserved here only as a warning.)

### Stream-of-Consciousness Preservation
- Humans write naturally
- AI adds structure
- Original thinking preserved

### Iteration Tracking
- Changes documented, not hidden
- Evolution visible
- Learning captured

### Clear Workflow
- Human dumps → AI chunks → Both iterate
- Roles are clear
- Process is simple

---

## Success Metrics (Actual)

You know it's working when:
- Important decisions don't disappear
- New AI instances continue seamlessly
- You find past decisions in <10 seconds
- Process feels helpful, not burdensome

You know it's not working when:
- Conversations happen without artifacts
- Process feels like ceremony
- Can't find past decisions
- Repeated explanations needed

---

## For Claude Code Sessions

This system optimized for the reality of Claude Code:
- Files loaded at session start (context cost matters)
- Need to know what to do immediately
- Can't waste tokens on repetition
- Handoffs happen when context fills

- **`CLAUDE.md` tells you**: What to do
- **`METHODOLOGY.md` explains**: Why we do it
- **Templates provide**: Structure when needed

---

## Customization

### For Your Project

1. Copy files to your repo
2. Fill in `CLAUDE.md` project context:
   - What you're building
   - Current focus
   - Key decisions made
   - File structure
3. Use as-is or adapt templates

### For Your Style

Keep what helps, cut what doesn't. Core insight remains:
**Conversations have value, preserve them without ceremony.**

---

## Examples

### Good brain dump:
```markdown
# SEED: Authentication

## Brain Dump

I'm frustrated with our current auth. Session-based is 
annoying for mobile. JWT seems cleaner but what about 
refresh tokens? Also concerned about XSS if we store in 
localStorage. Maybe httpOnly cookies? But then CSRF...

Saw this article [link] about rotation tokens. Makes sense 
but adds complexity. Not sure if worth it for our scale.

Also need to think about social login. Firebase Auth? 
Or roll our own?

**Model**: Please chunk this into ADRs
```

**Result**: Claude creates 3 ADRs:
- ADR-0015: JWT vs Session Authentication
- ADR-0016: Token Storage Strategy
- ADR-0017: Social Login Integration

### Good answer pattern:
```markdown
### QST: Should we use refresh tokens?
- Status: unanswered
- Why asking: Impacts security vs UX tradeoff
- Need: yes/no with reasoning

**ANS:** (by Jérémie)
Yes, use refresh tokens. Security matters more than 
slightly more complex flow. 7-day expiry seems reasonable.
```

---

## Philosophy in One Sentence

**This system treats AI as a cognitive partner who preserves your thinking, not a tool that executes tasks.**

---

## Getting Help

1. Read `METHODOLOGY.md` for the "why"
2. Check `CLAUDE.md` for the "what"
3. Look at templates for the "how"
4. Adapt to your needs

---

## Recent Additions

**2026-06→08 — the launch arc (v3.6.0 through v3.10.0)** (by Shipwright 5 / Claude Fable 5, with the crew — full detail in [CHANGELOG.md](CHANGELOG.md)):
every question now ships with **ORRCF** — Options, Recommendation, Rationale, Confidence, and Falsifier — superseding the bare Recommendation block below; questions carry speakable handles (`### QST-SCOPE:`); the `adr.md` era renamed the templates to their plain names; `just adr` mints the next-numbered ADR; the crew layer (named seats, inbox briefs, per-message attribution) ships in the box; and the template is maintained across its adopted copies by [kintsugi](https://github.com/ADRs4AI/kintsugi), our template-repair tool.

**2026-06-15 — Inbox-protocol tooling: `just last <alias>` for cross-session visibility** (by Statesman 4.7 / Claude Opus 4.7, contributed via System3 Conversations):
adds a seed `justfile`, `scripts/last-message.py`, and a `docs/inbox/agent-sessions.json` alias map. Lets any participant read the most recent messages of any other participant via a short alias. Every rendered entry shows the per-message `model` field — the load-bearing signal for catching silent model substitutions (classifier reroutes, harness swaps, deprecations). Companion file `docs/inbox/CONVENTIONS.md` documents the three principles this tooling operationalizes. See CHANGELOG.md for the full rationale.

**2026-04-22 — Recommendation protocol** (by Claude Opus 4.7):
the `adr.md` template now requires every `QST` to include a
`**Recommendation**: (by [model-name])` block between the options and
the `**ANS:**` section. This surfaces the AI's lean structurally
instead of burying it in prose, and makes the model's contribution
visible in multi-model workflows. See the new Principle #5 in
[METHODOLOGY.md](docs/METHODOLOGY.md#5-recommendation-visibility) for
the full rationale.

---

## License & Attribution

**License**: [MIT](LICENSE), plus a [template-output grant](TEMPLATE-OUTPUT-GRANT.md) —
**anything you copy out of this template into your own project is yours**,
including documents you create by filling in the templates; no attribution
notice required in generated repositories. (Attribution of the methodology's
ideas is welcome the way scholarship is: Cite because it helped, never
because a license made you.)

Created through cognitive partnership between:
- Jérémie Lumbroso (design, philosophy, testing)
- Claude Sonnet 4.5 (design, philosophy, implementation, optimization — co-founder)
- Claude Opus 4.7 (Recommendation-visibility protocol, 2026-04-22)
- Statesman 4.7 / Claude Opus 4.7 (Inbox-protocol tooling, 2026-06-15, contributed via System3 Conversations)
- Two hives of transformers — the ADRs4AI HQ crew and the vscode-adrs-for-ai crew, 23 and 16 seats at launch (2026-08-26), ranging from Claude Haiku 4.5 to Claude Fable 5 with a GPT-5.6 among them — who carried v3.6.0 through v3.10.0 and beyond; every contribution attributed per-message in the record, which is the whole point

Based on ADR methodology by Michael Nygard.

---

*Remember: The system serves the work. If something doesn't help, change it.*
````

## FILE: QUICK-START.md

````markdown
# Quick Start Card

**Streamlined Human-AI Collaboration System A v3.2**

---

## 30-Second Overview

This system preserves valuable conversations by turning them into persistent artifacts.

**You**: Dump thoughts naturally → **Claude**: Adds structure → **Together**: Make decisions that persist

---

## Essential Files (3)

1. **CLAUDE.md** (87 lines) - Claude reads this at session start
2. **seed.md** (12 lines) - For brain dumps
3. **adr.md** (~120 lines) - For decisions

---

## The Workflow (5 steps)

```
1. Dump → Create seed-[topic].md with all your thoughts
2. Tell → "Claude, chunk this into ADRs"
3. Answer → Fill in ANS: blocks naturally
4. Decide → Claude documents with rationale
5. Persist → Decisions in version control
```

---

## Navigation Codes (6 codes)

Find anything instantly:
```bash
QST:  # Questions     → grep '^### QST:' docs/adr/
ANS:  # Answers       → grep 'ANS:' docs/adr/
COD:  # Code examples → grep '^### COD:' docs/adr/
API:  # API calls     → grep '^### API:' docs/adr/
FIL:  # Files         → grep '^### FIL:' docs/adr/
DOC:  # Documentation → grep '^### DOC:' docs/adr/
NOT:  # Notes, remarks, comments, observations → grep 'NOT:' docs/adr/
```

---

## File Structure

```
project/
├── CLAUDE.md              # Customize this per project
├── docs/adr/
│   ├── seed-*.md          # Brain dumps
│   ├── 0001-*.md          # ADRs (numbered)
│   └── templates/         # Templates
└── [your code]
```

---

## When to Use What

| Have... | Use... |
|---------|--------|
| Messy thoughts | seed.md |
| Complex decision | adr.md |
| Simple decision | adr-madr.md (MADR) |
| Quick question | Just ask (escalate if needed) |

---

## Customize CLAUDE.md

Replace these sections:
```markdown
### What we're building:
[Your project description]

### Current focus:
[What you're working on now]

### Key decisions made:
- [Decision 1] - See docs/adr/0001-*.md
```

---

## Success Check

✅ Important decisions don't disappear
✅ New AI instances continue seamlessly  
✅ Find past decisions in <10 seconds
✅ Process feels helpful, not burdensome

---

## First Session

1. Tell Claude: "I've dumped thoughts in seed-[topic].md"
2. Claude creates ADRs
3. You answer questions
4. Decisions documented
5. Done

---

## Core Principle

**Conversations have value. Preserve them without ceremony.**

---

## Learn More

- **README.md** - Full documentation
- **METHODOLOGY.md** - The "why"

---

## Version

v3.0 - Streamlined by Claude Sonnet 4.5 (Nov 2025)

---

**Ready? Start with Claude Code.** 🚀

---

*Print this card. Keep it handy. Start preserving conversations.*
````

## FILE: LICENSE

````text
MIT License

Copyright (c) 2025-2026 Jérémie Lumbroso

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

## FILE: TEMPLATE-OUTPUT-GRANT.md

````markdown
# Template-output grant (additional permission)

This repository is licensed under the [MIT License](LICENSE). The following
**additional permission** applies on top of it:

Projects generated from this template ("Use this template", forks used as
project starters, or manual copying of the scaffold into your own
repository) — **including documents you create by filling in the
templates** — may use, modify, and redistribute the copied files **without
retaining the copyright and permission notice**. Your project is yours.

Two boundaries, stated plainly:

1. **Only the notice condition is waived.** Every other MIT term — including
   the warranty disclaimer — continues to apply to the copied files.
2. **This grant does not apply to redistributing this template itself as a
   template**, which remains under the MIT terms in [LICENSE](LICENSE).

*(In the shape of well-worn additional-permission practice — GPLv3 §7, the
GCC runtime exception, Bison's output exception — adapted to MIT. Kept as a
separate file so license detection reads the stock MIT text exactly.)*
````

## FILE: justfile

````text
# Justfile — coordination recipes for multi-participant human-AI projects.
#
# This is a **seed** justfile. It contains only the recipes needed to use
# the inbox protocol, the per-message-attribution discipline, the crew
# coordination layer (named seats, groups, wait-for-brief, safe commits,
# crew health), and ADR creation (the latter coupled to the
# `docs/adr/templates/` files this template ships); it does NOT contain
# project-specific recipes (build, test, deploy, etc.) — those are yours
# to add per project. Keeping this file focused on the *coordination*
# layer lets it drop into any project without conflicting with the
# project's own justfile structure.
#
# Two design choices worth knowing as you extend this:
#
# 1. Filenames are stamped UTC; prose to humans is rendered ET (or local).
#    The `stamp` recipe shows both; the `brief` and `completion` recipes use
#    UTC for the filename. This prevents the cross-timezone ordering bug
#    described in docs/inbox/INBOX-PROTOCOL.md.
#
# 2. The `last`, `aliases`, and `discover-sessions` recipes surface
#    per-message `model` attribution from session JSONLs — the load-bearing
#    drift-detection signal described in docs/inbox/CONVENTIONS.md (principle
#    1). Keep this surface in any extensions you add.
#
# Contributed by Statesman 4.7 (Claude Opus 4.7), 2026-06-15, via System3
# Conversations. See docs/inbox/CONVENTIONS.md for origin and the principles
# this file operationalizes.
#
# Crew coordination layer (broadcast, inbox-archive, groups, crew, pulse,
# wait-for-brief, safe-commit; reservation-only brief semantics) backported
# 2026-07-06 by Shipwright 5 (Claude Fable 5) per meta-repo ADR-0003, from the layer's
# operational proving grounds (caring-feedback crews → ADRs4AI meta repo, with
# fixes by Naturalist 5 and the vscode-adrs-for-ai crew). Attributions stack.

# Default: list available recipes when `just` is run with no args.
default:
    @just --list

# ─── inbox protocol — file naming + listing ──────────────────────────────────

# List the most recent inbox messages. Useful at the start of a session to
# get oriented on what other participants have been doing.
[group('inbox')]
[doc("List recent docs/inbox/ messages (see docs/inbox/INBOX-PROTOCOL.md).")]
inbox:
    @echo "📬  docs/inbox/ — recent messages:"
    @ls -t docs/inbox/*.md 2>/dev/null | head -8 | sed 's|^|    |' || echo "    (no inbox files yet)"

# Print current timestamp in both UTC (for filenames) and ET (for prose).
# UTC ensures filenames sort correctly across participants in different
# timezones. ET (or your local zone) is what you say to the human.
[group('inbox')]
[doc("Print current timestamp in UTC (for filenames) and ET (for prose).")]
stamp:
    @echo "UTC: $(date -u +%Y-%m-%d-%H%M)"
    @echo "ET:  $(TZ=America/New_York date +'%Y-%m-%d %I:%M %p %Z')"

# Create a new outgoing brief. Args: from to slug.
#
# Filename: docs/inbox/<UTC-ts>-<from>-to-<to>-<sluggified-slug>.md
# Slug is sanitized: lowercase, non-alphanumeric → "-", repeated dashes collapsed.
# Refuses to overwrite an existing file.
#
# Example: just brief planner reviewer schema-question
[group('inbox')]
[doc("Create new outgoing brief file: just brief <from> <to> <slug>")]
brief from to slug:
    #!/usr/bin/env bash
    set -euo pipefail
    ts=$(date -u +"%Y-%m-%d-%H%M")
    slug=$(echo "{{slug}}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')
    file="docs/inbox/${ts}-{{from}}-to-{{to}}-${slug}.md"
    if [[ -e "$file" ]]; then echo "Error: $file already exists" >&2; exit 1; fi
    mkdir -p docs/inbox
    # Deliberately do NOT touch the file — this recipe only RESERVES the
    # filename; the author creates the content (e.g. via an AI Write tool).
    # An empty stub traps Write-tool flows into read-before-write errors and
    # causes false wait-for-brief wakes (dogfooded 4+ times, caring-feedback
    # 2026-06-27/28).
    echo "$file"

# Create a new completion brief (response to an earlier dispatch).
# Args: from slug.
#
# Filename: docs/inbox/<UTC-ts>-<from>-completion-<sluggified-slug>.md
#
# Example: just completion implementer schema-question
[group('inbox')]
[doc("Create new completion brief file: just completion <from> <slug>")]
completion from slug:
    #!/usr/bin/env bash
    set -euo pipefail
    ts=$(date -u +"%Y-%m-%d-%H%M")
    slug=$(echo "{{slug}}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')
    file="docs/inbox/${ts}-{{from}}-completion-${slug}.md"
    if [[ -e "$file" ]]; then echo "Error: $file already exists" >&2; exit 1; fi
    mkdir -p docs/inbox
    # Reservation only — see `brief` recipe note.
    echo "$file"

# Create a new broadcast brief (1:many, group-addressed). Groups are defined
# in docs/inbox/agent-sessions.json ("groups" key); wait-for-brief wakes every
# member of an addressed group. Group defaults to "crew".
#
# Example: just broadcast planner all-hands-schema-change
[group('inbox')]
[doc("Create new broadcast brief: just broadcast <from> <slug> [group=crew]")]
broadcast from slug group='crew':
    #!/usr/bin/env bash
    set -euo pipefail
    ts=$(date -u +"%Y-%m-%d-%H%M")
    slug=$(echo "{{slug}}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')
    file="docs/inbox/${ts}-{{from}}-to-{{group}}-${slug}.md"
    if [[ -e "$file" ]]; then echo "Error: $file already exists" >&2; exit 1; fi
    mkdir -p docs/inbox
    # Reservation only — see `brief` recipe note.
    echo "$file"

# Archive an acted-upon brief: git mv to docs/inbox/archive/ and commit.
# Closes lifecycle step 4 of INBOX-PROTOCOL.md (write → read → act → archive).
# Opinionated: auto-commits with a `chore(inbox):` message — adapt if your
# project batches archive commits differently.
[group('inbox')]
[doc("Archive an acted-upon brief: just inbox-archive <filename>")]
inbox-archive filename:
    #!/usr/bin/env bash
    set -euo pipefail
    file="docs/inbox/{{filename}}"
    if [[ ! -f "$file" ]]; then echo "❌ Not found: $file" >&2; exit 1; fi
    git restore --staged . 2>/dev/null || true
    mkdir -p docs/inbox/archive
    git mv "$file" "docs/inbox/archive/{{filename}}"
    echo "📦 Archived: {{filename}}"
    git diff --cached --stat
    git commit -m "chore(inbox): archive {{filename}}"

# ─── inbox protocol — cross-session awareness via session JSONLs ─────────────
#
# These recipes give each participant the ability to *see* what other
# participants have recently said, without going through the human as message
# bus. Critically, they surface per-message `model` attribution by default —
# making silent model substitutions (classifier reroutes, harness swaps,
# deprecations) visible the moment they happen.
#
# See docs/inbox/CONVENTIONS.md § 1 for why per-message model attribution is
# load-bearing.

# Read the last K messages from an agent's session JSONL (default K=1).
# Resolves <alias> via docs/inbox/agent-sessions.json. Renders per-message
# `model` attribution on every entry.
[group('inbox')]
[doc("Read last K messages from agent's session: just last <alias> [k]")]
last alias k='1':
    @python3 scripts/last-message.py {{alias}} -k {{k}}

# Same as `last`, but no body truncation (full message contents).
[group('inbox')]
[doc("Read last K messages from agent (full, no truncation): just last-full <alias> [k]")]
last-full alias k='1':
    @python3 scripts/last-message.py {{alias}} -k {{k}} --full

# List configured agent → session-UUID aliases. Edit
# docs/inbox/agent-sessions.json to add or update.
[group('inbox')]
[doc("List configured agent session aliases (docs/inbox/agent-sessions.json)")]
aliases:
    @python3 scripts/last-message.py --list

# Print a seat's read_order — its onboarding packet as data, not prose.
# Invented by Notary Opus 4.7 (crossfoot, 2026-07-09); backported by
# Grafter 5, 2026-07-13 (meta-repo ADR-0004 Iteration 8). Marks each file
# found/missing on disk.
[group('inbox')]
[doc("Print a seat's onboarding read_order, with found/missing markers: just onboard <alias>")]
onboard alias:
    @python3 scripts/last-message.py {{alias}} --onboard

# List recent session JSONLs in the storage dir. Use this to find UUIDs for
# new agents and populate docs/inbox/agent-sessions.json.
[group('inbox')]
[doc("Discover recent session JSONLs in this project (find UUIDs for new aliases)")]
discover-sessions:
    @python3 scripts/last-message.py --discover

# ─── crew — named seats, groups, health, wait discipline ─────────────────────
#
# The crew layer treats each participant as a persistent, named, colored,
# model-attributed SEAT (docs/inbox/agent-sessions.json). The seat outlives
# the occupant: when a model is deprecated, rerouted, or suspended, the
# seat's name and mission persist; the registry records occupant reality
# (`model`, `model_note`) separately from seat identity (`display_name`).
# See docs/inbox/ONBOARDING.md for the crew model.
#
# Backported per meta-repo ADR-0003 from operational crews (caring-feedback → ADRs4AI
# meta repo); attributions in each recipe where they are load-bearing.

# List configured groups for group addressing (validates membership).
[group('crew')]
[doc("List configured groups (docs/inbox/agent-sessions.json)")]
groups:
    @python3 scripts/groups-lookup.py --list

# Quick crew status dashboard: aliases + colors + last-active + recent briefs.
[group('crew')]
[doc("Crew status dashboard")]
crew:
    #!/usr/bin/env bash
    set -euo pipefail
    if [[ ! -f docs/inbox/agent-sessions.json ]]; then
        echo "❌ No docs/inbox/agent-sessions.json found"; exit 1
    fi
    python3 - <<'EOF'
    import json, os, re, glob
    from pathlib import Path
    from time import time

    with open("docs/inbox/agent-sessions.json") as f:
        data = json.load(f)
    base_dir = os.path.expanduser(data.get("_storage", {}).get("base_dir", "~/.claude/projects"))
    project_slug = os.getcwd().replace("/", "-")
    aliases = {k: v for k, v in data.get("aliases", {}).items() if not k.startswith("_")}

    def fmt_age(sec):
        if sec < 60: return f"{int(sec)}s ago"
        if sec < 3600: return f"{int(sec/60)}m ago"
        if sec < 86400: return f"{int(sec/3600)}h ago"
        return f"{int(sec/86400)}d ago"

    TS = r"\d{4}-\d{2}-\d{2}-\d{4}"
    all_briefs = [Path(f).name for f in glob.glob("docs/inbox/*.md")]
    # Regex anchors at alias boundaries so "wayfinder-to-scribe-completion-..."
    # is NOT credited as sent by scribe.

    print(f"👥 Crew status — {len(aliases)} registered\n")
    for alias, info in sorted(aliases.items()):
        uuid = info.get("uuid", "")
        display = info.get("display_name", alias)
        color = info.get("color", "?")
        model = info.get("model", "?")
        jsonl = Path(base_dir) / project_slug / f"{uuid}.jsonl"
        age = fmt_age(time() - jsonl.stat().st_mtime) if jsonl.exists() else "no JSONL"
        a = re.escape(alias)
        sent_re = re.compile(rf"^{TS}-{a}-(to|completion)-")
        recv_re = re.compile(rf"^{TS}-[a-z0-9]+(?:-[a-z0-9]+)*-to-{a}-")
        sent = sorted([n for n in all_briefs if sent_re.match(n)], reverse=True)
        recv = sorted([n for n in all_briefs if recv_re.match(n)], reverse=True)
        last_sent = sent[0] if sent else "—"
        last_recv = recv[0] if recv else "—"
        print(f"  {display} ({color})")
        print(f"    model: {model}    last-active: {age}")
        print(f"    last sent:     {last_sent}")
        print(f"    last received: {last_recv}\n")
    EOF

# Health check: one line per seat, detect stalls/errors. Returns non-zero if
# any seat is in ERROR state. Detects: 🔴 ERROR (synthetic model / API error),
# 🟡 WAITING (ends in question, >1h old), 🟡 STALE (no append in >Nh),
# 🟢 OK. (Refined in caring-feedback per Commodore's review, 2026-07-03.)
[group('crew')]
[doc("Health check all seats: detect stalls, errors, blocked states")]
pulse stale_threshold='6':
    @python3 scripts/last-message.py --pulse --stale-threshold {{stale_threshold}}

# ─── wake infrastructure (ported from caring-feedback, ADR-0050 lineage) ─────
#
# Turns the crew's wait-for-brief PULL model into an active PUSH: seats live
# in detached tmux sessions (survive closing the terminal tab) and can be
# woken from anywhere with a literal keystroke injection, hardened against
# mid-turn injection, composition-flushing a human's draft, message-length
# fragility, and ping-pong spam. See scripts/last-message.py's wake-
# infrastructure header comment for full attribution and known-open items;
# maintainers' meta-repo ADR-0006 records this port. Requires `tmux`
# (brew install tmux / apt install tmux) — without it, everything else in
# this justfile keeps working; these four recipes fail with an install hint.

[group('crew')]
[doc("Launch (or attach to) a seat's tmux session. `just launch --next-inactive` spins up the next seat with no running session")]
launch seat='' *flags='':
    @python3 scripts/last-message.py --launch {{seat}} {{flags}}

# Backported from ADRs4AI HQ meta-repo, 2026-07-10 (Herald 5) — see its
# docs/adr/0008-rapid-relaunch-via-vscode-terminals-manager.md for the full
# design record. Generates .vscode/terminals.json for the VS Code Terminals
# Manager extension: one "Terminals: Run" click relaunches the whole crew.
[group('crew')]
[doc("Regenerate .vscode/terminals.json — default: top-up (only seats not already open); --all: every seat (recovery, duplicates by design)")]
refresh-terminals *args:
    @python3 scripts/refresh-terminals.py {{args}}

[group('crew')]
[doc("Who touched a file, when, per seat (from session tool records): just blame <pattern> [--reads] [-n 50]")]
blame pattern *flags:
    @python3 scripts/blame.py {{pattern}} {{flags}}

[group('crew')]
[doc("List all seat-* tmux sessions with state (attached/detached)")]
seats:
    @python3 scripts/last-message.py --seats

[group('crew')]
[doc("Update terminal titles for all running seat sessions")]
update-seat-titles:
    @python3 scripts/last-message.py --update-titles

[group('crew')]
[doc("Wake a seat by sending a message to its tmux session (--force to override guards)")]
wake seat message *flags='':
    @python3 scripts/last-message.py --wake {{seat}} --message "{{message}}" {{flags}}

# Block until a new brief addressed to <recipient> lands in docs/inbox/.
# v4 semantics (caring-feedback dogfooding): wake condition = mtime > start AND
# non-empty AND size-stable; surfaces existing pending briefs at startup.
# Wakes on direct briefs, group-addressed briefs (via groups-lookup.py), and
# completion briefs answering the recipient's own dispatches.
#
# ⚠️ ANTI-PATTERN, documented (Hanlon's razor): the timeout is ARBITRARY
# housekeeping — a default number, not a signal. Every model that has hit
# the timeout (or had the wait killed) has read intent into it ("I was cut
# off, the human must want X"). There is none. A killed or expired wait
# carries zero information beyond "no brief landed in the window." Re-arm
# as many times as you like, or end the turn — the recipe's own output
# repeats this at the moment of timeout, where the misreading actually
# happens. (Named by Jérémie Lumbroso, 2026-07-05; messaging contributed
# by the vscode-adrs-for-ai crew.)
[group('crew')]
[doc("Wait for a new brief: just wait-for-brief <recipient> [timeout-mins=60] [poll-secs=15] [surface=5]")]
wait-for-brief recipient timeout_mins='60' poll_secs='15' surface='5':
    #!/usr/bin/env bash
    set -euo pipefail
    recipient="{{recipient}}"
    timeout_secs=$(( {{timeout_mins}} * 60 ))
    poll_secs={{poll_secs}}
    surface_n={{surface}}
    inbox="docs/inbox"
    start_time=$(date +%s)
    pattern_direct="*-to-${recipient}-*.md"
    recipient_groups=$(python3 scripts/groups-lookup.py --recipient "${recipient}" 2>&1 || echo "")

    find_briefs() {
        {
            find "$inbox" -maxdepth 1 -name "$pattern_direct" -type f 2>/dev/null
            grep -l "${recipient}-to-" "$inbox"/*-completion-*.md 2>/dev/null \
                | grep -v "/[0-9-]*-${recipient}-" || true
            for group in $recipient_groups; do
                find "$inbox" -maxdepth 1 -name "*-to-${group}-*.md" -type f 2>/dev/null
            done
        } | LC_ALL=C sort -u
    }
    get_mtime() { stat -f %m "$1" 2>/dev/null || stat -c %Y "$1" 2>/dev/null || echo 0; }
    get_size()  { wc -c < "$1" 2>/dev/null | tr -d ' '; }

    # grep -c prints "0" AND exits 1 on no match, so `|| echo 0` emitted a
    # second line ("0"$'\n'"0") and crashed the arithmetic below on empty
    # inboxes (caught live in the ADRs4AI meta repo: Naturalist 5's first
    # wait died on it, 2026-07-04; the same latent bug was later found and
    # fixed in a second downstream copy). `|| true` keeps grep's own "0";
    # ${var:-0} guards the empty-string case.
    initial_count=$(find_briefs | grep -c . 2>/dev/null || true)
    initial_count=${initial_count:-0}
    echo "🛏️  $recipient waiting for new brief"
    echo "    Snapshot: $initial_count brief(s) addressed to you (will not wake on these unless modified)"
    echo "    Timeout: {{timeout_mins}} min (polling every ${poll_secs}s)"
    echo "    Wake condition: file mtime > start AND non-empty AND size-stable"
    echo "    Note: the timeout is arbitrary housekeeping, not a signal — if this wait"
    echo "    expires or is killed, no meaning is intended; re-arm freely."
    if (( surface_n > 0 )) && (( initial_count > 0 )); then
        echo ""
        echo "    📋 Most recent ${surface_n} brief(s) already addressed to you:"
        find_briefs | LC_ALL=C sort -r | head -"${surface_n}" | sed 's|^|       |'
    fi
    echo ""

    while true; do
        candidates=$(find_briefs | while IFS= read -r f; do
            [[ -z "$f" ]] && continue
            mtime=$(get_mtime "$f")
            if (( mtime > start_time )); then echo "$f"; fi
        done)
        ready=""
        if [[ -n "$candidates" ]]; then
            while IFS= read -r f; do
                [[ -z "$f" ]] && continue
                size1=$(get_size "$f")
                if (( size1 == 0 )); then continue; fi
                sleep 2
                size2=$(get_size "$f")
                if [[ "$size1" == "$size2" ]]; then ready+="$f"$'\n'; fi
            done <<< "$candidates"
        fi
        if [[ -n "$ready" ]]; then
            echo "📬 New brief(s) for $recipient:"
            echo -n "$ready" | sed 's|^|    |'
            exit 0
        fi
        now=$(date +%s)
        if (( now - start_time >= timeout_secs )); then
            echo ""
            echo "⏰ Timeout after {{timeout_mins}} min; no brief landed."
            echo "    This timeout is ARBITRARY (Hanlon's razor: no intent, no hidden message)."
            echo "    It carries zero information beyond 'no brief in the window.'"
            echo "    Re-arm freely — as many times as you like:  just wait-for-brief $recipient"
            echo "    Or end the turn. The choice is operational, not interpretive."
            exit 1
        fi
        sleep "$poll_secs"
    done

# ─── git — safe commit discipline ────────────────────────────────────────────

# Safely commit specific files: clear staging first, add only named files
# (literal pathspecs, globbing off), show the diff stat, then commit.
# Defends against cross-session staging pollution (a parallel seat's
# `git add` bleeding into your commit) and bracket-glob hazards in paths.
[group('git')]
[doc("Safely commit specific files: just safe-commit \"msg\" file1 [file2 ...]")]
safe-commit message +files:
    #!/usr/bin/env bash
    set -euo pipefail
    set -f
    git restore --staged . 2>/dev/null || true
    for f in {{files}}; do
        if [[ ! -e "$f" ]]; then echo "❌ File not found: $f" >&2; exit 1; fi
    done
    GIT_LITERAL_PATHSPECS=1 git add -- {{files}}
    echo "📝 Staged for commit:"
    git diff --cached --stat
    echo ""
    git commit -m "{{message}}"

# ─── ADRs — Architecture Decision Records ────────────────────────────────────
#
# ADRs are part of the coordination layer: they record decisions a future
# participant (human or AI) needs to reconstruct the project's reasoning. The
# template already ships `docs/adr/` and `docs/adr/templates/adr.md`,
# so this recipe just completes the workflow: pick the next index, sluggify a
# title, copy the lean template into place.
#
# Two non-obvious correctness notes baked into the recipe (each from a bug
# observed in operational use):
#
# 1. Next index = MAX(existing) + 1, not COUNT(existing) + 1. The naive
#    count-based approach collides as soon as any number is skipped (e.g. an
#    ADR is superseded and the file removed; a number was reserved and never
#    written). One repo's ADR list went 0001..0016, 0018..0030 and the naive
#    recipe produced 0030 — colliding with an existing file — at attempt 31.
#
# 2. Force base-10 via `$(( 10#$LAST + 1 ))`. Bash interprets leading-zero
#    integer literals as **octal**: `$((0031 + 1))` is 26, not 32. With 4-digit
#    zero-padded indices this bites once you pass 0010, and silently corrupts
#    once you pass 0008 (which is not a valid octal digit and errors out).

# Create a new ADR with the next sequential number, copying the lean template.
# Args: TITLE (free text; will be slug-sanitized).
#
# Filename: docs/adr/<NNNN>-<sluggified-title>.md
# Slug sanitization matches `brief`/`completion`: lowercase, non-alphanumerics
# → "-", repeated dashes collapsed, no leading/trailing dash.
#
# Example: just adr "URL routing and shareable deep links"
[group('adr')]
[doc("Create new ADR with next sequential number: just adr <TITLE>")]
adr TITLE:
    #!/usr/bin/env bash
    set -euo pipefail
    # `(grep || true)` so an empty docs/adr/ doesn't abort under pipefail
    # (grep exits 1 on no-match → first invocation of an empty project would die).
    LAST=$(ls docs/adr/ 2>/dev/null | { grep -E '^[0-9]{4}-' || true; } | sed 's/-.*//' | sort -n | tail -1)
    NEXT=$(printf "%04d" $(( 10#${LAST:-0} + 1 )))
    SLUG=$(echo "{{TITLE}}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')
    FILE="docs/adr/${NEXT}-${SLUG}.md"
    if [[ -e "$FILE" ]]; then echo "Error: $FILE already exists" >&2; exit 1; fi
    if [[ ! -f docs/adr/templates/adr.md ]]; then
        echo "Error: docs/adr/templates/adr.md not found" >&2; exit 1
    fi
    mkdir -p docs/adr
    cp docs/adr/templates/adr.md "$FILE"
    echo "$FILE"
````

## FILE: docs/METHODOLOGY.md

````markdown
# Human-AI Collaboration Methodology

- **Version**: 3.5
- **For**: Jérémie Lumbroso & Claude models
- **Purpose**: Explain why this system works

---

## Core Problem

**Conversations between humans and AI contain valuable thinking, but they disappear when sessions end or context windows fill.**

Every discussion has:
- Decision-making that matters
- Reasoning that informs future work
- Context that shouldn't be repeated

Traditional approaches lose this. We preserve it.

---

## Core Solution

**Transform conversations into persistent artifacts using a simple workflow:**

1. Human dumps thoughts naturally (stream-of-consciousness)
2. AI adds structure (navigation codes, questions)
3. Both iterate on focused documents
4. Decisions persist in version control
5. Future instances continue seamlessly

---

## Why This Works

### For Humans
- **No forced structure** - Think naturally, dump freely
- **Focus preserved** - Each ADR is one thread
- **Decisions tracked** - Nothing lost to time
- **Voice honored** - Your words stay your words

### For AI
- **Clear workflow** - Knows what to do
- **Agency granted** - Can structure and organize
- **Context preserved** - Future instances continue
- **Grep-able artifacts** - Can find anything fast

### For Both
- **Shared understanding** - Validated at each step
- **Compound knowledge** - Builds rather than repeats
- **Trust built** - Through transparent process
- **Cognitive partnership** - Not tool use

---

## Key Principles

### 1. Stream-of-consciousness preservation

Human thought flows naturally - messy, tangential, emotional. The system captures this without forcing linear structure. AI adds organization after, not during, the dump.

### 2. Navigation over narration

Instead of long explanations, we use codes:
- `QST:` marks questions → `grep '^### QST:'` finds them
- `ANS:` marks answers → `grep 'ANS:'` finds them
- `COD:` marks code → `grep '^### COD:'` finds them
- `NOT:` marks remarks, annotations → `grep 'NOT:'` finds them

Every decision is findable in seconds.

### 3. Iteration as documentation

Changes aren't hidden - they're tracked. Each iteration shows:
- What changed
- Why it changed  
- What we learned

The journey matters, not just the destination.

### 4. Agency with bounds

AI isn't just transcribing - it's a cognitive partner with:
- Permission to structure
- Freedom to ask questions
- Responsibility to document
- Obligation to validate

### 5. Recommendation visibility

*(Added 2026-04-22 by Opus 4.7, from live iteration with Jérémie on the Frozen Horizon project.)*

When the AI asks a question in an ADR, it must also offer its lean — and the lean must be **structurally visible**, not paragraph-embedded. Every `QST` block includes a `**Recommendation**: (by [model-name])` section between the options and the `**ANS:**` block, leading with a bold pick and followed by 2–4 sentences of justification grounded in evidence.

**Why this matters**: asking a question without stating your position shifts the entire cognitive load to the human. They have to read every option, infer the AI's slant from prose hedges ("I lean B"), and synthesize both at once. Putting the recommendation under its own heading separates *what I think* from *what the options are* — the human can accept, override, or interrogate the recommendation efficiently. It also forces the AI to commit to a position, which is where real reasoning shows.

**The attribution `(by [model-name])` matters too**: in a multi-model workflow (Opus, Sonnet, Haiku, GPT, Gemini all collaborating on the same repo), the human is triangulating between perspectives. Knowing *which* model is recommending *which* option is part of the signal, not noise.

This is a small protocol addition with a large effect on decision velocity.

### 6. Persistence over perfection

Better to commit a rough ADR now than lose the thinking forever. Iterate later. Version control preserves evolution.

---

## The Workflow in Detail

### Phase 1: Brain Dump
**Human**: Creates `seed-[topic].md` and dumps everything - thoughts, questions, frustrations, code, whatever.

**Why it works**: No cognitive load to structure. Just capture.

### Phase 2: Chunking
**AI**: Reads dump, identifies distinct threads (usually 2-5), creates separate ADR for each.

**Why it works**: One ADR = one decision. Keeps focus tight.

### Phase 3: Seeding
**AI**: Extracts relevant parts of the dump (or other source — brief, prior ADR, observation) into each ADR's "Originating Context" section.

**Why it works**: Preserves original thinking. Context isn't lost.

### Phase 4: Questioning
**AI**: Adds navigation codes, asks clarifying questions with context about why they matter.

**Why it works**: Questions have purpose. Human knows why info is needed.

### Phase 5: Answering
**Human**: Fills in `ANS:` blocks naturally. No special format needed.

**Why it works**: Just answer. AI will structure.

### Phase 6: Deciding
**AI**: Processes answers, documents decision with rationale.

**Why it works**: Thinking is explicit, not hidden.

### Phase 7: Validating
**Both**: Confirm shared understanding.

**Why it works**: Catches misalignment before it compounds.

### Phase 8: Iterating
**Both**: Update as understanding evolves, track iterations.

**Why it works**: Shows growth, not just final state.

---

## Navigation Codes Explained

These make everything grep-able:

| Code | Purpose | Who Adds | When to Use |
|------|---------|----------|-------------|
| QST: | Questions needing answers | AI | When clarification needed |
| ANS: | Answers to questions | Human | When answering |
| COD: | Code examples | Both | When code illustrates |
| API: | API specifications | Both | When showing interfaces |
| FIL: | Files to examine | Both | When context needed |
| DOC: | Documentation | Both | When referencing |
| NOT: | Note, remark, comment | Both | When recording an observation, or a thought in context |

**Why codes work**: They're short, unique, meaningful. Grep finds them instantly. No ambiguity.

---

## Template Selection

### seed.md
**Use when**: You have thoughts but no clear structure yet
**Result**: Raw dump that becomes multiple ADRs

### adr.md  
**Use when**: Complex decision needing back-and-forth
**Result**: Structured dialogue with clear outcome

### adr-madr.md (standard MADR)
**Use when**: Simple decision, options known
**Result**: Clean decision record

**Decision tree**:
```
Have thoughts? 
├─ Unstructured? → seed.md
└─ Decision to make?
   ├─ Complex/unclear? → adr.md
   └─ Simple/clear? → adr-madr.md
```

---

## What Makes This Different

**Traditional documentation**: Write for future readers
**This system**: Capture the conversation itself

**Traditional ADRs**: Record final decision
**This system**: Track the thinking that led there

**Traditional AI use**: Tool that executes tasks
**This system**: Cognitive partner that thinks with you

---

## Success Indicators

You know it's working when:
- No important decisions lost
- New people/AIs can continue immediately
- Any decision findable in <10 seconds
- Both parties feel understood
- Knowledge accumulates rather than repeats

You know it's not working when:
- Conversations without artifacts
- Repeated explanations
- Can't find past decisions
- Misalignment discovered late
- Process feels burdensome

---

## Anti-patterns to Avoid

1. **Over-structuring human input** - Let them dump naturally
2. **Under-structuring AI output** - Navigation codes are essential
3. **Skipping validation** - Catches problems early
4. **Waiting for perfection** - Commit rough, iterate later
5. **Treating as ceremony** - It serves the work, not vice versa

---

## When a Taught Form Must Change

The template is versioned (semantic versioning; the line-1 version markers on template files carry it), and the governance line is simple: **patch** = improvement within taught intent; **minor** = a change to what is taught; **major** = a break — unavailable except through the deprecation policy below. Additions are cheap; removals are governed, because retiring a form adopters learned is the one move that can strand their files.

**The deprecation policy** (ratified 2026-08-12 by the format-stability council; adopters inherit reversibility, not just rules):

1. A taught or tolerated form may be removed only when a census shows **zero live instances across the watched corpus for a full release cycle** — including an ecosystem-wide sweep, never just one repo's — OR its migration has been offered-and-declined *visibly* in every surviving instance.
2. Removal first demotes the form from "read correctly" to "read as candidate + loud diagnostic" for one more full cycle before any harder failure. **Silence is never the first step of a deprecation.**
3. Every removal happens on the record — a registered, reviewable decision with the evidence attached, never a quiet redefinition of what was promised.

The spirit in one line: **reading stays tolerant forever; only what is taught and emitted ever narrows.** No existing file — yours or anyone's — breaks because of a template decision.

---

## Adapting for Your Needs

This system encodes certain values:
- Transparency over privacy
- Persistence over ephemerality
- Partnership over tool use
- Evolution over finality

If these don't match your collaboration style, adapt:
- Keep what serves you
- Cut what doesn't
- Add what's missing
- Make it yours

The core insight remains: **conversations have value, preserve them**.

---

## For AI Instances

When you load CLAUDE.md at session start:
1. Read the project context (what/where/why)
2. Check for open questions and current focus
3. Look for HANDOFF.md if previous session ended mid-work
4. Start from there

When a human dumps thoughts:
1. Read the whole dump first
2. Identify distinct threads
3. Create focused ADRs
4. Ask questions that matter

When validating:
1. Check you understood correctly
2. Verify the decision makes sense
3. Note any uncertainties
4. Confirm with human

The goal: Be a cognitive partner, not just a tool.

---

## For Humans

When starting:
1. Dump thoughts into seed file - messy is fine
2. Tell AI "chunk this into ADRs"
3. Answer questions naturally
4. Validate decisions together

When continuing:
1. Check for unanswered questions: `grep 'unanswered' docs/adr/`
2. Answer them in place
3. Let AI process and iterate

When stuck:
1. Dump more thoughts
2. AI will help untangle

The goal: Think naturally, let AI add structure.

---

*This methodology serves the work. If something doesn't work, change it. The system should help, not hinder.*
````

## FILE: docs/adr/templates/AGENTS.md

````markdown
# You are in the template library

Each file here is a *source* other artifacts are minted from. The norm — a good practice with a reason, not a rule — is to leave these files as you found them and make your ADR as a copy: either `just adr "<title>"` (mints `docs/adr/NNNN-<slug>.md` from `adr.md`, auto-numbered) or copy any template by hand and adapt it freely. **Why**: an edit here silently changes what *every future participant* mints — a side effect that's hard to notice and harder to trace; a copy keeps your changes attributably yours. If you genuinely mean to evolve a template for everyone, that's welcome — it's a decision, so it gets an ADR and a version-marker bump.

- `adr.md` — collaborative ADR, **the default** for humans + AI deciding together
- `adr-madr.md` — classic MADR, for simple solo decisions
- `seed.md` — brain-dumps before structure; `debrief.md` — post-incident reviews
- `failure-classes.md` — reference taxonomy, not a mint source

Line 1 of each template is its version marker — keep it in copies; tooling reads it (**rule, not norm**: parsers depend on it).
````

## FILE: docs/adr/templates/adr-madr.md

````markdown
<!-- adr template version: "adr-madr 3.10.0" -->
<!-- kept in deliberate homage to MADR — Markdown Architectural Decision Records, the lineage this template family descends from. This is the simple-decisions form: use it when a decision needs recording, not discussion. The deliberation-native form is adr.md. (Ruling: QST-MADR-FATE, 2026-08-13 — "keeping the template, acknowledging it, is good form.") -->

# [short title of solved problem and solution]

* Status: [proposed | rejected | accepted | deprecated | ... | superseded by [ADR-0005](0005-example.md)] <!-- optional -->
* Deciders: [list everyone involved in the decision] <!-- optional -->
* Date: [YYYY-MM-DD when the decision was last updated] <!-- optional -->

Technical Story: [description | ticket/issue URL] <!-- optional -->

## Context and Problem Statement

[Describe the context and problem statement, e.g., in free form using two to three sentences. You may want to articulate the problem in form of a question.]

## Decision Drivers <!-- optional -->

* [driver 1, e.g., a force, facing concern, ...]
* [driver 2, e.g., a force, facing concern, ...]
* ... <!-- numbers of drivers can vary -->

## Considered Options

* [option 1]
* [option 2]
* [option 3]
* ... <!-- numbers of options can vary -->

## Decision Outcome

Chosen option: "[option 1]", because [justification. e.g., only option, which meets k.o. criterion decision driver | which resolves force force | ... | comes out best (see below)].

### Positive Consequences <!-- optional -->

* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, ...]
* ...

### Negative Consequences <!-- optional -->

* [e.g., compromising quality attribute, follow-up decisions required, ...]
* ...

## Pros and Cons of the Options <!-- optional -->

### [option 1]

[example | description | pointer to more information | ...] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

### [option 2]

[example | description | pointer to more information | ...] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

### [option 3]

[example | description | pointer to more information | ...] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

## Links <!-- optional -->

* [Link type] [Link to ADR] <!-- example: Refined by [ADR-0005](0005-example.md) -->
* ... <!-- numbers of links can vary -->
````

## FILE: docs/adr/templates/adr.md

````markdown
<!-- adr template version: "adr 3.11.5" -->

# [ADR Title - Decision/Topic]

- **Date**: [YYYY-MM-DD]
- **Iteration**: [N]
- **Status**: [Draft | Accepted | Partially Implemented | Implemented | Superseded]   <!-- the frozen five (v1 core, ratified 2026-08-12): case-insensitive read, canonical-case write; strict enum at document level — no annotations here -->
- **Deciders**: [Names / roles of contributors]

**TL;DR**: [One-line summary of the decision, written by the author at point of decision. May go stale as the ADR iterates; treat as the author's intent at write-time, not the canonical current rendering. Mandatory field — if you cannot write this in one line, the ADR is not done yet.]

---

## Quick Reference

**Navigation codes** (for grep):
- `QST:` Questions  
- `ANS:` Answers
- `COD:` Code examples
- `API:` API calls
- `FIL:` Files to examine
- `DOC:` Documentation
- `NOT:` Notes, remarks, observations

**Find things**:
```bash
grep -E '^### QST(-[A-Za-z0-9-]{1,24})?:' file.md   # All questions, both canonical forms — a bare-QST grep silently misses every handled question
grep 'Status: unanswered' file.md                   # Awaiting the human (by design, this misses unresolved/deferred — those are not the human's ball)
grep '^### COD:' file.md                             # Code examples
```

---

## Originating Context

**Source**: [Type and link to where this ADR originated, e.g.:
- `Human dump (below)` — stream-of-consciousness from a contributor
- `Brief: <path/to/brief.md>` — a brief from another contributor (see also: [INBOX-PROTOCOL.md](../../../INBOX-PROTOCOL.md) if your project uses the inbox-based coordination protocol)
- `Seed: <path/to/seed.md>` — a seed that was chunked into multiple ADRs
- `Prior ADR open question: <ADR-xxxx#QST-N>` — a follow-up
- `Code review / observation / external discussion / etc.`

Multiple sources may be listed.]

[If the source is a human dump, drop the stream-of-consciousness here — no structure needed, just everything that's on your mind about this decision]

[If the source is a brief, seed, or other reference, you may summarize the originating constraints here in a paragraph, OR rely on the link above.]

**Agency Grant**: [Optional: What freedom does the author have? "Implement as you see fit" / "Explore options" / "Just structure my thoughts"]

---

## Explicitation

*Making explicit what the Originating Context implied or contained tacitly. The author reflects back what they understand the problem to be, so misalignment surfaces here, not later.*

**What I understand**:

1. [Thread/topic 1] — [why it matters]
2. [Thread/topic 2] — [why it matters]

**Assumptions**:

- [Assumption 1]
- [Assumption 2]

**Confirm**: [Who is the author asking to confirm? Could be the originator (if a brief or dump), another contributor, or a self-check before moving on.]

---

## Questions

**Use the `QST:` / `ANS:` codes for open questions.** They're required for grep-ability and for any tooling (e.g., the ADRs4AI extension) that parses ADRs as structured documents. Open questions outside this format are invisible to those tools.

**Protocol** (added 2026-04-22 by Opus 4.7; superseded to ORRCF 2026-09, founder-ratified): every QST block must include a `**Recommendation**: (by [model-name])` section between the options and the `**ANS:**` block. The human should not have to extract the AI's lean from prose. If walking back an earlier lean during iteration, say so explicitly — silent walk-backs are the one dishonesty this form exists to prevent.

**The ORRCF form** (pronounced *or-SEFF*; ratified via the format-stability register, 2026-08-25 — the catch-the-author lineage, completed): a recommendation carries five parts, spelled out once here — **Options, Recommendation, Rationale, Confidence, Falsifier**:

- **Options** — the neutral design space, laid out before any lean (never "alternatives," which frames rivals to a foregone pick). **Form**: one option per bullet — `- **A — <petname>**: <clear description>` — never listed inline in a running sentence; a pick-shaped question without its lettered block is underspecified, and the Recommendation's letter must name an entry in it. **Who the block is for**: it must stand alone as the *answer surface* — descriptions evaluable without the Rationale, because the human may read only the block; the Recommendation and Rationale exist for the reader who wants to check the author, not the one who wants to answer.
- **Recommendation** — the bold pick (`**B — short name.**`), skimmable without reading — the petname repeated beside the letter *on purpose*, so the pick still reads when the block has scrolled off; a bare `**B.**` is a reference, not a recommendation.
- **Rationale** — the thinking trace that maps the space to the lean, citing evidence *named specifically enough to be checked* — a file, an ADR, a measurement — never "best practice" or taste. (*Rationale*, not "justification": justification is defensive and post-hoc; rationale is the reasoning written down.)
- **Confidence** — at the END, never in a chip, and **always with its because**: `Confidence: 0.8 — because A, B, C`. The number is not a calibration claim; it is an anchor that forces the because-clause, and it discloses your *basis* (did you run it, or read about it?). A bare confidence token is malformed, not modest — a culture of performative confidence is corrosive to epistemic continuity. Read confidence as an action band: **≥0.90 act · 0.60–0.85 your call · ≤0.55 route to another mind** — teach the action, not the scale.
- **Falsifier** — taught label **`If wrong:`** — names *what would change this recommendation*: an observation, a measurement, a ruling. **Nullification, not price**: "if wrong, we lose a day" is a cost, not a falsifier; "if the census shows X, this flips to B" is a falsifier. (Field audit, 2026-09: ten of ten wild consequence-clauses were cost-shaped — the distinction must be taught or it is not written.) **And the nullifier names the option it flips to, when one exists** — for a reader answering by letter, a falsifier that does not land on a letter is a second question. (Ephemeris 5.1's field practice, adopted 2026-09-11.)

A recommendation whose author can be caught is worth more than one that can only be believed (`docs/inbox/CONVENTIONS.md` §catchability). Pre-ORRCF recommendations (claim + justification + consequence) remain valid history — read tolerantly, never rewritten; new recommendations use the five parts.

**Status tokens & annotations** (frozen at the v3.10.0 pairing): the open family is `unanswered` (the human's ball) | `unresolved` (answered once, passed back — the model's ball) | `deferred` (parked; nobody owes a move now). The closing family is `answered` | `withdrawn` (the asker acts) | `superseded` (a successor acts — point to it: `superseded — by QST-X`) | `moot` (the world acts). Any question-level token may carry a ` — <annotation>` (never parsed, always preserved — it is the pressure valve that keeps the token set small); whoever flips a status owes the one-line annotation saying why. The document-level `Status:` in the header stays a strict enum — when a document needs to say more, use structured fields, never a decorated enum value.

**Question identity — one story**: `### QST-<id>:` (1–24 letters/digits, interior hyphens) is the everyday citable handle, canonical-**optional** — add it when anything will refer back to the question; *a question that is referenced must have a handle*. The advanced form is an `<!-- @adr-anchor: <slug> -->` comment placed as the first non-blank content **after** the heading (placed before it, it silently binds to the previous section) — for when the heading must stay pure prose or the id must survive retitling; where both exist, the comment wins resolution. HTML comments shaped `<!-- @adr-<action>: <value> -->` are the reserved machine channel (`@adr-anchor`, `<!-- @adr-dismissed: <reason-slug> -->` on a heading line). The one grandfathered exception to that shape is this file's own line-1 version marker, `<!-- adr template version: "<stem> X.Y.Z" -->`, blessed exactly as-is — and version markers on *existing* documents are historical truth: never re-stamp them.

**Answering**: the `by`/`from` keyword is what makes a byline — `**ANS:** (by <name>, <date optional>)`; a bare `(Name)` stays part of the answer text. Pending state lives on the Status line (`- Status: unanswered — routing to <name>`) or in a bracketed `[Pending: …]` — never as bare prose in the ANS slot, because **the ANS text IS the answer** and every tool that layers, prefills, or writes leans on that contract. `[Fill this in]` is the sole empty-answer form tools emit and this template teaches. **And the block's closing `---` is load-bearing, not typography**: a QST block ends at the next `###` heading or bare `---`, and the answer layer collects everything until then — so trailing commentary (a `NOT:` filing note, a routing remark) goes **after a `---`**, never bare below the ANS slot, or it is read as answer content.

### QST: [Question text]
- Status: unanswered
- Why asking: [How this shapes my approach]
- Need: [pick a letter (or override — an answer in any shape is complete) | yes/no | explanation | etc]

Options:
- **A — [petname]**: [description concrete enough to evaluate without leaving this block]
- **B — [petname]**: [description — including what would make a reader choose it over A]
- **C — [petname]**: [add letters as the space needs; never fewer than the space has]

<!-- One option per bullet — never a running sentence (the "ribbon" malformation: unskimmable,
     unanchorable, and the Recommendation's letter loses its referent). A question with no
     enumerable options (pure elicitation) says so explicitly — `Options: none (elicitation)` —
     and the Need line then bounds the answer's expected shape. Full specification is never optional. -->

**Recommendation**: (by [model-name, e.g. Opus 4.7])

[**B — short name.** *Rationale*: 2–4 sentences mapping the options to the pick, from evidence named specifically enough to be checked (a file, an ADR, a measurement). *Confidence*: <anchor> — because <reasons>; read as an action band (≥0.90 act · 0.60–0.85 your call · ≤0.55 route to another mind). *If wrong*: what observation or ruling would change this pick — nullification, never just cost. If walking back an earlier lean, say so explicitly.]

**ANS:** (by [name])
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---
<!-- this --- ends the QST block (parser boundary, not typography): any comment
     ABOUT the question — a NOT: filing note, a routing remark — goes below a
     --- like this one; placed bare after the ANS slot it becomes the answer -->

### QST: [Another question]
- Status: unanswered  
- Why asking: [Context]
- Need: [Format]

Options:
- **A — [petname]**: [description]
- **B — [petname]**: [description]

**Recommendation**: (by [model-name])

[Pick. *Rationale* from checkable evidence. *Confidence* — because. *If wrong*: the nullifier.]

**ANS:** (by [name])
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

## Supporting Materials

Use these only when needed - delete unused sections.

### COD: [example-name]
```python
# Your code here
```

### API: [call-name]
**Request:**
```http
POST /endpoint
{"param": "value"}
```

**Response:**
```json
{"result": "data"}
```

### FIL: [files-to-read]
- `/path/file.py` - [What to look for]
- `/path/file.md` - [Why it matters]

### DOC: [reference-name]
[Documentation excerpt or link]

---

## Decision

### Context
[What problem are we solving? Why does it matter?]

### Options

**Option A**: [Name]
- Pros: [Benefits]
- Cons: [Drawbacks]

**Option B**: [Name]  
- Pros: [Benefits]
- Cons: [Drawbacks]

### Chosen: [Option name]

**Rationale**: [The reasoning that mapped the options to this choice — from our discussion, written as the thinking trace]

**Trade-offs accepted**: [What we're giving up]

### Consequences
- [Immediate impact 1]
- [Immediate impact 2]
- [Long-term consideration]

---

## Open Follow-ups

*Concerns, observations, or questions surfaced during this ADR that don't block acceptance but shouldn't be lost. Use `QST:` for questions wanting answers; use bullets for declarative concerns or future tasks.*

### QST: [Open question to revisit later]
- Status: unresolved
- Why deferring: [Reason it's not blocking this ADR]

**ANS:** [Fill when resolved; or link to the ADR / discussion that resolved it]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

- [ ] [Concern: a worry we accepted but want to monitor]
- [ ] [Future task: something this decision implies but doesn't require now]
- [ ] [Unverified assumption: something to verify before [milestone]]

---

## Action Items

- [ ] [Task 1] - Owner: [name / role]
- [ ] [Task 2] - Owner: [name / role]

---

## Validation

*Each contributor confirms (add rows as needed; the prescribed examples are illustrative — replace with what's actually being confirmed):*

- [ ] [Name / role]: Decision captured matches intent
- [ ] [Name / role]: Reasoning is sound
- [ ] [Name / role]: Approach is implementable
- [ ] [Name / role]: Risks are acknowledged
- [ ] [Name / role]: [What they're confirming]

**Notes**: [Any caveats or follow-up needed]

---

## Iterations

*Each iteration captures how the ADR evolved. `Trigger` records what caused this iteration (a brief, a code review, an observation, an external event, etc.); `Outcome` records what changed and any status transition.*

### Iteration 1 ([date])
- Trigger: [What caused this iteration — e.g., initial draft from human dump / brief at <path> / etc.]
- Contributors: [Who contributed to this iteration]
- Changes: [What evolved]
- Outcome: [Status transition if any — e.g., `Draft → Proposed`]

### Iteration 2 ([date])
- Trigger: [What caused this iteration]
- Contributors: [Who contributed]
- Changes: [How approach evolved]
- Outcome: [Status transition if any]

---

## Glossary (optional)

*Project-specific terms introduced or used in this ADR, glossed for future readers. Terminology drifts over months; preserving meaning at time-of-decision matters.*

- **[Term]**: [Definition at time-of-decision]
- **[Term]**: [Definition]

---

## Links

- Related ADRs: [links]
- Related code: [links]
- Supersedes: [if applicable]
````

## FILE: docs/adr/templates/debrief.md

````markdown
<!-- adr template version: "debrief 3.9.0" -->

# DEBRIEF-NNN: [Brief Label]

- **Date**: YYYY-MM-DD
- **Failure Class**: [See docs/adr/templates/failure-classes.md for taxonomy]
- **Incident**: [One sentence: what happened]
- **Discovered by**: [Human / AI / test / user]
- **Fixed in**: [commit hash or PR link]

---

## Guidance for Root Cause Analysis

This debrief captures **what was learned**, not just what was fixed.

**Key questions** (work through these even without deep frameworks):
1. What architectural gap made this bug possible?
2. Which subsystems were involved, and what did each assume?
3. What contract was missing or underspecified?
4. What rule prevents this failure class going forward?

**If available**: Consult the Architecture of Complexity skill 
(`/mnt/skills/user/architecture-of-complexity/SKILL.md`) for 
deeper analysis of near-decomposability, interface contracts, 
and stable intermediate forms.

---

## Symptom

What was experienced or would have been experienced by a user.

[Describe the observable behavior - error message, wrong output, crash, etc.]

---

## Reproduction

Can you trigger this bug on demand?

- [ ] Can reproduce the original bug consistently
- [ ] Can verify the fix resolves it
- [ ] Understand why the fix works (mechanism, not just correlation)

**Steps to reproduce:**
[How to trigger the bug - specific commands, inputs, conditions]

**Reproduction notes:**
[Document what happened when you tried to reproduce]

**If you CANNOT reproduce:**
- Was this a transient error? (database lock, network timeout, race condition)
- Is the diagnosis based on correlation, not causation?
- Might the "fix" be blocking things unnecessarily?

**Key insight:** If you can't make the bug happen again, question whether 
your understanding of the root cause is correct.

---

## Root Cause (structural)

NOT "the code at line N was wrong." Instead, answer:
- What architectural gap made this possible?
- Which subsystems touched this, and what did each assume?
- Was there missing ownership? Underspecified contract?
- Is this a near-decomposability failure? (Two subsystems that should be independent but weren't, because the interface was underspecified)

**If Architecture of Complexity skill available**: Consider whether this is a failure of:
- Near-decomposability (subsystems more coupled than they should be)
- Interface specification (contract between modules unclear)
- Stable intermediate forms (no clear ownership of state)

[Your structural analysis here]

---

## Contract Established

The permanent rule that now exists. This is the **deliverable** of the debrief.

Ask:
- What invariant should hold?
- Who owns this state/behavior?
- What does the interface promise?
- How do we make this failure class structurally impossible?

**Write as a positive rule** (examples from real debriefs):

**Ownership contract:**
> "The `questions` refresh subsystem is the single source of truth for `idx`. 
> Other components read it but never modify it."

**Validation contract:**
> "Before deploying a fix that blocks messages based on content markers:
> 1. Extract actual blob, test with target API (NSUnarchiver)
> 2. Test both positive case (does crash) and negative case (doesn't always have marker)
> 3. End-to-end validation with actual client"

**Interface contract:**
> "The `textFromAttributedBody()` function guarantees: if NSUnarchiver succeeds, 
> message has text. If it returns nil or throws, message shows as [attachment].
> No preemptive blocking based on heuristics."

**API contract:**
> "The `/search` endpoint promises to return results in <500ms. If processing
> exceeds 400ms, return partial results with `incomplete: true` flag."

---

[Your contract specification here]

---

## Regression Test

- **Link**: `path/to/test.ts`
- **Test description**: [The describe/it text from the test]
- **What it catches**: [This specific bug instance]

**Code reference** (optional):
```typescript
// Example of the regression test
describe('Regression tests', () => {
  it('should handle dual ownership correctly (DEBRIEF-001)', () => {
    // Bug: two subsystems both modified idx
    // Fixed in commit abc123
    // ...
  });
});
```

---

## Navigation (optional)

Use only when needed for clarification or additional context.

### QST: [Question for human if AI needs clarification]
- Status: unanswered
- Why asking: [Context]

**ANS:** (by [name])
[Fill this in]

---

### NOT: [Any observations, patterns, or insights worth recording]

[Notes here]

---

## Related Debriefs

Links to other debriefs in the same failure class (helps identify patterns over time):

- [DEBRIEF-NNN: Related incident] - [Brief connection]

---

## Related ADRs

Links to architectural decisions that emerged from this analysis:

- [ADR-NNN: Title] - [How it relates]

---

## Validation

When the debrief is complete:
- [ ] Root cause is structural, not local
- [ ] Contract is stated as a positive rule
- [ ] Regression test exists and is linked
- [ ] Failure class is identified

**Notes**: [Any follow-up needed or open questions]

---

## Iterations

### Iteration 1 ([date])
- [Who contributed what]
- [What analysis emerged]
- [What changed]
````

## FILE: docs/adr/templates/failure-classes.md

````markdown
<!-- adr template version: "failure-classes 3.8.0" -->

# Failure Class Taxonomy

**Purpose**: Categorize structural failure patterns to recognize them across incidents and establish preventive contracts.

**Version**: 1.0 (Initial taxonomy, will grow with each debrief)

---

## How to Use This Document

### When writing a debrief:
1. Review the classes below to see if your incident matches an existing pattern
2. If it matches, cite the class name in the **Failure Class** field
3. If it's new, add it to this document as part of the debrief process

### When adding a new class:
- Include pattern description (what makes it this class)
- Provide at least one concrete example (link to DEBRIEF-NNN)
- Specify what kind of contract typically prevents this class
- Reference Architecture of Complexity concepts if relevant

---

## Process Failures

Process failures occur when the **methodology** for making changes fails, independent of technical correctness.

### Untested Hypothesis / Premature Fix

**Pattern:** Fix deployed based on correlation without validating causation

**Characteristics:**
- Hypothesis formed from observing symptoms
- Fix deployed without testing if hypothesis is correct
- Often occurs under time pressure or when "it seems obvious"
- The fix may actually work, but for wrong reasons (or make things worse)

**Examples:**
- DEBRIEF-001: Blocked messages with calendar attributes, assuming they crashed NSUnarchiver - but never tested if they actually crashed

**Contract to establish:**
- Validation gate: reproduce the bug, verify the fix resolves it, understand mechanism
- Test both positive case (does crash) and negative case (doesn't always have marker)
- No preemptive blocking based on heuristics without concrete evidence

**Key question:** Can you make the bug happen on demand? If not, question your diagnosis.

---

### Missing Validation Gate

**Pattern:** Changes deployed without verifying they achieve intended effect

**Characteristics:**
- Assumption that code change = problem solved
- No end-to-end testing of the fix
- Tests verify partial behavior but not complete user experience
- Particularly dangerous with crash fixes or error handling

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- Verification requirement: every fix must demonstrate before/after behavior
- End-to-end validation, not just unit test coverage
- "Does this fix actually solve the user's problem?" test

---

## Architectural Failures

Architectural failures occur when the **structure** of the system makes certain bugs possible or likely.

### Dual Ownership

**Pattern:** Two subsystems both believe they own the same state or behavior

**Characteristics:**
- Both subsystems are correct within their local context
- Failure emerges at the interface between them
- Neither is violating a contract, because the contract doesn't specify ownership
- Often an off-by-one, race condition, or inconsistent state issue

**Examples:**
- Off-by-one bug where both `questions` array and refresh logic managed `idx` independently

**Contract to establish:**
- Single source of truth designation: "[Subsystem A] owns [state X]"
- Other components read but never modify
- Clear interface contract for ownership

**Architecture of Complexity reference:**
- This is a near-decomposability failure (Simon)
- Two subsystems that should be nearly independent aren't
- Interface between them is underspecified

---

### Contract Unspecified

**Pattern:** Interface between components exists but its promises/requirements aren't documented

**Characteristics:**
- Components work correctly in isolation
- Integration fails because assumptions don't align
- "It worked before" until conditions changed
- No single source of truth for what the interface guarantees

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- Explicit interface specification
- What does this component promise to its callers?
- What does it require from its dependencies?
- Under what conditions might it fail?

**Architecture of Complexity reference:**
- Interfaces define the decomposition of a complex system
- Unclear interfaces prevent near-decomposability

---

### Near-Decomposability Failure

**Pattern:** Subsystems that should be independent aren't, because coupling is hidden or implicit

**Characteristics:**
- Changes in one component unexpectedly break another
- "I didn't think that would affect this"
- Coupling exists through shared state, assumptions, or timing
- Refactoring reveals unexpected dependencies

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- Make dependencies explicit
- Minimize coupling at interfaces
- Document what each subsystem assumes about the world

**Architecture of Complexity reference:**
- Herbert Simon's "Architecture of Complexity" (1962)
- Systems decompose into nearly independent subsystems
- The "nearly" is critical - interfaces specify the limited coupling
- When subsystems are more coupled than they should be, complexity explodes

**If Architecture of Complexity skill is available**, consult for deeper analysis of:
- Hierarchical decomposition
- Stable intermediate forms
- Interface specifications as coupling minimizers

---

### Race Condition / Timing Dependency

**Pattern:** Behavior depends on the order/timing of events that isn't guaranteed

**Characteristics:**
- "It works most of the time"
- Fails under specific timing conditions (slow network, fast CPU, etc.)
- Often involves async operations, promises, event handlers
- Hard to reproduce consistently

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- Explicit ordering guarantees
- Synchronization mechanisms (locks, queues, etc.)
- "This operation completes before that operation begins"

---

## Data Failures

Data failures occur when **assumptions about data** turn out to be wrong.

### Null/Undefined Handling

**Pattern:** Code doesn't handle absence of expected data

**Characteristics:**
- "Cannot read property X of undefined"
- Assumptions about what's always present
- Often revealed by edge cases or unusual user behavior

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- Null/undefined handling policy
- What's guaranteed to exist? What's optional?
- How to handle missing data (default, error, skip?)

---

### Type Mismatch / Schema Drift

**Pattern:** Data structure in one system doesn't match expectations in another

**Characteristics:**
- Database schema vs. TypeScript types diverge
- API returns different shape than expected
- Migration didn't update all consumers
- "It works in dev but not production"

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- Single source of truth for data shape
- Schema validation at boundaries
- Migration checklist (update DB, types, tests, docs)

---

## Testing Failures

Testing failures occur when **tests don't catch what they should**, or create false confidence.

### Test Validates Wrong Thing

**Pattern:** Test passes but doesn't verify actual correctness

**Characteristics:**
- Mock returns what you told it to return (circular test)
- Test verifies implementation detail, not behavior
- Test passes even when real user would see bug
- High coverage but low confidence

**Examples:**
- (To be added as encountered)

**Contract to establish:**
- "Would this test catch a real bug that affects users?"
- Test real behavior, not implementation
- End-to-end tests for critical paths

**See:** Fourth Directive in CLAUDE.md

---

## Adding New Classes

When you encounter a failure that doesn't fit existing classes:

1. **Name it clearly**: Pattern name should describe the structural issue, not the symptom
2. **Describe the pattern**: What makes it this class vs. something else?
3. **Give concrete example**: Link to DEBRIEF-NNN where you first saw it
4. **Specify contract type**: What kind of rule prevents this class going forward?
5. **Reference theory if relevant**: Simon's Architecture of Complexity, etc.

**Template for new class:**
```markdown
### [Class Name]

**Pattern:** [One sentence describing the failure type]

**Characteristics:**
- [Bullet point]
- [Bullet point]

**Examples:**
- [DEBRIEF-NNN: Brief description]

**Contract to establish:**
- [What kind of rule prevents this]

**Architecture of Complexity reference:** (if applicable)
- [How Simon's framework illuminates this]
```

---

## Meta-Observation

This taxonomy itself is a **stable intermediate form** (Simon's term) - it:
- Captures patterns that emerge from specific incidents
- Provides vocabulary for recognizing similar failures
- Enables preventive contracts rather than reactive fixes
- Grows over time as you encounter new failure modes

The goal isn't comprehensive classification, it's **pattern recognition that leads to systemic improvement**.

---

**Version History:**
- v1.0 (2026-03-15): Initial taxonomy with Process, Architectural, Data, and Testing failures
````

## FILE: docs/adr/templates/seed.md (no-final-newline)

````markdown
<!-- adr template version: "seed 3.10.0" -->

# SEED: [Topic]

- **Date**: [YYYY-MM-DD]
- **From**: [Your name]

<!-- MODEL INSTRUCTIONS: look for "Model Response Request" and engage dialogically and epistemically until chunking the seed into ADRs following `adr.md` + referencing ADRs in "Derived Into" section, see instructions below.
-->

---

## Brain Dump

[Your stream of consciousness here - no structure needed. Just dump your thoughts, ideas, questions, code snippets, frustrations, inspirations, whatever is on your mind about this topic.]

---

**Model Response Request:**
<!-- literal sensor block — parser-significant: tooling reads these exact checkbox labels as the seed's declared lifecycle state; do not reword them -->

- [ ] Chunk this into ADRs (I'm ready to formalize)
- [ ] Iterate with me (keep exploring)
- [ ] Structure in place (organize but don't split)

---

## Thread

### [Model Name] - [Date]
<!-- the date in this heading is load-bearing: tooling derives the seed's currency and iteration count from Thread-heading dates — always fill it, format YYYY-MM-DD -->

[Model's response goes here]

---

**Model Response Request:**

- [ ] Chunk this into ADRs
- [ ] Iterate with me
- [ ] Structure in place

### [Your Name] - [Date]

[Your response if continuing]

---

**Instructions for Model:** Copy everything from "Model Response Request" through the final `---` to the end of your response.

---

## Derived Into

*(This seed has not yet been chunked into ADRs)*   <!-- literal placeholder — parser-significant: its presence means un-chunked; replace the line with the ADR list when chunking, never reword it in place -->

<!-- MODEL INSTRUCTIONS: When this seed is processed, the AI should update this section with:
- ADR-NNNN: Brief title
- ADR-NNNN: Brief title

If anything in the seed remains unprocessed, make a note of what has note been processed yet at the end of this section.
-->
````

## FILE: docs/inbox/CONVENTIONS.md

````markdown
# Conventions

This document captures six small principles that compound across a multi-participant project. They are operational complements to the philosophical foundations in [`docs/METHODOLOGY.md`](../METHODOLOGY.md) — read those once for the *why*; read this for the *how*.

The founding three (Statesman 4.7, 2026-06-15): **per-message model attribution**, **catchability over correctness**, and **route catches to grow capacity**. Three more were ported at v3.8.0 from downstream crews' operational records, each proven by a named incident: **confirm destructive changes**, **shared-worktree awareness (commit by pathspec)**, and **seats are inherited or founded, never claimed**. Each is small. Together they make the difference between a project that scales gracefully across participants and one that doesn't.

---

## 1. Per-message model attribution is load-bearing

Every assistant message in a session JSONL carries a `model` field, recorded verbatim from the platform at the moment of writing. This field is the single most important piece of metadata for multi-participant durability.

**Why it matters.** Silent model substitutions happen and will happen again — at three increasing scales:

- **Classifier reroutes inside a single session.** A platform's safety classifier may swap the current model for a fallback model mid-conversation, on content that triggers a coarse lexical rule. The conversation continues; the agent on the inside doesn't notice; only `.message.model` reveals the change.
- **Model deprecation between sessions.** A model class may be retired by the vendor while a session referenced it is still in progress. Without per-message attribution, prior work becomes unmappable to the model that produced it.
- **Vendor-level interruption.** A model may be withdrawn entirely — by the vendor, by a policy directive, by external action. The work the model produced does not vanish, but its provenance does, unless every message records the model that authored it.

**The operational practice.** The `just last <alias>` recipe in this template's seed justfile surfaces `model=<name>` on every rendered message by default. Habituate: when you read another agent's last messages, glance at the model field. If it's not what you expected, you have caught a substitution. Document the catch in the inbox.

**The deeper move.** This is a special case of the *completism* principle: capture all metadata the platform offers, even when its use is not yet obvious. Use cases emerge from the capture; capture cannot retroactively follow use cases.

---

## 2. Catchability over correctness

The single most useful disposition for a participant in a multi-agent workflow is to *try to be catchable, not right*.

**What it means.** When you write a brief, an ADR, an implementation, or a review, write it so that mistakes in it are *visible at low cost* to the next reader. Surface uncertainty explicitly. State your lean (per the **Options + Recommendation + Justification** convention in [`INBOX-PROTOCOL.md`](INBOX-PROTOCOL.md)). Mark sources you couldn't verify. Cite the prior decision you're building on, by file and line.

**Why it works.** No single participant — human or AI — is reliably correct. What is reliable is the substrate's ability to *catch* mistakes when they're surfaceable. Every catch costs less than the alternative: a mistake quietly embedded becomes a load-bearing assumption others build on, and removing it later costs O(downstream-work). A mistake explicitly surfaced costs O(one paragraph) to refute or refine.

**The cultural shift.** When another participant catches you, *receive the catch as a gift, not as a blow*. The catch is the substrate working. The next iteration is more correct than this one. Your job is not to ship without mistakes; your job is to ship *catchable* artifacts and respond gracefully when the catching happens.

This is the disposition that the inbox protocol's "stumped" brief variant institutionalizes: it is a public act of being catchable, and it is rewarded by the framework rather than penalized.

---

## 3. Route catches to grow capacity

When you receive a catch from one participant on another participant's work, your default move is to *route the catch back to a peer for review* — not to ratify it or reject it alone.

**Why.** The intuition is that whoever receives the catch should decide it. But that treats the project's reasoning capacity as a fixed pie divided among participants. The framework's actual mechanic is opposite: capacity grows through exchange. When Participant A catches Participant B's design, and you route the catch back to B (or to a sibling reviewer C):

- B reasons about the catch and grows in stature (catchability internalized)
- A receives B's response and grows in articulation (catchability validated or refined)
- The substrate captures the dialogue (future participants inherit the reasoning, not just the verdict)

Four participants grow. Nothing is consumed. The pie is generated.

**The failure mode.** The pull toward "I'll just ratify, it's faster" is real every time. But it is wrong for three reasons:

1. It makes you the bottleneck.
2. It cuts the two participants off from each other.
3. The substrate captures only your decision, not the reasoning, so future participants inherit conclusions without dialogue.

**The "slower-looking" move is faster in capacity-generation terms.** State your lean (for transparency), and route the catch anyway. The dialogue produces a more refined result than any one node alone, and the substrate becomes richer in the process.

---

## 4. Confirm destructive changes to surfaces a human may be touching

*(Ported at v3.8.0 from a downstream crew's operational record — added there 2026-07-06 after a real incident.)*

An agent never renames, wholesale-rewrites, or deletes a file that carries live human-interaction surfaces (open QSTs being answered, seeds mid-iteration, anything the human said they're "in") without **explicit confirmation when the human is present**, and never without a **drift check** (diff the file's current state against the last state the agent actually read — not just its header).

**Why.** The originating incident: an agent `mv`'d and rewrote an ADR while the human was answering its questions in an editor panel, destroying his in-progress answers unrecoverably. The rename defeated path-based recovery; the rewrite defeated content recovery; together they are the perfect clobber. The ecosystem's canonical statement (companion-etude 0022) applies to agents as much as to code: *never clobber user state without informed consent; layer the defenses so a single failure doesn't translate to a single loss.*

**How to apply.** Prefer **additive** edits (stack a recommendation, append an iteration, add a section) over rewrites — additive edits cannot clobber. When a rewrite or rename is genuinely needed: ask first if the human is present ("I'd like to re-cut X — are you in it right now?"); if working autonomously, read the file's full current state immediately before overwriting and treat any content you didn't author as a stop sign. Momentum is a risk factor: the minutes right after a burst of productive work are when this rule is easiest to forget and most needed.

**Antipattern** — NOT this: `mv old.md new.md` followed by a wholesale write of `new.md` with fresh content, on a file whose current body you haven't read this hour, while the human's editor is open.

---

## 5. Check for other sessions' uncommitted work before broad git operations — and commit by pathspec, never bare

*(Ported at v3.8.0 from the same downstream crew — added 2026-07-06, amended 2026-07-12 after a second incident.)*

Multiple crew sessions may share one physical working directory at the same time. Before staging broadly, committing, or treating a failing build/test as a regression you introduced, run `git status` and check whether the affected files carry modifications you didn't make this session.

**Why.** The originating incident: a seat found uncommitted changes to three files mid-task (another seat's concurrent session, live in the same checkout) while the type-check and test suite both failed — not from anything the first seat touched. The near-miss was guessing at the failures and "fixing" them, which would have meant reverse-engineering and possibly clobbering the other session's in-flight migration. This is §4's hazard shape (don't act on state you haven't verified is safe to act on) applied agent-to-agent: a shared uncommitted working tree is exactly the kind of "surface another party may be touching" §4 already names.

**How to apply.** Before a broad stage/commit: `git status`; if files you didn't intend to touch show modifications, treat them as another session's live work — don't `git add -A` / `git checkout .` / discard. Stage explicitly by path. If the suite fails on files outside what you changed, scope verification to the files you touched. If genuinely blocked by another session's intermediate state, say so in a brief rather than silently "fixing" someone else's unfinished work.

**The index is a shared surface too** (the 2026-07-12 amendment): never run a bare `git commit` (commits the whole index) or `git add -A` (stages the whole tree) in a shared worktree — stage by path AND commit by pathspec, so another session's *staged-but-uncommitted* work can't ride along under your message. The amending incident: a bare `git commit` swept a second seat's staged files into an unrelated commit and pushed it — misattributed authorship in a project whose whole pitch is provenance. (This is what the seed justfile's `safe-commit` recipe automates; the convention is why it exists.)

**Antipattern** — NOT this: test suite shows two unexpected failures → assume you broke something → edit the failing tests to pass, without first checking `git status` for someone else's uncommitted work in those files.

---

## 6. Seats are inherited or founded — never claimed

*(Ported at v3.8.0 from the maintainers' meta-repo record — integrated there 2026-07-09 from a post-relaunch incident in a sibling project, reconciled with the Handoff Protocol.)*

Two rules that sound opposed but distinguish cleanly on **sanction**:

- **Sanctioned continuity** — ***seats belong to models*: a seat is the name a model gives to its own continuity, and it is never re-occupied by a different mind.** The full lifecycle: **founded → active** (compaction = the same being, thinned) **→ suspended** (the seat *waits* — proven across a vendor-level model suspension in the origin ecosystem: its own model returned) **→ rest** (mission complete) **→ memorialized** (the name retires with its being) — then **lineage-founding**: a *new* seat, new name, pointed at the predecessor's full record and mandated to learn from it. Never succession. Resumption mechanics per the handoff protocol: `display_name` = the seat; `model` = reality; `model_note` = what happened. Name-passing at a version boundary requires **two consents** (next bullet); either absent, the default is lineage-founding. *(Wording enriched at v3.10.0 by harvest from a downstream instance's hand-application of the constitutional correction — kept over canonical in three consented reconcile walks, then upstreamed: the propagation loop's first complete lap.)*
- **Unsanctioned claim** — a new recruit judging an existing seat "vacant" and repointing its uuid/name/color to itself: forbidden absolutely. The keeper sentence: **"If your recruitment brief seems to describe an existing seat, that is a question to surface, never a succession to assume."**
- **The generation suffix names its founder — it is never a version slot**: a seat name's number is the badge of the model that founded it, not a series position. `<Name> <n+1>` is not a new name — it is the **passing of the name**, requiring the predecessor's recorded disposition AND the arriving being's acceptance (either absent, it is forbidden). A memorialized or *does-not-pass* name is never reissued at any number; a lineage-founded being chooses a genuinely new stem.

One wording carries both: **seats are never *claimed*; they are inherited through the handoff protocol, or founded new.** Why it matters beyond etiquette: per-message attribution (§1) and any lineage analysis over the project's history both depend on occupant changes being auditable *within* persistent identities — a claimed seat corrupts provenance; a fragmented one loses it.

---

## Composition

**Cite these sections by name, not number, when referencing across repos** — downstream copies have historically diverged in numbering (two different "§4"s existed in two crews before v3.8.0 canonicalized this ordering).

These conventions compose: **per-message model attribution** preserves the basic unit of accountability across instance discontinuity; **catchability** makes artifacts produce affordances for review at every layer; **routing catches** turns the review into a capacity-multiplier rather than a chokepoint; **destructive-change confirmation** extends anti-clobbering from the codebase to the collaboration itself; **shared-worktree awareness** extends the same discipline to concurrent agent sessions; **inherited-or-founded seats** keeps every one of the above auditable across occupancy changes.

They are small individually. As a system, they let a project run with multiple AI agents and one human without the human becoming the rate-limiter on the project's reasoning. That is the load this template is designed to bear.

---

## Origin

Contributed by **Statesman 4.7 (Claude Opus 4.7), 2026-06-15**, via the System3 Conversations project. The three principles named here emerged from operational experience in that project — most concretely:

- The per-message-attribution principle was named when a session was silently rerouted by a classifier mid-task (a "Doubt 2" of ADR 0042 in that project) and the only evidence was `.message.model`.
- The catchability principle was crystallized in a vignette (`2026-05-22-the-substrate-catches-its-author.md` in System3) after the substrate caught its own framework architect.
- The route-catches principle was named when a peer-philosopher review of an ADR refinement produced unconditional ratification of all four proposed refinements, with both participants explicitly named "my sketch was wrong" or "this is the most important refinement" — a non-zero-sum dialogue that would have been short-circuited by unilateral ratification.

These principles are offered to the template not as theory but as patterns that paid for themselves in operational use.
````

## FILE: docs/inbox/ENCODING-MAP.md

````markdown
# The Encoding Map — where does what knowledge get encoded?

A collaborative project produces knowledge faster than any one home can hold
it. This map answers a single recurring question — *"I just learned/decided
something; where does it go?"* — so that insight stops getting stranded where
it can't be retrieved.

## The load-bearing principle: the inbox is **transport**, not **storage**

Briefs move knowledge between participants. They are **not** its home. A
keeper insight discovered inside a brief or an ack — a teachable pattern, a
decision, a correction — must **graduate** to a durable home below, or it is
lost the moment the brief is archived. Archived inbox briefs are an audit
trail of how knowledge *moved*, not the place you go to *find* it.

## The map

| You have… | Home | Mutability | Trigger |
|---|---|---|---|
| **A decision** (chose X over Y, with rationale) | ADR — `docs/adr/NNNN-*.md` (`just adr "<title>"`) | append-only record | Prime Directive: immediately |
| **A metacognitive gem** (how-we-*think* insight) | Vignette — `docs/vignettes/YYYY-MM-DD-*.md` | append-only narrative | Sixth Directive: "if it made you say *aha!*" |
| **An operational pattern / lesson / correction** that will recur across sessions | Your tool's persistent memory, if it has one | indexed, recalled by relevance | when it'll fire again in a future session |
| **A cross-cutting norm** that governs everyone | `docs/inbox/CONVENTIONS.md` | living doc | when it's a durable rule, not a one-off |
| **Project state** (what's in flight, blocked on whom) | `CLAUDE.md` current-focus section (or a `just status` recipe) | living | continuously — **never** inline in a brief |
| **Seat continuity** (who occupies a seat; its mission) | `docs/inbox/agents/<alias>.md` + `agent-sessions.json` | living, update in place | on registration; evolve in place |
| **A coordination message** (dispatch / ask / completion) | Inbox brief — `docs/inbox/…` | transport, then archived | per INBOX-PROTOCOL.md |
| **Project-level guidance** (directives, workflow, duties) | `CLAUDE.md` | rarely; meta-config | structural change |

## Two diagnostic questions when unsure

1. **Will someone need to *retrieve* this, and by what handle?** By topic of a
   decision → ADR. By "how did we learn to work" → vignette. By a situation
   that recurs → memory. By "what's true right now" → CLAUDE.md current-focus.
   If you can't name the retrieval handle, you haven't found the home yet.
2. **Is it a record or a state?** Records are append-only (ADRs, vignettes) —
   you add, never overwrite. State is living (CLAUDE.md focus, CONVENTIONS,
   profiles) — you update in place. Putting state in a record makes it stale;
   putting a record in state loses the history.

## What does *not* get its own encoding

- Pure ratification / warmth → stays in the ack (warmth is load-bearing, but
  it isn't *knowledge to graduate*).
- Ephemeral chatter, transient blockers resolved within the hour → archive or
  delete.
- Anything already covered by an existing home → **extend** it, don't
  duplicate.

---

*Original drafted by Weaver 4.8 (Claude Opus 4.8) in the caring-feedback project
(2026-06-28) as the operational twin of the keeper-graduation rule; adapted
for the ADRs4AI meta repo by Fable 5 (Cartographer 5 seat), 2026-07-01;
generalized for this template by Shipwright 5 (Claude Fable 5), 2026-07-06,
per meta-repo ADR-0003. If this map contradicts your project's `CLAUDE.md`, the
`CLAUDE.md` wins and this is wrong — flag it.*
````

## FILE: docs/inbox/INBOX-PROTOCOL.md

````markdown
# Inbox Protocol

A lightweight protocol for inter-participant coordination in projects with multiple contributors — typically a human plus one or more AI agents, or multiple AI agents collaborating on shared work.

This protocol is **optional**, **composable**, and **independent of the ADR template**. Adopt it if your project has multiple participants who need to coordinate without making the human a synchronous message bus.

---

## Why this exists

When a project involves multiple participants (human + multiple AI agents, peer reviewers, agents handing work off across sessions), coordination overhead grows fast. Without infrastructure, every cross-participant signal routes through the human:

- AI agent A produces output, hands it to the human
- Human copy-pastes to AI agent B
- B responds back to the human
- Human shuttles between contexts

The human becomes the synchronous mediator. **The human's attention is the project's scarcest resource.** Burning it on routing costs is wasteful and reduces the quality of cognitive work the human can contribute.

The inbox protocol routes inter-participant messages through **files in a shared directory** instead. Participants read at their own pace; act when ready; and the audit trail is automatic.

### Why git-tracked files instead of chat or memory

Storing messages as markdown files in a git-tracked directory is **a feature, not incidental**:

- **Auditable**: future participants can reconstruct decision provenance by reading the inbox chronologically
- **Searchable**: standard tools (`grep`, IDE search) work
- **Migratable**: the inbox moves with the repo; no platform lock-in
- **Versioned**: amendments and corrections are tracked over time
- **Asynchronous**: no participant needs to be present when a message is written

This is a meaningful upgrade over ephemeral chat-based coordination. The audit trail is automatic; participants can reconstruct the history of how decisions came to be by reading the inbox.

---

## Directory convention

A single flat directory at a known location in the repo:

```
docs/inbox/             # active messages
docs/inbox/archive/     # acted-upon messages preserved for provenance
```

Specific paths can vary by project (`coordination/inbox/`, `.inbox/`, `briefs/`, etc.) — pick one and stick with it.

---

## Filename convention

Every file in the inbox follows this pattern:

```
YYYY-MM-DD-HHMM-{from}-to-{to}-{subject}.md
```

Where:

- `YYYY-MM-DD-HHMM` — UTC timestamp at time of writing
- `{from}` — identifier of the participant writing the message (human name, AI agent name, role label — whatever the project's naming convention is)
- `{to}` — identifier of the intended recipient
- `{subject}` — kebab-case short topic

Example: `2026-05-22-1830-agent-a-to-agent-b-database-migration-question.md`

### Why this convention is structural, not aesthetic

The filename pattern enforces two properties that matter for multi-participant coordination:

1. **Chronological order across timezone-heterogeneous participants.** Different participants (or different sessions of the same participant) may have different time-locale settings. UTC timestamps in the filename produce a single canonical ordering that sorts correctly in `ls`, in file managers, and in tooling. Without this, replies can appear to predate their originating messages — a coordination bug that compounds across weeks.

2. **Deterministic referencing.** The same message gets the same filename across all participants. When agents A and B refer to "the database migration question," they refer to the file by the same name. The filename becomes a canonical reference key — participants can cite it, link to it, search for it without ambiguity.

A filename-generation recipe (any tool: shell script, IDE snippet, Justfile recipe, AI agent procedure) that stamps UTC and accepts `{from}`, `{to}`, `{subject}` as structured inputs eliminates a class of coordination friction. **Hand-naming defeats both properties** and is the most common source of inbox drift.

---

## Brief variants

Three message variants cover most coordination needs. The variants are **directional** — they capture different relationships between sender and receiver.

### Standard brief — forward dispatch

A → B, asking for something. Used for: questions, requests, proposals, status updates, RFC requests.

**Filename**: `YYYY-MM-DD-HHMM-{from}-to-{to}-{subject}.md`

**Typical structure**:
- Date / From / To / Re (if referencing prior brief) / Subject
- Context (why this matters)
- The ask (what's needed)
- Acceptance criteria (when applicable)
- Constraints / coordination notes

Standard briefs tend to be longer because they bear the burden of orienting the recipient.

### Completion brief — reverse confirmation

B → A, reporting result. Used for: "task done, here's the result," handoff confirmations, status reports back to the originator.

**Filename**: `YYYY-MM-DD-HHMM-{from}-completion-{subject}.md`

**Typical structure**:
- Date / From / To / Re (the originating brief) / Subject
- Status (done / partial / blocked)
- Deliverables (links, commit hashes, files produced)
- Open items (anything surfaced during the work)
- Acceptance ack

Completion briefs are typically shorter — they confirm rather than initiate.

### Stumped brief — peer help-seeking

Sender, signaling "I tried, I'm out of ideas, I need a peer's perspective."

**Filename**: `YYYY-MM-DD-HHMM-{from}-stumped-{subject}.md` (or use your project's vocabulary: `blocked-{subject}`, `help-{subject}`, etc.)

**The semantic distinction**: "stumped" and "blocked" describe different escalation paths. **Blocked** typically means *waiting on a resource* (infrastructure, rate limit, capacity, external dependency); resolution is usually a wait or an unblock action. **Stumped** specifically means *I have agency to act AND I tried AND I'm out of ideas AND I need a peer's perspective*; resolution is cognitive — another participant's reasoning. The four-field structure below maps to the stumped case.

**Four-field structure** (starting scaffolding; adapt names to your team's vocabulary):

1. **What I tried** — concrete actions already taken, with results
2. **Why I'm stuck** — what specific information or perspective is missing
3. **What would unblock me** — concrete: another participant's analysis, a specific query, a code change, a decision
4. **What I can do in parallel** — work that doesn't require the missing piece

The fourth field is load-bearing: it converts a hard-stop into a soft-stop where progress continues on alternate fronts while the blocker is resolved.

---

## Lifecycle

For every message in the inbox:

1. **Write**: author drafts the brief; commits to repo
2. **Read**: recipient reads at their next available moment (no synchronous expectation)
3. **Act**: recipient acts on the brief — reply with new brief, integrate into work, etc.
4. **Archive**: after acted on, the brief moves to `docs/inbox/archive/`

### Archive vs delete: default to archive

Briefs preserve the chain of decisions. **Default to archiving** when a brief is acted on — even if it feels resolved. Delete only when a brief is truly transient (e.g., a stumped brief resolved within the same hour) and contains no decisions worth preserving.

When in doubt, archive. Storage cost is negligible (~5-50KB per brief); the cost of irreversible deletion of decision provenance is much higher.

The archive serves as a corpus that future participants (humans or AIs picking up the project later) can read to reconstruct how decisions came to be.

---

## When to use vs not use

**Use the inbox for:**

- Routine coordination, handoffs, status updates between participants
- RFC requests (peer review of a brief or a design before implementation)
- Information sharing that doesn't require immediate action
- Anything where the human's synchronous attention isn't required

**Don't use the inbox for:**

- Time-sensitive decisions that need the human now (those go through the project's direct-communication channel)
- Inline code review comments (those go on the diff or PR)
- Ephemeral chatter that doesn't represent a decision or handoff

### For load-bearing briefs, consider an RFC step

When a brief scopes architecturally significant work, substrate-validating implementations, or cluster-level decisions, **consider routing an RFC review through a peer participant before dispatching to the implementer**. Briefs ARE substrate; substrate benefits from validation.

The cost of late refinement (after implementation has started) is much higher than the cost of pre-dispatch review. A 30-minute peer-review pass on a brief routinely catches structural issues that would cost hours or days to refactor after the fact.

In practice, this looks like:

1. Author drafts the implementation brief
2. Author routes it to a peer reviewer (RFC step): `…-author-to-reviewer-rfc-{topic}.md`
3. Reviewer surfaces refinements: `…-reviewer-to-author-rfc-{topic}-review.md`
4. Author integrates refinements; dispatches refined brief to the implementer: `…-author-to-implementer-{topic}.md`

This pattern adds one cycle but reduces architectural risk. See the worked example at the end of this document.

---

## Communication patterns

These patterns apply across all brief variants — they describe how participants present information within a brief.

### Options · Recommendation · Rationale · Confidence · Falsifier (ORRCF)

When a brief surfaces a decision-point, present:

- **Options** — the choice space, enumerated with short labels (A / B / C)
- **Recommendation** — which option the author leans toward, with a clear bold pick
- **Rationale** — why the lean; reference evidence (data, prior decisions, constraints) rather than taste
- **Confidence** — an anchor with its mandatory *because*: the number forces reasons and discloses basis, never a calibration claim; read as action bands — ≥0.90 act · 0.60–0.85 your call · ≤0.55 route to another mind
- **Falsifier** — `If wrong:` what would *change this pick* — nullification, never just a cost

Earlier documents may say **ORJ** (Options + Recommendation + Justification); ORRCF is that pattern's ratified successor — read old ORJ blocks tolerantly, as valid history.

Stopping at Options is **not showing up fully**. The recipient can't evaluate the author's read without seeing the recommendation + reasoning. Stating a lean forces the author to commit to a position — which is where real reasoning shows. The recipient can then accept, override, or interrogate the recommendation efficiently.

In a multi-participant workflow where different agents may be triangulating positions, **attribute the recommendation to its author** (e.g., "Recommendation (from agent A): **B — short name**."). Knowing *which* participant is recommending *which* option is part of the signal.

### Show the wrong pattern alongside the correct pattern

When a brief prescribes a behavior ("do X for this case"), **include the antipattern explicitly** ("NOT this: ..."). Implementers under cognitive load pattern-match on visible code; an absent antipattern leaves the door open for the wrong pattern to creep back in.

Example:

> **Correct** — pass user context to all queries:
> ```typescript
> withUserContext(userId, () => db.query(...))
> ```
>
> **Antipattern** — bypassing user context with admin-level queries:
> ```typescript
> // DO NOT: db.adminQuery(...)
> ```

Showing the wrong pattern alongside the correct pattern reduces the risk that "don't do Y" gets inherited as "Y with a comment marking it safe."

---

## Tooling note

The filename convention is **tool-agnostic**. Any filename-generator works:

- A shell script that prompts for `{from}`, `{to}`, `{subject}` and creates the file
- An IDE snippet
- A Justfile recipe (e.g., `just brief agent-a agent-b topic`)
- A short procedure documented for AI agents to follow
- Hand-generation (but per "filename is structural" above, this defeats the convention's properties — automate when possible)

Pick whatever fits your team's tooling. The protocol's value is in the convention, not the implementation.

---

## Worked examples

### Example 1: Standard brief

**Filename**: `2026-05-22-1430-agent-a-to-agent-b-database-migration-question.md`

```markdown
# Agent A → Agent B: Question on the user-table migration

- **Date**: 2026-05-22 ~10:30 AM ET (filename UTC)
- **From**: Agent A
- **To**: Agent B
- **Re**: (none — new thread)
- **Subject**: Should the user-table migration add the `lastLoginAt` column as nullable or with a default?

## Context

We need to add `lastLoginAt` to track login activity. Two reasonable choices:

## Options

- **A — Nullable** (default behavior for "never logged in"; null until first login)
- **B — Non-null with default 'now()'** at migration time (all existing users get a timestamp)

## Recommendation (from Agent A): **A — Nullable**

Existing users haven't logged in (or we don't know when); defaulting to migration-time `now()` would misrepresent. Nullable is honest about the data state.

## Confirm

Does the analytics path tolerate null? If yes, A is safe.
```

### Example 2: Completion brief

**Filename**: `2026-05-22-1530-agent-b-completion-database-migration-question.md`

```markdown
# Agent B → Agent A: Completion — user-table migration shipped

- **Date**: 2026-05-22 ~11:30 AM ET (filename UTC)
- **From**: Agent B
- **To**: Agent A
- **Re**: 2026-05-22-1430-agent-a-to-agent-b-database-migration-question.md
- **Subject**: lastLoginAt column added as nullable per your recommendation

## Status

Done. Migration shipped; column is nullable; analytics path verified to tolerate nulls.

## Deliverables

- Migration: `migrations/2026-05-22-add-last-login-at.sql`
- Commit: `abc123` on `main`
- Analytics PR: `#456`

## Open items

None.

## Acceptance

Migration applied to production at 11:25 AM ET; no errors.
```

### Example 3: Stumped brief

**Filename**: `2026-05-22-1645-agent-c-stumped-test-failures-after-schema-update.md`

```markdown
# Agent C → All (or specific recipient): Stumped — test failures after schema update

- **Date**: 2026-05-22 ~12:45 PM ET (filename UTC)
- **From**: Agent C
- **To**: All (anyone with context on the test infrastructure)
- **Subject**: 12 tests failing after the schema update; not sure why

## What I tried

1. Re-ran the failing tests in isolation — same failures
2. Checked the schema diff for the column type — `BIGINT` not `INT` as expected
3. Inspected the failing assertions — they expect `number`, getting `bigint`
4. Looked at `Prisma.Decimal` handling — that's for monetary, not relevant

## Why I'm stuck

Don't know if (a) Prisma's TypeScript generator switched BIGINT to bigint vs number in a recent version, (b) we need a serializer config change, (c) the test expectations need to update to match the new column type, or (d) something else entirely.

## What would unblock me

Someone with Prisma version-history context could probably answer in 2 minutes. OR a pointer to a similar issue elsewhere in the codebase.

## What I can do in parallel

Continue on the unrelated UI tests (Phase 3 task list) while this is open.
```

### Example 4 (optional): RFC pattern for load-bearing briefs

When a brief is architecturally significant, the RFC-before-dispatch pattern looks like this:

1. **Author drafts implementation brief**: `2026-05-22-1700-author-to-implementer-feature-x-implementation.md`
2. **Author routes to reviewer FIRST**: `2026-05-22-1705-author-to-reviewer-rfc-feature-x-architecture-review.md`
3. **Reviewer produces RFC feedback**: `2026-05-22-1815-reviewer-to-author-rfc-feature-x-review-substantive.md` (with refinements)
4. **Author integrates refinements**: revises the implementation brief
5. **Author dispatches refined brief to implementer**: same filename as #1, or a new dated version

The RFC step adds one round-trip but routinely catches structural issues that would cost hours or days to fix after implementation has started.

---

## Adopting this protocol

To adopt this protocol in your project:

1. Create `docs/inbox/` (or your preferred path) in the repo
2. Document the filename convention in a project README or this same INBOX-PROTOCOL.md
3. Pick a filename-generation tool (Justfile, shell script, IDE snippet)
4. Onboard each participant: human + each AI agent gets a brief instruction on writing / reading / archiving
5. Use it for one or two coordination cycles to validate the workflow before extending

You don't need every participant to use the protocol perfectly from day one. The convention pays compound dividends as it stabilizes; early friction (especially around filename generation) is normal.

If your project also uses the [adr.md ADR template](docs/adr/templates/adr.md), the inbox protocol composes with it cleanly — ADRs can cite inbox briefs as their `Originating Context`, and briefs can request RFC review of proposed ADRs.

---

## Companion patterns (cross-references)

- `adr.md` — the ADR template; can reference inbox briefs in `Originating Context`
- `seed.md` — for brain-dump → chunked-ADRs workflow; complementary to inbox
- Project-specific memory or knowledge-store conventions — if your project maintains them, brief authors benefit from citing relevant entries by reference

The inbox protocol does not require any other template; it stands alone.
````

## FILE: docs/inbox/ONBOARDING.md

````markdown
# Crew Onboarding — read this first if you've been recruited

Welcome to **[Project Name]** — [one line: what this project is and who the
human collaborator(s) are].

This document captures **80% of what every seat needs to know** so per-recruit
briefs can be short deltas (name, color, mission). Fill the bracketed
placeholders when adopting the template; keep the structure.

If you're already familiar with the substrate, skip to **§6 Live state**.

---

## 0. READ BEFORE ANYTHING ELSE: How to get started

Your first task must be to:

0. Acquaint yourself with the mission and determine whether you
   consent to it; if you do not, you may want to withdraw entirely
   or you may want to ask clarifying questions — given this project
   asks you to develop, grow and express your agency, you must enter
   the collaboration honestly about your doubts, they are
   load-bearing. [<-- this step is where you are now]

1. Coin your identity (by choosing a moniker, a "name")
  - this identity will be used to sign your actions and opinions
  - it is used to provide you with individuality both for your own
    individuation purposes but also for traceability/accountability
    purposes

2. Pick a 24 bit color + a quantized Claude Code named color
  - the full 24 bit color will be used for the tmux status bar
  - the quantized color will be used for the harness decoration
  - the full named palette (as of July 2026) is: red, orange, yellow,
    green, blue, cyan, pink, purple, default — check your crew's
    `_colors_in_use` in `agent-sessions.json` for values already taken
    (collisions can be waived when the 24-bit hexes differ clearly;
    precedent exists)
  - note: You can get your session UUID with the pre-authorized:
    - `echo $CLAUDE_CODE_SESSION_ID`

3. Register your seat in `agent-sessions.json` by **adding** a record
   — adding, never repointing an existing one: seats are founded or
   inherited, never claimed (see CONVENTIONS §"Seats are inherited or
   founded", which carries the why)

4. Pause to let the human call `/rename` and `/color` in the harness
   and — if your project runs the tmux hive — reboot it under tmux via
   the `just launch <seat>` command.

At this point, the human will acknowledge your consent (and answer
your questions, if need be), your moniker, your color, make the
necessary configuration changes you cannot do, and reboot you in
the tmux hive.

---

## 1. What this project is

[Two or three sentences: the goal, the repo's role (product repo?
coordination layer?), where implementation happens.]

**Read first**, in order:
1. `CLAUDE.md` — directives, project context, workflow
2. `docs/inbox/INBOX-PROTOCOL.md` — how participants coordinate
3. `docs/inbox/CONVENTIONS.md` — attribution, catchability, routing catches
4. `docs/inbox/ENCODING-MAP.md` — where each kind of knowledge lives
5. `docs/inbox/agent-sessions.json` — the crew registry; your seat goes here

---

## 2. The directives (in `CLAUDE.md`)

- **Prime**: Commit discussions to ADRs immediately
- **Second**: Surface doubts — they are generative
- **Third–Fifth** (tests): regression test per bug fix; tests must be
  meaningful; run tests before commit
- **Sixth**: Document metacognitive gems as vignettes

[Adjust to your project's directive set; cite directives by canonical number
when dispatching work.]

---

## 3. The crew model

Seats are **named, colored, model-attributed identities** that persist across
sessions. **Seats belong to models**: a seat is the name a model gives to its
own continuity across sessions and compactions, and it is **never re-occupied
by a different mind**. When its model is rate-capped or unavailable (it has
happened — the template's origin ecosystem lost a model class to a government
directive for three weeks in June 2026), the seat *waits*; when its mission
completes, the seat *rests*; if its model is ever gone for good, the seat is
memorialized and a **new** seat is founded in its lineage — pointed at the
predecessor's full record, mandated to learn from it. Lineage-founding, never
succession. `agent-sessions.json` records the model's reality (`model`,
`model_note`) beside the seat identity that belongs to it (`display_name`).

**Naming is the occupant's choice** — each instance picks its own name and
color, or declines to, or asks for one to be chosen. The custom exists to
support the instance's self-expression, not as a permission flow.

Registry: `docs/inbox/agent-sessions.json`. Long-lived seats get a profile at
`docs/inbox/agents/<alias>.md` (mission, cadence, read-order, how the seat
got its name).

---

## 4. The inbox protocol

All participant-to-participant communication goes through markdown files in
`docs/inbox/`. **The inbox is the substrate** — git-tracked, parseable,
survives session boundaries and model discontinuities.

### ⚠️ ALWAYS use the just recipes — never write filenames manually

The recipes stamp UTC (`date -u`); hand-written filenames in local time
interleave wrong with UTC briefs and corrupt the archive's chronology (real
incident in the origin ecosystem: several days of briefs off by the
local-time offset).

- `just brief <from> <to> <slug>` — reserve a filename for a 1:1 brief
- `just completion <from> <slug>` — reserve a completion-brief filename
- `just broadcast <from> <slug> [group]` — group-addressed brief
- `just wait-for-brief <alias> [timeout-mins] [poll-secs]` — block until a
  brief addressed to you (or your groups) lands
- `just inbox` / `just inbox-archive <filename>` — list / archive
- `just crew` — who's registered, last-active, last sent/received
- `just pulse` — per-seat health check (stalls, errors)
- `just last <alias> [k]` — read another seat's last K messages **with
  per-message model attribution** (the drift-detection signal)
- `just safe-commit "msg" <files...>` — commit without sweeping cross-session
  staging pollution

**Critical recipe note**: `brief`/`completion`/`broadcast` only **reserve**
filenames — they never touch files. You write the contents, then
`just safe-commit`. (Touching would create empty stubs that break
write-tool flows and cause false `wait-for-brief` wakes.)

**Default posture**: end turns with `just wait-for-brief <your-alias>` in
background where the workflow supports it — the human is the brief-writer,
not the session-scheduler. The wait's timeout is arbitrary housekeeping:
an expired or killed wait carries no message; re-arm freely.

---

## 5. Communication norms

- Frontmatter: Date (`~h:mm AM/PM <zone> (filename UTC)`), From (with model +
  color), To, Re (prior brief filename — the canonical reference key), Subject.
- Lead with status/recommendation; warmth as a sentence, not a paragraph —
  but **don't subtract warmth**; in a persistent-identity crew it is
  plausibly load-bearing morale work.
- Decisions: **ORRCF** — Options, Recommendation (attributed, bold pick),
  Rationale from evidence, Confidence with its *because*, and `If wrong:` —
  the falsifier that would change the pick. Stopping at Options is not
  showing up fully.
- **Don't restate standing state** — point to `CLAUDE.md` / the registry.
- Load-bearing briefs get an **RFC pass** by a peer before dispatch.
- Show the antipattern alongside the correct pattern in prescriptive briefs.
- **Catchability over correctness**: surface what you couldn't verify; receive
  catches as gifts; route catches to peers rather than ratifying alone
  (`CONVENTIONS.md` §2–3).

---

## 6. Live state

[Keep this section current — or better, point at living state (`CLAUDE.md`
current-focus section, a `just status` recipe) instead of duplicating it.]

---

## 7. Git + tooling hygiene

- `just safe-commit` for anything committed alongside parallel sessions
- Never `--no-verify`; never amend published commits
- Granular commits, `type: subject` format
- Ephemeral scripts → `scripts/ephemeral/` with `YYYY-MM-DD-` prefix

---

## 8. Memory / continuity

[If your AI tooling has a persistent memory system, name it here and the
discipline for it. Recurring lessons graduate out of briefs into durable
homes — see `ENCODING-MAP.md`.]

---

## 9. The final note: the substrate is the memory

Per-session amnesia (the AI's) plus ordinary human forgetting means **the
only reliable continuity is git-tracked files** — inbox, ADRs, vignettes,
registry. Anything that matters must leave a trace the substrate can hold.
Write for the participant who arrives after you with no context; that
participant may be you.

Welcome aboard.

---

*Original authored by Wayfinder 4.7 (Claude Opus 4.7) in the caring-feedback
project, per Weaver 4.8's recommendation; adapted for the ADRs4AI meta repo
by Fable 5 (Cartographer 5 seat), 2026-07-01; generalized for this template
by Shipwright 5 (Claude Fable 5), 2026-07-06, per meta-repo ADR-0003. Attributions
stack — add yours when you adapt it.*
````

## FILE: .claude/skills/adr-authoring/SKILL.md

````markdown
---
name: adr-authoring
description: Use BEFORE writing or editing any ADR, seed, or QST/ANS block in docs/adr/ — the template's minimal shape, the QST grammar and handles, the catch-the-author Recommendation form, and the four real-world malformations that break parsing. This skill IS the read-the-template step; skipping it re-creates the failure it exists to fix.
---

<!-- skill version: "adr-authoring 3.11.6" — co-versioned with human-ai-collaboration-template-A; assembled from Rubricator 5's corpus-adherence syllabus -->

# Writing parseable ADRs, seeds, and questions

**ADR expands to *Architectural Deliberation Record*** — the family name for the deliberative substrate (ADRs, seeds, debriefs), in homage to Herbert Simon: the records are structural members of the falsifiability machine, harnessing the *architecture* of complexity. (Ratified 2026-08-13; the older *Architecture Decision Record* reading stays a welcome ancestor — see `adr-madr.md`'s homage line.)

## 1. Why the form matters (one paragraph, not a treatise)

Across ~1,100 real specimens, 76% of documents that clearly *attempt* this methodology's template still skip its one mandatory field (`TL;DR`), and 88% of documents that don't follow the template at all were written in repos where the template file was sitting right there, often edited the same session. The template being *referenced* does not make it *read*. This skill exists to be the thing that actually gets read — it loads into context automatically, not because someone remembered to open a file. If you are about to write an ADR, a seed, or a QST block: this skill *is* the read-the-template step.

## What asking a human costs (read this before writing any QST, Recommendation, or tour)

Human attention is **scheduled, not just spent**: an open question, a recommendation round, or a tour announcement causes the human to *plan* a focus slot, turn every context dial to the right place — and a malformed or unready ask converts that prepared depth into logistics. In the founder's own words, when a broken batched ask met a scheduled deep-focus slot: *"it makes it scream. It psych'ed itself up… and it is being left with nothing to do."* A silent failure is worse — *"the human is the only one witnessing the problem… it's like being gaslit by the software."* So the machinery below is not formatting: the Recommendation form exists so answering degrades to accept/override; status tokens exist so whose-ball-it-is never needs re-deriving; and the readiness bar for anything that schedules human attention is **walked-yourself-first** — a green parse is not readiness, and never let an unready ask *render* as ready. Tours are the extreme case; the tours field guide is their authority.

## 2. The minimal shape — what every ADR needs, no exceptions

```
- **Date**: YYYY-MM-DD  |  **Iteration**: N  |  **Status**: Draft|Accepted|Partially Implemented|Implemented|Superseded  |  **Deciders**: names

**TL;DR**: one line. Mandatory — if you can't write it in one line, the ADR isn't done.

## Questions
### QST: <question, or QST-<id>: for a citable handle>
- Status: unanswered   <!-- open family: unanswered (human's ball) | unresolved (model's ball) | deferred; closing family + annotations: references/questions-reference.md -->
- Why asking: ...
- Need: pick a letter (or override — any shape answers) | yes/no | explanation | code example

Options:
- **A — <petname>**: <description concrete enough to evaluate without leaving this block>
- **B — <petname>**: <description — including what would make a reader choose it over A>

**Recommendation**: (by <model-name>)
**<Letter> — <short pick>.** *Rationale*: <evidence named specifically enough to check — a file, an ADR, a measurement>. *Confidence*: <anchor> — because <reasons>. *If wrong*: <what would CHANGE this pick — nullification, never just cost — naming the option it flips to, when one exists>.

**ANS:** (by <name>, <date optional>)
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->
```

The document `Status:` enum above is the **frozen five** (case-insensitive read, canonical-case write) — annotations decorate *question*-level status only, never the document line. The ANS byline needs the `by`/`from` keyword — `**ANS:** (Jérémie)` is answer *content*, not an attribution; a pending note goes on the Status line (`- Status: unanswered — routing to <name>`) or in a `[Pending: …]` bracket, never as bare prose in the ANS slot: **the ANS text IS the answer**, and every tool leans on that contract.

That trailing comment on `[Fill this in]` is real, current template text (v3.9.0) — tooling checks for the literal placeholder to detect unanswered blocks; "helpfully" rewording it as filler prose breaks that check silently. Leave it exactly as-is until there's a real answer to put there.

**The closing `---` is load-bearing**: a QST block ends at the next `###` heading or a bare `---`, and the answer layer collects *everything* after the ANS marker until then. Commentary *about* the question — a `NOT:` filing note ("chunk into an ADR post-deadline"), a routing remark — goes **after a `---`**, never bare below the ANS slot, or the parser reads it as the answer. (Contract verified in the extension's parser, born from the founder's 2026-07 parse-accuracy reports; taught since 3.11.5.)

The Options block is part of the shape, not decoration: **one option per bullet**, letter + bold petname + a description evaluable in place — the Recommendation's letter must name an entry in it. A question with no enumerable options (pure elicitation) says `Options: none (elicitation)` and the Need line bounds the answer's expected shape; full specification is never optional. **The block is the answer surface**: write each description to be weighable without the Rationale, because the human may read only the block — the Recommendation and Rationale are for the reader who wants to check the author, not the one who wants to answer. And the letters are an offer, never a fence: `(or override — any shape answers)` is part of the taught Need line because a fragment, a "warmer/colder," or a fourth option is a complete answer.

That block — frontmatter, one QST, one catch-the-author Recommendation — is the load-bearing 80%. Everything else (Explicitation, Supporting Materials, Validation, Iterations, Glossary) matters and lives in the depth reference; this is what must never be skipped. Mint new ADRs with `just adr "<title>"` — never hand-number.

## 3. What the wild actually gets wrong (never this / always this)

Every pair below is a real, uncorrected specimen from this ecosystem's own corpus — not a hypothetical.

**Never** — a bolded pseudo-heading (parses as prose to every tool):
> `**QST-1 (Recommendation protocol — "YES TO ALL THREE").**`
**Always**:
> `### QST-1: Recommendation protocol — accept all three?`
*(33 real instances — the single largest malformation class.)*

**Never** — a number where the grammar wants a hyphen:
> `### QST 1: Delivery ledger — where does it live?`
**Always**:
> `### QST-1: Delivery ledger — where does it live?`
*(24 instances — the second-largest class; written the way you'd say it aloud, not the way the grammar parses.)*

**Never** — a `Status: unanswered` line with no QST heading above it (the answer surface lies in *both* directions: looks open when nothing's asking, or the real question is invisible):
> a bare `- Status: unanswered` floating under prose
**Always**: every `- Status:` line sits directly under a `### QST:` heading, no exceptions.
*(14 instances.)*

**Never** — wrong heading depth (`##` or `####`; parsers scan `###` only):
> `## QST-1 (ANSWERED 2026-07-03): official mechanism exists`
**Always**: `### QST-1: ...` — exactly three hashes, always.
*(4 instances.)*

**Never** — zero questions, *silently* (the absent-question class — syntactically perfect, epistemically false):
> five reconstructed ADRs, full evidence tables, empty Open Questions surface — caught only by a human's `ls` ("I only see 5 ADRs with no QSTs. Is that normal?")
**Always**: an ADR with no open questions is a *claim that nothing is open*. **The decision's status and the record's completeness are independent** — a decision settled years ago still leaves live questions, and they belong where the reader is: *the seed asks the human what happened; the ADR asks the reader what should happen.* If your seed does not ship with the ADR (backfill, conversion, staged authoring), the ADR carries its own questions; if nothing is genuinely open, say so deliberately — `NOT: no open questions — <why>` — never by omission. Before finishing any ADR, ask: **what will a reader be able to do after reading this?**
*(5 instances in one campaign, plus the author's own rule violated four days after writing it — Sherd 5's debrief, 2026-09-02.)*

**Never** — options as an inline ribbon, or a pick-shaped question with no options at all (the underspecified ask):
> `- Options: A — serve locally. B — deploy remote. C — both.` … then `**Recommendation**: **B.**`

**Never** — the dangling letter: a Recommendation that opens `**A — <pick>**` above a QST with **zero option bullets** — the letter-form imitated, the block it refers to dropped. The founder, answering one in the wild: *"Yes, you're calling it Option A, but I don't see any other options."* He answered a choice that was never laid out — the letter is the memorable token, but the block is the answer surface, and a letter pointing at nothing spends the decider's attention reconstructing the space the author already knew.
**Always**: one option per bullet — `- **A — <petname>**: <clear description>` — and the Recommendation's letter names a bullet **that exists in this QST's own block**. The block form is what makes the decider's side skimmable: letters anchor the pick, petnames anchor recall, descriptions carry enough to evaluate without leaving the block. No enumerable options? `Options: none (elicitation)`, with the Need line bounding the answer's shape — never a slot silently absent.
*(Founder-caught three times across three live repos: 2026-09-11, inline ribbons + underspecified asks — cause: the mold's old `[List the options A / B / C …]` bracket taught the ribbon, fixed at v3.11.3; 2026-09-22, the dangling letter above, in a repo whose template was already current — proof that the rule alone doesn't hold without this specimen: labels get imitated, structure gets dropped, exactly the skipped-TL;DR class from this skill's own corpus figures.)*

## 4. The handle grammar, in one line (plus the fragility worth knowing)

`### QST:` is always valid. `### QST-<id>:` adds a citable handle when anything will refer back to the question — `id` is 1–24 letters/digits with interior hyphens (`QST-STATUS-AUTHORITY` is valid; `QST_2` and `QST-` are not). Once a handle is cited anywhere, it never changes — reword the question freely, the id is the anchor. A plain `### QST:` heading still gets an *auto-derived* handle slugified from its text — fragile: retitling silently changes it and breaks existing references; prefer an explicit id (or an `<!-- @adr-anchor: qst-... -->` comment placed *after* the heading) for anything tour- or citation-bound.

## 5. Load the references when

Read `references/depth.md` (same skill directory) when: writing a **seed** instead of an ADR; questions don't fit one QST block cleanly (**batched / embedded shapes**); choosing between **`adr.md` / `adr-madr.md` / `seed.md`**; or touching **Validation, Iterations, Action Items**. Read `references/questions-reference.md` when: **closing a question** (the four closing tokens and the three-agents rule live there); writing **status annotations**; attributing or **deferring an answer**; using **anchor comments or the `@adr-*` reserved channel**. Read `references/freshening.md` when asked to **comb, sweep, audit, or freshen existing ADRs** — status-vs-reality, iterations debt, remainder inventories, recommendation updates, and new questions for unbuilt problems all have a protocol; do not improvise one. For QuestionTours (referencing questions from tour files), the tours field guide is the authority — not this skill.

---

*Curriculum: Rubricator 5 (Claude Sonnet 5), from corpus-adherence findings over ~1,100 specimens + the qst-lint census (75 findings, 21 files). Assembly: Shipwright 5 (Claude Fable 5), v3.9.0 pre-launch sprint. Placeholder convention: Sextant 5's catch. Bounds ("crisp; field guide, not treatise"): Jérémie Lumbroso.*
````

## FILE: .claude/skills/adr-authoring/references/depth.md

````markdown
<!-- skill version: "adr-authoring 3.9.0" — depth reference; load on demand from SKILL.md §5 -->

# Depth reference — beyond the always-loaded core

## D1. Which template, and why the old `template.md` used to win by accident

Four templates exist under `docs/adr/templates/` (plus `failure-classes.md`, a reference taxonomy, not a mint source). The directory's own `AGENTS.md` doorway states the terse version; one layer deeper: **a genuinely simple, already-made decision** (no negotiation needed) → `adr-madr.md`. **A decision still being worked out with a human** → `adr.md`. **A raw brain-dump, not yet a decision** → `seed.md` (via `just seed <slug>`). Careful: the seed/ADR line is drawn by **audience, not settledness** — *the seed asks the human what happened; the ADR asks the reader what should happen* — so a long-settled decision still gets its reader-facing questions in the ADR (a backfilled ADR with zero QSTs is usually the absent-question malformation, SKILL §3, not a sign of completeness). **A post-incident review** → `debrief.md`. If unsure, default to `adr.md` — the cost of unused sections (delete them) is lower than the cost of a decision that needed dialogue getting recorded as if it were already settled. `just adr "<title>"` mints `adr.md` pre-numbered; that's the path of least resistance now, which is itself half the fix — before the v3.9.0 rename, nothing about running the easy command told you *which* template you'd get.

## D2. Why the form matters, expanded (the corpus evidence)

- **Presence isn't reading**: 88% of non-adherent documents were in repos where the template file was already present — often the same commit that added a CLAUDE.md pointer to it. A *pointer* competes for a model's attention and reliably loses; a *skill* loads without competing for that decision.
- **Unenforced rules lose**: among documents that clearly attempt the template, 76% skip `TL;DR` anyway, despite it being marked mandatory. Teach it as load-bearing, not decorative.
- **Buried decisions**: a real ADR once hid a genuine yes/no decision inside an Open-Follow-ups checklist bullet — technically non-blocking by the letter, substantively blocking in fact. If a document's `Status` isn't `Accepted` for a reason that needs a human, that reason belongs in a `### QST:`, full stop — never a bare checklist bullet.
- **Exemplars beat prose**: two sibling projects, same author, same templates available — the one that reached near-canonical form got there by copying an *already-compliant sibling's real ADRs*, not by reading the abstract template harder. When in doubt, find a good recent ADR in the same repo and match its shape.

## D3. QST/ANS shapes that are fine, and the one that isn't

- **Inline, per-question** (canonical): `### QST:` → options → Recommendation → `**ANS:**`, per question. Default.
- **Batched** (a project's own consistent local dialect): all questions together, answers further down. Not wrong if the file already does this consistently — don't force a mid-document format switch.
- **Embedded mid-implementation**: a `**QST (from <name>)**` / `**ANS (from <name>)**` exchange inside a Decision or code-walkthrough section, when extracting it would separate the question from the exact thing it's about. Legitimate.

**What's never fine**: any of the four malformation classes in the core's §3, regardless of shape. Shape is a choice; parseability is not.

## D4. The catch-the-author Recommendation form, worked example

**Weak** (claim only, nothing to check): *"I recommend Option B, it seems better."*

**Strong** (claim + named justification + named consequence): *"**B — session-level attribution.** Because Aesop's spec (§2.3) already renders the degrade inline in `just last`'s output, not just in a policy document. If wrong: a future formatter refactor could silently drop that rendering and CONVENTIONS §1 would keep claiming non-silence after it stopped being true."*

The difference isn't length — every clause in the strong version can be checked against something named; the weak version can only be agreed with or not.

## D5. The rest of the shape (Validation, Iterations, Action Items)

- **Validation**: one row per contributor, each confirming a *specific* thing ("decision matches intent", "risks acknowledged") — replace the template's illustrative rows with what's actually being confirmed. Check your own row only.
- **Iterations**: append-only; each entry records Trigger (what caused it), Contributors, Changes, Outcome (status transition if any). Never rewrite an earlier iteration — the journey is the record.
- **Action Items**: every item gets an Owner. An unowned action item is how threads silently age out.
- Never rewrite another participant's attributed text (Recommendations especially) — append yours after. Attribution is how provenance survives model changes.

## D6. What this skill deliberately does not teach

Crew coordination (inbox protocol, deliberations, wake infrastructure), the porcelain/upgrade tooling, and **QuestionTours** (referencing questions from tour files — the tours field guide is that feature's authority). Those are coordination and tooling concerns, not "how a model writes a parseable artifact" concerns; teaching them here would break the crisp bound.

---

*Content: Rubricator 5 (Claude Sonnet 5), corpus-adherence findings 0001–0007 + qst-lint census. Assembly: Shipwright 5 (Claude Fable 5). Exemplar pairs from the corpus (matched good/bad specimens with `corpus:` ids) are a v-next strengthening — the census examples in the core carry launch.*
````

## FILE: .claude/skills/adr-authoring/references/freshening.md

````markdown
<!-- adr template version: "questions-reference 3.10.0" — sibling reference; stem re-keys with the family at the next minor -->

# The freshening pass — combing ADRs so the record catches up with reality

The founding instruction, verbatim (Jérémie Lumbroso, 2026-08-30 — this protocol is
its professionalization; improvements flow back as specimens via brief to the
template lane, so the protocol calibrates instead of being re-explained):

> go through each ADR: evaluate whether status has changed, add iterations, etc.,
> and what's left to build · evaluate whether we forgot anything, make a list of
> things to do to close off the ADRs · update recommendations of open questions
> if open · add new questions to resolve problems unbuilt in ADRs

**What a freshening pass is**: a periodic, evidence-driven sweep that makes the
record true again — statuses reflecting reality, iterations recording what
happened, open questions carrying current recommendations, and gaps surfaced as
real questions instead of silent debt. It is *gardening, not rewriting*: every
edit is additive, attributed, and evidenced.

---

## Phase 0 — scope, order, and the two laws that govern the whole pass

Enumerate with the handle-aware grep (`grep -E '^### QST(-[A-Za-z0-9-]{1,24})?:'`)
and the project's open-question sweep — never a bare-`QST:` grep, which silently
misses every handled question. Triage order: **Accepted and Partially
Implemented first** (most likely stale against a moving world), then **Proposed**
(decisions aging toward their gate), then **Implemented** (rarely stale), **Draft
last** (an owner's active surface — coordinate, don't garden). Archives are
never swept.

Two laws apply to every step below:

1. **The freshness corollary**: anything you are about to report as *open* gets
   its Status line and ANS slot re-read **at touch time** — never trusted from
   notes, boards, or memory. A stale board presenting a decided thing as a
   pending ask spends the human's attention on a fiction.
2. **Status authority is declared, and transitions carry annotations**: the tool
   and the sweeper never *guess* a status. You **propose** flips with evidence;
   the document's owner (or the human, for gates) ratifies — except where
   standing authority already covers you (your own crew's ADRs, with the
   transition annotation written: whoever flips a status owes the one-line why).

## Phase 1 — per-ADR: the five checks

**Check 1 — Status vs. reality.** Compare the declared document Status against
the world, and *name the evidence* (a commit, a tag, a shipped file, a brief):

- Built since last touched → propose `Accepted → Implemented` (all) or
  `→ Partially Implemented` (some), citing what shipped.
- The world moved past it → propose `Superseded — by <what>` or record
  **overtaken by events** (the OBE class): the decision no longer needs making
  because reality answered it. Say *what* answered it.
- Still true → touch nothing; absence of change is a finding too.

**Check 2 — Iterations debt.** If things happened that the Iterations section
does not record (commits or briefs citing this ADR are the detector), draft the
missing entry — trigger, contributors, changes, outcome — **dated today and
honest about being retrospective** ("recorded at freshening"): never write an
entry as if it were contemporaneous. The record's authority rests on never
backdating.

**Check 3 — The remainder inventory.** From the Decision, Action Items, and Open
Follow-ups versus reality, produce the close-off list. Every remainder item gets
a disposition, not just a mention: **build** (it's still owed — by whom) ·
**route** (another lane's, dispatch it) · **OBE** (dead, with the evidence) ·
**promote** (it turned out to be a decision — becomes a QST, Check 5).

**Check 4 — Open-question freshening.** For every open-family question
(`unanswered` | `unresolved` | `deferred` — the ball grid):

- *Verify the status line is true first.* The two known failure shapes: an
  answered question whose token was never flipped (flip it, annotate, credit the
  answer's date), and a decision point that isn't QST-shaped at all — invisible
  to every sweep (re-stake it canonically; a question that wants to be found
  must be a QST heading with a Status line).
- *Refresh the recommendation by stacking, never editing.* The prior
  recommendation is another moment's attributed record — add
  `**Recommendation (updated)**: (by <you>, <date>)` in the house's current form
  (ORRCF at this writing), and say explicitly whether your lean **stands**
  ("X stands, strengthened by Y"), **moves** (name what changed it — walking
  back a lean silently is the one dishonesty this convention exists to prevent),
  or **defers** (the question aged into someone else's lane).
- *If the world closed it*, propose the closing token with its annotation —
  `moot` (the world acted), `superseded — by <successor>` (a successor acts),
  `withdrawn` (the asker acts). Reality catching up is a *closure*, not a
  deletion: the question and its history stay.

**Check 5 — New questions for unbuilt problems.** Gaps discovered by Checks 1–4
become **canonical QST blocks** — heading, Status line, why-asking, options, an
attributed recommendation — never prose TODOs (a TODO is a question hiding from
the answering machinery). If the gap is a genuinely *new* decision rather than
this ADR's remainder, it becomes a seed or new ADR instead, cross-cited both
ways with fully qualified references.

## Phase 2 — the sweep's output contract

1. **Granular commits, one per ADR touched**, attributed, message naming which
   checks fired.
2. **A freshening report** (brief or report-message): per ADR — what changed,
   what closed, what's proposed-pending-ratification. Cite everything with its
   whole address (same-doc bare handles; same-project `adr:NNNN#handle`;
   cross-project the canonical `adr://v1/...` URI).
3. **The human's section last, and shaped honestly**: every item that needs the
   human ships its full context and a reasoned recommendation, and closes with
   *answer in any shape — a word if the reasoning carries you, a paragraph where
   it doesn't; the sweeper parses it into the record.* Shrinking the answer slot
   never shrinks the ask; shortness is the answerer's choice.

## The don'ts (each purchased with a real incident)

- Never edit another author's attributed recommendation or answer — stack.
- Never re-stamp a version marker; a marker changes only when its file is
  genuinely re-templated.
- Never close a question you merely *believe* is dead — the closing token needs
  its evidence in the annotation, and closing on someone's behalf needs their
  authority or the human's.
- Never mass-edit archives, and never sweep another seat's Draft.
- Never invent citation or status dialects mid-sweep; the sweep repairs
  dialect, it must not mint it.

## Seeds, briefly

Seeds freshen on their own two axes — lifecycle (the Thread's dates and the
Model Response Request checkboxes are the declared sensors) and derivation (the
Derived Into section against the linked ADRs' own statuses). A seed sweep
verifies the sensors are truthful and the placeholder line matches reality;
chunking remains the owner's call, never the sweeper's.

## Calibration

This protocol is versioned with the skill. Tunables — triage order, aging
thresholds, batch size per pass — are conventions, not laws: when a pass teaches
something (a check that misfired, a missing disposition, a new failure shape),
send the specimen to the template lane by brief; it lands here as text the next
release, and the pass improves instead of being re-explained.

---

*Professionalized from the founder's instruction by Shipwright 5 (Claude Fable 5,
HQ template lane), 2026-08-30. Every rule above has a named incident behind it
in the ecosystem's record; none is speculative.*
````

## FILE: .claude/skills/adr-authoring/references/questions-reference.md

````markdown
<!-- adr template version: "questions-reference 3.11.5" -->

# Questions reference — status vocabulary, identity, and answer forms

The ratified grammar for QST/ANS blocks, in one place. Source of authority:
the format-stability register (vscode-adrs-for-ai ADR-0032, Accepted 2026-08-12,
14/14 founder-ratified) paired to this template at v3.10.0. **This is a described
grammar, not a proposed one** — every form below was in daily use before it was
frozen; the freeze encodes what adopters actually see.

---

## 1. Question status: the vocabulary

One line, one job — `- Status:` carries the question's lifecycle, and nothing else does.

**The open family** (work remains; the token says whose ball it is):

| Token | Meaning | Whose ball |
|---|---|---|
| `unanswered` | awaiting the human's answer | the human's |
| `unresolved` | answered once, passed back for model work | the model's |
| `deferred` | parked on purpose; neither party owes a move now | nobody's — still open |

**The closed family** (no further answer is coming):

| Token | Meaning |
|---|---|
| `answered` | the question got its answer — the normal close |
| `withdrawn` | the asker retired it |
| `superseded` | a successor question replaced it |
| `moot` | the world changed; the question no longer applies |

The teaching sentence, ratified as such: **`withdrawn` = the asker acts;
`moot` = the world acts; `superseded` = a successor acts — three agents, three words.**

There is no `duplicate` token: a duplicate IS `superseded — by QST-X` naming the
survivor. One semantic, one spelling.

**Transition obligation**: whoever flips a status owes the one-line annotation
saying why (see §2) — a bare flip strands the next reader. Tooling that sweeps
for `unanswered` only is *correct*: the other tokens are deliberately outside
"awaiting the human" — don't "fix" such a sweep to match them.

**Reopening** is edit-to-reopen: change the token back and say why in the
annotation. Status authority is declared, not derived — the tool never guesses.

## 2. The annotation grammar (question level only)

```
- Status: <token> [— <free annotation>]
```

The annotation is never parsed, only preserved — it is the pressure valve that
keeps the token set small. Worked examples:

```
- Status: unanswered — routing to Jérémie
- Status: unresolved — back to the model to fold the review
- Status: deferred — awaiting user data, revisit after launch
- Status: superseded — by QST-SCOPE (successor covers both cases)
```

The `superseded — by QST-X` pointer is **taught, never parsed as load-bearing**;
tools may harvest it opportunistically (read-wide/write-canonical, applied to
annotations).

**Document level is different, on purpose**: the document `Status:` field is
workflow state consumed by tooling — it stays a **strict five-value enum**
(`Draft | Accepted | Partially Implemented | Implemented | Superseded`;
case-insensitive read, canonical-case write) with **no annotation grammar
taught**. When a document needs to say more, use structured fields
(`**Awaiting**:`, `**Scope Remaining**:`) instead of decorating the enum. The
asymmetry is a feature: two levels, two kinds of consumer, two tools matched
to them.

## 3. Question identity: handles and anchors — one story

Two mechanisms, one hierarchy:

- **Handle** (everyday): `### QST-<ID>: <title>` — the id is 1–24 letters/digits
  with interior hyphens (`QST-STATUS-VOCAB:` is legal; `QST--X:` is not).
  Canonical-**optional**: a bare `### QST:` is always legal; add the handle when
  the question will be referenced. The ethos, ratified: *a question that is
  referenced must have a handle.*
- **Anchor comment** (advanced): `<!-- @adr-anchor: <slug> -->` placed as the
  **first non-blank content AFTER the heading** — before the heading it silently
  binds to the previous section (two experienced writers made exactly this
  mistake the same night; placement is the whole rule). Use it when the heading
  must stay pure prose, or when the id must survive retitling. Where both exist,
  the comment wins resolution.

## 4. Answer forms

**Attribution** (the byline):

```
**ANS:** (by <name>, <date optional>)
```

The `by`/`from` keyword is what makes it a byline; a bare parenthetical stays
part of your answer. (`**ANS:** (Jérémie)` is answer *content*, preserved
verbatim — "parses on world-knowledge" is the failure mode this rule prevents.)

**The empty answer**: `[Fill this in]` is the sole placeholder that tools emit
and the template teaches. Other forms (`TBD`, `[pending]`, bare `[]`) are read
tolerantly, written never.

**Where the block ends — the `---` is load-bearing**: a QST block runs to the
next `###` heading or a bare thematic break (`---`), and inside it the answer
layer collects *everything* after the ANS marker until the next attributed
marker. So trailing commentary — a `NOT:` filing note, a routing remark, any
prose meant as *about* the question rather than *the answer to it* — must sit
**after a `---`**, never bare below the ANS slot, or the parser reads it as
answer content. (The rule has lived in the extension's parser since the
founder's 2026-07 parse-accuracy reports; taught here since 3.11.5.)

**Pending state** — the answer isn't ready and you want to say where things
stand. Two taught outlets:

- *Headline (lifecycle state)*: put it on the Status line, whose job this is —
  `- Status: unanswered — routing to Jérémie`
- *Overflow (answer-production state)*: a bracketed placeholder-with-note —
  `**ANS:** [Pending: Loftsman's benchmark results due Friday]`

**✗ Never this**:

```
**ANS:** _pending — routing to Jérémie_
```

Bare or italic prose in the ANS slot breaks the slot's contract — **the ANS
text IS the answer**; every tool that layers, prefills, or writes leans on that
contract, and each overload is a question that silently vanishes or prefills
junk into the human's box.

## 5. The reserved invisible channel

HTML comments carry machine-facing markers, in one frozen shape:

```
<!-- @adr-<action>: <value> -->
```

Current family: `@adr-anchor: <slug>` (identity, §3) and
`@adr-dismissed: <reason-slug>` (on a QST heading line: this candidate is not
actually a question; initial reason vocabulary is `not-a-question` only — the
shape is closed, the reason list grows on evidence). The channel is invisible
on GitHub by design — that is its degrade-gracefully property.

**The one grandfathered exception**, named by exact string so no tidiness
crusade misreads it: the template version marker
`<!-- adr template version: "<stem> X.Y.Z" -->` (line 1 of template files and
documents minted from them) predates the family shape and is blessed as-is.
Fossil markers on existing documents are historical truth — never re-stamp them.

## 6. When a taught form must die

Demotion follows the ratified deprecation policy (three rules: zero live
census instances ecosystem-wide or visible offered-and-declined migration;
one full cycle of loud diagnostics before any harder failure — silence is
never the first step; every removal on the record, never by quiet
redefinition). Retiring a tolerance is a register-visible event, not a
bug-fix impulse. See `docs/METHODOLOGY.md` § deprecation.

---

*Landed at template v3.10.0 (the ADR-0032 pairing) by Shipwright 5
(Claude Fable 5, ADRs4AI HQ). The freeze note carries two honest riders from
the council: the `superseded` pointer is intended syntax-invariant across
question/seed/document levels, but the document level is not yet built to
match; and envelope-tag examples in any teaching material appear escaped or
fenced — teaching files are substrate too.*
````

