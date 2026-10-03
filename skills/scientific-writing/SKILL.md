---
name: scientific-writing
description: Procedure, rules and tools for writing or revising scientific papers so the text is correct, consistent, supported by its data, and written in paperlint's house style (the prose of J. Marino, H. Hosseinabadi and M. Stefanini). Use whenever drafting, rewriting, reviewing or editing a paper, a section, an abstract, an introduction, a caption, an appendix or a response to referees, in LaTeX or plain text, in any field.
---

# Writing scientific papers

paperlint splits the work in two. **Checking** is what it does reliably: terms defined,
notation consistent, every number from its data, claims no stronger than the evidence,
limitations with their consequence, derivations complete, captions that reproduce the
figure. **Prose** belongs to the authors. paperlint drafts only from a paragraph plan the
author approved, matches the paper's example prose instead of following style rules, and
keeps a rewrite only when a blind comparison prefers it. Rounds of patches toward a
checklist are what make text read as generated, so paperlint does not do them.

Files in this skill's directory:
- `rules.md`: the correctness rules (eleven short sections). Read all of it once per
  session.
- `examples.md`: author corrections, before and after. Read before drafting.
- `scripts/lint.py`: the checker. By default it reports errors only; `--style` adds
  notes.
- `scripts/check_refs.py`: checks `.bib` entries against Crossref.
- `scripts/pdf_comments.py`: lists the annotations of a reviewed PDF with the text
  they mark.
- `scripts/init_project.py`: creates `paperlint.toml` and `glossary.toml` for a paper.
- `style.md`: the house style, the prose of J. Marino, H. Hosseinabadi and
  M. Stefanini, profiled with verbatim paragraphs from their papers. It is the same for
  every paper and is not a setting.

Agents: `referee` (wrong, doubtful or overstated claims), `cold-reader` (at most five
places a reader gets lost), `literature` (sources for claims), `compare` (blind A/B
judge of two versions against the house style).

## Project files

A paper directory may contain `paperlint.toml` (checker settings, audience),
`glossary.toml` (one name per object), `CLAUDE.md` (decisions, required content, evidence map), `paperlint_map.md` and
`paperlint_ledger.md`. Read them before working on the paper; they override the
general rules where they conflict.

## Style, in every command

Every command that writes, rewrites, fixes or proposes a sentence follows the example
prose, not a checklist. This is the one style procedure; the commands call it.

1. **Read both example sets in full** before the first edit of the session, not by
   searching them: this skill's `style.md` (the house style) and `examples.md`
   (reviewers' corrections as pairs). Where they disagree, `examples.md` wins for the
   flagged pattern; a recorded decision in the paper's `CLAUDE.md` or ledger about its
   own content wins over both.
2. **Write a style brief** of three to eight lines before drafting: how the house
   style runs for this kind of text (sentence length, how claims, numbers and credit are introduced), and
   the pairs of `examples.md` that apply to the text at hand (for example "Formulas
   read aloud", "Counterfactual instead of the consequence", "Redundancy"). Put it in
   the command's working file (`comments.md`, the ledger) or the report.
3. **Check every changed paragraph against the brief** before compiling: no sentence
   repeats a flagged version, and each reads like the accepted ones. A checker that
   contradicts the house style (a sentence-length note against prose that runs long
   sentences) loses.
4. **Compare blind.** A paragraph rewritten beyond a clause goes to the `compare`
   agent against its old version, with two or three paragraphs of
   `style.md`. Keep the new one only if it wins and makes the same claims.

## Procedure

1. **Read** the project files, the section, the sections it builds on, and the code and
   data behind it.
2. **Check** (always): run `lint.py`, audit against `rules.md` sections 1 to 9, launch
   the `referee` and `cold-reader` agents, and fix each confirmed error with the
   smallest edit, in the sentence that has it. Recompute every number from its script.
3. **Rewrite** (only when asked): a plan of one claim per paragraph, approved by the
   author; one fresh draft matched to `style.md`; the `compare` agent against
   the old version; the winner checked as in step 2.
4. **Compile, render and look** at the pages, including figures and equations.
5. **Report** errors first, then other fixes, rejected findings, and author decisions
   as questions with a recommendation. Author corrections about content go to the
   project files; about style, to `examples.md` as an anonymised pair.
