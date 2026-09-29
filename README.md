# paperlint

paperlint helps Claude write and finish scientific papers that read as if a scientist
wrote them: clear, precise and easy to follow. That is its main goal. It is a plugin for [Claude Code](https://claude.com/claude-code),
Anthropic's coding assistant.

Text written with an LLM often has the same problems. It uses technical terms without
defining them, states slogans instead of facts, repeats itself across sections, cites
papers for things they do not say, and refers to things the reader has not seen yet.
paperlint gives Claude a set of writing rules, a fresh reader, a literature agent and
the checks to enforce them, and runs them until the text is finished. Even text
without any of these errors can read as generated: every sentence of the same length,
one definition after another, a paragraph patched with one sentence per review comment.
paperlint rereads every paragraph as a whole and rewrites the ones that read that way.

## Three commands

| Command | Use it when | What you do | What it does |
|---|---|---|---|
| `/paperlint:write` | You need new text: a section, an appendix, a caption, an abstract | Describe the main ideas in your own words | Plans the paragraphs, shows you the plan, writes, finds and verifies the references, then revises the draft until it is finished |
| `/paperlint:revise` | A section exists and should be made as good as it can be | Name the section | Rounds of checks, fresh reads, literature checks and fixes, until a round finds nothing new |
| `/paperlint:finish` | The paper is complete and should be ready to submit | Name the file | Revises every section in order, then checks the paper as one text and writes the abstract last |

All three read the whole paper, not only the section in front of them, because a
section is never independent of the rest: it uses symbols defined elsewhere, builds on
earlier results and must not repeat them. They fix the small things on their own
(definitions, notation, pointers, wording, missing reasons) and ask you only about
content: what the paper claims, what it includes, and anything your code or data must
decide.

## Install

You need Claude Code and Python 3.11 or newer. In a Claude Code terminal, type

```
/plugin marketplace add juardilag/paperlint
/plugin install paperlint@paperlint
```

From a shell, or inside the VS Code extension, where `/plugin` is not available, run

```bash
claude plugin marketplace add juardilag/paperlint
claude plugin install paperlint@paperlint
```

Then type `/reload-plugins` in Claude Code, or restart it. Type `/paperlint` and the
commands appear.

To update later, run `claude plugin marketplace update paperlint` and
`claude plugin update paperlint@paperlint`, then `/reload-plugins`.

## Tutorial

The examples follow an invented paper: a new stochastic method for the dynamics of
atoms in an optical lattice coupled to a phonon bath. It lives in `paper/main.tex`,
with its bibliography in `paper/refs.bib` and its simulation data in `data/`. Open
Claude Code in the folder that contains the paper.

### Step 0. Set up the paper once

```
/paperlint:setup
```

Claude creates `paperlint.toml` (the settings) and `glossary.toml` (one name per
object). It reads the paper and proposes glossary entries, for example "always
*lattice site*, never *node*". You approve them before they are saved.

Then write a short `CLAUDE.md` next to the paper with what Claude cannot guess: where
the code and the data behind each figure are, decisions you have already taken ("all
simulations use periodic boundary conditions"), and content the paper must contain. The commands read it every time,
and they add your decisions to it as you make them.

### Step 1. Write a new section: `/paperlint:write`

Give the file, what to write and where, and then the ideas, as you would explain them
to a co-author. Bullet points, half sentences and equations in plain text are fine.

```
/paperlint:write paper/main.tex new appendix after App. A, "Accuracy of the method" --
- the method is exact when the lattice is non-interacting; say why
- the error grows with the interaction U and falls with the filling; show it with
  Fig. 4 (data in data/error_vs_U.csv)
- the time step: convergence check in Fig. 6, below 1% at dt = 0.01
- compare with the exact solution for 8 sites, which we did in Sec. III B
```

What happens:

1. Claude reads the whole paper, the glossary, `CLAUDE.md` and the data you named.
2. If your ideas leave a content choice open, it asks you, once, with a recommendation.
   For example: "Should the error be shown for both fillings of Fig. 4, or only for
   half filling? I recommend both, since the text claims the error falls with the
   filling." It does not ask about wording or notation.
3. It shows you the plan: one topic sentence per paragraph and, for each, the figure,
   equation or number it rests on. You answer "ok" or change it. This is the only stop.
   Add `--no-confirm` to skip it.
4. It writes the text in the paper's own notation. Every statement about other work
   goes to the literature agent, which reads the papers and verifies the references on
   Crossref. Every number comes from your data, with its source.
5. It inserts the text, adds the pointer from the introduction, and runs
   `/paperlint:revise` on it (step 2).

You get the text in the file, the plan as approved, the references with what each one
supports, the source of every number, and a short list of open questions.

### Step 2. Make a section as good as it can be: `/paperlint:revise`

```
/paperlint:revise paper/main.tex Method
/paperlint:revise paper/main.tex "Derivation of the equations of motion"
/paperlint:revise paper/main.tex 420-560
```

This is the command you will use most. It works in rounds.

1. **Context.** Claude reads the whole paper and keeps a map of it in
   `paperlint_map.md`: what each section establishes, every symbol and term with where
   it is defined, every number with its source.
2. **Checks.** The linter, then Claude's own audits (terms, notation across the whole
   paper, back-references, repetition, claims), then a fresh reader, a second Claude
   that sees only the paper and asks "what is this?", "why?" and "says who?".
3. **Triage.** Each finding goes into one class.
   - *Editorial* findings are fixed without asking. This covers definitions, notation,
     pointers, wording, a missing reason, and detail that belongs in an appendix.
   - *Literature* findings go to the literature agent, which reads the sources and
     quotes them.
   - *Author decisions* are collected for you. This covers claims about your results,
     scope and structure, and anything your code must decide.
   - *Rejected* findings are recorded with a one-line reason.
4. **Self-check.** After fixing, Claude rereads every changed sentence against the
   equations around it and searches the whole paper for every symbol, term and label it
   touched, so an edit does not create a problem somewhere else.
5. **Ledger.** Everything settled goes into `paperlint_ledger.md`. The next round, and
   the next session, will not raise it again.

It stops when a round brings nothing new that must be fixed, or after three rounds. The
report lists the errors found first (a sign, a factor, a claim the data do not
support), then the changes, the literature used, and the questions only you can answer.

What a run typically finds on a derivation appendix: a sign that turns a damping term
into anti-damping, a missing factor of two in a frequency, a symbol that means one thing
in the appendix and another in the main text, and a claim credited to a paper that shows
it only for a special case. The first three are fixed on the spot. For the last, the
literature agent reads the cited paper, quotes what it actually shows, and the text is
changed to match.

### Step 3. Finish the paper: `/paperlint:finish`

```
/paperlint:finish paper/main.tex
```

Use it when every section is written. It runs `/paperlint:revise` on each section in
reading order, updating the map as it goes, so each section is checked against the
revised text before it. Then it reads the paper as one text.

- The introduction promises what the results deliver, and the conclusions claim
  nothing more.
- Each fact appears once. The introduction and the method share no paragraph.
- One meaning per symbol and one name per object, in figures and tables too.
- Every number in the text and captions matches its figure, table or data file.
- Every citation supports its sentence, and the bibliography matches Crossref.
- The abstract is rewritten last, from the finished paper.

It compiles the paper, looks at every page, and reports the state of the paper and the
decisions left to you. Use `--from Results` to start later, or `--skip` for sections you
want left alone.

### Teaching it

When you correct Claude, say whether the correction is general ("never put numbers in
the introduction") or only for this paper ("we always say *filling*, never *density*"). General
corrections become rules in `rules.md`. Decisions for this paper go into `CLAUDE.md`,
`glossary.toml` or the ledger, and every later run follows them.

## Files paperlint keeps next to your paper

| File | Written by | Holds |
|---|---|---|
| `paperlint.toml` | `/paperlint:setup` | Settings of the checker |
| `glossary.toml` | setup, then you | One name per object, words to avoid, appendix-only terms |
| `CLAUDE.md` | you, then the commands | Where code and data are, decisions, required content |
| `paperlint_map.md` | the commands | What each section says, symbols, terms, numbers, labels |
| `paperlint_ledger.md` | the commands | Findings fixed, rejected, or decided by the authors |

You can read and edit all of them. Deleting the map is harmless: it is rebuilt.
Deleting the ledger means old findings can come back.

## Building blocks

The three commands call these. You can also run them on their own.

| Command | Does |
|---|---|
| `/paperlint:lint main.tex --section Introduction` | Mechanical checks only (table below) |
| `/paperlint:review main.tex Introduction` | One fresh read and its triage, no rounds |
| `/paperlint:literature main.tex 120-140` | Finds, reads and quotes the sources behind claims |
| `/paperlint:check-refs refs.bib` | Compares `.bib` entries with Crossref |
| `/paperlint:scientific-writing` | The writing procedure and rules, loaded automatically |

Every time Claude edits a `.tex` file in a folder with a `paperlint.toml`, the checker
also runs on the changed paragraphs, and Claude fixes what it reports straight away.

## What the checker reports

| Code | Problem |
|---|---|
| PL001 | Sentence longer than 27 words |
| PL002, PL003 | Colon or semicolon in a sentence |
| PL004 | Em dash (—) |
| PL005 | Sentence starts with a symbol, a number or an acronym |
| PL006 | Sentence starts with `\cref` instead of `\Cref` |
| PL007 | Vague, informal or stock word, such as "very", "in order to", "recipe", "Notably" or "plays a key role" |
| PL008 | Empty opening, such as "It is clear that" or "There are" |
| PL009 | More than four words in italics |
| PL010 | A word your glossary says to avoid |
| PL011 | Acronym used before it is spelled out |
| PL012 | Sentence starts with a bare "This", as in "This means that" |
| PL013 | Reference typed by hand, such as `Eq.~\ref{…}` |
| PL014 | Things described as if they were people, as in "the model remembers" |
| PL015 | Sentence longer than 25 words (a milder note) |
| PL016 | More than one pointer in parentheses in a sentence, such as "(Sec. II) … (App. A)" (a note) |
| PL017 | The "not X but Y" contrast that LLMs overuse (a note) |
| PL018 | The same modifier three times in a paragraph, as in "exactly … exactly … exact" (a note) |
| PL019 | A paragraph built as a list, "The first … The second …" (a note for two, a warning for three) |
| PL020 | An object acting as an agent, as in "The model tests the kernel" (a note) |

You can also run the checker without Claude, for example before submitting.

```bash
python3 ~/.claude/plugins/marketplaces/paperlint/skills/scientific-writing/scripts/lint.py main.tex
```

## Change the defaults

Some rules are strong preferences rather than universal rules. By default the checker
flags colons, semicolons and em dashes, and sentences longer than 25 words. The writing
rules also keep numbers out of the introduction. You can switch these off. For example,
in `paperlint.toml`,

```toml
[style]
ban_colons = false
hard_sentence_words = 35

[words]
known_acronyms = ["DNA", "GPU"]   # acronyms your readers know without a definition

[checks]
disable = ["PL014"]
```

The file created by `/paperlint:setup` lists every setting with a short explanation.
Your journal's style guide always takes priority.

## For developers

The writing rules are in `skills/scientific-writing/`. `SKILL.md` is the procedure,
`rules.md` holds the full rules, and `examples.md` holds sentences that were rejected
next to the versions that were accepted. The checker and the other scripts are in
`skills/scientific-writing/scripts/`.

```bash
python3 -m unittest discover tests            # run the tests
claude plugin validate .claude-plugin/plugin.json
claude --plugin-dir .                         # try local changes in a session
```

To add a rule, write the general principle in `rules.md` and one rejected/accepted pair
in `examples.md`. To add a check, add it to `lint.py` with a test in `tests/`.

Claude Code only updates an installed plugin when its version changes. Raise `version`
in `.claude-plugin/plugin.json` with every release.

## License

MIT. See [LICENSE](LICENSE).
