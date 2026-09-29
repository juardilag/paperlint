---
name: review
description: Cold-read and referee review of one section of a paper by the cold-reader and referee agents, followed by triage of its findings. Use when the user asks for a review, a cold read, a reader's check, or "would a reader understand this section".
argument-hint: "<file.tex> <section title or line range>"
---

Review a section as a reader with no context would.

1. Identify the file and the section from `$ARGUMENTS`; ask if either is missing.
2. Launch the `cold-reader` agent with the file path and the section title (or line
   range), and in parallel the `referee` agent, which reads as an expert of the field
   and flags doubtful claims and pedantry. Tell both where the paper directory is, so
   they can read `paperlint.toml`, `glossary.toml` and `CLAUDE.md`. A definition the
   cold reader asks for and the referee calls pedantic is settled by the audience: a
   reference always, a clause only if that audience needs it.
3. When it returns, triage every finding against the text yourself: confirm it, or say
   why it is wrong (e.g. the term is defined two paragraphs earlier). Do not pass findings
   on unchecked.
4. For each confirmed finding, decide where the answer belongs, following section 6 of
   `skills/scientific-writing/rules.md` (main text vs. appendix):
   - **Main text**, as a clause, only if the reader needs it to follow the argument of
     the section: a definition at first use, the reason for a choice, a missing premise.
   - **Appendix**, with a pointer from the main text, for derivation details, factors,
     conventions, special cases and validity conditions.
   - **No change** if an appendix already answers it and the text points there.
   - **Literature**, for "says who?" findings and statements about other papers that
     the text does not support: pass them to `/paperlint:literature` rather than
     answering from memory.
   A review should not make a method section longer. If the confirmed fixes add more
   than a few clauses to the main text, move the detail to the appendix instead.
   Editorial fixes (definitions, notation, pointers, wording, the reason for a factor,
   a standard convention) do not need the authors. Only content decisions do. See
   `/paperlint:revise`, which applies this policy and runs rounds until the section is
   done.
   The cold reader's rhythm verdict (rules.md, section 2b) is triaged like any other
   finding: check each failed paragraph yourself, and give your own verdict of every
   paragraph, with its weakest sentence, so a paragraph it passed by mistake is caught.
   A rhythm fix redrafts the paragraph; it does not append to it.
5. Show the user the confirmed findings, grouped by severity, each with the quoted words,
   the proposed fix and where it goes (main text, appendix, or no change). Ask before
   editing, unless the user asked you to fix them.
6. After fixing, run `lint.py` on the section (see the lint skill) and report both results.
   Also compare the length of the section before and after, and say if it grew.
