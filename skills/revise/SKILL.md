---
name: revise
description: Revise one section of a paper to a finished state in a single command. Reads the whole paper for context, then runs lint, audits, literature checks and cold reads in rounds, fixes the editorial findings without asking, self-checks every edit against the rest of the paper, keeps a ledger of settled findings, and stops when a round brings nothing new that must or should be fixed. Only content decisions go to the authors. Use when the user asks to revise, review, finish, polish or "run the plugin on" a section, an appendix, a caption or the abstract.
argument-hint: "<file.tex> <section title or line range>"
---

Bring one section to a finished state and stop. A section is never independent of the
rest of the paper: every round reads and checks it in the context of the whole paper.

**The main goal is prose that reads as written by a scientist, not generated**, for a
researcher of the journal's field (`audience` in `paperlint.toml`), not for a student. Correct
physics and defined terms are necessary, but a section is not finished while any
paragraph reads as a list, a chain of definitions or a patchwork of fixes (rules.md,
section 2b). Every fix is judged by that goal as well: a fix that answers a finding by
appending a sentence is not done until the paragraph reads whole again.

## Before the first round

1. **Target.** Identify the file and the section from `$ARGUMENTS`. Load the
   `scientific-writing` skill and read `rules.md` (all of it the first time in a
   session) and `examples.md`.
2. **Project files.** Read `paperlint.toml`, `glossary.toml`, `CLAUDE.md` and the ledger
   `paperlint_ledger.md` in the paper directory (create the ledger if missing). The
   ledger lists findings already settled: fixed, rejected with the reason, or decided
   by the authors. Author decisions are not reopened by the command, with two
   exceptions: a correctness question (a claim that may be false) is never settled by a
   decision on wording, and a later comment by a co-author that contradicts a recorded
   decision is reported to the user as a conflict. Record who decided and when, so
   conflicts between co-authors can be seen. Review comments in a PDF (highlights,
   strike-outs, sticky notes) are read from the annotations themselves, with the text
   each one marks, not from the rendered page.
3. **Paper map.** Read the whole paper once and write or update `paperlint_map.md` in
   the paper directory:
   - per section, one line on what it establishes and which results it uses;
   - every symbol with its meaning and where it is defined;
   - every technical term with where it is defined;
   - every number the text quotes, with its source (figure, table, data file);
   - every equation, figure and table label that other sections refer to.
   Rebuild an entry whenever its section changed. The map is how the section is checked
   against the rest of the paper; it is not a substitute for reading the neighbouring
   sections, which you also do.
4. **Code and data.** If `CLAUDE.md` names the code or data behind the results, locate
   them. A claim about what a run did is checked there, not guessed.
5. Record the word count of the section.

## Each round

1. **Mechanical.** Run `lint.py` on the section and fix everything it reports. The
   texture checks PL018 (a repeated modifier), PL019 (an enumeration) and PL020 (an
   object as agent) are info-level because they can be false positives, but each one
   is read and either fixed or dismissed with a reason; they mark the paragraphs the
   rhythm audit starts from.
2. **Audits**, done by you, against the section and the paper map:
   - terms: each defined at its first use in the whole paper, with a reference, and
     each the precise name the field uses for the object (the annihilation and creation
     operators of a mode, not its "ladder operators");
   - notation: one meaning per symbol in the whole paper, including averages and
     brackets; the same symbol as in the other sections for the same object;
   - back-references: every this, that, it, the same points to one object just named;
   - redundancy: each fact once in the paper, not only in the section; premises kept;
   - claims: numbers match their source, statements about other work are supported,
     results are stated no more strongly than the figures and data show, and the
     paper's own choices (a bath, a parameter, a coupling) are stated as choices, not as
     facts about a regime ("for this test we add ...", not "at large N the bath is ..."). Recompute every
     number quoted for a figure from its data over the plotted window, and check every
     statement about an inset against what the inset draws (read the plotting code); an
     exception stated in a summary points to the panel that shows it;
   - why: ask "what is it?" and "why?" of every sentence, as a researcher of the
     journal's field who knows only the earlier text, and answer only the questions such
     a reader would ask. A quantity given by a formula says what it is physically and
     why it has that value, without reading the formula aloud; a correction or replacement says what goes wrong without it; a property
     the text claims (real, positive, conserved) but the displayed formula does not
     show, because of an i or a sign, gets its reason. The answer
     is one clause in the main text; its mechanism goes to the appendix;
   - weight (rules.md, sections 2 and 3): cut every sentence that defines what the
     audience knows, restates a displayed formula in words, or coins a name the paper
     uses less than twice; every paragraph opens with the physics it is for;
   - consequences (rules.md, section 5): every limitation says whether it invalidates
     the results and on which timescale or regime the method holds; every statement
     that a test isolates something gives the reason; every scaling is given in general
     before the paper's instance; a consequence is stated directly, not as a
     counterfactual; the closing does not preview what later sections find;
   - conventions and lineage: a stochastic equation states Itô or Stratonovich next to
     it; a known class of equations cites its classic literature; typography (hats,
     bold) is the same in every equation of the paper;
   - method applied: every equation of motion in a results section follows from the
     general method; compare it with the method and with the code behind the figure;
   - structure (method sections): the central equation comes first and each of its
     terms is explained after it; the procedure follows. The step that carries the main
     idea and the recovery of the known method get the space they need; technical detail
     stays short (rules.md, section 6);
   - generality: the method is stated in the most general form its derivation supports,
     with where it holds approximately beyond the exact case (rules.md, section 5);
   - examples: list the examples the paper treats, and test every general statement of
     the method on each one; a statement with an exception says so;
   - restrictions: every "only", "at zero temperature", "for weak coupling" the text
     states has a reason in the text or the appendix; one that has none is checked
     against the derivation, the code and the literature, and is a correctness finding
     if it cannot be confirmed;
   - framing: credit to other work says what it did and what this paper adds, and no
     sentence presents the paper as carrying out someone else's plan;
   - scope: every statement about a step of the method holds for every case the paper
     uses (all systems, samplings, integrators); a general step does not single out
     one kind of system but points to the appendix that treats each;
   - rhythm first (rules.md, section 2b), the most important audit: reread every
     paragraph of the section whole, not sentence by sentence, and apply the read-aloud
     test. Rewrite any paragraph that reads as a list, a chain of definitions, a
     patchwork of added sentences, or instructions outside a procedure. Give each
     paragraph the rhythm verdict of rules.md, section 2b (order, enumeration, agent,
     repetition, why, pointers) and write down its weakest sentence; "reads fine" is
     not a verdict. For the opening and the closing paragraph of the
     section, first write down in two or three plain sentences what the paragraph must
     tell the reader and why, then draft it fresh from that note without looking at the
     current text, and keep whichever version reads better. Patching an opening
     sentence by sentence keeps its list structure. This audit runs in every round, and
     again after the fixes, because the other fixes create patchwork;
   - main text vs. appendix (rules.md, section 6): detail in the appendix, the argument
     in the main text; the section does not grow without a reason.
3. **Cold read and referee read.** Launch the `cold-reader` and the `referee` agents on
   the section, in parallel. Pass both the paths of the ledger and the paper map, and
   tell them not to raise settled findings again unless the text changed. The cold
   reader finds what an outsider cannot follow; the referee finds what an expert doubts
   or finds pedantic. When the two conflict (the cold reader asks for a definition the
   referee calls pedantic), the audience in `paperlint.toml` decides: a reference is
   always given, a clause only if that audience needs it. Its rhythm verdict does not replace your own: a paragraph that
   either of you fails is a should-fix finding.
4. **Triage.** Check every finding against the text. Put each one in one class:
   - **Editorial**: fix it now, without asking. This covers undefined terms and
     symbols, inconsistent notation, missing pointers, ambiguous references, wording,
     sentence structure, redundancy, a missing one-clause reason for a factor or a step,
     the statement of a standard convention (for example the Stratonovich reading of
     physical noise), and moving detail between the main text and an appendix. Where a
     standard answer exists in the literature, use it and cite it.
   - **Literature**: a claim about other work, a "says who?", or a statement that needs
     a source. Launch the `literature` agent (one per topic, in parallel) and apply the
     result when the sources support it. Present a result as derived in the paper when
     no source states it.
   - **Author decision**: collect it for the report and do not edit. This covers what
     the paper claims about its own results, the scope and the structure of the paper,
     adding or removing a result, a figure or a section, anything the code or the data
     must decide, and anything the authors already decided (`CLAUDE.md`, the ledger).
     A correctness finding is never put in this class to avoid checking it: check it
     first (derivation, code, `literature` agent), and send only the decision that
     remains to the authors.
   - **Rejected**: the finding is wrong. Write the reason in one sentence.
5. **Apply** the editorial and literature fixes. Length budget: a round that adds text
   cuts at least as much elsewhere in the section, unless it fixes a wrong claim or a
   missing consequence. Cut pedantic sentences first.
6. **Self-check every edit** before anything else runs:
   - reread each changed paragraph from its first sentence, as a whole, against
     rules.md section 2b; if the edit added a sentence, rewrite the paragraph so the new
     content sits inside the sentences that need it, instead of appending it;
   - check each changed sentence against the equations and symbols around it (signs,
     factors, which variable, which average), and against the paper map;
   - grep the whole paper for every symbol, term, label and equation number the edit
     touched, and fix the other occurrences so the paper stays consistent;
   - if an edit removed a definition, find the next use of that term and define it
     there;
   - if an edit rewrote a pointer or a fragment as a claim, check that the claim is no
     narrower than what it replaced (every case the pointer covered);
   - if an edit changed a derivation, follow it to the equation it produces and check
     that the result is unchanged or that every later use is updated.
   Edits of the previous round are the most common source of new findings. The
   self-check is what keeps a round from creating work for the next one.
7. **Close the round.** Rerun `lint.py`, compile, and update the ledger and the map.

## When to stop

Stop after a round in which the cold read and the audits bring no new finding of
severity must fix or should fix, and every paragraph of the section passes the rhythm
verdict (rules.md, section 2b) in both your audit and the cold read. A paragraph that
reads as generated is a should-fix finding. A new finding is one that is not in the
ledger and does not repeat a rejected one. Stop also after three rounds, and say so.
Do not start another round for consider-level findings only; fix the editorial ones in
passing.

Rhythm is the exception to the three-round limit, because it is the main goal. If a
paragraph still fails the rhythm verdict after the last round, do one more pass on
those paragraphs alone: redraft each from a note of what it must say, rerun `lint.py`,
self-check the edit, and give the rewritten paragraphs a cold read with the rhythm
verdict only. Report any paragraph that still fails.

A cold reader always finds something. The ledger, the self-check and this rule are what
end the loop.

## Report

- The section length before and after. If it grew, say why, and what was cut.
- The rhythm verdict of the final text: one line per paragraph with its first words,
  pass or fail, and its weakest sentence.
- The paragraphs rewritten for rhythm, each with what made it read as generated.
- What was changed, grouped by class, with the before and after for anything an author
  had flagged. Name every change outside the section made for consistency.
- Errors found (a sign, a factor, a wrong claim), listed first and separately.
- The literature used, with what each source supports.
- The rejected findings, each with its reason.
- The author decisions, each as one question with a recommendation. These are the only
  items the authors need to act on.
- The lint result, whether the paper compiles, and whether the run converged or
  stopped at three rounds.

Turn every author correction into a rule: in `rules.md` if it is general, in the
paper's `CLAUDE.md` or `glossary.toml` if it concerns this paper only.
