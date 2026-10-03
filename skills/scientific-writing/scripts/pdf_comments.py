#!/usr/bin/env python3
"""List the review annotations of a PDF, one per line, with the text they mark.

Usage: pdf_comments.py annotated.pdf [--json]

Prints page, type, colour, author, the marked text (highlight, underline, strike-out)
and the comment. Ink (handwriting) and stamps have no text: they are listed with their
position, and the page must be rendered (pdftoppm -r 110 -f N -l N) and read by eye.
Needs pypdf; the marked text comes from pdftotext (poppler).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

SKIP = {"/Link", "/Popup", "/Widget"}


def colour(c) -> str:
    """Name an annotation colour roughly; reviewers use colour as a legend."""
    if not c or len(c) != 3:
        return ""
    r, g, b = (float(x) for x in c)
    if max(r, g, b) - min(r, g, b) < 0.15:
        return "black" if r < 0.5 else "grey"
    if r > 0.6 and g > 0.6 and b < 0.5:
        return "yellow"
    if r > 0.6 and b > 0.5 and g < 0.6:
        return "pink"
    if r >= g and r >= b:
        return "red"
    if g >= r and g >= b:
        return "green"
    return "blue"


def marked_text(pdf: str, page: int, rect, height: float) -> str:
    """Text inside rect (PDF coordinates) on 1-based page, via pdftotext -x -y -W -H."""
    x0, y0, x1, y1 = (float(v) for v in rect)
    cmd = ["pdftotext", "-f", str(page), "-l", str(page), "-x", str(int(x0)),
           "-y", str(int(height - y1)), "-W", str(int(x1 - x0) + 1),
           "-H", str(int(y1 - y0) + 1), "-layout", pdf, "-"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout
    except (OSError, subprocess.TimeoutExpired):
        return ""
    return " ".join(out.split())


def comments(pdf: str) -> list[dict]:
    from pypdf import PdfReader
    rows = []
    for i, page in enumerate(PdfReader(pdf).pages, start=1):
        h = float(page.mediabox.height)
        for ref in page.get("/Annots") or []:
            a = ref.get_object()
            kind = a.get("/Subtype")
            if kind in SKIP:
                continue
            rect = a.get("/Rect")
            row = {"page": i, "type": str(kind).lstrip("/"), "colour": colour(a.get("/C")),
                   "author": str(a.get("/T", "")), "comment": str(a.get("/Contents", "")).strip(),
                   "marked": "", "rect": [round(float(v)) for v in rect] if rect else []}
            if kind in {"/Highlight", "/Underline", "/StrikeOut", "/Squiggly"} and rect:
                row["marked"] = marked_text(pdf, i, rect, h)
            rows.append(row)
    return rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdf")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        rows = comments(args.pdf)
    except ImportError:
        print("pdf_comments.py needs pypdf (pip install pypdf); otherwise render the pages "
              "with pdftoppm and read the annotations by eye", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return 0
    for n, r in enumerate(rows, start=1):
        mark = f' marks "{r["marked"]}"' if r["marked"] else ""
        note = f': {r["comment"]}' if r["comment"] else ""
        who = f' ({r["author"]})' if r["author"] else ""
        print(f'C{n} p.{r["page"]} {r["type"]} {r["colour"]}{who}{mark}{note}'
              + ("" if mark or note else f' at {r["rect"]}: read the rendered page'))
    if not rows:
        print("no annotations: the comments may be scanned or flattened; render the pages "
              "and read them by eye")
    return 0


if __name__ == "__main__":
    sys.exit(main())
