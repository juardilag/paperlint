#!/usr/bin/env python3
"""Find text a reviewer struck out that has come back, reworded or not.

Usage: strikes.py main.tex [--review review/] [--min 0.6]

Reads every annotated PDF in the review folders next to the main file (all PDFs
except before.pdf, diff.pdf and summary.pdf), collects the strike-outs with
pdf_comments.py, and looks for each struck passage in the current source. A passage
counts as back when a stretch of the source of the same length shares at least --min
of its content words and reads in the same order. Each hit is printed with the round,
the comment number and the matching source line, so it can be removed again or kept
by a recorded decision in CLAUDE.md. A strike kept on purpose (moved, not cut, or
overruled by the authors) is listed in CLAUDE.md as `kept-strike: <round> C<n>` with
the reason, and is not reported again.
"""
from __future__ import annotations

import argparse
import difflib
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SKIP_PDFS = {"before.pdf", "diff.pdf", "summary.pdf"}
STOP = set("""the and for with that this which from are its into than then them they
there their these those was were has have had not but also only each when where while
can may will would should could been being any all one two our out off per via""".split())


def words(text: str) -> list[str]:
    """Content words, lower case: LaTeX commands and math dropped, short words skipped."""
    text = re.sub(r"(?<!\\)%[^\n]*", " ", text)
    text = re.sub(r"\$[^$]*\$|\\\(.*?\\\)", " ", text, flags=re.S)
    text = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", " ", text)
    return [w for w in re.findall(r"[a-z]{3,}", text.lower()) if w not in STOP]


def returns(struck: list[str], source: str, minimum: float = 0.6) -> list[tuple[int, float, int]]:
    """(index of struck passage, score, source offset) for each passage found again.

    The score is the fraction of the passage's content words in the best window of the
    source, times how much of their order survives (difflib ratio); passages of fewer
    than six content words are skipped, since a short phrase recurs by chance.
    """
    toks = [(m.group(), m.start()) for m in re.finditer(r"[A-Za-z]+", source)]
    src_words, offs = [], []
    for w, o in toks:
        lw = w.lower()
        if len(lw) >= 3 and lw not in STOP:
            src_words.append(lw)
            offs.append(o)
    clean = re.sub(r"(?<!\\)%[^\n]*", lambda m: " " * len(m.group()), source)
    keep = set(words(clean))
    found = []
    for i, passage in enumerate(struck):
        whole = words(passage)
        if len(whole) < 6:
            continue
        # A long strike can come back in part, so its pieces are searched too.
        pieces = [whole] + [whole[k:k + 10] for k in range(0, len(whole) - 9, 5)
                            if len(whole) > 15]
        hit = _best(pieces, src_words, offs, keep, minimum)
        if hit:
            found.append((i, *hit))
    return found


def _best(pieces, src_words, offs, keep, minimum):
    """(score, offset) of the best-matching piece at or above the threshold, or None."""
    top = None
    for p in pieces:
        need, n = Counter(p), len(p)
        best, at = 0.0, -1
        win: Counter = Counter()
        for j, w in enumerate(src_words):
            win[w] += 1
            if j >= n:
                win[src_words[j - n]] -= 1
            if j >= n - 1:
                hit = sum(min(c, win[w2]) for w2, c in need.items()) / n
                if hit > best:
                    best, at = hit, j - n + 1
        if best < minimum or at < 0:
            continue
        order = difflib.SequenceMatcher(None, p, src_words[at:at + n]).ratio()
        score = best * order
        if score >= minimum * 0.8 and any(w in keep for w in src_words[at:at + n]):
            if top is None or score > top[0]:
                top = (round(score, 2), offs[at])
    return top


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("tex")
    ap.add_argument("--review", default=None, help="review folder (default: next to the .tex)")
    ap.add_argument("--min", type=float, default=0.6)
    args = ap.parse_args(argv)
    tex = Path(args.tex)
    source = tex.read_text(encoding="utf-8")
    review = Path(args.review) if args.review else tex.parent / "review"
    pdfs = sorted(p for p in review.glob("*/*.pdf") if p.name not in SKIP_PDFS)
    if not pdfs:
        print(f"no annotated PDFs in {review}")
        return 0
    try:
        from pdf_comments import comments
    except ImportError:
        print("strikes.py needs pdf_comments.py next to it", file=sys.stderr)
        return 2
    notes = tex.parent / "CLAUDE.md"
    kept = set(re.findall(r"kept-strike:\s*(\S+)\s+C(\d+)",
                          notes.read_text(encoding="utf-8") if notes.exists() else ""))
    hits = 0
    for pdf in pdfs:
        try:
            rows = comments(str(pdf))
        except ImportError:
            print("strikes.py needs pypdf (pip install pypdf)", file=sys.stderr)
            return 2
        struck = [(n, r) for n, r in enumerate(rows, start=1)
                  if r["type"] == "StrikeOut" and r["marked"]]
        for i, score, off in returns([r["marked"] for _, r in struck], source, args.min):
            n, r = struck[i]
            if (pdf.parent.name, str(n)) in kept:
                continue
            line = source.count("\n", 0, off) + 1
            print(f'{tex.name}:{line}: {pdf.parent.name} C{n} ({r["author"] or "reviewer"}) '
                  f'struck text is back ({score:.2f}): "{r["marked"][:90]}"')
            hits += 1
    print(f"{hits} struck passage(s) back" if hits else "no struck passage is back")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
