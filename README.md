# schemas — model-native teaching bundles of the ADRs4AI methodology

Each released version of [human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
is transformed into **one flat, fetchable markdown bundle** — the whole teaching
corpus (CLAUDE.md, the molds, the skills, the protocols, the LICENSE) behind a
single URL, so any model anywhere can learn the methodology in one fetch:

> *one-file access to the whole picture, so a model that encounters one of the
> subfiles can automatically, painlessly recover the full context.*

**Served at `https://schemas.adrs.systems`:**

| URL | What |
|---|---|
| [`/v1/template/latest/template-latest.md`](https://schemas.adrs.systems/v1/template/latest/template-latest.md) | the newest bundle (mutable alias, like a concept DOI) |
| [`/v1/template/<tag>/template-<tag>.md`](https://schemas.adrs.systems/v1/template/v3.11.6/template-v3.11.6.md) | immutable, per released version |
| [`/llms.txt`](https://schemas.adrs.systems/llms.txt) | the machine index |

**The vows** (ADR-0043 at ADRs4AI HQ is the record):
- **Immutability**: a versioned path never changes content after publication —
  this repo's append-only git history is the audit.
- **Fence safety is proven, not claimed**: every publish runs a round-trip test
  (build → extract → byte-compare all files) before anything lands; the fence
  is computed longer than the longest backtick run in the corpus.
- **This is a publisher, not a mirror**: releases are *transformed* into
  bundles (the word "mirror" was ruled out on contract-truth — Mint №88). It
  consumes the template only through its public GitHub Releases, the same door
  strangers use.
- **Scope is a reviewable manifest** ([`scope.json`](scope.json)), never vibes;
  the Apache-2.0 `LICENSE` and `NOTICE` ride in every bundle (§4's redistribution
  terms, honored by construction).

Builds trigger on each template release (`repository_dispatch`) or manually
(`workflow_dispatch` with a tag). Pattern precedent, honored: the maintainer's
own pre-Repomix concatenator
([gist](https://gist.github.com/jlumbroso/f9c18f116e3fa5250bbd388245b10f1d)).

Part of the [ADRs4AI](https://github.com/ADRs4AI) ecosystem · Apache-2.0
