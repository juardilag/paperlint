---
name: finish
description: Bring the whole paper to a submission-ready state. Checks every section in reading order for errors (the revise check), then checks the paper as one text (the argument from start to end, notation and terms across sections, repeated facts, every number against its data, captions and legends against the text, cross-references, the bibliography against Crossref), compiles and inspects the PDF, and reports what the authors still have to decide. Rewrites only the abstract, from an approved plan. Use when the user asks to finish or prepare the whole paper for submission or for a co-author.
argument-hint: "<file.tex> [--from <section>] [--skip <section,...>]"
---

Finish the paper as one text. Sections checked separately still contradict each
other, repeat each other and drift apart in notation; this command fixes that. It
checks; it does not rewrite the authors' prose.

## 1. Prepare

1. Load the `scientific-writing` skill, read `rules.md` and `examples.md`; any
   paragraph written or redrafted uses its drafting procedure. Read the project files.
2. Build a map of the whole paper in your working notes (not saved).
3. Run the blind test on the whole paper (`/paperlint:blindtest`) for the before
   score.
4. Run `lint.py` on the whole file (errors only) and `check_refs.py` on the `.bib`
   file. Fix the unambiguous findings, keep the rest for the report.

## 2. Check every section

Run the **Check** part of the `revise` skill on each section in reading order
(introduction, method, results, conclusions, appendices, captions with the section
that first refers to each figure), honouring `--from` and `--skip`. Update your map
after each section.

## 3. Check the paper as one text

- **The argument.** The introduction promises what the results deliver; the
  conclusions claim nothing the results do not show; the abstract matches both.
- **Claims across the paper.** Every general statement and restriction of the method
  checked against every example, and against the introduction and abstract that repeat
  it. Credit to earlier work stated once, with what the paper adds.
- **Say it once.** Each fact in one place; the introduction and the method share no
  paragraph; an appendix does not repeat the main text.
- **Notation and terms.** One meaning per symbol and one name per object everywhere,
  including figures, tables and appendices; every term defined at first use in reading
  order; typography the same in every equation.
- **Numbers.** List every number in the text, captions and tables (with its line),
  run the scripts of the evidence map (`CLAUDE.md`), and flag each number that no
  script output contains, with the same rounding everywhere. A flagged number gets a
  script line that prints it, or leaves the text; scope words next to it ("all",
  "only", "up to") are checked with it.
- **Figures.** Captions carry every parameter that reproduces the figure and any
  takeaway they state matches the data; legends use the text's terms; figures
  referenced in order. Then all figures side by side against the last bullet of
  rules.md section 7 (colors and markers per object, inset markers and gaps, axes
  height, grid, legends inside, tick labels clear of frames, insets clear of axes and
  data), from the rendered pages and the plotting code.
- **AI disclosure.** If AI tools did more than light editing, the paper says which
  tool and version, how it assisted, and how the authors directed and verified it:
  research use (code, derivations, analysis) in the methods, other use (drafting,
  revision) in the Acknowledgments (APS policy, June 2026; follow the target
  journal's). A missing or vague disclosure goes to the authors.
- **References.** Every cross-reference resolves; every citation supports its
  sentence (doubtful ones to the `literature` agent).
- **Abstract and title, last.** Propose a plan for the abstract (problem, what is new,
  main results in words) and wait for approval; draft it with the
  drafting procedure (job `abstract`), keep it only if the `compare` agent prefers it to the current
  one, and check that the title says what the paper does.

## 4. Converge

Every fix of steps 2 and 3 can break a neighbouring sentence (in practice five or six
regressions per whole-paper pass). Repeat until a pass finds no real error:
1. Audit: `referee`, `cold-reader` and `rule-checker` on every part, told to report
   only **A** (real errors: wrong, inconsistent, undefined, unsupported) and **B**
   (clear rule violations), no wording preferences.
2. Apply the A and B fixes.
3. Re-audit only the changed sentences plus the paragraph around each, the same way.
Stop when a pass has A = 0 and its B fixes are one-phrase edits; report the count of
A and B per pass.

## 5. Compile and inspect

Compile and render every page: link boxes that cover a figure (rules.md, section 9), overfull lines, figures against captions, labels
against the text's terms, unresolved references, the order of floats.

## Report

- The state of the paper and what is left before submission.
- Errors found (signs, factors, numbers, wrong claims), listed first.
- Changes at the level of the whole paper, with before and after.
- The bibliography result.
- The `budget` table: every section's length against its median and limit, and for
  each section over its limit, the ideas proposed to move or cut (author decisions).
- The blind-test separation (AUC) before and after, with the same seed.
- Author decisions, each as one question with a recommendation, ordered by impact.
