---
name: lint
description: Run the paperlint mechanical checks on a LaTeX paper, a section or a line range, and fix what they find. Use when the user asks to lint, check style, or check a section of a paper.
argument-hint: "[file.tex] [--section TITLE | --lines A-B]"
---

Run the mechanical style checks of the scientific-writing skill.

1. Find the paper: use the file in `$ARGUMENTS` if given, otherwise the files listed in
   the nearest `paperlint.toml`, otherwise ask.
2. Run
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/lint.py" $ARGUMENTS`
   (add `--no-info` for a shorter report; `--list-checks` explains the codes).
3. Group the findings by code and show the user a short summary.
4. Offer to fix them. When fixing, follow `skills/scientific-writing/rules.md`: a long
   sentence becomes two sentences, not a sentence with a colon; a colon becomes a full
   stop or a rewrite, not a dash. After fixing, run the linter again on the same range and
   report the result. If a finding is a false positive, say so instead of changing the
   text.
