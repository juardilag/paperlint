---
name: scientific-writing
description: Procedure, rules and tools for writing or revising scientific papers so the text is correct, consistent, supported by its data, and reads like the published prose of J. Marino, H. Hosseinabadi and M. Stefanini (paperlint's house style, learned from a corpus of their real paragraphs). Use whenever drafting, rewriting, reviewing or editing a paper, a section, an abstract, an introduction, a caption, an appendix or a response to referees, in LaTeX or plain text, in any field.
---

# Writing scientific papers

paperlint does two jobs and keeps them apart. **Checking** finds what is wrong:
undefined terms, inconsistent notation, numbers that do not match their data, claims
stronger than the evidence, limitations without their consequence. It fixes each with
the smallest edit. **Drafting** writes prose, and learns how from real paragraphs of the
house style, never from rules or from its own earlier drafts.

The measure of the prose is the blind test (`/paperlint:blindtest`): a judge that does
not know which is which tries to tell the paper's paragraphs from held-out published
ones. In the first tests it told all of them apart. Every change to how paperlint
writes is kept only if it lowers that score.

Files in this skill's directory:
- `rules.md`: the correctness rules. Read all of it once per session.
- `examples.md`: the tells of generated prose, and what real readers objected to.
- `style.md`: a short description of the house style and a few verbatim paragraphs,
  the fallback when the corpus is missing.
- `corpus_ids.txt`: the papers of the corpus.
- `scripts/corpus.py`: builds the corpus in `~/.paperlint/corpus` and retrieves real
  paragraphs by the job they do (abstract, opening, intro, method, results, appendix,
  conclusion, caption).
- `scripts/blindtest.py`: makes and scores the blind test; `stats` prints per-section
  diagnostics against the corpus.
- `scripts/learn.py`: records an author's hand edits as pairs in the paper's
  `author_edits.md`.
- `scripts/lint.py`: the checker (errors only; `--style` adds notes nobody has to
  follow). `check_refs.py`: `.bib` against Crossref. `pdf_comments.py`: annotations of
  a reviewed PDF. `init_project.py`: creates `paperlint.toml` and `glossary.toml`.

Agents: `referee` (wrong or overstated claims), `cold-reader` (at most five places a
reader gets lost), `literature` (sources), `compare` (blind A/B of two versions against
real paragraphs), `judge` (the blind test).

## Project files

`paperlint.toml` (checker settings, audience), `glossary.toml` (one name per object),
`CLAUDE.md` (decisions with who and when, required content, evidence map) and
`author_edits.md` (the authors' own edits). Read them before working on the paper. No
history of findings is kept: what was fixed is in git, a rejected finding is said once
in a report, and a decision goes to `CLAUDE.md`. Reviewers read the text fresh each
time.

## Drafting, in every command that writes prose

This is the one procedure for writing a paragraph, whether new or redrafted. Use it
for every new paragraph, for every paragraph a check touched twice or more, and for
every paragraph the user asks to rewrite. A single error fix is not drafting: it is the
smallest edit in the sentence that has the error.

1. **Facts.** Write down what the paragraph must carry: each claim, each number with
   its source, each reference, each symbol it introduces or uses, each hedge, and each
   decision of `CLAUDE.md` that applies. Take them from the old paragraph, the approved
   plan, the code and the data. This list is the only thing that passes from the old
   text to the new one. A cross-reference or a reason is not a fact: keep one where a
   reader needs it to follow, and let the others go.
2. **Models.** Retrieve real paragraphs that do the same job:
   `corpus.py retrieve <job> "<the facts or the plan line>"`, three of them, and read
   them whole. Read the afters of the paper's `author_edits.md` and the tells of
   `examples.md`. If the corpus is missing, run `corpus.py build`; if that fails, use
   the paragraphs of `style.md` and say so in the report.
3. **Draft blind.** Write the paragraph from the facts and the models only, without
   looking at the old wording, which pulls a draft back toward itself. Write it the way
   the models are written: how they open (from the setting, the figure or the previous
   point, rarely from a thesis), how long their sentences run, where they give a reason
   and where they let the order carry it, how they use "we", how they introduce a
   number and credit other work, and how they speak to the reader ("we note that",
   "of course", "notice", a hedge where the evidence is partial, a stock phrase of the
   field). Do not copy their phrases, and do not write toward a sentence length:
   match the variety of the models, not an average.
4. **Check the facts.** Every item of the list is in the draft, with the same strength
   and the same hedge, and no new claim is added. A missing or changed claim is fixed
   now. What a draft may and should add is discourse, which a list of facts lacks and
   published paragraphs are full of: how the paragraph follows from the previous one,
   what a result means for the reader or for the question the paper asks, a comparison
   with work the paper already cites, a remark that guides the reader ("notice that
   ...", "in other words ..."). Discourse that would need its own evidence is a claim.
5. **Compare.** Give the `compare` agent the old and the new paragraph as A and B in
   random order, with the three models. Keep the new one only if it wins and makes the
   same claims; on a tie, show both to the user.
6. **Measure.** After a section was drafted or redrafted, run the blind test on it
   with the same seed as before (`/paperlint:blindtest <file> --section <title>`) and
   report the separation (AUC) before and after.

Never add a sentence to answer a finding when a clause does it, and never answer a
reader's "why?" in the main text unless the argument needs the answer there; the
mechanism goes to an appendix, or nowhere.

## Checking

1. **Read** the project files, the section, the sections it builds on, and the code and
   data behind it. Build a map of the paper in your working notes (what each section
   establishes, where each symbol and term is defined, the source of each number). It
   is not saved: it is rebuilt from the current text every run.
2. **Check**: run `lint.py`, audit against `rules.md` sections 1 to 9, launch the
   `referee` and `cold-reader` agents on the text as it is now, and fix each confirmed
   error with the smallest edit, in the sentence that has it. Recompute every number
   from its script.
3. **Compile, render and look** at the pages, including figures and equations.
4. **Report** errors first, then other fixes, rejected findings with a reason, and
   author decisions as questions with a recommendation. An author's decision goes to
   `CLAUDE.md`, with who and when; an author's edit of the prose is recorded with
   `/paperlint:learn`.
