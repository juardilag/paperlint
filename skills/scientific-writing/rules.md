# Rules for scientific writing

These rules are about **correctness and clarity**, which a checker can enforce. They
are deliberately few. **Style is not a rule.** It is learned from the house style (the
corpus, `scripts/corpus.py`) and the authors' own edits (`author_edits.md`), and
measured by the blind test; mechanical style rules made earlier drafts read as
generated (`lint.py --style` keeps them as optional notes). Professional English
(section 10), including the ban on semicolons and punctuation dashes, is correctness
and is enforced.

The authors own the prose. A paragraph the authors wrote or approved is changed only to
fix an error, with the smallest edit that fixes it, unless they ask for a rewrite.

**Write no more than is needed.** A language model adds: a reason, a caveat, a check,
a definition, a summary, each defensible alone. Co-authors then spend their rounds
cutting, and most of their corrections are strikes. So the default for any sentence
is not to write it. Every sentence, clause and caveat must pass the deletion test of
section 8 before it is written, not after a reviewer strikes it, and a check that
finds a problem prefers the fix that removes words to the fix that adds them.

## 1. Every term is defined where it is first used
- A technical term, symbol or acronym gets its meaning at its first use in the paper,
  in a clause, with a reference where the field has one. A reader of the journal
  (`audience` in `paperlint.toml`) who knows the term gets the reference only.
- A term that needs more than a clause is described in plain words in the main text,
  and the term itself is kept for the appendix.
- This includes every index, subscript and label (what $n$ and $m$ run over) and
  every argument a function gains ($H(\phi)$ after $\hat H$). Every symbol of a
  displayed equation is named in the sentence that introduces or follows it, even one
  a reader could guess; the `audience` exemption covers terms, never symbols
  (`lint.py` PL023). A quantity referred back to is named physically, not by its
  symbol alone ("the spectral density $J$", not "the $J$ of panel (a)").
- A pronoun or "this" points to one object just named; after a sentence that names
  several, name the subject again ("the spectral density depends", not "it depends").
  A specific object is named specifically: "the critical exponent $\nu$ of the photon
  number", not "a critical exponent"; "NM-TWA and the exact solution", not "the two";
  "the cavity is not integrated out", not "keep the cavity".
- Nothing is referred to before it is introduced. "The X" presupposes that the reader
  has met X: "the exact master equation", "the linearised result", "the baths" and a
  field $B$ are errors until the text has said which one. Section openings and
  roadmaps included: "the memoryless loss of Sec. X" before Sec. X calls it memoryless. A quantity that relates
  two objects names both ("the coupling $\eta_q$ of the cavity to mode $q$").
- Nothing appears suddenly. A new tool (a Poisson bracket, a coupling operator), a
  comparison (with another method) or a change of subject is prepared by the sentence
  before it, so the reader knows why it is there before it is used.
- A connective states a relation that holds ("by", "in turn", "therefore" only for a
  means, a sequence, a consequence); otherwise drop it.

## 2. One name and one symbol per object
- The same object has the same name and symbol in every section, figure, legend and
  table (`glossary.toml`). One symbol has one meaning in the whole paper.
- The appendices use the notation of the main text, never their own: no shorthand
  for a combination the main text writes out ($g/\sqrt N$, not a new $g_N$), no
  change of variable mid-derivation without saying so, and the same variables
  ($\mathbf m$ in the appendix if the main text's equation is in $\mathbf m$).
- Every average says what it runs over (noise realisations, initial conditions,
  both), in the formula as well as in the words, and one symbol never averages over
  different ensembles.
- A special case keeps the general notation, with a label added: the cavity's memory
  kernel is $\Sigma^R_c$, not a new $\Sigma_c$.
- Typography is the same in every equation (hats, bold, indices), and a function
  keeps its argument wherever it appears ($J(\omega)$, not $J$ in one place).
- A sentence about an equation names only what the equation shows (no indices the
  equation does not carry).

## 3. Claims are no stronger than the evidence
- Every number in the text comes from saved data and a script that prints it.
  Recompute it before quoting it; never take it from a comment, a README table or
  memory. Its scope words ("at all ten frequencies", "only", "up to") are part of
  the number and are recomputed with it.
- A result is stated as strongly as its figure and data show, no more ("agrees within
  the statistical error" is checked against the error).
- The paper's own choices (a bath, a parameter) are stated as choices, not as facts
  about a regime. A choice or condition carries its reason in the main text only when
  the argument that follows uses that reason, or when a reader of the field would
  otherwise doubt the choice; then in one clause. Any other reason, a property of a
  sampling scheme, a variance the formula already shows or a detail a referee might
  ask about, goes to an appendix or is cut (section 8, the deletion test). A reason
  the method already gives is pointed to, not repeated.
- An asymptotic value (an exponent, a limit, a scaling law) is attached to plotted
  data only where the data reach it in the plotted range, checked on the reference
  too; otherwise the data are said to be pre-asymptotic, with the value they do reach,
  and legends and labels carry no asymptotic value. A limit stated for a parameter
  set to zero ("for $\kappa\to0$") is not attributed to a run at a small finite value.
- When two checks disagree on a fact (converged or not, inside the error or not), the
  fact is recomputed from the saved data before either version is written.
- A regime word ("non-Markovian", "weak", "fast", "comparable", "memory") holds at the
  paper's parameter values: compare the timescales or frequencies it names, and say
  in which sense the word is meant where it is first used.
- State the general case first, then the paper's instance ("1/S for a spin of length
  S, so 2/N here"). Test every general statement of the method on every example the
  paper treats; a statement with an exception says so.
- Statements about other work are checked against the source (the `literature`
  agent), and credit says what that work did and what this paper adds. "We follow
  Ref. X" only for what X did; a calculation of this paper (its code) is this paper's.
  A wording a reviewer proposes is checked like any other claim. A method is
  credited to the work that introduced it, not only to its latest or a co-author's
  formulation.
- A special case is marked as an example ("for example, ..."), not stated as the
  general rule. A preview or bridge to the next section is a claim too: every word
  holds for all the cases it covers, and it ranks nothing ("of increasing
  difficulty").

## 4. Every limitation has its consequence
- An approximation, a dropped term or a growing error is stated with whether it
  invalidates the results and in which regime or timescale the method holds, with a
  pointer to where the paper tests it.
- A test that isolates one effect says why it isolates it.
- A stochastic equation states Itô or Stratonovich, next to it in a derivation (the
  main text, `sections.md`, Method).

## 5. The method contains what the results use
- Every parameter or ingredient a results section uses is introduced in the method,
  with how it enters. A parameter the results never vary does not belong in the paper
  (check the code).
- How a results section applies the method, part by part (Model, Equations of
  motion, Initial state, Measurement, Result), is in `sections.md`, Results.

## 6. The main text argues, the appendix proves
- Each section says why, what is known and what it does; what its opening and its
  parts do is in `sections.md`, by section type. Results that matter stay in the main
  text; their derivation, the technical detail and the precise size of a deviation go
  to an appendix. A fix for a review finding moves an explanation there; it never adds
  one to the main text.
- Each displayed equation does one job: an equation of motion and the definition of a
  quantity it uses (a force) are separate, separately labelled equations.
- The main text can be followed without opening an appendix. It sends the reader to
  an appendix for a proof or a detail, never for a concept, a table or an equation
  needed to understand the sentence: a pointer is not an explanation.

## 7. Captions reproduce the figure
A caption is read without the text, so it is checked like text: every rule of this
file applies to it, and what a caption contains, and how the figures of a paper share
one language, is in `sections.md`, Figure captions.

## 8. Concise, with everything the reader needs to follow
The text is as short as it can be while the reader can still follow what the paper
contributes and why each step is taken. Both halves are errors to check: a sentence
the argument does not need, and a step of the argument (what is compared, why a case
behaves as it does, what a test isolates) the reader is left to supply.
- A fact appears once in the paper, in the section that shows it, and a mechanism
  is explained once; later mentions point back to it. A premise that a later argument
  needs is recalled where it is needed. Inside a sentence too: a qualifier is said
  once (`lint.py` PL026).
- The deletion test: a sentence, clause or displayed equation of the main text that
  no later sentence, figure, claim or step of the argument uses is cut, or moved to
  the appendix that proves or details it. A displayed equation is used when the text
  refers to it or to the quantity it defines. This test decides when rules pull apart
  (section 1 asks for a definition, section 3 for a reason, section 6 for an
  appendix): a definition or reason that fails it is not added; one that passes stays,
  in one clause.

## 9. LaTeX mechanics
- Cross-reference with one mechanism (`\cref`/`\Cref`, `\Cref` at a sentence start),
  never by hand, and check how it renders: an appendix is cited as an appendix, never
  as "Sec. A 4" (in revtex, `\label[appendix]{...}`, `lint.py` PL028).
- Every displayed equation fits its column: no `Overfull \hbox` in the log for the
  text you touched; render the page and look at it.
- New references go into the `.bib` file, and the authors are told which.
- No link covers a figure: a hyperlink broken across a page restarts on the next
  page and covers any float there, so keep bibliography entries unbroken
  (`\interlinepenalty=10000` before `\bibliography`) and check the compiled PDF.

## 10. Professional English
The register is not style: a sentence a journal's copy editor or a referee would mark
as informal, unidiomatic or ungrammatical is an error, in a paragraph the authors wrote
as much as in a draft, in a section title or a caption as much as in the text. Fix it
with the smallest edit, in the field's words.
- Grammatical, idiomatic English as published in the target journal: articles,
  agreement, prepositions and collocations a native-speaking physicist would use
  ("is subject to a damping", not "gets the damping"; "satisfies its own equation of
  motion", not "obeys an equation of its own").
- No colloquialism, slang or conversational verb ("gets", "buys", "kicks in", "for
  free", "does the job", "the trick", "nothing else enters"). No anthropomorphism: a
  bath has a finite correlation time, it does not "forget"; a spin couples to a field,
  it does not "see" it (`lint.py` PL014).
- The technical term where one exists, used as the field uses it ("the bath
  correlation time is short compared with the relaxation time", not "the bath forgets
  faster than the system relaxes"). A word that has no physical reading in its
  context is an error (examples.md, "Words that do not fit the physics").
- Formal, precise, measured: no contractions, no exclamations, no rhetorical
  questions outside a stated research question, no hype words the data cannot carry.
- Professional is not stiff: "we" narrates, sentence length varies, and the field's
  stock phrases are welcome (`style.md`). This rule removes informality, never voice.
- Section 8 decides which ideas stay; this rule keeps the grammar of the ones that
  do. Cut whole ideas, never articles, verbs or connectives: no clipped appositives
  ("the field outside", a noun phrase hung on a displayed equation, `lint.py` PL029),
  no stacked noun phrases, no telegraphic sentences. Compressed prose reads as
  generated as surely as padded prose, and a section over its budget loses ideas,
  not grammar.
- Openings and closings of sections and appendices are where generated prose shows
  most: before writing one, retrieve corpus paragraphs that do the same job and match
  how they open and close, without echoing their wording (`sections.md`).
- No semicolons and no dashes used as punctuation (`---`, an em dash, or a spaced
  `--`) in running text: they are rare in published physics prose and typical of
  generated text. Use a connective ("because", "so", "whereas", "while") or two
  sentences, and a comma or parentheses for an aside. En dashes in ranges and names
  (2--5, Caldeira--Leggett) are correct (`lint.py` PL003, PL004).
- One spelling convention for the whole paper, American English by default, as at the
  APS, AIP and IOP journals: -ize and -ization (polarize, realization), -or (color,
  behavior), -er (center), -yze (analyze), single l (modeled, labeled), gray, toward.
  A paper for a journal that wants British spelling sets `spelling = "british"` in
  `paperlint.toml` (`lint.py` PL025). Bibliography entries keep the spelling of the
  published titles.

## 11. Maintaining the rules
- A rule is added only for an error a checker or a reader can verify, never for
  taste. Before a rule is added, find the rule it overlaps and merge them; this file
  does not grow by more than it shrinks without a reason. A check a pattern can do
  goes to `lint.py`, not here.
- A rule that asks for text (a definition, a reason, a caveat) is checked against
  the deletion test before it is added: reviewers strike what checkers add, and a rule
  that only adds makes every round longer than the last.
- A rule that holds for one kind of section only (an opening, a Model paragraph, a
  caption) goes to `sections.md`, under its section type, and that type's review
  status is updated.
- An author's edit of the prose is recorded as a pair with `/paperlint:learn`, not
  as a rule. A reviewer's remark about style becomes an objection in `examples.md`,
  with their words and no invented rewrite. The house style itself is not changed by a
  paper's authors.
- A change to how paperlint writes is kept only if the blind test on a fixed sample
  (same paper, same seed) does not get worse.
- An author correction about content goes to the paper's `CLAUDE.md` or
  `glossary.toml`.

## 12. The project file `CLAUDE.md`
`CLAUDE.md` holds what a reader of the paper and its code cannot infer, and every
command reads it, so every line costs attention. It holds decisions (who, when and
why; one without its reason is flagged), content the authors require, the evidence
map (script, data and command for each figure, table and quoted number, and where
heavy runs go), the build, and the review status with open author items. It does not
hold terminology (`glossary.toml`), lint settings (`paperlint.toml`), the history of
findings, a map of the paper, style, or anything the paper, code or git history
states. One checkable instruction per line; objects named by label, not number;
entries replaced, never duplicated; a co-author comment that contradicts an entry is
reported to the user as a conflict. Text a co-author struck stays out: no check,
rule or lint finding restores it, even reworded. A struck passage kept on purpose
(moved rather than cut, or overruled by the authors) is listed as
`kept-strike: <round> C<n>` with its reason, and `strikes.py` reports every other
struck passage that is back.
