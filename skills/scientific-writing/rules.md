# Rules for scientific writing

These rules are about **correctness and clarity**, which a checker can enforce. They
are deliberately few. **Style is not a rule.** It comes from the paragraphs in the
paper's `style_examples.md` (published prose the authors admire, in the target journal)
and from the authors' own corrections in `examples.md`. Style rules applied
mechanically (sentence-length caps, punctuation bans, banned openers) make prose read
as generated, so paperlint does not enforce them; `lint.py --style` still offers them
as notes for an author who wants to read them.

The authors own the prose. A paragraph the authors wrote or approved is changed only to
fix an error, with the smallest edit that fixes it, unless they ask for a rewrite.

## 1. Every term is defined where it is first used
- A technical term, symbol or acronym gets its meaning at its first use in the paper,
  in a clause, with a reference where the field has one. A reader of the journal
  (`audience` in `paperlint.toml`) who knows the term gets the reference only.
- A term that needs more than a clause is described in plain words in the main text,
  and the term itself is kept for the appendix.
- A pronoun or "this" points to one object just named.

## 2. One name and one symbol per object
- The same object has the same name and symbol in every section, figure, legend and
  table (`glossary.toml`). One symbol has one meaning in the whole paper.
- Typography is the same in every equation (hats, bold, indices).

## 3. Claims are no stronger than the evidence
- Every number in the text comes from saved data and a script that prints it.
  Recompute it before quoting it; never take it from a comment, a README table or
  memory.
- A result is stated as strongly as its figure and data show, no more ("agrees within
  the statistical error" is checked against the error).
- The paper's own choices (a bath, a parameter) are stated as choices, not as facts
  about a regime.
- State the general case first, then the paper's instance ("1/S for a spin of length
  S, so 2/N here"). Test every general statement of the method on every example the
  paper treats; a statement with an exception says so.
- Statements about other work are checked against the source (the `literature`
  agent), and credit says what that work did and what this paper adds.

## 4. Every limitation has its consequence
- An approximation, a dropped term or a growing error is stated with whether it
  invalidates the results and in which regime or timescale the method holds, with a
  pointer to where the paper tests it.
- A test that isolates one effect says why it isolates it.
- A stochastic equation states Itô or Stratonovich next to it.

## 5. The method contains what the results use
- Every parameter or ingredient a results section uses is introduced in the method,
  with how it enters. A parameter the results never vary does not belong in the paper
  (check the code).
- A results section applies the method: its equations of motion follow from the
  general ones and agree with the code behind the figure.

## 6. The main text argues, the appendix proves
- Each section says why, what is known and what it does. Results that matter stay in
  the main text; their derivation and the technical detail go to an appendix.
- A derivation is one ordered chain: the model and its terms first, each step from the
  ones before, the approximation last, remarks after. A derivation that fails this is
  rewritten as a whole.
- Every numerical step the results rely on (noise sampling, discretisation,
  truncation, boundary terms, the integrator) is described well enough to
  reimplement, and agrees with the code.

## 7. Captions reproduce the figure
- A caption says what is plotted against what, the model and every parameter, the
  sampling, and what each line, marker and band is, so the figure can be reproduced
  from it. Settings shared by all panels are given once.
- Whether a caption also states the takeaway, and how long it runs, is style: follow
  the paper's `style_examples.md`. A takeaway it states must match the text and the
  data.
- Legends and axis labels use the text's terms; re-render the figure after a change
  of term.

## 8. Each fact is stated once
- A fact appears once in the paper, in the section that shows it. A premise that a
  later argument needs is recalled where it is needed.

## 9. LaTeX mechanics
- Cross-reference with one mechanism (`\cref`/`\Cref`, `\Cref` at a sentence start),
  never by hand.
- Every displayed equation fits its column: no `Overfull \hbox` in the log for the
  text you touched; render the page and look at it.
- New references go into the `.bib` file, and the authors are told which.

## 10. Maintaining the rules
- A rule is added only for an error a checker or a reader can verify, never for
  taste. Before a rule is added, find the rule it overlaps and merge them; this file
  does not grow by more than it shrinks without a reason.
- An author correction about style becomes a before/after pair in `examples.md` (or
  in the paper's `style_examples.md` if it concerns one paper), not a rule.
- An author correction about content goes to the paper's `CLAUDE.md` or
  `glossary.toml`.

## 11. The project file `CLAUDE.md`
`CLAUDE.md` holds what a reader of the paper and its code cannot infer. Every command
reads it, so every line costs attention on every run.

What belongs:
- **Decisions**, each with who took it, when and why. A decision without its reason
  is flagged, because nobody can later tell whether it still applies.
- **Content the authors require**, and where it goes.
- **The evidence map**: for each figure, table and quoted number, the script, the data
  and the command that regenerate it, and where heavy runs are executed.
- **Build**: how to compile, and any setting a command must not change.
- **Review status**: which sections are revised, and the open author items, each one
  line pointing to the ledger.

What does not belong: terminology (`glossary.toml`), settled findings
(`paperlint_ledger.md`), lint settings and the audience (`paperlint.toml`), the map of
sections and symbols (`paperlint_map.md`), style (`style_examples.md`), and anything
the paper, the code or the git history already states.

Form: one checkable instruction per line or bullet; objects named by label, not
number; entries replaced, never duplicated; a later co-author comment that contradicts
an entry is reported to the user as a conflict.
