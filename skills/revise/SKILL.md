---
name: revise
description: Revise one section of a paper to a finished state in a single command. Runs the lint checks, the audits and cold reads in rounds, fixes the editorial findings without asking, keeps a ledger of settled findings so they are not raised again, and stops when a round brings nothing new that must or should be fixed. Only content decisions go to the authors. Use when the user asks to revise, finish, polish or "run the plugin on" a section.
argument-hint: "<file.tex> <section title or line range>"
---

Bring one section to a finished state and stop.

## Before the first round

1. Identify the file and the section from `$ARGUMENTS`. Read the project files
   (`paperlint.toml`, `glossary.toml`, `CLAUDE.md`), the section, the sections it builds
   on and the appendices it points to.
2. Open the ledger `paperlint_ledger.md` in the paper directory (create it if missing).
   It lists findings already settled for this paper: fixed, rejected with the reason,
   or waiting for the authors. Every round reads it, and so does every cold reader.
3. Record the word count of the section.

## Each round

1. **Mechanical.** Run `lint.py` on the section and fix everything it reports.
2. **Audits.** Do the audits of the scientific-writing procedure yourself: terms,
   notation (one meaning per symbol in the whole paper, not only in the section),
   back-references, redundancy, claims.
3. **Cold read.** Launch the `cold-reader` agent on the section. Pass it the path of the
   ledger and tell it not to raise settled findings again unless the text changed.
4. **Triage.** Check every finding against the text. Put each one in one class:
   - **Editorial**: fix it now, without asking. This covers undefined terms and
     symbols, notation that is inconsistent, missing pointers to appendices, ambiguous
     references, wording, sentence structure, redundancy, a missing one-clause
     reason for a factor or a step, the interpretation of a standard convention, and
     moving detail between the main text and an appendix (rules.md, section 6).
     Where a standard answer exists in the literature, use it and cite it.
   - **Literature**: a claim about other work, or a "says who?". Send it to the
     `literature` agent and apply the result if the sources support it.
   - **Author decision**: collect it for the report and do not edit. This covers what
     the paper claims about its own results, the scope and the structure of the paper,
     adding or removing a result, a figure or a section, anything the code or the data
     must decide, and anything an author has already decided (see `CLAUDE.md` and the
     ledger).
   - **Rejected**: the finding is wrong. Write the reason in one sentence.
5. **Apply** the editorial and literature fixes. Follow section 6 of `rules.md`: the
   main text keeps what the reader needs to follow the argument, the appendix keeps the
   rest. Then rerun `lint.py`, compile, and update the ledger.

## When to stop

Stop after a round in which the cold read and the audits bring no new finding of
severity must fix or should fix. A new finding is one that is not in the ledger and
does not repeat a rejected one. Stop also after three rounds, and say so. Do not start
another round for consider-level findings only; fix the editorial ones in passing.

A cold reader always finds something. The ledger and this rule are what end the loop.

## Report

- The section length before and after. If it grew, say why.
- What was changed, grouped by class, with the before and after for anything an author
  had flagged.
- The rejected findings, each with its reason.
- The author decisions, each as one question with a recommendation. These are the only
  items the authors need to act on.
- The lint result and whether the paper compiles.

Turn every author correction into a rule: in `rules.md` if it is general, in the
paper's `CLAUDE.md` or `glossary.toml` if it concerns this paper only.
