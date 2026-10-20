#!/usr/bin/env python3
"""update_llms_txt.py — regenerate the root llms.txt index from v1/template/*.

Scans published versions (immutable dirs) and rewrites the machine index so
every publish keeps the front door current. Stdlib only.
"""
import os, re

BASE = "https://schemas.adrs.systems"
vers = sorted(
    (d for d in os.listdir("v1/template")
     if d != "latest" and os.path.isdir(os.path.join("v1/template", d))),
    key=lambda v: [int(x) for x in re.findall(r"\d+", v)], reverse=True)

lines = [
    "# ADRs for AI (ADRs4AI) — teaching bundles",
    "",
    "> Model-native teaching bundles of the ADRs4AI methodology: each released",
    "> version of the canonical human-AI collaboration template, concatenated into",
    "> one fetchable markdown file — one-file access to the whole picture, so a",
    "> model that encounters one of the subfiles can automatically, painlessly",
    "> recover the full context.",
    "",
    "## The bundle",
    "",
    f"- [Latest (mutable alias, re-resolved at use)]({BASE}/v1/template/latest/template-latest.md)",
]
for v in vers:
    lines.append(f"- [{v} (immutable)]({BASE}/v1/template/{v}/template-{v}.md)")
lines += [
    "",
    "## Provenance",
    "",
    "- Source: https://github.com/ADRs4AI/human-ai-collaboration-template-A (Apache-2.0; the license and NOTICE travel in every bundle)",
    "- Cite the living work: concept DOI 10.5281/zenodo.23303469",
    "- Publisher: https://github.com/ADRs4AI/schemas — versioned URLs are immutable after publication; `latest/` is the one mutable alias",
    "",
]
open("llms.txt", "w").write("\n".join(lines))
print(f"llms.txt: {len(vers)} version(s) indexed")
