---
name: learn
description: "Record the authors' own edits of the paper as before/after pairs, so paperlint imitates how the authors write. Diffs the .tex against a git revision sentence by sentence and appends the changed passages to author_edits.md next to the paper. Use after an author edited the text by hand, or when the user says 'learn from my edits'."
argument-hint: "<file.tex> [--rev HEAD] [--who <name>]"
---

1. Make sure the "before" is paperlint's text: the revision passed with `--rev`
   (default `HEAD`) must be the last version Claude wrote, and the working tree the
   author's edit. If Claude edited the file after that revision, ask the user which
   revision to compare with.
2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/learn.py" <file.tex> --rev <rev> --who <name> --dry-run`
   and show the pairs. Drop any pair that is a content change rather than a rewording
   (a number, a result, a reference added); a content change that reflects a decision
   goes to `CLAUDE.md` instead.
3. Run it again without `--dry-run`, or append the kept pairs by hand.
4. Report how many pairs were recorded. Every drafting command reads them.
