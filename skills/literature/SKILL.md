---
name: literature
description: Find, read and quote the sources behind claims in a paper, verify the references on Crossref, and propose BibTeX and replacement sentences. Use when the user asks to find references, check what another paper did, support a claim, answer "says who?" findings of a review, or add citations to a passage.
argument-hint: "<file.tex> <line range, section, or the claims to check>"
---

Support claims with sources that were actually read.

1. Identify the paper and the claims from `$ARGUMENTS`. A claim is a quoted sentence
   with its line, a "says who?" finding from `/paperlint:review`, or a question such as
   "what did Ref. X assume?". If only a section is given, list its unsupported claims
   first and confirm them with the user.
2. Group the claims by topic. Launch one `literature` agent per topic, in parallel. Give
   each agent the file path, the lines, the paper directory, and any candidate papers
   the user named.
3. When the agents return, check their work yourself:
   - Re-verify every recommended DOI on Crossref (`curl
     https://api.crossref.org/works/<DOI>`), or write the new entries to a scratch
     `.bib` file and run
     `python3 "${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/check_refs.py" <file>`.
   - Drop any claim the agent marks as supported without a quote.
   - Check that each proposed sentence is no stronger than its quotes, and that it
     follows section 6 of `rules.md` (main text or appendix).
4. Show the user, per claim: supported / partly / not supported, the quotes, the
   proposed sentence and where it goes. List the claims no source supports, and say
   which ones should be weakened or removed. Ask before editing, unless the user asked
   you to fix them.
5. When editing, add the verified entries to the `.bib` file, change the text, then run
   `lint.py` on the changed paragraphs and compile. Report which references were added
   and which existing entries were corrected.

Equation and section numbers of arXiv versions can differ from the published ones. Cite
them in the paper only after checking the published version, or cite the reference
without the number.
