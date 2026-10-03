---
name: setup
description: Set up paperlint for a paper - create paperlint.toml and glossary.toml, propose glossary entries from the paper's own terminology, build or audit CLAUDE.md (evidence map, decisions, required content, review status). Use when the user wants to start using paperlint on a paper, or when a paper has no paperlint.toml, or to build or check its CLAUDE.md.
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
4. Build or audit `CLAUDE.md` in the paper directory, following rules.md, section 11.
   Derive what you can instead of asking for it:
   - the evidence map: for every figure and table file the paper includes, find the
     script that writes it and the data it reads (search the repository for the file
     name and for the save calls), and the command that regenerates it; ask the user
     only for what the search cannot settle, such as where heavy runs are executed;
   - decisions and required content: collect them from the ledger (author decisions),
     from review files and annotated PDFs in the directory, and from the user, each
     with who, when and why;
   - build: the compile command and any preamble settings the commands rely on;
   - review status: from the ledger, if it exists.
   If a `CLAUDE.md` already exists, do not rewrite it. Check it against section 11 and
   report, entry by entry, what to keep, move to another project file, merge, update or
   delete. Show the proposal and write only what the user agrees to.
5. Run the linter once on the whole paper and report the errors it finds, so the user
   sees the starting point. Style notes are available with `--style` but are not
   targets.
