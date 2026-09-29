---
name: setup
description: Set up paperlint for a paper - create paperlint.toml and glossary.toml, and propose glossary entries from the paper's own terminology. Use when the user wants to start using paperlint on a paper, or when a paper has no paperlint.toml.
argument-hint: "[paper directory]"
---

Set up paperlint for one paper.

1. Run
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/init_project.py" $ARGUMENTS`.
   It never overwrites existing files.
2. Ask the user who reads the paper (journal and field, e.g. "PRA: quantum optics and
   many-body theory"), propose a value from the journal class or the paper if you can,
   and write it as `audience` in `[paper]` of `paperlint.toml`. Every command uses it to
   decide which terms need a definition and which questions a referee would ask.
3. Read the paper. Propose `glossary.toml` entries for:
   - objects that appear under two or more names (e.g. "decay rate" and "relaxation
     rate"), with the name to keep and the ones to avoid;
   - specialist terms that should stay in the appendices;
   - acronyms that the field uses without definition, if any;
   - symbols with their single meaning.
   Show the proposal and write it only after the user agrees.
4. Suggest a `CLAUDE.md` in the paper directory for decisions that are not terminology:
   required content, build command, review status. Keep it short.
5. Run the linter once on the whole paper and report the counts per check, so the user
   sees the starting point.
