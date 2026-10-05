---
name: write
description: Write a new section, subsection, appendix, caption or abstract of a paper from the author's description of its main ideas. Reads the whole paper, its code and data, proposes a paragraph plan for the author to approve, drafts once in the style of the paper's example prose, verifies references and numbers, and checks the result for errors. Use when the user asks to write, draft, add or create new text for a paper.
argument-hint: "<file.tex> <what to write and where> -- <the main ideas, in your own words>"
---

Write new text from the author's ideas. The author supplies the content and approves
the plan; the command supplies a draft, the references and the checks.

## 1. Understand the request

1. From `$ARGUMENTS`, identify the file, the kind of text and where it goes. The rest
   is the author's brief: the ideas, results, equations, figures and sources.
2. Load the `scientific-writing` skill; every paragraph is written with the drafting procedure of the `scientific-writing` skill (facts, real paragraphs retrieved from the corpus, a blind draft, the fact check, blind comparison). Read
   `rules.md`, `examples.md` and the project files (`paperlint.toml`, `glossary.toml`,
   `CLAUDE.md`, `author_edits.md`).
3. Read the whole paper and build its map in your working notes. The new text uses the paper's
   notation and terms, does not repeat other sections, and fits between its
   neighbours.
4. Read the code, data and figures the brief or `CLAUDE.md` point to. Every number and
   result comes from there.

## 2. Ask only what the brief leaves open

In one message, and only about content you cannot settle from the brief, the paper or
the code: the main claim when two readings are possible, which result carries the
argument, what goes to an appendix, the length. Recommend an answer for each. Never
ask about wording.

## 3. Plan, and wait

One line per paragraph: the job it does (opening, method, results, appendix,
conclusion, caption), the claim it makes and the evidence it rests on (equation,
figure, number with its source, reference), in the order of the argument. A method
section shows its central equation early, in the most general form the derivation
supports (rules.md, sections 5 and 6), after one or two sentences that name its
actors in words, so the reader meets each symbol already knowing what it does. Show the plan and wait for approval, unless the
arguments contain `--no-confirm`. The plan is where the author shapes the text.

## 4. Draft once

- Write each paragraph from its approved plan line with the drafting procedure: its
  facts, three retrieved paragraphs that do the same job, a draft written from those
  alone. Do not write toward checklists or word counts. Then read the text whole and
  fix only the joins between paragraphs.
- Use the paper's notation and terms; a new symbol or term goes into the glossary only
  if the author agrees.
- For every statement about other work, launch the `literature` agent; cite only what
  it confirms and add the verified entries to the `.bib` file.
- Take every number from the script that prints it, never from memory or comments.
- Insert the text with a label, and add references to it where the paper needs them.

## 5. Check

Run the **Check** part of the `revise` skill on the new text: `lint.py` (errors
only), the audits of `rules.md`, sections 1 to 9, the `referee` and `cold-reader`
agents, and minimal fixes. Compile and look at the rendered pages.

## Report

- Where the text went and its length; the approved plan, and any departure from it.
- The references added, each with what it supports; claims presented as new.
- Every number with its source.
- The check report: errors fixed, rejected findings, author decisions.
- The blind-test separation (AUC) of the new text (`/paperlint:blindtest <file> --section`).
