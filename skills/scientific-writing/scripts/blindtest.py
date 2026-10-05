#!/usr/bin/env python3
"""Can a reader tell the paper's paragraphs from the house style's?

    blindtest.py make  PAPER.tex [-n 10] [--seed S] [--section TITLE]  -> a work dir
    blindtest.py score WORKDIR                                          -> separation (AUC)
    blindtest.py stats PAPER.tex                                        -> fingerprints

`make` mixes n paragraphs of the paper with n held-out paragraphs of the corpus
(`corpus.py`), shuffled, into WORKDIR/blind.md, and keeps the key in WORKDIR/key.json.
The `judge` agent reads blind.md, judges each paragraph on its own (no quota) and writes
WORKDIR/labels.txt ("<n> <percent human>" per line); `score` prints the separation
(AUC): 0.5 means the paper's paragraphs cannot be told from published ones, 1.0 that
they always can. Use the same seed to compare two versions of a text.

`stats` prints per section the measures that separated the two in the first test
(sentence length, "we", because/so, colons and dashes, parentheses). They are a
diagnostic of where to look, never targets to write toward.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus  # noqa: E402

ENVS = r"equation|align|eqnarray|gather|multline|figure|table|ruledtabular|tabular"


def tex_body(tex: str) -> str:
    body = tex.split("\\begin{document}", 1)[-1]
    body = re.sub(r"(?<!\\)%.*", "", body)
    body = re.sub(rf"\\begin\{{({ENVS})\*?\}}.*?\\end\{{\1\*?\}}", " [equation] ", body, flags=re.S)
    return body.split("\\end{document}")[0]


def _ref(m: re.Match) -> str:
    """A cross-reference as a published paper prints it, numbered from its label so two
    labels never print the same, and the form gives nothing away."""
    labels = m.group(1).split(",")
    n = [int(hashlib.md5(x.encode()).hexdigest(), 16) % 30 + 1 for x in labels]
    kind = labels[0].split(":")[0]
    roman = ["I", "II", "III", "IV", "V"]
    if kind == "fig":
        return "Figs. " + " and ".join(str(x % 9 + 1) for x in n) if len(n) > 1 else f"Fig. {n[0] % 9 + 1}"
    if kind == "eq":
        return "Eqs. " + " and ".join(f"({x})" for x in n) if len(n) > 1 else f"Eq. ({n[0]})"
    if kind == "tab":
        return f"Table {roman[n[0] % 5]}"
    if kind == "app":
        return f"Appendix {'ABCD'[n[0] % 4]}"
    return f"Sec. {roman[n[0] % 5]}"


def tidy(p: str) -> str:
    p = re.sub(r"\$[^$]*\$", "[math]", p)
    p = re.sub(r"~?\\cite[pt]?\{[^}]*\}", " [ref]", p)
    p = re.sub(r"\\(?:[cC]ref|ref|eqref)\{([^}]*)\}", _ref, p)
    p = re.sub(r"\\(emph|textit|textbf|mathrm)\{([^}]*)\}", r"\2", p)
    p = re.sub(r"\\(label|footnote)\{[^}]*\}", "", p)
    p = re.sub(r"\\[a-zA-Z]+\*?(\[[^]]*\])?(\{[^}]*\})?", "", p)
    return re.sub(r"\s+", " ", p.replace("~", " ")).strip()


def sections(tex: str) -> list[tuple[str, str]]:
    parts = re.split(r"\\(?:sub)*section\*?\{([^}]*)\}", tex_body(tex))
    return [("front", parts[0])] + list(zip(parts[1::2], parts[2::2]))


def paragraphs(text: str, lo: int = 60, hi: int = 180) -> list[str]:
    out = [tidy(p) for p in re.split(r"\n\s*\n", text)]
    return [p for p in out if lo <= len(p.split()) <= hi and p.count(". ") >= 2]


def make(tex: Path, n: int, seed: int, section: str | None) -> Path:
    rng = random.Random(seed)
    secs = sections(tex.read_text())
    if section:
        secs = [s for s in secs if section.lower() in s[0].lower()]
    ours = [p for _, body in secs for p in paragraphs(body)]
    real = [re.sub(r"\$[^$]*\$", "[math]", r["text"]) for r in corpus.load("test")
            if r["job"] not in ("abstract", "caption") and 60 <= r["words"] <= 180]
    n = min(n, len(ours), len(real))
    items = [("llm", p) for p in rng.sample(ours, n)] + [("human", p) for p in rng.sample(real, n)]
    rng.shuffle(items)
    work = Path.home() / ".paperlint" / "blind" / time.strftime("%Y%m%d-%H%M%S")
    work.mkdir(parents=True)
    (work / "blind.md").write_text("".join(f"[{i}] {p}\n\n" for i, (_, p) in enumerate(items, 1)))
    (work / "key.json").write_text(json.dumps({"paper": str(tex), "seed": seed, "n": n,
                                               "key": [k for k, _ in items]}))
    print(work)
    return work


def score(work: Path) -> float:
    """AUC: the chance that a random published paragraph gets a higher probability of
    being human than a random paragraph of the paper. 0.5 = indistinguishable."""
    key = json.loads((work / "key.json").read_text())["key"]
    p = {}
    for line in (work / "labels.txt").read_text().splitlines():
        m = re.match(r"\s*\[?(\d+)\]?\W+(\d+(?:\.\d+)?)", line)
        if m:
            p[int(m.group(1))] = float(m.group(2))
    ours = [p.get(i, 50.0) for i, k in enumerate(key, 1) if k == "llm"]
    real = [p.get(i, 50.0) for i, k in enumerate(key, 1) if k == "human"]
    auc = sum((r > o) + 0.5 * (r == o) for r in real for o in ours) / (len(real) * len(ours))
    print(f"separation (AUC) {auc:.2f}  (0.5 = indistinguishable, 1.0 = always told apart)")
    print(f"mean probability human: paper {sum(ours) / len(ours):.0f}%, published {sum(real) / len(real):.0f}%")
    return auc


def measures(text: str) -> dict:
    sents = [s for s in re.split(r"(?<=[.?!])\s+(?=[A-Z\[])", text) if len(s.split()) > 3]
    n = [len(s.split()) for s in sents]
    w = max(sum(n), 1)
    low = text.lower()
    per = lambda pat: 1000 * len(re.findall(pat, low)) / w  # noqa: E731
    return {"sent": len(n), "mean": statistics.mean(n) if n else 0,
            "short": sum(x < 12 for x in n) / max(len(n), 1),
            "we": per(r"\bwe\b|\bour\b|\bus\b"), "so/because": per(r"\bso\b|\bbecause\b"),
            "colon+dash": per(r":|—|–| -- "), "paren": per(r"\(")}


def stats(tex: Path) -> None:
    head = f"{'':22s}{'sent':>5s}{'mean':>6s}{'short':>7s}{'we':>6s}{'so/bec':>8s}{'col+dash':>9s}{'paren':>7s}"
    print(head + "   (per 1000 words; short = share under 12 words)")
    rows = [("CORPUS (house)", " ".join(r["text"] for r in corpus.load("train") if r["job"] != "caption"))]
    rows += [(t[:22], " ".join(paragraphs(b, 20, 10_000))) for t, b in sections(tex.read_text())]
    for name, text in rows:
        if len(text.split()) < 150:
            continue
        m = measures(text)
        print(f"{name:22s}{m['sent']:5d}{m['mean']:6.1f}{m['short']:7.2f}{m['we']:6.1f}"
              f"{m['so/because']:8.1f}{m['colon+dash']:9.1f}{m['paren']:7.1f}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("tex", type=Path)
    m.add_argument("-n", type=int, default=10)
    m.add_argument("--seed", type=int, default=1)
    m.add_argument("--section")
    s = sub.add_parser("score")
    s.add_argument("work", type=Path)
    t = sub.add_parser("stats")
    t.add_argument("tex", type=Path)
    a = ap.parse_args()
    if a.cmd == "make":
        make(a.tex, a.n, a.seed, a.section)
    elif a.cmd == "score":
        score(a.work)
    else:
        stats(a.tex)


if __name__ == "__main__":
    main()
