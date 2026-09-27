---
name: review
description: Cold-read review of one section of a paper by the cold-reader agent, followed by triage of its findings. Use when the user asks for a review, a cold read, a reader's check, or "would a reader understand this section".
argument-hint: "<file.tex> <section title or line range>"
---

Review a section as a reader with no context would.

1. Identify the file and the section from `$ARGUMENTS`; ask if either is missing.
2. Launch the `cold-reader` agent with the file path and the section title (or line
   range). Tell it where the paper directory is, so it can read `glossary.toml` and
   `CLAUDE.md`.
3. When it returns, triage every finding against the text yourself: confirm it, or say
   why it is wrong (e.g. the term is defined two paragraphs earlier). Do not pass findings
   on unchecked.
4. Show the user the confirmed findings, grouped by severity, each with the quoted words
   and a proposed fix. Ask before editing, unless the user asked you to fix them.
5. After fixing, run `lint.py` on the section (see the lint skill) and report both results.
