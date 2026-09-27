#!/usr/bin/env python3
"""Create paperlint.toml and glossary.toml for a paper (never overwrites).

Usage: init_project.py [paper_dir] [--main main.tex] [--bib refs.bib]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parents[3] / "templates"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Set up paperlint for a paper.")
    ap.add_argument("paper_dir", nargs="?", type=Path, default=Path.cwd())
    ap.add_argument("--main", help="main .tex file (default: guessed)")
    ap.add_argument("--bib", help="bibliography file (default: guessed)")
    args = ap.parse_args(argv)
    d = args.paper_dir.resolve()
    if not d.is_dir():
        print(f"{d} is not a directory", file=sys.stderr)
        return 2

    main_tex = args.main
    if not main_tex:
        cands = [p for p in d.glob("*.tex") if "\\documentclass" in p.read_text(errors="ignore")]
        main_tex = cands[0].name if cands else "main.tex"
    bib = args.bib
    if not bib:
        bibs = sorted(p.name for p in d.glob("*.bib"))
        bib = bibs[0] if bibs else "refs.bib"

    for name in ("paperlint.toml", "glossary.toml"):
        dst = d / name
        if dst.exists():
            print(f"kept existing {dst}")
            continue
        text = (TEMPLATES / name).read_text()
        if name == "paperlint.toml":
            text = re.sub(r'files = \["main.tex"\]', f'files = ["{main_tex}"]', text)
            text = re.sub(r'bib = \["refs.bib"\]', f'bib = ["{bib}"]', text)
        dst.write_text(text)
        print(f"wrote {dst}")
    print(f"main file: {main_tex}, bibliography: {bib}")
    print("Next: edit glossary.toml with your paper's terminology, then run lint.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
