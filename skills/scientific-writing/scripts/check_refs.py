#!/usr/bin/env python3
"""Check BibTeX entries against Crossref.

For each entry the script looks the work up on Crossref (by DOI when the entry has
one, otherwise by title and first author) and compares the first author, year,
volume, first page and title. It reports mismatches and suggests missing DOIs. It
never edits the .bib file.

Usage:
    check_refs.py refs.bib
    check_refs.py refs.bib --keys Lindblad1976,Rabi1937
    check_refs.py refs.bib --json

Set PAPERLINT_MAILTO=you@example.org (or --mailto) to use Crossref's polite pool.
Results are cached next to the .bib file in .paperlint-refs-cache.json.
Standard library only.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.crossref.org/works"


# ---------------------------------------------------------------------------
def parse_bib(text: str) -> list[dict]:
    """Minimal BibTeX parser: @type{key, field = {..} | ".." | number, ...}."""
    entries = []
    for mt in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        kind = mt.group(1).lower()
        if kind in {"comment", "preamble", "string"}:
            continue
        i = mt.end()
        depth = 1
        j = i
        while j < len(text) and depth:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        body = text[i:j - 1]
        fields = {}
        k = 0
        while k < len(body):
            fm = re.match(r"\s*,?\s*([A-Za-z][\w\-]*)\s*=\s*", body[k:])
            if not fm:
                break
            name = fm.group(1).lower()
            k += fm.end()
            if k < len(body) and body[k] == "{":
                d, s = 0, k
                while k < len(body):
                    if body[k] == "{":
                        d += 1
                    elif body[k] == "}":
                        d -= 1
                        if d == 0:
                            k += 1
                            break
                    k += 1
                value = body[s + 1:k - 1]
            elif k < len(body) and body[k] == '"':
                e = body.find('"', k + 1)
                value = body[k + 1:e]
                k = e + 1
            else:
                vm = re.match(r"[^,\s}]+", body[k:])
                value = vm.group(0) if vm else ""
                k += len(value)
            fields[name] = re.sub(r"\s+", " ", value).strip()
        entries.append({"type": kind, "key": mt.group(2), **fields})
    return entries


def plain(s: str) -> str:
    """Strip LaTeX markup and accents, lower-case, for comparisons."""
    s = re.sub(r"<[^>]+>", "", s)            # Crossref titles carry HTML tags
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = re.sub(r"\\.", "", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s.lower())).strip()


def first_author_family(authors: str) -> str:
    first = re.split(r"\s+and\s+", authors)[0] if authors else ""
    if "," in first:
        return plain(first.split(",")[0])
    parts = plain(first).split()
    return parts[-1] if parts else ""


def raw_first_family(authors: str) -> str:
    """First author's family name as written (Crossref ranks better with case)."""
    first = re.split(r"\s+and\s+", authors)[0] if authors else ""
    first = re.sub(r"[{}\\]", "", first)
    return first.split(",")[0].strip() if "," in first else (first.split() or [""])[-1]


def work_year(work: dict):
    for k in ("published-print", "issued", "published-online"):
        parts = (work.get(k) or {}).get("date-parts") or [[None]]
        if parts[0] and parts[0][0]:
            return parts[0][0]
    return None


def first_page(p: str) -> str:
    return re.split(r"[-\u2013\u2014,]+", p.replace("--", "-"))[0].strip() if p else ""


# ---------------------------------------------------------------------------
class Crossref:
    def __init__(self, mailto: str | None, cache_file: Path):
        self.mailto = mailto
        self.cache_file = cache_file
        try:
            self.cache = json.loads(cache_file.read_text())
        except Exception:
            self.cache = {}

    def _get(self, url: str):
        if url in self.cache:
            return self.cache[url]
        headers = {"User-Agent": "paperlint-check-refs/0.1"
                   + (f" (mailto:{self.mailto})" if self.mailto else "")}
        for attempt in range(2):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=20) as r:
                    data = json.load(r)
                self.cache[url] = data
                time.sleep(0.1)
                return data
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    self.cache[url] = None
                    return None
                time.sleep(1.0)
            except (urllib.error.URLError, TimeoutError):
                time.sleep(1.0)
        raise ConnectionError(f"Crossref did not answer: {url}")

    def by_doi(self, doi: str):
        d = self._get(f"{API}/{urllib.parse.quote(doi)}")
        return d["message"] if d else None

    def search(self, entry: dict):
        """Best Crossref match for an entry without DOI, or None."""
        title = entry.get("title", "")
        author = raw_first_family(entry.get("author", ""))
        year = entry.get("year", "")
        queries = [
            {"query.bibliographic": " ".join(x for x in (title, author, year) if x), "rows": 5},
            {"query.title": title, "query.author": author, "rows": 5},
        ]
        best, score = None, 0.0
        for q in queries:
            d = self._get(f"{API}?{urllib.parse.urlencode(q)}")
            for it in (d or {}).get("message", {}).get("items", []):
                t = plain((it.get("title") or [""])[0])
                r = difflib.SequenceMatcher(None, plain(title), t).ratio()
                fam = plain(((it.get("author") or [{}])[0]).get("family", ""))
                if fam and fam == plain(author):
                    r += 0.2
                if year and str(work_year(it)) == str(year):
                    r += 0.1
                if r > score:
                    best, score = it, r
            if score >= 1.2:
                break
        return best if score >= 0.8 else None

    def save(self):
        try:
            self.cache_file.write_text(json.dumps(self.cache))
        except OSError:
            pass


def compare(entry: dict, work: dict) -> list[str]:
    issues = []
    title = (work.get("title") or [""])[0]
    ratio = difflib.SequenceMatcher(None, plain(entry.get("title", "")), plain(title)).ratio()
    if ratio < 0.85:
        issues.append(f"title differs: Crossref has '{title}'")
    fam = first_author_family(entry.get("author", ""))
    cr_auth = work.get("author") or []
    cr_fam = plain(cr_auth[0].get("family", "")) if cr_auth else ""
    if fam and cr_fam and fam != cr_fam:
        issues.append(f"first author '{fam}' but Crossref has '{cr_auth[0].get('family')}'")
    year = str(work_year(work)) if work_year(work) else None
    if entry.get("year") and year and entry["year"] != year:
        issues.append(f"year {entry['year']} but Crossref has {year}")
    vol = work.get("volume")
    if entry.get("volume") and vol and plain(entry["volume"]) != plain(vol):
        issues.append(f"volume {entry['volume']} but Crossref has {vol}")
    page = first_page(work.get("page", "")) or work.get("article-number", "")
    if entry.get("pages") and page and first_page(entry["pages"]) != page:
        issues.append(f"pages {entry['pages']} but Crossref has {work.get('page') or page}")
    return issues


def _unrelated(entry: dict, work: dict) -> bool:
    """A search hit whose first author and year both disagree is another work."""
    fam = first_author_family(entry.get("author", ""))
    cr = plain(((work.get("author") or [{}])[0]).get("family", ""))
    y = work_year(work)
    year_differs = bool(entry.get("year") and y and str(y) != entry["year"])
    title = plain((work.get("title") or [""])[0])
    title_differs = difflib.SequenceMatcher(None, plain(entry.get("title", "")),
                                            title).ratio() < 0.85
    author_differs = bool(fam and cr and fam != cr)
    return year_differs and (author_differs or title_differs)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check BibTeX entries against Crossref.")
    ap.add_argument("bib", type=Path)
    ap.add_argument("--keys", help="comma-separated keys to check (default: all)")
    ap.add_argument("--mailto", default=os.environ.get("PAPERLINT_MAILTO"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-cache", action="store_true")
    args = ap.parse_args(argv)

    entries = parse_bib(args.bib.read_text(encoding="utf-8"))
    if args.keys:
        want = {k.strip() for k in args.keys.split(",")}
        entries = [e for e in entries if e["key"] in want]
        missing = want - {e["key"] for e in entries}
        for k in sorted(missing):
            print(f"{k}: not in {args.bib}", file=sys.stderr)
    cache = args.bib.parent / ".paperlint-refs-cache.json"
    cr = Crossref(args.mailto, cache if not args.no_cache else Path(os.devnull))

    results = []
    for e in entries:
        res = {"key": e["key"], "status": "ok", "issues": [], "doi": e.get("doi")}
        if e["type"] in {"misc", "online", "software", "unpublished"} and not e.get("doi"):
            res["status"] = "skipped"
            res["issues"].append(f"@{e['type']} entry, not checked")
            results.append(res)
            continue
        try:
            work = cr.by_doi(e["doi"]) if e.get("doi") else None
            searched = work is None
            if work is None:
                work = cr.search(e)
        except ConnectionError as err:
            res["status"] = "error"
            res["issues"].append(str(err))
            results.append(res)
            continue
        if work is None:
            res["status"] = "not found"
            res["issues"].append("no matching work on Crossref; check by hand")
        elif searched and _unrelated(e, work):
            res["status"] = "not found"
            res["issues"].append("no matching work on Crossref; closest is "
                                 f"'{(work.get('title') or [''])[0]}' ({work.get('DOI')})")
        else:
            res["issues"] = compare(e, work)
            if res["issues"]:
                res["status"] = "mismatch"
            if not e.get("doi") and work.get("DOI"):
                res["suggest_doi"] = work["DOI"]
        results.append(res)
    cr.save()

    if args.json:
        print(json.dumps(results, indent=1))
    else:
        for r in results:
            line = f"{r['key']}: {r['status']}"
            if r.get("suggest_doi"):
                line += f" (doi = {{{r['suggest_doi']}}})"
            print(line)
            for i in r["issues"]:
                print(f"    - {i}")
        bad = [r for r in results if r["status"] in {"mismatch", "not found", "error"}]
        print(f"{len(results)} entries checked, {len(bad)} need attention")
    return 0


if __name__ == "__main__":
    sys.exit(main())
