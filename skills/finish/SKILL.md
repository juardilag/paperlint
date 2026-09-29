---
name: finish
description: Bring the whole paper to a submission-ready state. Runs the revise procedure on every section in reading order, then checks the paper as one text (the argument from start to end, notation and terms across sections, repeated facts, numbers against figures and data, captions and legends against the text, the abstract and title written last, the bibliography against Crossref), compiles and inspects the PDF, and reports what the authors still have to decide. Use when the user asks to finish, polish or prepare the whole paper for submission or for a co-author.
argument-hint: "<file.tex> [--from <section>] [--skip <section,...>]"
---

Finish the paper as one text. Sections that were revised separately still contradict
each other, repeat each other and drift apart in notation; this command is where that is
fixed.

## 1. Prepare

1. Load the `scientific-writing` skill and read `rules.md` and `examples.md`. Read the
   project files and the ledger.
2. Build `paperlint_map.md` from scratch for the whole paper (see the revise skill).
3. Run `lint.py` on the whole file and `check_refs.py` on the whole `.bib` file. Fix the
   mechanical findings and the bibliography mismatches that are unambiguous, and keep
   the others for the report.

## 2. Revise every section

Run the revise procedure (the `revise` skill) on each section in reading order:
introduction, method, results, conclusions, then the appendices, and the captions with
the section that first refers to each figure. Skip the abstract here. Use `--from` and
`--skip` from `$ARGUMENTS`. A section the ledger marks as finished, and that has not
changed since, gets one round instead of full rounds: `lint.py`, your rhythm verdict of
every paragraph, and a cold read and a referee read (the `referee` agent) with the
rhythm verdict. The rules may have changed
since the section was finished (a new plugin version), so a finished section is not
exempt from them. If that round finds a should-fix finding, run the full revise
procedure on the section.

Update the map after each section, so that the next section is checked against the
revised text.

## 3. Check the paper as one text

After all sections, read the paper from the title to the last appendix and check:

- **The argument.** The introduction promises exactly what the results deliver. Each
  section answers why, what is known and what it does, and leads to the next. The
  conclusions claim nothing the results do not show.
- **Claims across the paper.** Every restriction and every general statement of the method
  is checked against every example and against the introduction and the abstract that
  repeat it (a false "at zero temperature" in the method is usually also in the
  introduction). Credit to earlier work is stated once, in the introduction, with what
  the paper adds.
- **Expert reading and weight.** Launch the `referee` agent on each main section (in
  parallel) for claims a referee of the field would doubt, limitations without their
  consequence, missing conventions and lineage, and pedantry for the audience. The
  paper should read as written for researchers of the journal's field: no definition
  sentences for what they know, no formula read aloud, no section previewing what later
  sections find (only the introduction does that), and each paragraph spending its
  words on the physics it is for. Typography (hats, bold) is checked across every
  equation.
- **Length.** Every section within its budget (PL021 on the whole file), and the
  paper as short as its ideas allow (rules.md, section 0). Recaps and previews between
  sections are cut to a clause; caveats sit in the section that shows the result.
- **Say it once.** Each fact appears in one place. The introduction and the method
  share no paragraph. An appendix does not repeat the main text.
- **Notation and terms.** One meaning per symbol and one name per object across the
  whole paper, including figures, tables and appendices. Every term is defined at its
  first use in reading order.
- **Numbers.** Every value in the text, the captions and the tables matches its source
  (figure, table, data file or code), with the same rounding everywhere. Values quoted
  for a figure are recomputed from its data over the plotted window, statements about
  an inset are checked against what it draws, and every exception a summary states
  points to the panel that shows it.
- **Rhythm across the paper** (rules.md, section 2b), the most important check. Read
  every section opening and closing in a row: they must not share one template (every
  section opening "We test ...", every closing "Neither test ..."), and each transition
  must follow from the section before. Run `lint.py` on the whole file and read every
  PL018, PL019 and PL020 note, since repetition and enumeration also build up across
  paragraphs. Give the rhythm verdict again to every paragraph changed in this step,
  and redraft, rather than patch, the ones that fail.
- **Figures.** Captions are self-contained, use the text's terms and define only
  parameters that belong to their figure. Legends and axis labels use the text's
  terminology. Every figure is referenced in order.
- **References.** Every cross-reference resolves. Every citation supports the sentence
  it is attached to (send doubtful ones to the `literature` agent).
- **Abstract and title, written last.** Rewrite the abstract from the finished paper:
  the problem, what is new, and the main results in words, with no claim the paper does
  not support. Draft it fresh from a note of what it must say, give it the rhythm
  verdict and a cold read, and check that the title says what the paper does.

Fix what is editorial, following the class definitions of the revise skill, and
self-check every edit against the rest of the paper.

## 4. Compile and inspect

Compile, and render every page. Look at each figure, table and equation: overfull
lines, figures that do not match their caption, labels that do not use the text's terms,
unresolved references, and the order of floats.

## Report

- A short summary: the state of the paper and what is left before submission.
- The errors found (signs, factors, numbers, wrong claims), listed first.
- Per section: its length before and after, the main changes, and any paragraph that
  still fails the rhythm verdict.
- The changes made at the level of the whole paper (repeated facts removed, notation
  unified, numbers corrected, abstract rewritten, with before and after).
- The bibliography result.
- The author decisions, each as one question with a recommendation, ordered by how much
  they affect the paper.
