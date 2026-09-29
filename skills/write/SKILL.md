---
name: write
description: Write a new section, subsection, appendix, caption or abstract of a paper from the author's description of its main ideas. Interviews the author only where the description leaves a content choice open, reads the whole paper, its code and data for context, plans the paragraphs, drafts following the writing rules, finds and verifies the references, inserts the text, and then runs the revise procedure on it until it is finished. Use when the user asks to write, draft, add or create new text for a paper.
argument-hint: "<file.tex> <what to write and where> -- <the main ideas, in your own words>"
---

Write new text from the author's ideas, then finish it. The author supplies the content;
the command supplies the structure, the prose, the references and the checks.

## 1. Understand the request

1. From `$ARGUMENTS`, identify the file, the kind of text (section, subsection,
   appendix, caption, abstract, response to referees) and where it goes. The rest of
   the arguments is the author's description: the main ideas, results, equations,
   figures and sources they have in mind. Treat it as the content brief.
2. Load the `scientific-writing` skill. Read `rules.md` and `examples.md`, and the
   project files (`paperlint.toml`, `glossary.toml`, `CLAUDE.md`,
   `paperlint_ledger.md`).
3. Read the whole paper and build or update `paperlint_map.md` (see the revise skill):
   what each section establishes, the symbols, the terms, the numbers and the labels.
   The new text must use the paper's notation and terms, must not repeat what other
   sections say, and must fit between the section before and the section after.
4. Read the code, data and figures that the brief or `CLAUDE.md` point to. Numbers and
   claims about results come from there.

## 2. Ask only what the brief leaves open

Ask the author in one message, and only about content choices you cannot settle from
the brief, the paper or the code: the main claim when two readings are possible, which
result or figure carries the argument, what to include or leave to an appendix, the
intended reader of an appendix, the length. Offer a recommendation for each question.
Never ask about wording, structure within a paragraph, notation already fixed by the
paper, or references you can find. If the brief settles everything, ask nothing.

## 3. Plan

Write the topic sentence of every paragraph and read them in a row. Each topic
sentence states a claim, not a list item: the plan does not contain "The first test
... The second test ..." (rules.md, section 2b). For the opening and the closing
paragraph, also write two or three plain sentences on what the paragraph must tell the
reader and why; draft those paragraphs from that note. For a method section, the plan
opens with the central equation and explains its terms before the procedure, gives the
step that carries the main idea its full explanation, and states the most general form
the derivation supports (rules.md, sections 5 and 6). They must answer,
in order, why the section exists, what is known, and what it does, and the last one
must lead to the next section. For each paragraph, list the equations, figures,
references and numbers it uses and where each comes from. Put detail that the argument
does not need in an appendix plan (rules.md, section 6).

Show the author the plan (the topic sentences and, for a results section, the figure
and the number each paragraph rests on) and wait for approval before drafting, unless
the arguments contain `--no-confirm`. This is the one checkpoint of the command: a plan
is cheap to change and a draft is not.

## 4. Draft

- Write each paragraph from its topic sentence, following the checklist of the
  scientific-writing skill: plain words first, every term defined at first use in the
  paper and named as the field names it, notation introduced with its concept, each
  fact once, the reason for every factor and choice, claims no stronger than the data.
- Write for rhythm from the start (rules.md, section 2b): sentences joined by the
  relation between them, varied in length and opening, the authors or the physics as
  the subject (not "the model tests"), each modifier once, at most one pointer per
  sentence. A draft that has to be fixed for rhythm later keeps its structure.
- Use the notation and the terms of the paper map and the glossary. A new symbol or term
  is added to the glossary only if the author agrees.
- For every statement about other work, and for every step that needs a source, launch
  the `literature` agent (one per topic, in parallel). Cite only what it confirms, add
  the verified entries to the `.bib` file, and present as new what no source states.
- Take every number from the code, the data or the figure it describes, and say which.
  A number quoted for a figure is computed over the plotted window and runs, and a
  statement about an inset must be visible in that inset.
- Before handing the draft to revise, run `lint.py` on it and give every paragraph the
  rhythm verdict yourself, with its weakest sentence. Redraft the paragraphs that fail,
  in particular the opening and the closing.
- Insert the text at the place the author named, with a label, and add the references
  to it from the sections that need them (for example the roadmap of the introduction).

## 5. Finish

Run the full revise procedure (the `revise` skill) on the new text: rounds of lint,
audits, cold reads, literature and self-checks, with the ledger, until a round brings
nothing new or three rounds have run. Then compile and look at the rendered pages,
including figures and their captions.

## Report

- Where the text was inserted and its length.
- The plan as approved, and any place the draft departs from it, with the reason.
- The references added, each with what it supports, and the claims presented as new.
- Every number in the text with its source.
- The revise report (changes, rejected findings, author decisions), including the
  rhythm verdict of every paragraph of the new text.
- Open questions for the author, each with a recommendation.
