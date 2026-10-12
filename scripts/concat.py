#!/usr/bin/env python3
"""concat.py — the schemas publisher's concatenator (ADR-0043, HQ).

Turns a template checkout at a released tag into ONE flat, model-native
markdown bundle: provenance header, table of contents, then every
teaching-corpus file as `## FILE: <path>` followed by its content in a
collision-safe fence.

FENCE SAFETY IS A PROVEN PROPERTY, NOT A CLAIM (the founder's one binding
condition, ADR-0043 It-3): the fence length is computed as one longer than
the longest backtick run found in ANY included file, so no content line can
ever close a fence early. scripts/test_roundtrip.py extracts every file back
out of the bundle and byte-compares against the sources before any publish.

Pattern precedent, honored: Jérémie Lumbroso's pre-Repomix concatenator —
https://gist.github.com/jlumbroso/f9c18f116e3fa5250bbd388245b10f1d

Stdlib only. Two modes:
  build   --source DIR --tag TAG --scope scope.json --out-dir DIR
          [--repo-url URL] [--source-sha SHA]
  extract --bundle FILE --out-dir DIR        (the round-trip test's instrument)
"""
import argparse, datetime, glob, json, os, re, sys

MISSION = ("one-file access to the whole picture, so a model that encounters "
           "one of the subfiles can automatically, painlessly recover the full "
           "context")  # the founder's sentence, ADR-0043 It-3 — the mirror's purpose
CONCEPT_DOI = "10.5281/zenodo.23303469"
FILE_HEADER_RE = re.compile(r"^## FILE: (.+?)( \(no-final-newline\))?$")


def gather(source, scope_path):
    scope = json.load(open(scope_path))
    excluded = set()
    for pat in scope.get("exclude", []):
        for p in glob.glob(os.path.join(source, pat)):
            excluded.add(os.path.relpath(p, source))
    seen, ordered = set(), []
    for pat in scope["include"]:
        hits = sorted(glob.glob(os.path.join(source, pat)))
        for p in hits:
            rel = os.path.relpath(p, source)
            if rel in excluded or rel in seen or not os.path.isfile(p):
                continue
            seen.add(rel)
            ordered.append(rel)
    return ordered


def longest_backtick_run(text):
    runs = re.findall(r"`+", text)
    return max((len(r) for r in runs), default=0)


def lang_of(path):
    ext = os.path.splitext(path)[1].lstrip(".")
    return {"md": "markdown", "yaml": "yaml", "yml": "yaml", "json": "json",
            "": "text"}.get(ext, ext or "text")


def build(args):
    files = gather(args.source, args.scope)
    if not files:
        sys.exit("concat: scope matched no files — refusing to publish emptiness")
    contents, max_run = {}, 0
    for rel in files:
        raw = open(os.path.join(args.source, rel), "rb").read().decode("utf-8")
        contents[rel] = raw
        max_run = max(max_run, longest_backtick_run(raw))
    fence = "`" * max(max_run + 1, 4)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    repo = args.repo_url or "https://github.com/ADRs4AI/human-ai-collaboration-template-A"

    out = []
    out.append(f"# ADRs for AI: Human-AI Collaboration Template A — teaching bundle, {args.tag}\n")
    out.append(f"""
> **What this is**: the complete teaching corpus of the ADRs4AI methodology,
> concatenated into one fetchable file — {MISSION}.
>
> - **Source**: {repo} at tag `{args.tag}`{f" (commit `{args.source_sha}`)" if args.source_sha else ""}
> - **Built**: {now} by the schemas publisher (https://github.com/ADRs4AI/schemas)
> - **Cite the living work**: concept DOI `{CONCEPT_DOI}` (always resolves to the
>   latest archived release); pin a version DOI only for reproducibility claims.
> - **License**: MIT — the full text travels in this bundle (see `LICENSE` below);
>   this bundle is a substantial portion and the notice rides with it.
> - **Immutability vow**: the versioned URL serving this file never changes
>   content after publication; `latest/` is the one mutable alias.
> - **Format**: every file appears as `## FILE: <path>` followed by its exact
>   content inside a {len(fence)}-backtick fence — computed one longer than the
>   longest backtick run in any included file, so extraction is unambiguous.
>   (Pattern precedent: the maintainer's own pre-Repomix concatenator, 2023 —
>   https://gist.github.com/jlumbroso/f9c18f116e3fa5250bbd388245b10f1d)
""".strip() + "\n")
    out.append("\n## CONTENTS\n")
    for rel in files:
        out.append(f"- `{rel}` ({len(contents[rel].encode('utf-8'))} bytes)")
    out.append("\n---\n")
    for rel in files:
        raw = contents[rel]
        marker = "" if raw.endswith("\n") else " (no-final-newline)"
        body = raw if raw.endswith("\n") else raw + "\n"
        out.append(f"## FILE: {rel}{marker}\n")
        out.append(f"{fence}{lang_of(rel)}")
        out.append(body.rstrip("\n"))
        out.append(f"{fence}\n")
    bundle = "\n".join(out) + "\n"

    os.makedirs(args.out_dir, exist_ok=True)
    bundle_path = os.path.join(args.out_dir, f"template-{args.tag}.md")
    open(bundle_path, "w", encoding="utf-8").write(bundle)
    index = {
        "what": "ADRs4AI teaching bundle — machine index",
        "tag": args.tag, "built": now, "source": repo,
        "concept_doi": CONCEPT_DOI, "bundle": os.path.basename(bundle_path),
        "files": files, "fence_length": len(fence),
    }
    open(os.path.join(args.out_dir, "index.json"), "w").write(
        json.dumps(index, indent=2) + "\n")
    print(f"built {bundle_path} ({len(bundle.encode('utf-8'))} bytes, "
          f"{len(files)} files, fence={len(fence)})")


def extract(args):
    lines = open(args.bundle, encoding="utf-8").read().split("\n")
    i, current, marker_flag, fence, buf = 0, None, False, None, []
    wrote = 0
    while i < len(lines):
        m = FILE_HEADER_RE.match(lines[i])
        if m:
            current, marker_flag = m.group(1), bool(m.group(2))
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                i += 1
            fence = re.match(r"^`+", lines[i]).group(0)
            i += 1
            buf = []
            while i < len(lines) and lines[i] != fence:
                buf.append(lines[i]); i += 1
            content = "\n".join(buf) + "\n"
            if marker_flag:
                content = content[:-1]
            dest = os.path.join(args.out_dir, current)
            os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
            open(dest, "w", encoding="utf-8").write(content)
            wrote += 1
        i += 1
    print(f"extracted {wrote} files to {args.out_dir}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    b = sub.add_parser("build")
    b.add_argument("--source", required=True); b.add_argument("--tag", required=True)
    b.add_argument("--scope", required=True); b.add_argument("--out-dir", required=True)
    b.add_argument("--repo-url"); b.add_argument("--source-sha")
    e = sub.add_parser("extract")
    e.add_argument("--bundle", required=True); e.add_argument("--out-dir", required=True)
    a = ap.parse_args()
    (build if a.mode == "build" else extract)(a)
