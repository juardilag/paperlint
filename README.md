# paperlint

paperlint is a [Claude Code](https://claude.com/claude-code) plugin for scientific
papers. It does what a language model does reliably: it checks. It finds undefined
terms, inconsistent notation, numbers that do not match their data, claims stronger
than the evidence, limitations without their consequence, incomplete derivations and
captions that do not reproduce their figure, and fixes each with the smallest edit.

The prose belongs to the authors. paperlint does not rewrite text in rounds toward a
checklist, because that is what makes text read as generated. When asked to rewrite, it
drafts once from a paragraph plan the author approved, in the style of published papers
the authors chose, and keeps the new version only if a blind comparison prefers it.

## Install

You need Claude Code and Python 3.11 or newer. In Claude Code:

```
/plugin marketplace add juardilag/paperlint
/plugin install paperlint@paperlint
```

or from a shell, `claude plugin marketplace add juardilag/paperlint` and `claude plugin
install paperlint@paperlint`. Then run `/reload-plugins`. To update, run `claude plugin
marketplace update paperlint` and `claude plugin update paperlint@paperlint`.

## Getting started

Open Claude Code in the paper's folder and run `/paperlint:setup`. It creates
`paperlint.toml` and `glossary.toml`, builds a `CLAUDE.md` with the script and data
behind every figure, and asks for two or three published papers whose writing you
admire. Paragraphs from those papers go into `style_examples.md`, which is what every
draft is matched to. Then set the reader:

```toml
[paper]
audience = "PRB: cold atoms and condensed-matter theory"
```

## Commands

| Command | Use it to |
|---|---|
| `/paperlint:setup` | Prepare a paper once: settings, glossary, `CLAUDE.md`, style examples |
| `/paperlint:revise` | Check a section and fix its errors; `--rewrite` for a planned rewrite |
| `/paperlint:review` | Report on a section without editing |
| `/paperlint:write` | Draft new text from your ideas, via a plan you approve |
| `/paperlint:finish` | Check every section, then the paper as one text |
| `/paperlint:lint`, `/paperlint:literature`, `/paperlint:check-refs` | Run the checker, the source search or the Crossref check on its own |

`revise` checks the section against the whole paper, its code and its data, and fixes
errors with minimal edits. With `--rewrite` it first shows you a plan, one claim per
paragraph, and drafts only after you approve it.

## Agents

Each agent is a separate Claude that has not seen the conversation. It reads and
reports; it never edits.

| Agent | Reports |
|---|---|
| `referee` | wrong, doubtful or overstated claims and limitations without consequence; never style |
| `cold-reader` | at most five places where a reader from a neighbouring field gets lost |
| `literature` | whether the cited sources say what the text claims, with quotes |
| `compare` | which of two versions, shown blind, reads more like your example papers, and whether they make the same claims |

## Files next to the paper

| File | Holds |
|---|---|
| `paperlint.toml` | Checker settings and the audience |
| `glossary.toml` | One name per object, words to avoid |
| `style_examples.md` | Published paragraphs to match, and your style corrections as before/after pairs |
| `CLAUDE.md` | Decisions with who and why, required content, which script and data make each figure and number |
| `paperlint_map.md` | Where each symbol, term and number is defined |
| `paperlint_ledger.md` | Findings fixed, rejected or decided, so later runs do not raise them again |

When you correct Claude, the correction is stored where it works: a content decision in
`CLAUDE.md` or the glossary, a style correction as a before/after pair. Style
corrections never become rules.

## The checker

`lint.py` reports **errors** by default: an acronym used before it is defined, a term
the glossary avoids, a hand-typed reference, a lower-case reference macro at a sentence
start. It also runs on every paragraph Claude edits in a folder with a
`paperlint.toml`, and asks only for the smallest fix.

Style checks (sentence length, colons and semicolons, openers, stock phrases, repeated
words, list-shaped paragraphs) are off by default. Run them as notes with `--style`, or
switch some on in `paperlint.toml`:

```toml
[checks]
enable = ["PL007"]       # stock phrases
```

`--list-checks` lists every code and marks which are errors.

## Development

The rules are in `skills/scientific-writing/rules.md` (correctness only), the author
corrections in `examples.md`, the checker and its scripts in
`skills/scientific-writing/scripts/`, the agents in `agents/`, and each command in
`skills/<command>/SKILL.md`.

```bash
python3 -m unittest discover tests
claude plugin validate .claude-plugin/plugin.json
```

A rule is added only for an error a checker or a reader can verify, and replaces the
rule it overlaps. Raise `version` in `.claude-plugin/plugin.json` with every change.

## License

MIT. See [LICENSE](LICENSE).
