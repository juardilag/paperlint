---
name: lint
description: Run the paperlint checker on a LaTeX paper, a section or a line range. By default it reports errors only (acronyms used before they are defined, glossary terms, hand-typed references, lower-case references at a sentence start); `--style` adds style notes. Use when the user asks to lint or check a paper mechanically.
argument-hint: "[file.tex] [--section TITLE | --lines A-B] [--style]"
---

Apply the style procedure of the `scientific-writing` skill (read both example sets
in full, write the style brief, check every change against it) before fixing a finding: a
fix is the smallest edit that reads like the accepted examples, never a rephrasing
toward the checker.

1. Find the paper: the file in `$ARGUMENTS`, otherwise the files in the nearest
   `paperlint.toml`, otherwise ask.
2. Run
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/lint.py" $ARGUMENTS`
   (`--list-checks` explains the codes and marks which are errors and which are style).
3. Show a short summary grouped by code, and fix the errors with minimal edits, or say
   why one is a false positive. Rerun on the same range and report.
4. Style notes (`--style`) are shown to the user as notes. Do not rewrite the text
   toward them unless the user asks for a specific one.
