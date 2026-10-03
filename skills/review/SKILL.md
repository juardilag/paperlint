---
name: review
description: Review one section of a paper without editing it - a referee read for wrong, doubtful or overstated claims and limitations without consequence, and a cold read for the places a reader from a neighbouring field gets lost - followed by triage of the findings. Use when the user asks for a review, a cold read, a referee's check, or "would a reader understand this section".
argument-hint: "<file.tex> <section title or line range>"
---

Review a section and report; do not edit.

1. Identify the file and the section from `$ARGUMENTS`; ask if either is missing.
   Apply the style procedure of the `scientific-writing` skill (read both example sets
in full, write the style brief, check every change against it), so that every fix the review proposes is worded like the examples.
2. Launch the `referee` agent (correctness only) and the `cold-reader` agent (at most
   five places where a reader gets lost) in parallel, with the paper directory so they
   can read `paperlint.toml`, `glossary.toml`, `CLAUDE.md` and the ledger.
3. Triage every finding against the text yourself: confirm it, or say why it is wrong.
   A correctness finding is checked against the derivation, the code or the data
   before it is confirmed. A "says who?" goes to the `literature` agent.
4. For each confirmed finding, say where the answer belongs: a clause in the sentence
   that has the problem, a pointer to an appendix, an addition to an appendix, or no
   change. Never a new sentence when a clause does it.
5. Show the user the confirmed findings, grouped by severity, each with the quoted
   words, the proposed minimal fix and where it goes. Edit only if the user asks.
