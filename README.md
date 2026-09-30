# paperlint

paperlint is a [Claude Code](https://claude.com/claude-code) plugin for writing and
revising scientific papers. Its aim is prose that reads as written by a scientist for
the paper's readers, and is no longer than its ideas need.

Text drafted with a language model fails in recognisable ways. It uses terms before
defining them, states slogans instead of results, repeats itself across sections and
cites papers for claims they do not make. It is also too long, and its rhythm gives it
away: sentences of one length, chains of definitions, paragraphs patched with one
sentence per review comment. After a review it often swings the other way and explains
what every reader of the journal knows. paperlint checks for each of these failures and
fixes them section by section, reading each section against the whole paper.

## Install

You need Claude Code and Python 3.11 or newer. In Claude Code, type

```
/plugin marketplace add juardilag/paperlint
/plugin install paperlint@paperlint
```

or, from a shell or the VS Code extension,

```bash
claude plugin marketplace add juardilag/paperlint
claude plugin install paperlint@paperlint
```

Then run `/reload-plugins`. To update, run `claude plugin marketplace update paperlint`
and `claude plugin update paperlint@paperlint`, then `/reload-plugins` again.

## Commands

| Command | Use it to |
|---|---|
| `/paperlint:setup` | Prepare a paper once: settings, glossary and `CLAUDE.md` |
| `/paperlint:write` | Draft a new section from your ideas |
| `/paperlint:revise` | Bring an existing section to a finished state |
| `/paperlint:finish` | Revise every section in order, then check the paper as one text |
| `/paperlint:review` | Read a section once and report, without editing |

`revise` does most of the work. Each round runs the checker, audits the section
(terms, notation, claims against the data, the length the section's ideas need, the
rhythm of every paragraph) and sends it to two reviewing agents. Wording, definitions,
notation and pointers are fixed without asking. Questions about what the paper claims
or includes go to you. The run stops when a round finds nothing new, or after three
rounds, and reports the errors it found first.

The smaller commands `/paperlint:lint`, `/paperlint:literature` and
`/paperlint:check-refs` run one piece on its own: the checker, the source search, or a
comparison of the `.bib` file with Crossref.

## Agents

Each agent is a separate Claude that has not seen the conversation. It reads and
reports, and never edits.

| Agent | Reads as | Finds |
|---|---|---|
| `cold-reader` | a scientist from a neighbouring field | undefined terms, unclear references, missing reasons, paragraphs that read as generated |
| `referee` | an expert of the paper's field | wrong or overstated claims, limitations without consequence, pedantry |
| `literature` | a reader of the cited papers | claims the sources do not make; it quotes them and checks references on Crossref |

The cold reader asks for definitions and the referee calls some of them pedantic. The
`audience` in `paperlint.toml` settles the conflict. A term that reader knows gets a
reference, and a term the argument turns on gets a short clause with its meaning.

## Getting started

Open Claude Code in the folder of the paper and run `/paperlint:setup`. It creates
`paperlint.toml` and `glossary.toml`, proposes one name for each object the paper names
in two ways, and builds a `CLAUDE.md`. The `CLAUDE.md` maps each figure to the script
and data that produce it, and lists the decisions and required content it found in
review files. Nothing is saved until you approve it. Then set the reader:

```toml
[paper]
audience = "PRB: cold atoms and condensed-matter theory"
```

A typical session follows.

```
/paperlint:write main.tex new appendix "Accuracy of the method" --
- exact without interactions; say why
- the error grows with U, Fig. 4 (data/error_vs_U.csv)
- converged below 1% at dt = 0.01

/paperlint:revise main.tex Method
/paperlint:finish main.tex
```

`write` asks at most one question about content, shows you a plan of one topic
sentence per paragraph, drafts, and then revises the draft. `finish` rewrites the
abstract last.

When you correct Claude, say whether the correction is general or holds for this paper
only. A general correction becomes a rule in `rules.md`. One for this paper only goes to
`CLAUDE.md` or the glossary. Comments from co-authors can come as an annotated PDF.
Claude reads the highlights, strike-outs and notes, checks which still apply, and
reports where two co-authors disagree.

## Files next to the paper

| File | Holds |
|---|---|
| `paperlint.toml` | Checker settings and the audience |
| `glossary.toml` | One name per object, words to avoid, appendix-only terms |
| `CLAUDE.md` | Decisions with who and why, required content, which script and data make each figure |
| `paperlint_map.md` | What each section says, and where each symbol, term and number is defined |
| `paperlint_ledger.md` | Findings fixed, rejected or decided, so later runs do not raise them again |

You can edit all of them. The map is rebuilt when deleted. Deleting the ledger lets
settled findings come back.

## The checker

The checker `lint.py` also runs on every paragraph Claude edits in a folder with a
`paperlint.toml`. Codes marked *note* are hints that can be false positives.

| Code | Flags |
|---|---|
| PL001, PL015 | Sentence over 27 words, or over 25 (*note*) |
| PL002–PL004 | Colon, semicolon or em dash in running text |
| PL005, PL006 | Sentence opening with a symbol, number or acronym, or with `\cref` |
| PL007, PL008 | Vague or stock words ("very", "Notably"), empty openers ("It is clear that") |
| PL009 | More than four words in italics |
| PL010, PL011 | A word the glossary avoids, an acronym used before it is defined |
| PL012, PL013 | A bare "This" as subject, a hand-typed reference (`Eq.~\ref`) |
| PL014 | Objects described as people ("the model remembers") |
| PL016, PL017 | Several parenthetical pointers in one sentence, "not X but Y" (*notes*) |
| PL018–PL020 | Repeated modifier, paragraph built as a list, object as agent (*notes*) |
| PL022 | Paragraph over 150 words (*note*) |

Run it on its own with
`python3 ~/.claude/plugins/marketplaces/paperlint/skills/scientific-writing/scripts/lint.py main.tex`.
The `--words` flag prints the prose length of a section. Limits and bans are set in
`paperlint.toml`:

```toml
[style]
ban_colons = false
hard_sentence_words = 35

[words]
known_acronyms = ["DNA", "GPU"]

[checks]
disable = ["PL014"]
```

The file that `setup` creates lists every setting. Your journal's style guide takes
precedence.

## Development

The rules are in `skills/scientific-writing/rules.md`, with rejected and accepted
sentences in `examples.md`. The checker and its scripts are in
`skills/scientific-writing/scripts/`, the agents in `agents/`, and each command in
`skills/<command>/SKILL.md`.

```bash
python3 -m unittest discover tests
claude plugin validate .claude-plugin/plugin.json
claude --plugin-dir .
```

A new rule states its general principle in `rules.md` and adds one example pair. If it
conflicts with an existing rule, rewrite the old one so that both hold. A new check goes
into `lint.py` with a test. Raise `version` in `.claude-plugin/plugin.json` with every
change, since Claude Code updates a plugin only when its version changes.

## License

MIT. See [LICENSE](LICENSE).
