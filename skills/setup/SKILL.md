---
name: setup
description: Set up paperlint for a paper - create paperlint.toml and glossary.toml, and propose glossary entries from the paper's own terminology. Use when the user wants to start using paperlint on a paper, or when a paper has no paperlint.toml.
argument-hint: "[paper directory]"
---

Set up paperlint for one paper.

1. Run
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/init_project.py" $ARGUMENTS`.
   It never overwrites existing files.
2. Read the paper. Propose `glossary.toml` entries for:
   - objects that appear under two or more names (e.g. "decay rate" and "relaxation
     rate"), with the name to keep and the ones to avoid;
   - specialist terms that should stay in the appendices;
   - acronyms that the field uses without definition, if any;
   - symbols with their single meaning.
   Show the proposal and write it only after the user agrees.
3. Suggest a `CLAUDE.md` in the paper directory for decisions that are not terminology:
   required content, build command, review status. Keep it short.
4. Run the linter once on the whole paper and report the counts per check, so the user
   sees the starting point.
