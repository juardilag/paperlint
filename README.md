# paperlint

paperlint helps Claude write scientific papers that read as if a careful scientist wrote
them. It is a plugin for [Claude Code](https://claude.com/claude-code), Anthropic's
coding assistant for the terminal.

Text written with an LLM often has the same problems. It uses technical terms without
defining them, states slogans instead of physics, and refers to things the reader has
not seen yet. paperlint gives Claude a set of writing rules and the tools to check them,
so fewer of these problems reach you.

The rules come from a supervisor's line-by-line review of a physics paper written with
Claude. They apply to any field.

## What it does

- **Writing rules.** When you ask Claude to write or revise a section, it follows a
  fixed procedure. It plans the paragraphs, writes, checks its own text, and tells you
  what it changed.
- **Automatic checks.** Every time Claude edits your `.tex` file, a checker reads the
  changed paragraphs. It reports problems such as long sentences, undefined acronyms or
  vague words, and Claude fixes them straight away.
- **A fresh reader.** A second Claude reads one section without seeing your
  conversation. It lists every place where a reader would ask "what is this?" or "why?".
- **Reference check.** Your `.bib` entries are compared with the Crossref database, and
  wrong years, volumes or pages are reported.

## Install

You need Claude Code and Python 3.11 or newer. In Claude Code, type

```
/plugin marketplace add juardilag/paperlint
/plugin install paperlint@paperlint
```

Then restart Claude Code. Type `/paperlint` and you should see the commands listed below.

## Use it on your paper

Open Claude Code in the folder that contains your paper, for example `main.tex` and
`refs.bib`.

**1. Set up the paper.** Type `/paperlint:setup`. Claude creates two small files next to
your paper. `paperlint.toml` holds the settings, and `glossary.toml` records which name
the paper uses for each object. Claude reads your paper and suggests glossary entries,
for example "always say *memory kernel*, never *memory function*". You approve them
before they are saved. The automatic checks only run in folders that have a
`paperlint.toml`, so your other projects are not affected.

**2. Write or revise.** Ask in plain words, for example "Revise the introduction of
main.tex". Claude follows the writing rules on its own. At the end it lists what it
changed. It also lists open questions, such as a claim about another paper that it could
not verify.

**3. Check a section.** Type `/paperlint:lint main.tex --section Introduction`. You get
a list of problems with their line numbers, and Claude offers to fix them.

**4. Get a fresh read.** Type `/paperlint:review main.tex Introduction`. The fresh reader
reads the section and reports what a reader would not understand. Claude checks each
point before passing it on to you.

**5. Check the references.** Type `/paperlint:check-refs refs.bib`. Claude shows which
entries disagree with Crossref and suggests missing DOIs. Nothing changes without your
approval. Very old papers and book chapters are often missing from Crossref, so check
those by hand.

**6. Teach it.** When you correct Claude, say whether the correction is general or only
for this paper. General corrections become new rules. Choices for this paper go into
`glossary.toml` or into a `CLAUDE.md` file in the paper's folder, which Claude reads
every time.

## What the checker reports

| Code | Problem |
|---|---|
| PL001 | Sentence longer than 27 words |
| PL002, PL003 | Colon or semicolon in a sentence |
| PL004 | Em dash (—) |
| PL005 | Sentence starts with a symbol, a number or an acronym |
| PL006 | Sentence starts with `\cref` instead of `\Cref` |
| PL007 | Vague or informal word, such as "very", "in order to" or "recipe" |
| PL008 | Empty opening, such as "It is clear that" or "There are" |
| PL009 | More than four words in italics |
| PL010 | A word your glossary says to avoid |
| PL011 | Acronym used before it is spelled out |
| PL012 | Sentence starts with a bare "This", as in "This means that" |
| PL013 | Reference typed by hand, such as `Eq.~\ref{…}` |
| PL014 | Physical objects described as people, as in "the bath remembers" |
| PL015 | Sentence longer than 25 words (a milder note) |

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

## License

MIT. See [LICENSE](LICENSE).
