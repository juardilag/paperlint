#!/usr/bin/env python3
"""Record an author's own edits as before/after pairs.

    learn.py PAPER.tex [--rev HEAD] [--who NAME] [--dry-run]

Compares PAPER.tex with its version at git revision REV (default HEAD), sentence by
sentence, and appends every changed passage to `author_edits.md` next to the paper.
Run it after the author edited the text by hand and before Claude edits it again, so
the "before" is paperlint's text and the "after" is the author's. These pairs are the
only "accepted" versions paperlint imitates.
"""
from __future__ import annotations

import argparse
import datetime
import difflib
import re
import subprocess
import sys
from pathlib import Path


def sentences(tex: str) -> list[str]:
    tex = re.sub(r"(?<!\\)%.*", "", tex)
    out = []
    for para in re.split(r"\n\s*\n", tex):
        para = re.sub(r"\s+", " ", para).strip()
        if para:
            out += [s for s in re.split(r"(?<=[.?!])\s+(?=[A-Z\\])", para) if s]
    return out


def old_version(path: Path, rev: str) -> str:
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=path.parent,
                          capture_output=True, text=True, check=True).stdout.strip()
    rel = path.resolve().relative_to(Path(root).resolve())
    return subprocess.run(["git", "show", f"{rev}:{rel.as_posix()}"], cwd=root,
                          capture_output=True, text=True, check=True).stdout


def pairs(old: str, new: str) -> list[tuple[str, str]]:
    a, b = sentences(old), sentences(new)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != "equal":
            before, after = " ".join(a[i1:i2]), " ".join(b[j1:j2])
            if re.sub(r"\W", "", before) != re.sub(r"\W", "", after):
                out.append((before, after))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tex", type=Path)
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--who", default="author")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    found = pairs(old_version(a.tex, a.rev), a.tex.read_text())
    if not found:
        sys.exit("no edits since " + a.rev)
    day = datetime.date.today().isoformat()
    text = "".join(f"\n## {day}, {a.who}\n**Before:** {b or '(nothing)'}\n\n**After:** {f or '(cut)'}\n"
                   for b, f in found)
    if a.dry_run:
        print(text)
        return
    out = a.tex.parent / "author_edits.md"
    if not out.exists():
        out.write_text("# Author edits\n\nPairs recorded by `/paperlint:learn`: paperlint's text"
                       " before, the author's after. Drafts imitate the afters.\n")
    with out.open("a") as fh:
        fh.write(text)
    print(f"{len(found)} pairs -> {out}")


if __name__ == "__main__":
    main()
