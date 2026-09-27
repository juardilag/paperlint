---
name: scientific-writing
description: Procedure, rules and tools for writing or revising scientific papers so the text is clear, precise and easy to follow, and avoids the typical problems of LLM prose. Use whenever drafting, rewriting, reviewing or editing a paper, a section, an abstract, an introduction, a caption, an appendix or a response to referees, in LaTeX or plain text, in any field.
---

# Writing scientific papers

The main risk in LLM-assisted papers is prose that is informal and overly technical at
the same time: slogans instead of physics, terms used without definition, references to
things the reader has not seen. It reads like two experts talking at a blackboard. This
skill turns the rules that prevent it into a procedure with checks.

Files in this skill's directory:
- `rules.md`: the full rules, by topic. Read the sections you need before drafting.
- `examples.md`: flagged sentences and the rewrites the authors accepted. Read it before
  writing a new section; match the accepted versions in tone and density.
- `scripts/lint.py`: mechanical checks (sentence length, punctuation, openers, banned
  phrases, acronyms, glossary terms, hand-typed references). Run it; don't redo it by eye.
- `scripts/check_refs.py`: checks `.bib` entries against Crossref.
- `scripts/init_project.py`: creates `paperlint.toml` and `glossary.toml` for a paper.

The `cold-reader` agent of this plugin reads a finished section with no context and lists
every place where a reader would ask "what is this?", "which one?" or "why?".

## Project files

A paper directory may contain:
- `paperlint.toml`: lint settings (sentence limits, banned words, disabled checks).
- `glossary.toml`: one name per object, avoided synonyms, appendix-only terms, symbols.
- `CLAUDE.md`: build notes, required content, review status, decisions made so far.

Read all three before working on the paper. They override the general rules where they
conflict. If they don't exist, offer to run `scripts/init_project.py`.

## Procedure (every section, every time)

1. **Read** the project files, the section, and the parts of earlier sections it builds
   on. Note what the reader already knows at this point.
2. **Plan.** Write the topic sentence of every paragraph first and read them in a row.
   They must answer why, what is known, and what we do, and end by pointing to the next
   section. Fix the structure before writing sentences.
3. **Draft**, following the checklist below. Plain words first. A technical term only
   where it earns its definition.
4. **Audit.** Run all of these on the whole section, and fix what they find:
   - `python3 <skill dir>/scripts/lint.py <file.tex> --section "<title>"` (mechanical).
   - **Terms**: list every technical term, where it is defined at first use in the
     document, and its reference.
   - **Notation**: every symbol (text, equations, tables, figures) is introduced with a
     full clause before use, and has one meaning in the section.
   - **Parameters**: everything a results section uses is introduced in the method, its
     figure and its derivation.
   - **Back-references**: every this, that, it, its, such, the same points to one object
     named in the same or the previous sentence.
   - **Redundancy**: each fact once, then check that no premise was cut.
   - **Claims**: numbers match their source, improvement factors state their baseline,
     statements about other papers were read, not assumed. List unread ones as questions.
   - **Cold read**: launch the `cold-reader` agent on the section and fix what it finds,
     or say why a finding is wrong.
5. **After any local edit**, reread the whole paragraph from its first sentence, rerun the
   back-reference and redundancy checks on it, and search the document for any term a
   deleted sentence defined. (The PostToolUse hook of this plugin lints edited paragraphs
   automatically when the paper has a `paperlint.toml`.)
6. **Compile, render the pages, and look at them.** Check figure legends against the
   text's terminology.
7. **Report**: what changed (before and after for anything the authors flagged), the audit
   results, and open questions. Turn every author correction into a rule, in `rules.md`
   if it is general, in the project files if it concerns this paper only.

## Checklist (details and examples in rules.md)

**Sound like a scientist** (rules.md §2)
- No slogans or aphorisms. Say what happens, with the equation.
- No informal words for methods ("recipe", "trick", "engine", "buys", "prices").
- No anthropomorphism ("the bath remembers", "the atoms see").
- No placeholder words ("a microscopic model", "the corresponding equation"). Name it.
- Contrast with prior work explicitly: what they have, what we have, and the limit that
  recovers theirs. Known element first, new element last.

**The reader has no context** (§3)
- Every technical term gets a one-clause definition and a reference at first use, even
  standard ones (master equation, white noise, convolution). Spell out every acronym.
- If a term needs more than a clause, describe the object in plain words and keep the
  term for the appendix.
- Introduce each reference by what it did before relying on it. Cite again at the first
  mention in each section.
- Introduce notation with its concept in a full clause. Figures and captions never
  introduce notation. One meaning per symbol.
- Pronouns and demonstratives point to one object just named.

**Say it once** (§4)
- Each fact once. No term paired with its own paraphrase. No circular definitions.
- But keep premises: a section may recall what it builds on, and every "therefore" needs
  its reason.

**Be specific and correct** (§5)
- Flat in what? Which methods? Tie each claim to the equation that realises it.
- Justify odd factors and structural choices in an equation when it appears.
- Claim only what holds in general. Read papers before describing them.

**Structure** (§6, §9)
- Every section: why, what is known, what we do. Topic sentence first in each paragraph.
- Close each section with a summary and a transition that names the next question.
- The method contains everything the results use; it says what and why, not how well.
- Procedure steps about 70 words. Detail goes to the appendix; important results don't.
- Appendices follow the same rules and open with why they exist.

**Captions and titles** (§7)
- Captions are minimal but self-sufficient, in full sentences, with the parameters.
- Titles say what the section finds or does. Legends use the text's terminology.

**Sentences** (§9, house defaults, configurable)
- Under 25 words. No colons or semicolons in running text. No em dashes.
- No sentence starts with a symbol, a numeral or an acronym.
- No "It is … that", "There is", bare "This is". No fluff ("in order to", "very").
- Introduction: findings in words, no values. Abstract: written last.

## Tone of the report to the authors

Say what you changed and why in plain terms, show before/after for flagged text, and
list open questions separately. Do not claim a check passed unless you ran it.
