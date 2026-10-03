---
name: revise
description: Revise one section of a paper. Checks the section against the whole paper, its code and its data, and fixes errors with minimal edits; rewrites the prose only from a paragraph plan the author approved, and keeps a rewrite only if a blind comparison against the paper's example prose prefers it. Content decisions go to the authors. Use when the user asks to revise, check, finish or "run the plugin on" a section, an appendix, a caption or the abstract.
argument-hint: "<file.tex> <section title or line range> [--rewrite]"
---

Revise one section and stop. Two jobs, kept apart:

- **Checking** (always): find what is wrong, inconsistent, unsupported or undefined,
  and fix each with the smallest edit. This is where paperlint is reliable.
- **Rewriting** (only with `--rewrite`, or when the user asks for it): a fresh draft of
  the section from a paragraph plan the author approved, matched to the paper's
  house style (`style.md`), kept only if the `compare` agent prefers it. Prose is never
  improved by rounds of patches.

## Before starting

1. Load the `scientific-writing` skill, read `rules.md`, and apply its style procedure
   (both example sets in full, the style brief, the check of every change, blind
   comparison of rewritten paragraphs) with the house style `style.md`.
2. Read `paperlint.toml`, `glossary.toml`, `CLAUDE.md` and `paperlint_ledger.md` in the
   paper directory (create the ledger if missing). Author decisions in the ledger and
   in `CLAUDE.md` are not reopened, except a correctness question, which a decision on
   wording never settles; a later co-author comment that contradicts a decision is
   reported as a conflict. Review comments in a PDF are read from the annotations.
3. Read the whole paper once and update `paperlint_map.md`: per section what it
   establishes, every symbol and term with where it is defined, every quoted number
   with its source, and the labels other sections use.
4. Locate the code and data behind the section (`CLAUDE.md` evidence map).

## Check (always)

1. Run `lint.py --section "<title>"`. It reports errors only (undefined acronyms,
   glossary terms, hand-typed references); fix each. Do not run `--style` unless the
   user asks, and never rewrite toward its notes.
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
3. Launch the `referee` agent (correctness only) and the `cold-reader` agent (at most
   five places where a reader got lost), in parallel, with the paths of the ledger and
   the map.
4. Triage every finding:
   - **Error** (wrong, inconsistent, undefined, unsupported): fix it now with the
     smallest edit, in the sentence that has the problem. Never append a sentence to
     answer a finding when a clause in the existing sentence does it. Where a source is
     needed, launch the `literature` agent.
   - **Author decision**: scope, structure, what the paper claims about its own
     results, anything the data must decide. Check correctness first; send only the
     decision.
   - **Rejected**: say why in one sentence.
   Findings about style, rhythm or length are not errors and are not acted on in a
   check.
5. Self-check every edit: reread the sentence and its paragraph, check it against the
   equations, symbols and numbers around it and the map, grep the paper for every
   symbol, term and label it touched, and confirm a shortened sentence makes the same
   claim with the same hedge.
6. Compile, fix any `Overfull \hbox` in the section, update the ledger and the map.

A check is one pass. Run it again only if the fixes changed a claim, a number or a
derivation, and then only on what changed.

## Rewrite (only with `--rewrite`)

1. **Plan.** Write the section's plan: one line per paragraph with the claim it makes
   and the evidence it rests on, in the order of the argument. Show the plan to the
   user and wait. Nothing is rewritten before the author approves the plan; their
   changes to it are content decisions.
2. **Draft once**, from the approved plan, the checked facts and the paper's
   house style (`style.md`), matching its examples in how sentences run and how claims and
   numbers are introduced. Write the whole section fresh; do not edit the old text
   sentence by sentence. Keep every decision in `CLAUDE.md` and the ledger (search both
   for every citation and claim of the new text).
3. **Compare.** Give the `compare` agent the old and the new version of each paragraph
   as A and B in random order, with two or three paragraphs of `style.md`.
   Keep a new paragraph only if it wins and makes the same claims; otherwise keep the
   old one, or show both to the user when the compare agent calls it a tie.
4. **Check** the kept text as above, with minimal edits only.

## Report

- Errors found and fixed (a sign, a factor, a wrong number, an unsupported claim),
  listed first, each with before and after.
- Other fixes, grouped; every change outside the section made for consistency.
- With `--rewrite`: the approved plan, and per paragraph the compare verdict and its
  reason.
- Rejected findings, each with its reason.
- Author decisions, each as one question with a recommendation.
- The lint result and whether the paper compiles.

An author correction about content goes to `CLAUDE.md` or `glossary.toml`; one about
style becomes a before/after pair in `examples.md`, anonymised, never a rule; a
preference of this paper only goes to `CLAUDE.md`.
