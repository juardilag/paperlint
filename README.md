# paperlint

A [Claude Code](https://claude.com/claude-code) plugin for writing scientific papers that
read as written by a careful scientist, not by an LLM.

LLM-assisted papers fail in a recognisable way. The prose is informal and overly
technical at the same time: slogans instead of physics ("the relation is an identity of
the construction"), standard terms used without definition ("white noise", "master
equation"), pronouns that point nowhere, and sentences that assume the reader already
knows the paper. paperlint turns the rules that prevent this into something Claude
follows and checks:

| Part | What it does |
|---|---|
| **`scientific-writing` skill** | A writing procedure (plan, draft, audit, report), a one-page checklist, the full rules, and a bank of flagged → accepted rewrites. |
| **Linter** (`lint.py`) | Mechanical checks on LaTeX: sentence length, colons and semicolons, em dashes, sentence openers, banned phrases, acronyms used before definition, terms your paper has decided not to use, hand-typed references. |
| **Edit hook** | After Claude edits a `.tex` file, the linter runs on the edited paragraphs and Claude sees the report immediately. |
| **`cold-reader` agent** | Reads one section with no context, as a scientist from a neighbouring field, and lists every "what is this?", "which one?" and "why?". |
| **Reference checker** (`check_refs.py`) | Compares `.bib` entries with Crossref and suggests missing DOIs. |
| **Per-paper config** | `paperlint.toml` (style settings) and `glossary.toml` (one name per object). |

The rules come from a supervisor's line-by-line review of an LLM-assisted physics paper
and from the co-authors' later corrections. They are written for any field, with the
original examples kept as illustrations.

Requirements: Claude Code, and Python ≥ 3.11 on the `PATH` as `python3`. No Python
packages are needed.

---

## Tutorial

This walk-through takes a LaTeX paper from first setup to a reviewed section. It assumes
your paper is in `~/mypaper/` with `main.tex` and `refs.bib`.

### 1. Install the plugin

In Claude Code:

```
/plugin marketplace add juardilag/paperlint
/plugin install paperlint@paperlint
```

Or from a shell:

```bash
claude plugin marketplace add juardilag/paperlint
claude plugin install paperlint@paperlint
```

To try it without installing, start Claude Code with the plugin loaded for one session:

```bash
git clone https://github.com/juardilag/paperlint.git
claude --plugin-dir ./paperlint
```

Check that it loaded: `/paperlint:lint` should appear when you type `/paperlint`.

### 2. Set up your paper

Open Claude Code in your paper's directory and run

```
/paperlint:setup
```

This creates two files next to `main.tex` (it never overwrites existing ones):

- `paperlint.toml`: which files to lint, sentence limits, extra banned words, checks to
  switch off. Every setting is optional and documented in the file.
- `glossary.toml`: your terminology decisions. Claude reads the paper and proposes entries
  for objects that appear under several names, specialist terms that belong in the
  appendices, and symbols. You approve them before they are written.

The edit hook is **opt-in**: it runs only for `.tex` files in a directory tree that
contains a `paperlint.toml`. Your other LaTeX projects are not affected.

You can do the same without Claude:

```bash
python3 paperlint/skills/scientific-writing/scripts/init_project.py ~/mypaper
```

Optionally, add a short `CLAUDE.md` to the paper directory for decisions that are not
terminology: required content ("the recovery of method X must be in the main text"),
the build command, and what has been revised so far. Claude reads it automatically.

### 3. See where the paper stands

```
/paperlint:lint main.tex
```

You get findings like

```
main.tex:52:41: PL002 colon; prefer two sentences
    | bath entering the dynamics quadratically: it is integrated out exactly, so the d
main.tex:57:35: PL007 'recipe': write 'procedure' or 'method'
main.tex:442:15: PL005 starts with a symbol; recast the sentence
188 findings: PL001 x86, PL002 x38, PL003 x28, PL005 x4, PL007 x9, ...
```

Restrict it to one section or a line range:

```
/paperlint:lint main.tex --section Method
/paperlint:lint main.tex --lines 200-320
```

The linter also runs from a shell, without Claude, for example in CI:

```bash
python3 paperlint/skills/scientific-writing/scripts/lint.py main.tex --section Introduction
python3 paperlint/skills/scientific-writing/scripts/lint.py --list-checks
python3 paperlint/skills/scientific-writing/scripts/lint.py main.tex --json --strict
```

### 4. Write or revise a section

Ask Claude in plain words, for example

> Revise the method section of main.tex following the scientific-writing rules.

The `scientific-writing` skill loads automatically for writing tasks (you can also call
it as `/paperlint:scientific-writing`). Claude then

1. reads `paperlint.toml`, `glossary.toml`, `CLAUDE.md` and the earlier sections;
2. plans the paragraphs by their topic sentences (why, what is known, what we do);
3. drafts, following the checklist and the accepted examples;
4. runs the audits: the linter, and checks of terms, notation, parameters,
   back-references, redundancy and claims;
5. compiles and looks at the pages;
6. reports what changed, with before/after for anything you flagged, and lists open
   questions (for example, claims about other papers it could not verify).

While Claude edits, the hook lints each edited paragraph and feeds the findings back, so
mechanical problems are fixed as they appear rather than at the end.

### 5. Get a cold read

```
/paperlint:review main.tex "Method"
```

The `cold-reader` agent reads that section as someone who has never seen the paper and
knows nothing of your conversation. It checks earlier sections before calling a term
undefined. Claude then triages its findings (confirms or rejects each one) and proposes
fixes. This catches the problems the writer cannot see, because the writer already knows
what every term means.

### 6. Check the references

```
/paperlint:check-refs refs.bib
/paperlint:check-refs refs.bib --keys Lindblad1976,Rabi1937
```

Each entry is looked up on Crossref, by DOI when present, otherwise by title, first
author and year. Mismatched fields are reported with Crossref's value, and missing DOIs
are suggested. Nothing is changed without your approval. Old papers, book chapters and
some preprints are not on Crossref and are reported as "not found": check those by hand.
Set `PAPERLINT_MAILTO=you@example.org` to use Crossref's polite pool.

### 7. Teach it your corrections

When you or a co-author correct Claude, say whether the correction is general or specific
to this paper. Claude records it:

- a general rule goes into `rules.md` of the skill (in your installed copy, or better,
  as a pull request to this repository);
- a terminology decision goes into `glossary.toml`, where the linter enforces it;
- anything else specific to the paper goes into its `CLAUDE.md`.

Each rule is stated as a principle with one flagged/accepted example. This is how the
rules in this repository were built.

---

## Reference

### Checks

| Code | Check | Severity |
|---|---|---|
| PL001 | sentence longer than `hard_sentence_words` (default 27) | warning |
| PL015 | sentence longer than `max_sentence_words` (default 25) | info |
| PL002 | colon in running text (ratios such as 1:4 are allowed) | warning |
| PL003 | semicolon in running text | warning |
| PL004 | em dash (`---` or —); en dashes in ranges and names are fine | warning |
| PL005 | sentence starts with a symbol, a numeral or an acronym | warning |
| PL006 | sentence starts with `\cref` instead of `\Cref` | warning |
| PL007 | banned phrase (fluff, informal words for methods, LLM-isms) | warning |
| PL008 | expletive opener ("It is clear that …", "There are …") | warning |
| PL009 | italics on more than `emph_max_words` words | warning |
| PL010 | term the glossary says to avoid here | warning |
| PL011 | acronym used before it is defined as "… (ACR)" | warning |
| PL012 | bare demonstrative ("This means …", "This is …") | warning |
| PL013 | hand-typed reference (`Eq.~\ref{…}`, `\eqref`) with `reference_style = "cleveref"` | warning |
| PL014 | anthropomorphic verb ("remembers", "sees", "inherits") | info |

The linter masks math, comments, citations and commands instead of parsing LaTeX, so
every finding keeps its line and column. Math inside a sentence counts as one word;
display equations are ignored for sentence length. Text after `\appendix` is treated as
appendix for glossary scopes.

### `paperlint.toml`

```toml
[paper]
files = ["main.tex"]
bib = ["refs.bib"]
glossary = "glossary.toml"

[style]
max_sentence_words = 25
hard_sentence_words = 27
ban_colons = true
ban_semicolons = true
ban_em_dash = true
emph_max_words = 4
reference_style = "cleveref"   # or "any"

[words]
known_acronyms = ["DNA"]                     # need no definition in your field
allow = ["\\bvery\\b"]                       # switch off a default banned pattern
ban = ["clearly", { pattern = "\\bstate-of-the-art\\b", advice = "say what it improves on" }]
anthropomorphic = ["believes"]

[checks]
disable = ["PL014"]
```

### `glossary.toml`

```toml
known_acronyms = []

[[term]]
name = "memory kernel"                       # the name used in the text
avoid = ["retarded self-energy", "memory function"]
avoid_in = "main"                            # "main", "appendix" or "all"
note = "the appendix names it the retarded self-energy once"

[[term]]
name = "Weyl symbol"
appendix_only = true                         # flagged anywhere before \appendix
main_text = "function that represents the operator"

[[symbol]]                                   # documentation for Claude and the cold reader
symbol = "\\theta(\\tau)"
meaning = "Heaviside step function"
defined = "Sec. II, step 2"
```

### House defaults

A few rules are strong preferences of the original authors rather than universal rules:
no colons or semicolons in running text, no em dashes, sentences under 25 words, and no
numerical results in the introduction. They are on by default because they push LLM
prose toward plain English. Switch the mechanical ones off in `paperlint.toml` and
override the others in your paper's `CLAUDE.md`. Your journal's style always wins.

### Repository layout

```
.claude-plugin/plugin.json          plugin manifest
.claude-plugin/marketplace.json     lets users install from this repository
skills/scientific-writing/          the main skill
    SKILL.md                        procedure and checklist (always loaded)
    rules.md                        full rules (loaded on demand)
    examples.md                     flagged → accepted rewrites
    scripts/lint.py                 the linter
    scripts/hook_postedit.py        the edit hook
    scripts/check_refs.py           the reference checker
    scripts/init_project.py         creates the per-paper config
skills/{lint,review,check-refs,setup}/SKILL.md   slash commands
agents/cold-reader.md               the review agent
hooks/hooks.json                    PostToolUse hook on Edit|Write|MultiEdit
templates/                          paperlint.toml and glossary.toml templates
tests/                              unit tests and fixtures
```

## Development

```bash
python3 -m unittest discover tests      # 35 tests, no network
claude plugin validate .claude-plugin/plugin.json
claude --plugin-dir .                   # try your changes in a session
```

New checks belong in `lint.py` with a test in `tests/test_lint.py` and a line in the
checks table above. New rules belong in `rules.md`, with one flagged/accepted example in
`examples.md`. Keep rules general: an example may come from one field, the principle
must not.

## License

MIT. See [LICENSE](LICENSE).
