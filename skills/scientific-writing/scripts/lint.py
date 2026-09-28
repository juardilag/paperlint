#!/usr/bin/env python3
"""paperlint: mechanical style checks for LaTeX manuscripts.

The checks are the parts of the scientific-writing rules that a program can apply
without judgement: sentence length, punctuation, sentence openings, banned phrases,
acronyms used before they are defined, terms the paper has decided not to use, and
hand-typed cross-references. Everything that needs judgement (is this term defined?
does this paragraph argue?) is left to the writer and to the cold-reader agent.

The LaTeX source is "masked" rather than parsed: math, comments, citations and
commands are replaced by blanks or by one-character placeholders of the same
length, so every finding keeps its line and column in the original file.

Usage:
    lint.py main.tex                      # lint one file
    lint.py                               # lint the files listed in paperlint.toml
    lint.py main.tex --section Introduction
    lint.py main.tex --lines 120-180      # only findings in this line range
    lint.py main.tex --json               # machine-readable output
    lint.py --list-checks

Configuration is read from the nearest paperlint.toml (see templates/).
Standard library only; Python >= 3.11.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from dataclasses import asdict, dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Placeholders written into the masked text. Each replaces a whole construct
# and keeps the text length unchanged.
MATH = "\u24c2"        # inline math, counts as one word
DISPLAY = "\u039e"     # display math, not counted as a word
REF_LOWER = "\u24e1"   # \cref{...} and similar lower-case reference macros
REF_UPPER = "\u24c7"   # \Cref{...}
PARA = "\u00b6"        # paragraph or item break

CHECKS = {
    "PL001": "sentence longer than the hard limit",
    "PL002": "colon in running text",
    "PL003": "semicolon in running text",
    "PL004": "em dash",
    "PL005": "sentence starts with a symbol, a numeral or an acronym",
    "PL006": "sentence starts with a lower-case reference macro (use the capitalised one)",
    "PL007": "banned phrase",
    "PL008": "expletive opener (It is / There is)",
    "PL009": "italic emphasis on a whole phrase or sentence",
    "PL010": "term the project has decided not to use here (glossary)",
    "PL011": "acronym used before it is defined",
    "PL012": "bare demonstrative opener (This is / This means ...)",
    "PL013": "hand-typed cross-reference",
    "PL014": "anthropomorphic verb",
    "PL015": "sentence longer than the target length",
    "PL016": "more than one parenthetical pointer in a sentence",
    "PL017": "antithesis reflex ('not X but Y', ', not an X')",
}

# Each entry: regex (case-insensitive, word-bounded where it makes sense), advice.
DEFAULT_BANNED = [
    (r"\bthe fact that\b", "cut it; state the fact"),
    (r"\bit is (?:interesting|worth|important) to note\b", "cut it"),
    (r"\bin order to\b", "write 'to'"),
    (r"\bbasically\b", "cut it"),
    (r"\bessentially\b", "cut it, or say in what sense"),
    (r"\bvery\b", "cut it, or quantify"),
    (r"\bdue to\b", "state the cause ('because', 'caused by')"),
    (r"\brecipe\b", "write 'procedure' or 'method'"),
    (r"\btrick\b", "write 'method' or 'step'"),
    (r"\bbuys?\b", "write 'gives', 'allows' or 'costs'"),
    (r"\bprices?\b(?! of)", "write 'costs' or 'quantifies'"),
    (r"\bthe price of\b", "write 'the cost of'"),
    (r"\bengine\b", "write 'method', 'formulation' or 'code'"),
    (r"\bnovel\b", "cut it; say what is new"),
    (r"\bgroundbreaking\b", "cut it"),
    (r"\bunprecedented\b", "cut it, or quantify"),
    (r"\bdelve\b", "write 'study' or 'examine'"),
    (r"\bleverag(?:e|es|ed|ing)\b", "write 'use'"),
    (r"\bseamless(?:ly)?\b", "cut it"),
    (r"\brobust(?:ly)?\b", "say against what"),
    (r"\bcrucial(?:ly)?\b", "say why it matters"),
    (r"\bin the spirit of\b", "say what is taken from the work"),
    (r"\bnowhere else\b", "say where it enters, without the slogan"),
    (r"\bthree times (?:smaller|less)\b", "give the ratio"),
    (r"\btwice the size\b", "say which size, and give the ratio"),
    (r"\bcompared to\b", "write 'compared with'"),
    (r"\b(?:notably|importantly|interestingly|remarkably)\b",
     "cut it; say why the point matters"),
    (r"\bit is worth\b", "cut it"),
    (r"\bsheds? light on\b", "say what it shows"),
    (r"\bpaves? the way\b", "say what it makes possible"),
    (r"\ba testament to\b", "say what it shows"),
    (r"\bplays? an? (?:key|crucial|pivotal|central|vital) role\b", "say what it does"),
    (r"\bpivotal\b", "cut it, or say why it matters"),
    (r"\bintricate\b", "say what makes it complicated"),
    (r"\bunderscor(?:e|es|ed|ing)\b", "write 'shows', or cut it"),
    (r"\bshowcas(?:e|es|ed|ing)\b", "write 'shows'"),
    (r"\bmay potentially\b|\bcould possibly\b", "one hedge is enough"),
]

DEFAULT_ANTHROPOMORPHIC = [
    "remember", "remembers", "remembered", "forget", "forgets",
    "sees", "saw", "inherit", "inherits", "inherited",
    "knows", "wants", "decides", "tells", "feels", "chooses",
]

# Unit symbols with two or more capitals, which PL011 must not treat as acronyms.
DEFAULT_KNOWN = {
    "GB", "MB", "TB", "KB", "PB", "GiB", "MiB", "TiB",
    "GHz", "MHz", "THz", "PHz", "MeV", "GeV", "TeV", "PeV", "MW", "GW", "TW", "MPa", "GPa",
}

# Abbreviations after which a full stop does not end a sentence.
ABBREVIATIONS = {
    "e.g", "i.e", "cf", "vs", "etc", "al", "approx", "resp", "viz",
    "Eq", "Eqs", "Fig", "Figs", "Sec", "Secs", "Ref", "Refs", "Tab", "App",
    "No", "Nos", "Vol", "Ch", "Dr", "Prof", "St", "Mr", "Ms", "Mrs",
}

# Environments whose content is not prose.
DISPLAY_ENVS = {
    "equation", "equation*", "align", "align*", "alignat", "alignat*",
    "gather", "gather*", "multline", "multline*", "eqnarray", "eqnarray*",
    "displaymath", "math", "split", "flalign", "flalign*", "dmath", "dmath*",
}
SKIP_ENVS = {
    "tabular", "tabular*", "tabularx", "array", "verbatim", "verbatim*",
    "lstlisting", "minted", "tikzpicture", "pgfpicture", "thebibliography",
    "comment", "figure-placeholder",
}
# Commands whose arguments are removed entirely (not prose).
DROP_ARG_CMDS = {
    "cite", "citep", "citet", "citealp", "citeauthor", "citeyear", "nocite",
    "label", "ref", "eqref", "pageref", "autoref", "nameref", "vref",
    "includegraphics", "bibliography", "bibliographystyle", "usepackage",
    "documentclass", "input", "include", "url", "href", "hypersetup",
    "affiliation", "email", "address", "author", "date", "thanks",
    "crefname", "Crefname", "newcommand", "renewcommand", "def",
    "setlength", "addtolength", "vspace", "hspace", "vskip", "hskip",
    "begin", "end", "color", "textcolor", "pacs", "keywords",
}
LOWER_REF_CMDS = {"cref", "vref", "autoref"}
UPPER_REF_CMDS = {"Cref", "Vref", "Autoref"}
# Sectioning: the title is not linted as a sentence.
BREAK_CMDS = {
    "part", "chapter", "section", "subsection", "subsubsection", "paragraph",
    "subparagraph", "title", "item", "maketitle", "appendix", "par",
    "newpage", "clearpage", "bigskip", "medskip", "smallskip",
}
EMPH_CMDS = {"emph", "textit", "textsl"}
# Commands whose argument is kept as prose (their name and braces are blanked).
KEEP_ARG_CMDS = EMPH_CMDS | {
    "textbf", "texttt", "textrm", "textsf", "textsc", "textup", "text",
    "mbox", "caption", "footnote", "underline", "uline", "mathrm",
    "subcaption", "abstract",
}


# ---------------------------------------------------------------------------
@dataclass
class Finding:
    file: str
    line: int
    col: int
    code: str
    message: str
    excerpt: str = ""
    severity: str = "warning"


@dataclass
class Config:
    files: list[str] = field(default_factory=list)
    max_sentence_words: int = 25
    hard_sentence_words: int = 27
    ban_colons: bool = True
    ban_semicolons: bool = True
    ban_em_dash: bool = True
    emph_max_words: int = 4
    reference_style: str = "cleveref"   # "cleveref" or "any"
    known_acronyms: set[str] = field(default_factory=set)
    banned: list[tuple[str, str]] = field(default_factory=list)
    anthropomorphic: list[str] = field(default_factory=list)
    disabled: set[str] = field(default_factory=set)
    forbidden_terms: list[dict] = field(default_factory=list)
    root: Path = Path(".")


def load_config(start: Path, explicit: Path | None = None) -> Config:
    """Read the nearest paperlint.toml and the glossary it points to."""
    cfg = Config(banned=list(DEFAULT_BANNED),
                 anthropomorphic=list(DEFAULT_ANTHROPOMORPHIC),
                 known_acronyms=set(DEFAULT_KNOWN))
    path = explicit
    if path is None:
        d = start if start.is_dir() else start.parent
        for cand in [d, *d.parents]:
            if (cand / "paperlint.toml").is_file():
                path = cand / "paperlint.toml"
                break
    if path is None:
        cfg.root = start if start.is_dir() else start.parent
        return cfg
    cfg.root = path.parent
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    paper = data.get("paper", {})
    style = data.get("style", {})
    words = data.get("words", {})
    checks = data.get("checks", {})
    cfg.files = list(paper.get("files", []))
    for key in ("max_sentence_words", "hard_sentence_words", "ban_colons",
                "ban_semicolons", "ban_em_dash", "emph_max_words",
                "reference_style"):
        if key in style:
            setattr(cfg, key, style[key])
    cfg.known_acronyms |= set(words.get("known_acronyms", []))
    for pat in words.get("allow", []):
        cfg.banned = [(p, a) for p, a in cfg.banned if p != pat
                      and not re.fullmatch(p, pat, re.I)]
    for item in words.get("ban", []):
        if isinstance(item, str):
            cfg.banned.append((rf"\b{re.escape(item)}\b", "avoid"))
        else:
            cfg.banned.append((item["pattern"], item.get("advice", "avoid")))
    cfg.anthropomorphic += list(words.get("anthropomorphic", []))
    cfg.disabled = set(checks.get("disable", []))
    gpath = paper.get("glossary")
    if gpath:
        gfile = (cfg.root / gpath)
        if gfile.is_file():
            g = tomllib.loads(gfile.read_text(encoding="utf-8"))
            for term in g.get("term", []):
                for bad in term.get("avoid", []):
                    cfg.forbidden_terms.append({
                        "pattern": bad, "use": term.get("name", ""),
                        "scope": term.get("avoid_in", "all"),
                        "note": term.get("note", "")})
                if term.get("appendix_only"):
                    cfg.forbidden_terms.append({
                        "pattern": term["name"], "use": term.get("main_text", ""),
                        "scope": "main", "note": "appendix-only term"})
            cfg.known_acronyms |= set(g.get("known_acronyms", []))
    return cfg


# ---------------------------------------------------------------------------
def _match_brace(text: str, i: int) -> int:
    """Index just past the brace group that opens at text[i] == '{'."""
    depth = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return n


def _match_bracket(text: str, i: int) -> int:
    depth = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return n


class Masker:
    """Build a same-length copy of the source in which only prose survives."""

    def __init__(self, text: str):
        self.src = text
        self.m = list(text)
        self.emph_spans: list[tuple[int, int]] = []
        self.appendix_at = len(text)

    def blank(self, a: int, b: int, mark: str | None = None):
        for k in range(a, min(b, len(self.m))):
            if self.m[k] != "\n":
                self.m[k] = " "
        if mark is not None and a < len(self.m):
            self.m[a] = mark

    def run(self) -> str:
        t = self.src
        # 1. comments
        for mt in re.finditer(r"(?<!\\)%[^\n]*", t):
            self.blank(mt.start(), mt.end())
        t = "".join(self.m)
        # 2. preamble and after \end{document}
        b = t.find("\\begin{document}")
        if b >= 0:
            self.blank(0, b + len("\\begin{document}"))
        e = t.find("\\end{document}")
        if e >= 0:
            self.blank(e, len(t))
        t = "".join(self.m)
        mt = re.search(r"\\appendix\b", t)
        if mt:
            self.appendix_at = mt.start()
        # 3. environments
        for mt in re.finditer(r"\\begin\{([^}]+)\}", t):
            name = mt.group(1)
            if name in DISPLAY_ENVS or name in SKIP_ENVS:
                end = t.find("\\end{" + name + "}", mt.end())
                end = len(t) if end < 0 else end + len("\\end{" + name + "}")
                self.blank(mt.start(), end,
                           DISPLAY if name in DISPLAY_ENVS else PARA)
        t = "".join(self.m)
        # 4. display math \[ \] and $$ $$
        for mt in re.finditer(r"\\\[.*?\\\]|\$\$.*?\$\$", t, re.S):
            self.blank(mt.start(), mt.end(), DISPLAY)
        t = "".join(self.m)
        # 5. inline math
        for mt in re.finditer(r"(?<!\\)\$(?:[^$\\]|\\.)+?(?<!\\)\$|\\\(.*?\\\)",
                              t, re.S):
            self.blank(mt.start(), mt.end(), MATH)
            # a sentence that ends inside the math ("... + \mathrm{h.c.}$ In ...")
            inner = re.sub(r"[\s}]+$", "", mt.group(0)[:-1])
            if inner.endswith(".") and mt.end() - mt.start() > 2:
                self.m[mt.end() - 1] = "."
        t = "".join(self.m)
        # 6. commands
        i = 0
        n = len(t)
        while i < n:
            if t[i] != "\\":
                i += 1
                continue
            mt = re.match(r"\\([A-Za-z@]+)\*?", t[i:])
            if not mt:                      # \\, \,, \%, \{ ...
                nxt = t[i + 1] if i + 1 < n else ""
                if nxt in "%&#_{}$":
                    self.blank(i, i + 1)    # keep the literal character
                else:
                    self.blank(i, i + 2)
                i += 2
                continue
            name = mt.group(1)
            j = i + mt.end()
            # optional arguments
            while j < n and t[j] == "[":
                j = _match_bracket(t, j)
            if name in LOWER_REF_CMDS or name in UPPER_REF_CMDS:
                k = _match_brace(t, j) if j < n and t[j] == "{" else j
                self.blank(i, k, REF_UPPER if name in UPPER_REF_CMDS else REF_LOWER)
                i = k
                continue
            if name in DROP_ARG_CMDS:
                k = j
                while k < n and t[k] == "{":
                    k = _match_brace(t, k)
                    while k < n and t[k] == "[":
                        k = _match_bracket(t, k)
                self.blank(i, k)
                i = k
                continue
            if name in BREAK_CMDS:
                k = j
                if name not in {"item", "maketitle", "appendix", "par", "newpage",
                                "clearpage", "bigskip", "medskip", "smallskip"}:
                    while k < n and t[k] == "{":
                        k = _match_brace(t, k)
                self.blank(i, k, PARA)
                i = k
                continue
            if j < n and t[j] == "{" and name in KEEP_ARG_CMDS:
                k = _match_brace(t, j)
                if name in EMPH_CMDS:
                    self.emph_spans.append((j + 1, k - 1))
                self.blank(i, j + 1)
                self.blank(k - 1, k)
                if name == "caption":
                    self.m[i] = PARA
                    self.m[k - 1] = PARA
                i = j + 1
                continue
            # unknown command: drop the name, keep any brace argument as prose
            self.blank(i, j)
            i = j
        out = "".join(self.m)
        out = out.replace("~", " ").replace("{", " ").replace("}", " ")
        return out


# ---------------------------------------------------------------------------
def _line_col(src: str, pos: int) -> tuple[int, int]:
    line = src.count("\n", 0, pos) + 1
    col = pos - (src.rfind("\n", 0, pos) + 1) + 1
    return line, col


def split_sentences(masked: str) -> list[tuple[int, int]]:
    """Return (start, end) spans of sentences in the masked text."""
    spans = []
    n = len(masked)
    start = None
    i = 0
    while i < n:
        c = masked[i]
        if start is None:
            if c.isspace() or c == PARA:
                i += 1
                continue
            start = i
        # paragraph break: PARA marker or blank line
        if c == PARA or (c == "\n" and re.match(r"\n[ \t]*\n", masked[i:i + 50])):
            if start is not None and masked[start:i].strip():
                spans.append((start, i))
            start = None
            i += 1
            continue
        if c in ".!?":
            # abbreviation?
            mw = re.search(r"([A-Za-z.]+)$", masked[max(0, i - 12):i])
            word = mw.group(1).strip(".") if mw else ""
            nxt = masked[i + 1] if i + 1 < n else " "
            if nxt.isspace() or nxt == PARA or i + 1 >= n:
                if word not in ABBREVIATIONS and not (len(word) == 1 and word.isupper()):
                    spans.append((start, i + 1))
                    start = None
        i += 1
    if start is not None and masked[start:].strip():
        spans.append((start, n))
    return spans


WORD_RE = re.compile(r"[A-Za-z0-9\u24c2][A-Za-z0-9'\u2019\-]*")


def lint_text(src: str, fname: str, cfg: Config) -> list[Finding]:
    mk = Masker(src)
    masked = mk.run()
    out: list[Finding] = []

    def add(pos: int, code: str, msg: str, excerpt: str = "", sev="warning"):
        if code in cfg.disabled:
            return
        ln, col = _line_col(src, pos)
        out.append(Finding(fname, ln, col, code, msg, excerpt.strip()[:120], sev))

    def excerpt_at(a: int, b: int) -> str:
        return re.sub(r"\s+", " ", src[a:b])

    for a, b in split_sentences(masked):
        s = masked[a:b]
        words = WORD_RE.findall(s.replace(DISPLAY, " "))
        nwords = len(words)
        has_display = DISPLAY in s
        if nwords > cfg.hard_sentence_words and not has_display:
            add(a, "PL001", f"{nwords} words (hard limit {cfg.hard_sentence_words})",
                excerpt_at(a, b))
        elif nwords > cfg.max_sentence_words and not has_display:
            add(a, "PL015", f"{nwords} words (target {cfg.max_sentence_words})",
                excerpt_at(a, b), "info")
        first = s.lstrip()
        off = a + (len(s) - len(first))
        if first:
            ch = first[0]
            fw = re.match(r"[A-Za-z][A-Za-z0-9\-]*", first)
            token = fw.group(0) if fw else ""
            if ch == MATH:
                add(off, "PL005", "starts with a symbol; recast the sentence",
                    excerpt_at(off, min(b, off + 60)))
            elif ch.isdigit():
                add(off, "PL005", "starts with a numeral; write it in words or recast",
                    excerpt_at(off, min(b, off + 60)))
            elif ch == REF_LOWER:
                add(off, "PL006", "starts with a lower-case reference; use \\Cref",
                    excerpt_at(off, min(b, off + 60)))
            elif (token and re.fullmatch(r"[A-Z][A-Z0-9\-]*[A-Z0-9]", token)
                  and sum(c.isupper() for c in token) >= 2
                  and token not in cfg.known_acronyms):
                add(off, "PL005", f"starts with the acronym '{token}'; recast",
                    excerpt_at(off, min(b, off + 60)))
            if (re.match(r"There\s+(is|are|was|were|exists?|has been|have been)\b", first)
                    or re.match(r"It\s+(is|was|has been|seems|appears)\s+(?:\w+\s+){0,2}?"
                                r"(that|to|whether|how|why)\b", first)):
                add(off, "PL008", "expletive opener; make the real subject the subject",
                    excerpt_at(off, min(b, off + 60)))
            if re.match(r"(This|These|That|Those)\s+(is|are|was|were|means|shows|"
                        r"gives|makes|leads|allows|implies|yields|has|have|can|"
                        r"will|would|suggests|indicates|explains|demonstrates)\b",
                        first):
                add(off, "PL012", "bare demonstrative; name the object ('This kernel ...')",
                    excerpt_at(off, min(b, off + 60)))
        for mt in re.finditer(r":", s):
            p = a + mt.start()
            if cfg.ban_colons and not (mt.start() > 0 and s[mt.start() - 1].isdigit()
                                       and mt.end() < len(s) and s[mt.end()].isdigit()):
                add(p, "PL002", "colon; prefer two sentences", excerpt_at(max(a, p - 40), p + 40))
        if cfg.ban_semicolons:
            for mt in re.finditer(r";", s):
                p = a + mt.start()
                add(p, "PL003", "semicolon; prefer two sentences",
                    excerpt_at(max(a, p - 40), p + 40))
        if cfg.ban_em_dash:
            for mt in re.finditer(r"(?<!-)---(?!-)|\u2014", s):
                p = a + mt.start()
                add(p, "PL004", "em dash; rewrite with a comma or a full stop",
                    excerpt_at(max(a, p - 40), p + 40))
        refs = REF_LOWER + REF_UPPER
        groups = re.findall(r"\([^()]*[" + refs + r"][^()]*\)", s)
        if len(groups) > 1:
            add(a, "PL016", f"{len(groups)} pointers in parentheses; keep one, or make "
                "the reference the subject", excerpt_at(a, min(b, a + 80)), "info")
        for mt in re.finditer(r"\bnot\s+(?:only\s+)?(?:an?\s+|the\s+)?[\w\-]+(?:\s+[\w\-]+){0,2}"
                              r"\s+but\b|,\s*(?:and\s+)?not\s+(?:an?|the)\s+[\w\-]+"
                              r"(?:\s+[\w\-]+){0,3}\s*[.!?]?$", s.rstrip(), re.I):
            p = a + mt.start()
            add(p, "PL017", "antithesis; keep it only if a reader expects the rejected "
                "alternative", excerpt_at(max(a, p - 40), p + 60), "info")
        for pat, advice in cfg.banned:
            for mt in re.finditer(pat, s, re.I):
                p = a + mt.start()
                add(p, "PL007", f"'{mt.group(0)}': {advice}",
                    excerpt_at(max(a, p - 40), p + 40))
        if cfg.anthropomorphic:
            pat = r"\b(" + "|".join(map(re.escape, cfg.anthropomorphic)) + r")\b"
            for mt in re.finditer(pat, s, re.I):
                p = a + mt.start()
                add(p, "PL014", f"'{mt.group(0)}': describe what physically happens",
                    excerpt_at(max(a, p - 40), p + 40), "info")
        for term in cfg.forbidden_terms:
            if term["scope"] == "main" and a >= mk.appendix_at:
                continue
            if term["scope"] == "appendix" and a < mk.appendix_at:
                continue
            for mt in re.finditer(r"\b" + re.escape(term["pattern"]) + r"\b", s, re.I):
                p = a + mt.start()
                use = f"; use '{term['use']}'" if term["use"] else ""
                note = f" ({term['note']})" if term["note"] else ""
                where = " in the main text" if term["scope"] == "main" else ""
                add(p, "PL010", f"'{mt.group(0)}' is not used{where}{use}{note}",
                    excerpt_at(max(a, p - 40), p + 40))

    for ea, eb in mk.emph_spans:
        nw = len(WORD_RE.findall(masked[ea:eb]))
        if nw > cfg.emph_max_words:
            add(ea, "PL009", f"{nw} words in italics; emphasis belongs to single terms",
                excerpt_at(ea, eb))

    # Acronyms: the first use must be a definition "... (ACR)", or listed as known.
    seen: set[str] = set()
    for mt in re.finditer(r"(?<![A-Za-z\-])([A-Z][A-Za-z0-9]*[A-Z](?:-[A-Z]+)*)s?(?![A-Za-z])",
                          masked):
        tok = mt.group(1)
        if sum(c.isupper() for c in tok) < 2 or tok in seen:
            continue
        if re.fullmatch(r"[IVXLC]+", tok):          # roman numerals
            continue
        seen.add(tok)
        if tok in cfg.known_acronyms:
            continue
        before = masked[max(0, mt.start() - 1):mt.start()]
        after = masked[mt.end():mt.end() + 1]
        if before == "(" and after in (")", ","):
            continue
        add(mt.start(), "PL011", f"'{tok}' is used before it is defined as '... ({tok})'",
            excerpt_at(max(0, mt.start() - 40), mt.end() + 20))

    # Hand-typed references, checked in the source outside comments and math.
    if cfg.reference_style == "cleveref":
        for mt in re.finditer(
                r"(?:\b(?:Eqs?|Figs?|Figures?|Secs?|Sections?|Tables?|Appendix|"
                r"Appendices|Refs?)\.?\s*~?\s*\(?\s*)\\(?:ref|eqref)\{|\\eqref\{",
                src):
            if masked[mt.start()] == " " and src[mt.start()] not in "\\":
                # the match starts in blanked text only if it was a comment/math
                pass
            ln_start = src.rfind("\n", 0, mt.start()) + 1
            if "%" in src[ln_start:mt.start()].replace("\\%", ""):
                continue
            add(mt.start(), "PL013", "hand-typed reference; use \\cref / \\Cref",
                excerpt_at(mt.start(), mt.end() + 20))

    out.sort(key=lambda f: (f.line, f.col, f.code))
    return out


# ---------------------------------------------------------------------------
def section_range(src: str, title: str) -> tuple[int, int] | None:
    """Line range of the section whose title contains `title` (case-insensitive)."""
    heads = [(mt.start(), mt.group(1), mt.group(2))
             for mt in re.finditer(r"\\(section|subsection|subsubsection|appendix)\*?"
                                   r"(?:\{([^}]*)\})?", src)]
    level = {"section": 1, "subsection": 2, "subsubsection": 3, "appendix": 0}
    for idx, (pos, kind, t) in enumerate(heads):
        if t and title.lower() in t.lower():
            end = len(src)
            for pos2, kind2, _ in heads[idx + 1:]:
                if level[kind2] <= level[kind]:
                    end = pos2
                    break
            return _line_col(src, pos)[0], _line_col(src, end)[0]
    return None


def format_findings(findings: list[Finding], limit: int | None = None) -> str:
    lines = []
    shown = findings if limit is None else findings[:limit]
    for f in shown:
        tag = "" if f.severity == "warning" else f" [{f.severity}]"
        lines.append(f"{f.file}:{f.line}:{f.col}: {f.code}{tag} {f.message}")
        if f.excerpt:
            lines.append(f"    | {f.excerpt}")
    if limit is not None and len(findings) > limit:
        lines.append(f"... and {len(findings) - limit} more")
    counts: dict[str, int] = {}
    for f in findings:
        counts[f.code] = counts.get(f.code, 0) + 1
    if findings:
        summary = ", ".join(f"{k} x{v}" for k, v in sorted(counts.items()))
        lines.append(f"{len(findings)} findings: {summary}")
    else:
        lines.append("no findings")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Mechanical style checks for LaTeX papers.")
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--config", type=Path)
    ap.add_argument("--section", help="only the section whose title contains this text")
    ap.add_argument("--lines", help="only findings in this line range, e.g. 120-180")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-info", action="store_true", help="hide info-level findings")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--strict", action="store_true", help="exit 1 if there are findings")
    ap.add_argument("--list-checks", action="store_true")
    args = ap.parse_args(argv)

    if args.list_checks:
        for k, v in CHECKS.items():
            print(f"{k}  {v}")
        return 0

    start = args.files[0] if args.files else Path.cwd()
    cfg = load_config(start.resolve(), args.config)
    files = args.files or [cfg.root / f for f in cfg.files]
    if not files:
        print("no input files (pass a .tex file or list files in paperlint.toml)",
              file=sys.stderr)
        return 2

    findings: list[Finding] = []
    for path in files:
        src = path.read_text(encoding="utf-8")
        fs = lint_text(src, str(path), cfg)
        lo, hi = 1, 10 ** 9
        if args.section:
            rng = section_range(src, args.section)
            if rng is None:
                print(f"section '{args.section}' not found in {path}", file=sys.stderr)
                return 2
            lo, hi = rng
        if args.lines:
            a, _, b = args.lines.partition("-")
            lo, hi = max(lo, int(a)), min(hi, int(b or a))
        findings += [f for f in fs if lo <= f.line <= hi]
    if args.no_info:
        findings = [f for f in findings if f.severity != "info"]

    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=1))
    else:
        print(format_findings(findings, args.limit))
    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
