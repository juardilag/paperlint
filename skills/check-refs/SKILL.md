---
name: check-refs
description: Check BibTeX entries against Crossref (first author, year, volume, pages, title) and find missing DOIs. Use when the user asks to verify references, check the bibliography, or after adding references from memory.
argument-hint: "[refs.bib] [--keys KEY1,KEY2]"
---

Verify bibliography entries.

1. Find the `.bib` file in `$ARGUMENTS`, or from `bib` in `paperlint.toml`, or ask.
2. Run
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/check_refs.py" $ARGUMENTS`.
   It needs network access to api.crossref.org and sends only titles, authors and DOIs.
3. Report the entries that need attention. For each mismatch, say which field differs
   and what Crossref has. For "not found", say that it must be checked by hand (old
   papers, book chapters and preprints are often missing from Crossref).
4. Offer to correct mismatched fields and add suggested DOIs. Never change an entry
   without showing the user the change first, because a Crossref match can be wrong.
