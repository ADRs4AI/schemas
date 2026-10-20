#!/usr/bin/env python3
"""test_trailing_newlines.py — regression for the trailing-newline byte-loss class.

Bug (2026-10-20, caught by the round-trip gate ON RELEASE DAY, v3.12.0): the
bundle header's one-bit "(no-final-newline)" marker could only say "zero or
one" trailing newline, while build rstrip'd them ALL — so any file ending in a
blank line (the Apache LICENSE ends ".\n\n") extracted one byte short and the
publisher rightly refused to publish. Fix: the header now carries the COUNT
("(trailing-newlines: N)", absent = exactly one), and extract reconstructs it.
This test pins every class the one-bit marker could not represent, plus the
legacy marker (pre-v3.12 bundles remain extractable).

Run: python3 scripts/test_trailing_newlines.py   (stdlib only, exit 0 = pass)
"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CONCAT = os.path.join(HERE, "concat.py")

CASES = {  # filename -> exact bytes (all .md so one include glob covers them)
    "one-newline.md": b"ordinary file\n",
    "no-newline.md": b"no final newline",
    "blank-line-end.md": b"ends with a blank line\n\n",          # the LICENSE class
    "three-trailing.md": b"three trailing\n\n\n",
    "only-newlines.md": b"\n\n",
    "empty.md": b"",
    "backticks.md": b"has a ```` four-run of backticks\n",       # fence must grow past it
}

with tempfile.TemporaryDirectory() as tmp:
    src = os.path.join(tmp, "src")
    os.makedirs(src)
    for name, data in CASES.items():
        open(os.path.join(src, name), "wb").write(data)
    scope = os.path.join(tmp, "scope.json")
    json.dump({"include": ["*.md"], "exclude": []}, open(scope, "w"))

    out = os.path.join(tmp, "out")
    subprocess.run([sys.executable, CONCAT, "build", "--source", src,
                    "--tag", "vtest", "--scope", scope, "--out-dir", out],
                   check=True, capture_output=True)
    ex = os.path.join(tmp, "ex")
    subprocess.run([sys.executable, CONCAT, "extract", "--bundle",
                    os.path.join(out, "template-vtest.md"), "--out-dir", ex],
                   check=True, capture_output=True)

    bad = []
    for name, data in CASES.items():
        got = open(os.path.join(ex, name), "rb").read()
        if got != data:
            bad.append(f"{name}: want {data!r}, got {got!r}")

    # Legacy decode: a pre-v3.12 bundle's one-bit marker still extracts.
    legacy = ("## FILE: legacy.md (no-final-newline)\n\n"
              "````markdown\nold bundle, no final newline\n````\n")
    lb = os.path.join(tmp, "legacy-bundle.md")
    open(lb, "w").write(legacy)
    lex = os.path.join(tmp, "lex")
    subprocess.run([sys.executable, CONCAT, "extract", "--bundle", lb,
                    "--out-dir", lex], check=True, capture_output=True)
    lgot = open(os.path.join(lex, "legacy.md"), "rb").read()
    if lgot != b"old bundle, no final newline":
        bad.append(f"legacy marker: got {lgot!r}")

    if bad:
        print("✗ trailing-newline regression FAILED:", file=sys.stderr)
        for b in bad:
            print(f"  {b}", file=sys.stderr)
        sys.exit(1)
    print(f"✓ trailing-newline classes round-trip: {len(CASES)} cases + legacy marker")
