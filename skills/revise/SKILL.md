---
name: revise
description: Revise one section of a paper. Checks the section against the whole paper, its code and its data, and fixes errors with minimal edits; redrafts a paragraph that collected several fixes, or the whole section with --rewrite, from its facts and real paragraphs of the house style, keeping a redraft only if a blind comparison prefers it; measures the result with the blind test. Content decisions go to the authors. Use when the user asks to revise, check, finish or "run the plugin on" a section, an appendix, a caption or the abstract.
argument-hint: "<file.tex> <section title or line range> [--rewrite]"
---

Revise one section and stop. Two jobs, kept apart:

- **Checking** (always): find what is wrong, inconsistent, unsupported or undefined,
  and fix each with the smallest edit.
- **Drafting** (for a paragraph that collected two or more fixes, and for the whole
  section with `--rewrite` or when the user asks): the drafting procedure of the
  `scientific-writing` skill, from the paragraph's facts and real paragraphs of the
  house style. Prose is never improved by rounds of patches.

## Before starting

1. Load the `scientific-writing` skill and read `rules.md` and `examples.md`.
2. Read `paperlint.toml`, `glossary.toml`, `CLAUDE.md` and `author_edits.md` in the
   paper directory. Decisions in `CLAUDE.md` are not reopened, except a correctness
   question, which a decision on wording never settles; a later co-author comment that
   contradicts a decision is reported as a conflict. Review comments in a PDF are read
   from the annotations. If the directory still has a `paperlint_ledger.md` or
   `paperlint_map.md` from an older version, do not read them; offer once to move the
   author decisions they contain into `CLAUDE.md` and delete them.
3. Read the whole paper and build the map in your working notes (not saved): per
   section what it establishes, every symbol and term with where it is defined, every
   quoted number with its source, the labels other sections use.
4. Locate the code and data behind the section (`CLAUDE.md` evidence map).
5. Run `blindtest.py budget <file>` and note the section's length, median and limit
   (the "Length" part of the `scientific-writing` skill).
6. If the section will be drafted (`--rewrite`), run the blind test on it first
   (`blindtest.py make <file> --section "<title>" --seed 1`, the `judge` agent,
   `blindtest.py score`) to have the before score.

## Check (always)

1. Run `lint.py --section "<title>"`. It reports errors only; fix each. Do not run
   `--style` unless the user asks, and never write toward its notes.
2. Audit the section against `rules.md`, sections 1 to 9:
   - every term and symbol defined at first use, one name and one symbol per object
     across the paper (grep it);
   - every number recomputed from its data with the script that prints it, and every
     statement about a figure checked against what the plotting code draws;
   - every claim no stronger than its evidence, the paper's choices stated as
     choices, general statements tested on every example of the paper;
   - every limitation with its consequence; Itô or Stratonovich stated;
   - results equations derived from the method and compared with the code;
   - derivations as one ordered chain, numerical steps reimplementable;
   - captions carry every parameter that reproduces the figure, and any takeaway
     they state matches the data; legends use the text's terms;
   - each fact once; cross-references and column widths (`Overfull \hbox`).
3. Launch the `referee` and the `cold-reader` agents in parallel on the section as it
   is now. Give them the paper directory; they read `CLAUDE.md` for the decisions and
   nothing about earlier rounds.
4. Triage every finding:
   - **Error** (wrong, inconsistent, undefined, unsupported): fix it with the smallest
     edit, in the sentence that has the problem. A clause in that sentence, never a new
     sentence. Where a source is needed, launch the `literature` agent.
   - **A reader's "why?"**: answer in the main text only if the argument needs the
     answer there; otherwise in an appendix, or not at all. Say which in the report.
   - **Author decision**: scope, structure, what the paper claims about its own
     results, anything the data must decide. Check correctness first; send only the
     decision.
   - **Rejected**: say why in one sentence, in the report. Nothing is saved.
   Findings about style, rhythm or length are not errors and are not acted on in a
   check.
5. Self-check every edit: reread the sentence and its paragraph, check it against the
   equations, symbols and numbers around it and the map, grep the paper for every
   symbol, term and label it touched, and confirm a shortened sentence makes the same
   claim with the same hedge.
6. **Redraft patched paragraphs.** A paragraph that received two or more fixes in this
   check is redrafted with the drafting procedure (facts, models, blind draft, fact
   check, compare). Patches stacked in one paragraph are what reads as generated.
7. **Length.** Run `budget` again. The section must not be longer than it started. If
   it is over its limit, list its ideas and propose, as an author decision, which move
   to an appendix and which go; never compress to meet the limit.
8. Compile and fix any `Overfull \hbox` in the section.

A check is one pass. Run it again only if the fixes changed a claim, a number or a
derivation, and then only on what changed.

## Rewrite (only with `--rewrite`)

1. **Plan.** Within the section's budget: if the section is over its limit, the plan
   proposes which ideas leave it, and the author decides. One line per paragraph: the
   job it does (opening, method, results,
   appendix, conclusion, caption), the claim it makes and the evidence it rests on, in
   the order of the argument. Show the plan to the user and wait. Their changes to it
   are content decisions.
2. **Draft** each paragraph with the drafting procedure of the `scientific-writing`
   skill, from the approved plan line and the facts of the old text. Then read the
   section whole and fix the joins between paragraphs only.
3. **Check** the kept text as above, with minimal edits only.
4. **Measure.** Run the blind test on the section again with the same seed and report
   the separation (AUC) before and after. If it did not fall, say so plainly.

## Report

- Errors found and fixed (a sign, a factor, a wrong number, an unsupported claim),
  listed first, each with before and after.
- Other fixes, grouped; every change outside the section made for consistency; the
  paragraphs redrafted, with the compare verdict for each.
- With `--rewrite`: the approved plan, the compare verdict and its reason per
  paragraph, and the blind-test separation (AUC) before and after.
- Rejected findings, each with its reason.
- Author decisions, each as one question with a recommendation.
- The section's length before and after, against its median and limit.
- The lint result and whether the paper compiles.
- If the author edits the text by hand afterwards, suggest `/paperlint:learn` once.
