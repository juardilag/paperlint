---
name: finish
description: Bring the whole paper to a submission-ready state. Checks every section in reading order for errors (the revise check), then checks the paper as one text (the argument from start to end, notation and terms across sections, repeated facts, every number against its data, captions and legends against the text, cross-references, the bibliography against Crossref), compiles and inspects the PDF, and reports what the authors still have to decide. Rewrites only the abstract, from an approved plan. Use when the user asks to finish or prepare the whole paper for submission or for a co-author.
argument-hint: "<file.tex> [--from <section>] [--skip <section,...>]"
---

Finish the paper as one text. Sections checked separately still contradict each
other, repeat each other and drift apart in notation; this command fixes that. It
checks; it does not rewrite the authors' prose.

## 1. Prepare

1. Load the `scientific-writing` skill, read `rules.md`, and apply its style
   procedure (both example sets in full, the style brief, the check of every change,
   blind comparison of rewritten paragraphs) to every section it touches. Read the project files and the ledger.
2. Build `paperlint_map.md` from scratch for the whole paper.
3. Run `lint.py` on the whole file (errors only) and `check_refs.py` on the `.bib`
   file. Fix the unambiguous findings, keep the rest for the report.

## 2. Check every section

Run the **Check** part of the `revise` skill on each section in reading order
(introduction, method, results, conclusions, appendices, captions with the section
that first refers to each figure), honouring `--from` and `--skip`. Update the map
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
- **Numbers.** Every value in the text, captions and tables printed by its folder's
  script from saved data (`CLAUDE.md` evidence map), with the same rounding everywhere.
- **Figures.** Captions carry every parameter that reproduces the figure and any
  takeaway they state matches the data; legends use the text's terms; figures
  referenced in order.
- **References.** Every cross-reference resolves; every citation supports its
  sentence (doubtful ones to the `literature` agent).
- **Abstract and title, last.** Propose a plan for the abstract (problem, what is new,
  main results in words) and wait for approval; draft it once in the style of
  house style (`style.md`), keep it only if the `compare` agent prefers it to the current
  one, and check that the title says what the paper does.

## 4. Compile and inspect

Compile and render every page: link boxes that cover a figure (rules.md, section 9), overfull lines, figures against captions, labels
against the text's terms, unresolved references, the order of floats.

## Report

- The state of the paper and what is left before submission.
- Errors found (signs, factors, numbers, wrong claims), listed first.
- Changes at the level of the whole paper, with before and after.
- The bibliography result.
- Author decisions, each as one question with a recommendation, ordered by impact.
