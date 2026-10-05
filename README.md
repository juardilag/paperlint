# paperlint

paperlint is a [Claude Code](https://claude.com/claude-code) plugin for scientific
papers. It does what a language model does reliably: it checks. It finds undefined
terms, inconsistent notation, numbers that do not match their data, claims stronger
than the evidence, limitations without their consequence, incomplete derivations and
captions that do not reproduce their figure, and fixes each with the smallest edit.

The prose belongs to the authors. paperlint does not rewrite text in rounds toward a
checklist, because that is what makes text read as generated. When it writes, it aims
for prose that reads as a physicist wrote it, and it measures whether it got there.

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
behind every figure. Then set the reader:

```toml
[paper]
audience = "PRB: cold atoms and condensed-matter theory"
```

## Human-like writing

paperlint learns how to write from published physics papers, not from style rules.
`corpus.py build` fetches a set of well-written papers (listed in
`skills/scientific-writing/corpus_ids.txt`) into `~/.paperlint/corpus`, outside the
repository, and labels each paragraph by its job: opening, method, results, appendix,
conclusion or caption. Before writing a paragraph, paperlint lists the facts it must
carry, retrieves three real paragraphs that do the same job, and drafts from those
alone, without looking at the old wording. It may add what published paragraphs are
full of and fact lists lack: how a paragraph follows from the previous one, what a
result means, a remark that guides the reader. It never adds a claim.

Your own edits teach it too: after you rewrite Claude's text by hand, run
`/paperlint:learn`, and the before/after pairs go to `author_edits.md`, which every
draft reads. This is the strongest signal paperlint has, because your text is the
voice the paper should have.

Length is set the same way. `blindtest.py budget` gives every section a budget: the
median length of published sections that do the same job, with the upper quartile as
the limit. A section over its limit has too many ideas; paperlint proposes which to
move to an appendix or cut, and you decide. It never meets a budget by compressing the
same ideas into fewer words, which is what makes generated text dense.

The result is measured, not assumed. `/paperlint:blindtest` mixes paragraphs of your
paper with held-out published ones, and a blind judge gives each, on its own, a
probability of being written by a person. The score is the separation (AUC): 0.5 means
your paragraphs cannot be told from published prose, 1.0 that they always can. A
control with two groups of published authors scores at chance, so the test measures
generated prose, not a change of author. Text drafted by a language model still
scores high on it, which is why paperlint works best when the authors write the key
paragraphs and paperlint checks them.

## Commands

| Command | Use it to |
|---|---|
| `/paperlint:setup` | Prepare a paper once: settings, glossary, `CLAUDE.md` |
| `/paperlint:revise` | Check a section and fix its errors; `--rewrite` for a planned rewrite |
| `/paperlint:review` | Report on a section without editing |
| `/paperlint:write` | Draft new text from your ideas, via a plan you approve |
| `/paperlint:comments` | Implement a round of comments (annotated PDF, review notes): only the commented sections and what they affect, references, a one-page summary |
| `/paperlint:finish` | Check every section, then the paper as one text |
| `/paperlint:blindtest` | Measure how far the prose is from published prose (blind judge) |
| `/paperlint:learn` | Record your hand edits as pairs that drafts imitate |
| `/paperlint:lint`, `/paperlint:literature`, `/paperlint:check-refs` | Run the checker, the source search or the Crossref check on its own |

`revise` checks the section against the whole paper, its code and its data, and fixes
errors with minimal edits. A paragraph that collects two or more fixes is redrafted
instead of patched. With `--rewrite` it first shows you a plan, one claim per
paragraph, drafts only after you approve it, and reports the blind-test score before
and after.

`comments` works one round of review at a time. Attach the annotated PDF in the chat
(or drop it in `review/<date>/` next to the main file) and run `/paperlint:comments`;
add anything else in plain words, such as "also add key references on X" or "leave
App. B alone". Settings for every round go in `[comments]` of `paperlint.toml`. It changes only the sections with
comments, plus the appendices, figures and numbers those changes affect (unless you
exclude them), rereads until every comment is implemented, adds verified references
(`--topics` for key works on a subject), and leaves in the same folder a diff and a
one-page summary of what the comments say about how you write. The paper is compiled
where it lives; the round folder can be deleted afterwards.

## Agents

Each agent is a separate Claude that has not seen the conversation. It reads and
reports; it never edits.

| Agent | Reports |
|---|---|
| `referee` | wrong, doubtful or overstated claims and limitations without consequence; never style |
| `cold-reader` | at most five places where a reader from a neighbouring field gets lost |
| `literature` | whether the cited sources say what the text claims, with quotes |
| `compare` | which of two versions, shown blind, reads more like real paragraphs of the same job, and whether they make the same claims |
| `judge` | for the blind test: which paragraphs are published and which generated, and the tells |

## Files next to the paper

| File | Holds |
|---|---|
| `paperlint.toml` | Checker settings and the audience |
| `glossary.toml` | One name per object, words to avoid |
| `CLAUDE.md` | Decisions with who and why, required content, which script and data make each figure and number |
| `author_edits.md` | Your hand edits of Claude's text, as before/after pairs (`/paperlint:learn`) |

No history of findings is kept. Earlier versions kept a ledger of every finding and a
saved map of the paper; agents that read them repeated old wording and old disputes.
What was fixed is in git, a rejected finding is explained once in the report, and the
reviewers read the text fresh every time. A content decision goes to `CLAUDE.md` or the
glossary; a style correction is an edit you make, recorded with `/paperlint:learn`.
Neither becomes a rule.

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

The rules are in `skills/scientific-writing/rules.md` (correctness only), the tells
and readers' objections in `examples.md`, the corpus list in `corpus_ids.txt`, the
checker and its scripts in
`skills/scientific-writing/scripts/`, the agents in `agents/`, and each command in
`skills/<command>/SKILL.md`.

```bash
python3 -m unittest discover tests
claude plugin validate .claude-plugin/plugin.json
```

A rule is added only for an error a checker or a reader can verify, and replaces the
rule it overlaps. A change to how paperlint writes is kept only if the blind test on a
fixed sample (same paper, same seed, two seeds) does not get worse. Raise `version` in
`.claude-plugin/plugin.json` with every change.

## License

MIT. See [LICENSE](LICENSE).
