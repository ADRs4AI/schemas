#!/usr/bin/env python3
"""test_roundtrip.py — the fence-safety PROOF (ADR-0043 It-3's binding condition).

Builds a bundle from a real source tree, extracts every file back out, and
byte-compares each against its original. Exits nonzero on any mismatch.
The publisher's workflow runs this BEFORE any bundle is committed; a bundle
that cannot round-trip never publishes.

Usage: test_roundtrip.py --source DIR --tag TAG --scope scope.json
"""
import argparse, filecmp, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CONCAT = os.path.join(HERE, "concat.py")

ap = argparse.ArgumentParser()
ap.add_argument("--source", required=True)
ap.add_argument("--tag", required=True)
ap.add_argument("--scope", required=True)
a = ap.parse_args()

with tempfile.TemporaryDirectory() as tmp:
    out_dir = os.path.join(tmp, "out")
    subprocess.run([sys.executable, CONCAT, "build", "--source", a.source,
                    "--tag", a.tag, "--scope", a.scope, "--out-dir", out_dir],
                   check=True)
    bundle = os.path.join(out_dir, f"template-{a.tag}.md")
    ex_dir = os.path.join(tmp, "extracted")
    subprocess.run([sys.executable, CONCAT, "extract", "--bundle", bundle,
                    "--out-dir", ex_dir], check=True)

    import json
    files = json.load(open(os.path.join(out_dir, "index.json")))["files"]
    bad = []
    for rel in files:
        src, got = os.path.join(a.source, rel), os.path.join(ex_dir, rel)
        if not os.path.isfile(got):
            bad.append((rel, "MISSING from extraction")); continue
        if not filecmp.cmp(src, got, shallow=False):
            bad.append((rel, "BYTE MISMATCH"))
    if bad:
        for rel, why in bad:
            print(f"✗ {rel}: {why}", file=sys.stderr)
        sys.exit(f"round-trip FAILED on {len(bad)}/{len(files)} files — "
                 "fence safety is not proven; refusing to publish")
    print(f"✓ round-trip proven: {len(files)}/{len(files)} files byte-identical "
          f"through build→extract")
