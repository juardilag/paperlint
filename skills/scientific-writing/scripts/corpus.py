#!/usr/bin/env python3
"""The house-style corpus: real paragraphs, labelled by the job they do.

    corpus.py build                 fetch the papers of corpus_ids.txt and index them
    corpus.py retrieve JOB [TEXT]   the k real paragraphs closest to TEXT that do JOB
    corpus.py jobs                  how many paragraphs each job has

JOB is one of: abstract, opening, intro, method, results, appendix, conclusion,
caption. A drafter reads the retrieved paragraphs before writing a paragraph that
does the same job; that is how paperlint learns the house style from text instead
of from a description of it.

Every fifth paragraph (by a hash of its id) is held out as the "test" split: the
blind test samples only from it and retrieval never returns it, so the judge never
sees a paragraph the drafter imitated.

The texts live in ~/.paperlint/corpus (or $PAPERLINT_CORPUS), never in the repository.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
IDS = HERE.parent / "corpus_ids.txt"
ROOT = Path(os.environ.get("PAPERLINT_CORPUS", Path.home() / ".paperlint" / "corpus"))
RAW, INDEX = ROOT / "raw", ROOT / "corpus.jsonl"
JOBS = ("abstract", "opening", "intro", "method", "results", "appendix", "conclusion",
        "caption")
STOP = set("""the a an of and or in on to for with by from at as is are was were be been
this that these those which it its we our their there here than then also can may into
such not only more most both each between where when while over under one two""".split())


def read_ids() -> list[tuple[str, str, str]]:
    out = []
    for line in IDS.read_text().splitlines():
        line = line.split("#")[0].split()
        if line:
            out.append((line[0], line[1] if len(line) > 1 else "", line[2] if len(line) > 2 else ""))
    return out


def fetch(arxiv: str) -> str | None:
    path = RAW / f"{arxiv}.html"
    if path.exists() and path.stat().st_size > 20_000:
        return path.read_text(errors="ignore")
    for url in (f"https://arxiv.org/html/{arxiv}", f"https://ar5iv.labs.arxiv.org/html/{arxiv}"):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "paperlint-corpus/0.8"})
            text = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
        except Exception:
            continue
        if "ltx_para" in text:
            path.write_text(text)
            time.sleep(1)                       # be polite to arXiv
            return text
    return None


def _math(m: re.Match) -> str:
    alt = re.search(r'alttext="([^"]*)"', m.group(0))
    tex = html.unescape(alt.group(1)) if alt else ""
    return f"${tex}$" if tex and len(tex) <= 60 else "[math]"


def clean(fragment: str) -> str:
    s = re.sub(r"<math.*?</math>", _math, fragment, flags=re.S)
    s = re.sub(r"<cite.*?</cite>", "[ref]", s, flags=re.S)
    s = re.sub(r"<(table|figure)\b.*?</\1>", " ", s, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"\s+", " ", s).strip()


def job_of(title: str, sid: str, first_of_intro: bool) -> str:
    t = title.lower()
    if sid.startswith("A"):
        return "appendix"
    if "intro" in t:
        return "opening" if first_of_intro else "intro"
    if re.search(r"conclu|outlook|perspective|discussion|summary", t):
        return "conclusion"
    if re.search(r"method|model|protocol|setup|set-up|formalism|framework|derivation|keldysh|theory", t):
        return "method"
    return "results"


def parse(page: str, arxiv: str, min_words: int = 25) -> list[dict]:
    titles = {}
    for sid, head in re.findall(r'<section[^>]*id="([^"]+)"[^>]*>\s*<h\d[^>]*>(.*?)</h\d>', page, flags=re.S):
        titles[sid] = re.sub(r"^[\dA-Z.\s]+(?=[A-Z])", "", clean(head)).strip()
    rows, groups = [], {}
    abstract = re.search(r'class="ltx_abstract".*?</div>', page, flags=re.S)
    if abstract:
        text = clean(re.sub(r"<h6.*?</h6>", "", abstract.group(0), flags=re.S))
        rows.append(dict(pid="abstract", section="Abstract", job="abstract", text=text))
    for pid, frag in re.findall(r'<p[^>]*id="([^"]+)"[^>]*class="ltx_p"[^>]*>(.*?)</p>', page, flags=re.S):
        if ".I" in pid or pid.startswith(("fig", "T", "footnote")) or ".fn" in pid:
            continue
        groups.setdefault(pid.rsplit(".", 1)[0], []).append(clean(frag))
    intro_seen = False
    for key, parts in groups.items():
        sid = key.rsplit(".p", 1)[0]
        top = sid.split(".")[0]
        title = titles.get(sid) or titles.get(top) or ""
        job = job_of(titles.get(top, title), sid, not intro_seen)
        if job == "opening":
            intro_seen = True
        rows.append(dict(pid=key, section=title, job=job, text=" [equation] ".join(parts)))
    for i, cap in enumerate(re.findall(r'<figcaption[^>]*>(.*?)</figcaption>', page, flags=re.S)):
        text = re.sub(r"^(Figure|FIG\.|Fig\.)\s*\d+[:.]?\s*", "", clean(cap))
        rows.append(dict(pid=f"caption{i}", section="", job="caption", text=text))
    for r in rows:
        r["arxiv"] = arxiv
        r["words"] = len(r["text"].split())
        r["split"] = "test" if int(hashlib.md5(f"{arxiv}:{r['pid']}".encode()).hexdigest(), 16) % 5 == 0 else "train"
    return [r for r in rows if r["words"] >= min_words and r["text"].count(". ") + 1 >= 2]


def build() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    rows = []
    for arxiv, author, kind in read_ids():
        page = fetch(arxiv)
        if page is None:
            print(f"  {arxiv}: not available as HTML, skipped", file=sys.stderr)
            continue
        got = parse(page, arxiv)
        for r in got:
            r.update(author=author, kind=kind)
        rows += got
        print(f"  {arxiv} {author:12s} {len(got):4d} paragraphs")
    with INDEX.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    print(f"{len(rows)} paragraphs -> {INDEX}")


def load(split: str | None = None) -> list[dict]:
    if not INDEX.exists():
        sys.exit(f"no corpus at {INDEX}; run `corpus.py build` first")
    rows = [json.loads(line) for line in INDEX.open()]
    return [r for r in rows if split is None or r["split"] == split]


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z\-]{3,}", text.lower()) if w not in STOP}


def retrieve(job: str, text: str = "", k: int = 3, max_words: int = 220) -> list[dict]:
    """The k train paragraphs of this job closest to `text`, at most one per paper."""
    pool = [r for r in load("train") if r["job"] == job and r["words"] <= max_words]
    q = words(text)
    pool.sort(key=lambda r: -len(q & words(r["text"])) / (1 + len(words(r["text"]))) ** 0.5)
    out, seen = [], set()
    for r in pool:
        if r["arxiv"] not in seen:
            out.append(r)
            seen.add(r["arxiv"])
        if len(out) == k:
            break
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    sub.add_parser("jobs")
    r = sub.add_parser("retrieve")
    r.add_argument("job", choices=JOBS)
    r.add_argument("text", nargs="*", help="the draft, plan line or old paragraph to match")
    r.add_argument("-k", type=int, default=3)
    a = ap.parse_args()
    if a.cmd == "build":
        build()
    elif a.cmd == "jobs":
        rows = load()
        for j in JOBS:
            print(f"  {j:10s} train {sum(r['job'] == j and r['split'] == 'train' for r in rows):5d}"
                  f"  test {sum(r['job'] == j and r['split'] == 'test' for r in rows):4d}")
    else:
        for r in retrieve(a.job, " ".join(a.text), a.k):
            print(f"[{r['arxiv']}, {r['author']}, {r['section'] or r['job']}]\n{r['text']}\n")


if __name__ == "__main__":
    main()
