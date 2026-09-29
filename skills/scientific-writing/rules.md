# Rules for scientific writing

These rules come from line-by-line reviews of LLM-assisted papers by supervisors and
co-authors. They apply to any field. The examples are invented to illustrate them, most
of them in one imaginary physics paper about atoms in an optical lattice coupled to a
phonon bath. Apply the principle, not the example.

**House defaults.** A few rules are strong preferences rather
than universal rules: no colons or semicolons in running text, no em dashes, sentences
under 25 words, and no numbers in the introduction. They are on by default because they
push LLM prose toward plain English. A paper can switch the mechanical ones off in
`paperlint.toml`, and its `CLAUDE.md` can override the others. Journal style always wins
where it conflicts.

## 0. Say it in as few words as the ideas need
This rule and the rhythm rules of section 2b come first, because they are what most
separates generated text from a scientist's. An LLM writes more than was asked: it
answers every question in place, qualifies every claim, glosses every term, recalls
what came before and previews what comes next. Each addition is defensible and the sum
is a text that is dense and long. A scientist communicates every idea once, in the
fewest words that keep it clear, and leaves the reader's time alone. An author read an
introduction that had grown from 1519 to 1764 words while every fix in it was correct
and wrote: "the text is too dense, is too large ... a human seeks to communicate all the
ideas in a concise readable way, not wasting space or time".

- **Length follows the ideas, not the questions.** For every sentence ask: would the
  reader miss it if it were cut? If not, cut it. For every paragraph ask: what is its
  one idea, and does every sentence serve it?
- **Concision and the budget are different things.** Concision is a property of every
  sentence: it earns its place and says its idea once, in the fewest clear words. It
  applies to every section and is judged by reading. The budget is the length the
  section needs for what it must say. It is not a number fixed in advance or shared
  between papers: it is derived, section by section, from the section's own content.
- **Derive the budget from what the section must say.** Before revising or writing a
  section, write its idea inventory in `paperlint_map.md`:
  1. List every idea the section must convey: its role in the paper (why, what is
     known, what we do), what later sections use from it, and what `CLAUDE.md` requires.
     One line per idea, in plain words. An idea the paper does not need is struck from
     the list, not written shorter.
  2. Give each idea the words it needs, judged from what it is: a claim with its
     reason, a step of an argument, a piece of context with its references, an
     equation with its meaning, a definition clause for a term the argument turns on.
     The central idea gets the space it needs to be understood; a supporting fact gets
     a clause.
  3. The sum is the budget of the section. `lint.py --section "<title>" --words` gives
     the current prose length. Text beyond the budget is text the reader would not
     miss, and is cut, keeping every idea of the inventory.
  A section under its budget can still be verbose, so the concision audit runs on every
  sentence either way. PL022 marks a paragraph over `max_paragraph_words` as a place to
  look, not as a verdict.
- **A fix pays for itself.** A correction rewrites the sentence it corrects; it does not
  add one. A reason, a qualification or a definition goes into an existing sentence as
  a clause, or displaces something the reader would not miss. A revision does not end
  longer than it started unless the authors asked for new content.
- **Precision without bulk: qualify a claim where it is shown.** The introduction and
  the summaries state a finding in one clause; its conditions, numbers and caveats
  live in the section that shows it. "Relaxes to a state that obeys the relation" in
  the introduction, "at large N, within the statistical error, while the order
  parameter still relaxes" in the results. A referee's "overstated" is answered by a
  more exact word, not by a longer sentence.
- **Where generated text grows, and what to do instead:**
  - a survey that lists every method or paper: name the representative ones and the
    property they share;
  - a term glossed that the argument does not turn on: cite it (section 3, "The
    balance");
  - "X. X is Y." two sentences where one does: "X, which is Y";
  - a recap of the previous section or a preview of the next: one clause of transition;
  - stacked conditions and hedges: state each condition once, where it first applies;
  - an example after a clear statement: keep it only if the statement is not clear
    without it.
- **The cut test.** After drafting or revising, cut the text by a fifth without losing an
  idea. If that is possible, the draft was too long; keep the cut version.
- **Priority.** Correctness comes first, but correct and short: fix a wrong claim by
  rewording it. After correctness, concision and the rhythm of section 2b outrank the
  completeness of qualifications and glosses.

## 1. The core problem with LLM-speak
LLM writing is informal and overly technical at the same time. The syntax is odd, the
names for things are obscure, and many nontrivial points are taken for granted. It reads
like two experts talking at a blackboard, which makes it unreadable to anyone else.
- Assume every reader, even an expert and even in an appendix, needs a reminder of each
  concept or at least some context. Define what you use and, above all, say **why** you
  use it.
- This does not mean deriving everything from scratch. For known but technical material,
  cite the literature and describe only the minimum the reader needs to follow the
  argument.
- Don't overuse colons and semicolons; they are rare in real English prose. Prefer two
  sentences. When a colon is used, the next word is usually capitalised.
- Reference on scientific writing in English: Celia Elliott's guides,
  https://people.physics.illinois.edu/Celia/ (condensed in section 9).

## 2. Write like a scientist, not like an LLM
Reviewers flag these as "no human would say it like that":
- **Aphorisms and slogans.** Examples: "detailed balance is a property of the
  construction, not an assumption", "the coupling fixes everything", "prices the two
  shortcuts", "the only approximation, and it acts on the lattice alone". Say the physics
  plainly.
- **Dash asides** ("– the phonons are already in the noise –"). Use no em dashes at all.
  Rewrite with a comma or a full stop, not a colon or semicolon. En dashes only in ranges
  (2.1–2.6) and joined names (Caldeira–Leggett).
- **Meta phrases that do nothing**: "in the order it is carried out", "Applying the
  method.", "Table I gives both for…". Cut them.
- **Italic emphasis on whole sentences.** Don't use it.
- **Colloquial metaphors for technical quantities.** "How long the lattice remembers"
  should be "the phonon correlation time". Use scientific language.
- **Informal nouns and verbs for methods and results**: "the recipe", "the trick", "the
  engine", "buys", "prices", "the price of". Write "the method", "the procedure", "the
  formulation", "costs", "requires".
- **Compressed participle phrases** that pack a claim into a clause: "approximating the
  lattice alone", "with the atoms made classical rather than exact". Write the
  claim as a full sentence with a subject and a verb.
- **Narrating a concept as a sequence of actions**: "the phonons are traced out before
  the first trajectory is run". State what the method assumes or approximates instead.
- **Stiff, list-like, "student" prose**: short declarative sentences strung together
  without connecting logic. Paragraphs should flow and argue. Polish slowly; don't rush.
- **Placeholder words that name nothing**: "a microscopic model", "the corresponding
  equation", "a structured bath" with no structure given. Name the concrete object, for
  example "the Hamiltonian of the atoms, the phonons and their coupling (Eq. (2))".
- **Contrasts left implicit.** When the work differs from the closest prior work, say
  exactly what each side has, and show how the prior result is recovered as a limit.
  Example: "In Ref. [12] the damping depends only on the state at the same instant and
  the noise is white. Here the damping is a convolution with a memory kernel and the noise
  is coloured. With a flat phonon spectrum the kernel becomes δ(τ) and Ref. [12] is
  recovered."
- **Put the known or contrasted element first and the new element last.** "Instead of a
  rate equation, we start from the Hamiltonian…" reads better than "We start from the
  Hamiltonian…, Eq. (2) below, instead of a rate equation".
- **Losing context**: stating something as if it were obvious, or jumping to a quantity
  the reader wasn't prepared for ("the occupation decays at 2γ" in the middle of a
  kernel discussion: "the occupation of which site?"). Set up each quantity before it
  appears.
- **Anthropomorphism.** Atoms don't "inherit" or "see", baths don't "remember", cells
  don't "decide", drives don't "move" things, and a coupling doesn't "fix" anything. Describe the physics that
  actually happens.
- **Explain what a formula means; do not read it aloud.** A displayed equation already
  says which symbols are multiplied, integrated or summed. A sentence that repeats it in
  words ("the convolution adds up the past values of A, each weighted by the kernel at
  the time difference", "its first term is the classical dynamics, the second the
  force", "the step function enforces causality") is pedantic. A co-author wrote "the
  point is to explain the physical meaning of mathematical formulas, not to put them in
  words". Keep only what the equation does not show: what the quantity is physically,
  why it has this form, and what follows from it ("the damping at time t depends on the
  whole past of the system, over the memory time of the bath").
- **State a consequence directly, not as a counterfactual.** "With the classical noise,
  2T/ω in place of coth, the trajectories would relax to classical statistics" makes the
  reader invert the sentence. Write what the method does: "The coth factor carries the
  zero-point fluctuations of the bath, so the trajectories, although classical, relax
  to the quantum thermal state." One counterfactual is fine where the alternative is a
  method the reader knows.

## 2b. Rhythm and texture: what makes prose read as machine-written
A text can pass every rule above and still read as generated. These patterns cause it.
They are harder to see than a banned word, so check for them when rereading a paragraph.
- **Uniform short sentences.** The 25-word limit is a ceiling, not a target. A paragraph
  of ten sentences of twelve words reads as a list. Vary the length, and join sentences
  that belong together with the word that states their relation: because, so, but,
  although, while, whereas, which. Two full stops where one "because" would do lose the
  logic.
- **The same opening in every sentence.** "The kernel … The kernel … The noise … The
  noise …". Start some sentences with the condition, the contrast or the cause ("For a
  flat spectral density, …", "Because the bath is harmonic, …").
- **Chained definitions.** One sentence per term, each "X is Y, which means that Z",
  turns a paragraph into a glossary. Define a term inside the sentence that uses it, or
  define two related terms together. Use "which means that" at most once per paragraph.
- **Parenthetical pointers everywhere.** "(Sec. III A)", "(App. A2)", "(Table I)" after
  every clause. Keep at most one pointer in parentheses per sentence. When the pointer
  matters, make it the subject ("App. A2 derives the correlation"); when it does not,
  cut it. A roadmap sentence that lists the appendices is the exception.
- **Stacked qualifications.** "To leading order, at zero temperature, for the
  rotating-wave coupling, in the white-noise limit, …". State the conditions once, where
  they first apply, usually at the start of the paragraph, and do not repeat them in
  every sentence.
- **The antithesis reflex.** "X is a consequence of the derivation, not an additional
  assumption", "not A but B", "rather than". LLMs use this contrast by default. Keep it
  only where a reader would really expect the rejected alternative, and at most once in
  a section.
- **Numbered paragraphs.** "In the first ... The second test ...", "First ... Second
  ..." turn an argument into a list. Say how the items relate ("two known results
  constrain it from different sides"), and let each item follow from that claim. An
  enumeration is fine where the items really are a sequence (the steps of a procedure).
- **Objects as agents.** "The model tests the kernel", "the data confirm", "the
  simulation explores". The authors test, the data show. Write "We test the kernel on the
  model". Sections, figures and appendices that "show" or "derive" are accepted usage.
- **Repeated modifiers.** "integrated out exactly ... solved exactly ... an exact
  reference". A modifier said three times in a paragraph loses its meaning; say it once,
  where it matters.
- **Openings and closings are drafted, not patched.** Patching an opening sentence by
  sentence keeps its structure, including a list structure. Write down what the paragraph
  must tell the reader and why, then draft it fresh and compare.
- **Lists of three.** "clear, precise and robust", "why, what and how". A triple is a
  rhythm, not an argument. Name the items that matter, however many there are.
- **Signposting and transitions that carry nothing.** "Notably", "Importantly",
  "Crucially", "Interestingly", "It is worth noting", "Moreover" at the start of a
  sentence, "In this section we", "We now turn to", "As discussed above". Cut them. If a
  point is important, the sentence should say why.
- **Stock phrases.** "plays a key role", "sheds light on", "paves the way", "a testament
  to", "the landscape of", "intricate", "pivotal", "underscores", "showcases". Say what
  happens.
- **Echo endings.** A paragraph that ends by restating its first sentence ("This shows
  that the method is exact.") adds nothing. End on the new point, or on the step that
  leads to the next paragraph.
- **Paraphrase after a symbol.** "the noise ξ, the random force," or "Γ, the rate,"
  when both were already defined. Once a symbol is defined, use it alone.
- **Patchwork paragraphs.** Revisions add one sentence per finding: a definition here
  ("Here ω₀ is ..."), a reason there ("It equals ..."), until the paragraph is a string
  of answers with "then ... then ..." between them. When an edit adds a sentence, reread
  the paragraph whole and rewrite it so that each sentence follows from the one before.
- **Instructions outside a procedure.** "Take the rotating-wave coupling ..." in running
  prose reads as a lecture. Outside numbered steps, state the condition ("The limit
  requires ...", "For a flat spectral density, ...").
- **Over-hedging.** "may potentially", "could possibly", "appears to suggest". One hedge
  per claim, and only when the claim is uncertain. Results the paper shows are stated
  plainly.

- **Pedantry.** Sentences spent on what the reader of the journal already knows (what a
  Langevin equation is, what a step function does), or on reading a displayed formula
  aloud. It reads as a lecture, and it hides the physics the paragraph is for. The cure
  is to cut, not to rephrase.

- **Density.** Every clause carries a qualification, a gloss or a pointer, so the reader
  must hold five things at once. Cut to the one idea of the sentence, and move the
  qualifications to where they are shown (section 0).

The test: read the paragraph aloud. If it sounds like a list, a press release or a
lecture on terminology, rewrite it until it sounds like one scientist explaining a
result to another.

**The rhythm verdict.** Every command that writes or changes text (write, revise,
finish) and the cold reader judge each paragraph with the same seven questions, and
record its weakest sentence. "Reads fine" is not a verdict.
1. *Order.* Does each sentence follow from the one before, joined by the relation
   between them, or could the sentences be reordered without loss?
2. *Enumeration.* Is it built as a list ("The first ... The second ...") where the text
   could say how the items relate?
3. *Agent.* Does an object act like a person ("the model tests")?
4. *Repetition.* Is a modifier or a claim word repeated, or a noun phrase where a
   pronoun or a restructure would do?
5. *Why.* Does an opening say why, and does a closing end on the new point?
6. *Pointers.* Are references hung at sentence ends where they carry nothing?
7. *Weight.* Does a sentence tell the journal's reader what they already know, or
   restate a displayed formula in words? Would the reader miss it if it were cut? Is
   the paragraph dense with qualifications that belong where the result is shown? Cut.

A paragraph that fails any question is a should-fix finding. The opening and the closing
of a section get the strictest reading and are drafted fresh from a note of what they
must say, then compared with the current version (see "Openings and closings are
drafted, not patched" above).

## 3. The reader has no context
Terms
- **Define for the audience, inside the sentence that uses the term.** The reader is a
  researcher in the journal's field (`audience` in `paperlint.toml`), not a student.
  Every technical term gets a reference at its first use in the document, even a
  standard one; cite the original work where possible, otherwise a standard textbook.
  A definition is added only where that reader may not know the term, or where the
  paper uses it in its own sense, and it is a clause folded into the sentence that uses
  the term, saying what the object does in this paper ("a Langevin equation [refs], in
  which the jump operators set both the damping and the noise"). It is never a
  sentence of its own ("A Langevin equation is an equation of motion that contains,
  besides the deterministic dynamics, a damping term and a random force"): a co-author
  called a method opening built of such sentences "waaay too pedantic". Terms that
  readers of a neighbouring subfield have asked about (master equation, white and
  coloured noise, Wigner function, Poisson bracket, fluctuation–dissipation relation,
  multiplicative noise, "integrating out", named models; likelihood, random effect,
  cross-validation, knockdown outside physics) get the reference and, where the
  audience needs it, the clause. Both reviewers are satisfied that way: the one who
  asked "what is white noise? reference?" and the one who found the definitions
  pedantic.
- **The balance: a term the argument turns on gets its meaning, whoever the reader is.**
  The audience decides the terms used in passing, not the ones the paper's point rests
  on. If the contrast the section draws is between two terms (white and coloured noise,
  Markovian and non-Markovian, local and collective coupling), each gets a clause with
  its meaning at first use, even for experts: "the noise is white, uncorrelated between
  different times", "coloured, correlated over the memory time". A few words cost
  nothing, and without them a reader outside the subfield misses the point of the
  paper. After an audience rule removed such clauses, an author objected: "we must try
  not to assume anything of the reader; we can't explain everything, but this is
  important". The test for each term:
  1. Does the argument of the paragraph depend on what the term means? Then give the
     meaning in a clause, at first use in the paper.
  2. Is it standard vocabulary used in passing? Then a reference is enough, unless the
     audience may not know it.
  3. Either way, never a definition sentence of its own, and never a textbook
     explanation: a clause of five to ten words, fused into the sentence.
- The definition goes where the term first appears (usually the introduction), not later.
- Spell out every acronym at first use, including common ones (QED, GPU).
- **Use the precise name the field uses.** In second quantization a and a† are the
  annihilation and creation operators of a mode, not its "ladder operators". A loose or
  borrowed name reads as written by someone outside the field.
- **Prefer a plain description to a term that needs defining.** If a term needs more
  than one clause to define in the main text, describe the object in plain words instead
  and keep the term for the appendix (see 6). Examples: "the kernel describes how the
  phonons respond at time τ to a displacement of an atom at time 0" instead of "the
  retarded response function", and "a function of these variables" instead of "a Weyl
  symbol on phase space".
- Unusual properties of familiar objects need one sentence saying what they mean and why
  they arise. For example, "the noise is then complex" provoked "how can a noise be
  complex?". Write "Because the hopping operator is not Hermitian, the force on the atoms
  is a complex field, ξ = ξ₁ + iξ₂ with ξ₁ and ξ₂ real Gaussian noises", and give its
  correlation.
- Jargon ("a cumulant closure", "symmetrised correlators", "a counter-term") needs a
  one-line explanation. If it doesn't matter to the argument, drop it.
- If the document never uses something, don't mention it in the main text.
- **Coin a name only if it pays for itself.** A name the paper invents ("we call this the
  quadrature coupling") must be used several times later and be easier to read than
  what it stands for. Otherwise describe the object where it appears ("a Hermitian
  coupling operator") and move on. A co-author asked of such a name "do we care about
  this nomenclature? Does it help?". The same holds for a named case that only one
  table uses: name it in the table.

References
- Introduce every reference by what it did (authors, system, result) before leaning on
  it. "The rate equation of Ref. [12]" means nothing to someone who hasn't read [12].
- For every step of a method, cite where it was done first.
- **Cite the lineage of the formalism you adopt.** If the method takes the form of a
  known class of equations (a generalized Langevin equation, a Kalman filter, a mixed
  model), cite the classic literature of that class, not only the paper the equation was
  taken from. A co-author flagged a non-Markovian Langevin equation that cited only the
  quantum source: "you'd need to cite the extensive literature on classical,
  non-Markovian Langevin equations".
- **Credit precisely, and do not frame the paper as someone else's plan.** Say what the
  earlier work did, and next to it what this paper adds. "Ref. [12] outlined this
  extension in an appendix, and we carry it out" was flagged by the author of Ref. [12]
  himself: "this can give the referee the impression that the work is incremental".
  Credit belongs in the introduction, where the contribution is stated; the method
  describes the method. The same author also flagged the opening sentence of the method,
  "Hosseinabadi et al. derived from the Lindblad equation a Langevin equation ...": a
  section that opens with another group's result as its starting point reads as an
  extension of their work. Open with the physics (what the known approach cannot
  describe, and why), cite the earlier work inside that sentence, and name it only where
  the text uses its result (a limit that recovers it).
- Cite again at the first mention in each section, even if the introduction cited it.
  Readers jump straight to a section.

Symbols and notation
- Define every symbol and parameter before using it, with its full name: "H_S the system
  Hamiltonian", not "H_S the system".
- **Introduce notation together with its concept**, in a full clause. Write "a
  convolution, (K ∗ A)(t) = ∫dt′ K(t−t′)A(t′)", or "denote the set of all φ_α by φ".
  A terse apposition ("collectively φ") is not enough.
- Figures, captions, tables and later sections only use notation the text has already
  defined. They never introduce it (a caption saying "with ∗ the convolution" was
  flagged). The exception is parameters that belong only to one figure, which its caption
  defines. When a figure shows a symbol, check that the text defines it before the figure
  is referenced.
- **Typography is uniform.** If operators carry hats, every operator does, including H
  and H_S; if vectors are bold, every vector is. Check each equation, not only the one
  being edited. The reader takes a missing hat for a different object.
- Don't reuse a symbol for two things in the same section (e.g. θ for a step function and
  a phase). This includes averages and brackets. "The overline denotes the average over
  noise realisations" followed later by "from here on the overline denotes the average
  over trajectories" gives one symbol two meanings. Define it once, as the average that
  covers both (over trajectories, each with its own noise realisation).

Back-references
- **Demonstratives and pronouns must point to something unique that was just named.**
  "That Hamiltonian" or "this equation" leaves the reader searching. Write "the
  Hamiltonian of Eq. (2)" or "the Langevin equation (6)". The same applies to "the same",
  "such", "the corresponding", "the above", "it" and "its". Examples that failed:
  - "The same step underlies the fermionic method" did not say which step, or the same
    as what. It became "This sampling step is the same as in the method without phonons".
  - In "The convolution adds up its past values", "its" read as the convolution. It became
    "the past occupations n(t′)".
  - In "θ(τ) makes it vanish, and its decay time…", the nearest noun was θ, not the kernel.
- **No possessive pronoun that hangs a property on an equation or a list of works.**
  "Their damping depends only on the state ..., and their noise is white" (their = the
  Langevin equations of three cited papers) was disliked by an author, as was the
  parallel "Its damping ..., and its noise ...". Say where the property lives: "In these
  equations the damping depends ...", "The damping then depends ...". A possessive is
  fine for a physical owner ("the spectral density of the bath", "its temperature").
- Name the object when two candidates are in play ("its spectral density" with two baths).
- Don't use names that collide with better-known ones ("the standard model" for a
  physics model reads as the Standard Model). Name the model.

## 4. Say it once
- Don't restate the same idea in the introduction, the method and the results ("we have
  said that many times"). The introduction and the method must not share paragraphs.
- **No redundancy at any scale.** Each fact appears once.
  - Within a paragraph, don't repeat a quantity or claim in nearby sentences. "The
    phonons start at temperature T. They then enter only through T and J(ω)" states T
    twice. Write "a thermal phonon bath affects the atoms only through its temperature T
    and its spectral density J(ω)".
  - Don't define a term circularly ("the response function, the response of the bath").
  - **A "because" gives a reason, not the definition.** "Because the noise multiplies a
    function of the system variables, it is multiplicative" states the definition of
    multiplicative noise as its cause; an author asked "this makes no sense". Say what
    follows from the fact instead ("the noise is multiplied by a function of the state,
    so in the white-noise limit the equation must say where in a time step that function
    is evaluated").
- **A word that resolves a problem needs the problem in the text.** "Unambiguous",
  "consistent", "well defined", "regular", "no longer an issue" answer a question. If the
  text never raised that question, the reader cannot tell what the word means ("is
  unambiguous: what is that?"). This usually happens when a fix copies a reviewer's
  shorthand: the referee wrote "for coloured noise the Itô/Stratonovich ambiguity is
  absent", and the fix wrote "is unambiguous" without the ambiguity. Answer a finding in
  the paper's own terms: state the issue in one clause, then its resolution, or leave
  both out.
  - Don't pair a term with its own paraphrase ("the damping is local in time, set by the
    variables at the same instant"). If the plain version is clear, use only that.
  - Don't assert something and then derive it again two sentences later (the noise is
    "real", ... "the correlation is therefore real").
  - A paragraph that opens with a claim about Ref. [X] doesn't close by restating it ("The
    result is the rate equation of Ref. [X]"). The topic sentence makes the claim once.
  - Across a section, once a concept is explained, refer back to it and don't explain it
    again. Each explanation lives in one place: the words where the concept first appears,
    the formula where it is used.
- **Premises.** Cutting a repetition must not cut a premise.
  - A section opening may briefly recall what it builds on or contrasts with, even if the
    introduction said it. That recall is context, not redundancy.
  - Keep the copy the argument needs where it needs it, and cut the others.
  - A "therefore" needs its reason in the sentence before.
  - After cutting, reread the paragraph from its first sentence. In one paper, two
    redundancy cuts broke the method section: one made its opening meaningless and
    was reverted, the other left a "therefore" with no reason.

## 5. Be specific and correct
- **No vague qualifiers.** "A flat, memoryless bath" should say flat in what (the spectral
  density). "Methods that reach many sites [..]" should say which methods.
- **Tie each claim to the equation that realises it.** "We keep the bath at a microscopic
  level" must point to where that happens (the kernels computed from the spectral density
  in Eqs. (3) and (4)).
- **General case first, then the paper's instance.** A scaling, a condition or a
  parameter is stated for the general case ("of order 1/S for a spin of length S"), then
  for the case the paper uses ("1/N for a collective spin of N spins one-half"). Giving
  only the instance hides the physics and reads as a fact about the example.
- **A limitation comes with its consequence.** A sentence that states an approximation,
  a dropped term or a growing error must also say whether it invalidates the results,
  and in which regime or on which timescale the method holds, with a pointer to where
  the paper tests it. "The corrections accumulate at long times and grow with the
  strength of interactions" drew "draw a conclusion from this statement: does it
  invalidate the dynamics? What are the timescales in which we expect the method to
  work?". A limitation left without its conclusion is a must-fix finding.
- **Say why a test isolates what it tests.** "Sec. III A tests the memory kernel and
  Sec. III B the noise" needs the physics that separates them ("for a large spin the
  noise is suppressed, so this test probes the memory kernel alone"). Without the
  reason a co-author called it a "bizarre statement" and doubted it.
- **Every claim must survive a reader who knows the field.** A cold reader from a
  neighbouring field catches what is undefined; it does not catch what is wrong. Read
  each physics statement as a referee of the subfield would ("I doubt this statement"),
  and check the doubtful ones against the derivation, the code or the literature
  (the `referee` agent). A wrong or questionable claim is worse than a pedantic one.
- **Claim only what holds in general.** Don't state a scaling or a bound (e.g. "the error
  is suppressed as 1/N") unless it is true for the case at hand.
- **Don't claim less than holds either.** State the method in the most general form its
  derivation supports, even when every example is a special case, and say where it
  still holds approximately beyond the exact case. Flagged: a coupling written for one
  operator, A Σ_k g_k c_k, when the derivation holds for Σ_{n,k} g_{nk} A_n c_k; and "the
  bath can be integrated out exactly because it is harmonic" with no word that a
  non-harmonic bath gives the same equations at weak coupling.
- **Check every general statement of the method against every example in the paper.**
  List the examples, and test the sentence on each. "The fluctuation–dissipation
  relation of the thermal bath gives the noise kernel" was flagged because the paper's
  own integrated-out cavity does not obey that relation. A statement with an exception
  says so, or is limited to the cases it covers.
- **An unexplained restriction is verified, not accepted.** When a reader asks "why only
  at zero temperature?" and nobody can give the reason, check the claim against the
  derivation and the literature before keeping it. In one paper the restriction was
  kept "without the reason" as an author decision, and a co-author later wrote "that's
  false": the Markovian limit needs no assumption on the temperature. A correctness
  question is never closed by a decision on wording.
- **Unify before splitting into cases.** Before writing a step twice (a real noise and a
  complex noise, sampling the initial state and sampling the noise), look for a
  formulation that covers both, in the literature and in the co-authors' own papers.
  Two random inputs of one trajectory are sampled in one operation.
- **A choice of the model is stated as a choice, not as a fact about a regime.** "At
  large N the memory comes from a sub-Ohmic bath on the atoms" reads as if every large
  system had that bath, when the authors added it for one test. Write what was done:
  "For the second test we add a sub-Ohmic bath on the atoms". The same holds for
  parameters ("at strong coupling the bath is Ohmic" when the runs chose an Ohmic bath)
  and for any sentence whose subject is a regime (large N, low temperature, strong
  coupling) and whose content is the paper's setup.
- **A statement about the method covers every case the paper uses.** If the paper uses
  several variants of a step (several initial distributions, integrators, bath models),
  a sentence that names one either says it is an example ("for a spin, for example, ...")
  or points to where all of them are listed. Check the scope against the other sections
  and the code, not against the sentence being edited. Rewording is where this goes
  wrong: turning a fragment into a sentence, or a pointer into a claim, must not narrow
  what the text says.
  In a general method, a step stays general: it does not single out one kind of system
  ("for a spin, ..."), even as an example, when the paper treats several. It points to
  the appendix that gives each case, with the same wording in every step that does so.
- Speculative extensions either get made specific or go to the conclusions as outlook.
- **Justify every structural feature of an equation when it appears**: odd-looking
  factors (a −i/2 that comes from a convention), step functions (causality), and choices
  such as a Poisson bracket where a reader expects a constant.
  Say also what a factor carries physically when the argument depends on it, for example
  that coth(ω/2T) = 1 + 2n_B(ω) carries the zero-point fluctuations through its term 1,
  or that a factor 1/√N keeps a rate independent of the system size.
- **A property the formula does not show needs its reason.** When the text calls an
  expression real, positive, symmetric or conserved and the formula on the page
  displays an i, a minus sign or a missing symmetry, say in one clause why the property
  holds, or write the expression in a form that shows it. "Its correlation is real",
  next to −(i/2)Σ^K, was flagged because the reader sees the i. The fix names the
  reason (Σ^K is purely imaginary) and gives the spectrum in explicitly real form,
  πJ(|ω|)coth(|ω|/2T). The reason is one clause at most; if it needs a derivation, or
  splits into cases, it goes to the appendix with a pointer. A co-author struck out a
  four-sentence justification of this kind from a method step.
- **A quantity given by a formula says what it is and why it has that value**, in physical
  terms, not by reading the formula (section 2). "The
  decay rate Γ = 2πJ(ω₀)" leaves two questions: which rate (link it to where the reader
  met it, e.g. the jump operator of the master equation), and why 2πJ(ω₀) (the
  golden-rule rate of decay into the resonant bath modes, with a reference).
- **A correction says what it corrects.** "Eq. (A17) replaces the memory term for this
  case" leaves the reader asking why. Name the error in one clause at the place the
  correction is introduced ("the classical memory term makes the spin precess
  spuriously"), and let later sections refer back.
- **A why is one clause, not a derivation.** In the main text the reason names what goes
  wrong or what a factor means, at the level of the argument. The mechanism behind it
  (which operator identity fails, how a term is generated) goes to the appendix. Answering
  a "why?" with four sentences of mechanism was flagged as "too much technical detail".
- **Cut sentences the argument does not use.** "Ref. [12] absorbs the accompanying
  frequency shift into ω₀" answers a question nobody asked there; it belongs in the
  appendix or nowhere.
- **Standard conventions are stated, not left to the reader.** A stochastic equation
  with multiplicative noise says which calculus it uses (physical noise with a finite
  correlation time gives the Stratonovich interpretation in the white-noise limit, by the
  Wong–Zakai theorem). The statement goes next to the equation that has the noise, in
  the main text, not only in the appendix: a co-author flagged its absence from the
  method. Such conventions are editorial fixes, not author decisions.
- **Use technical terms correctly and consistently.** Check that a word like
  "stationary" is the right one. Use the same verb for the same operation, and a
  different verb for a different operation (e.g. "integrated out" for an exact removal,
  "eliminated" for an approximate reduction).
- Schematic figure panels: say whether the shapes are generic or specific to a model. A
  schematic caption carries no model formula (a struck-out "J ∝ ω^{1/2}e^{-ω/ω_c}" in a
  sketch), and panels that pair two quantities show them in the same representation
  (a kernel in time next to a spectrum in frequency was "weird"). Labels name the
  operation precisely ("initial sampling", not "sample").
- **Claims about other papers.** Read the paper before describing it, and keep the tone
  non-adversarial. If it can't be read, list the claim as an open question (procedure,
  step 4 in SKILL.md). Check author lists against arXiv or Crossref before questioning them.
- **Numbers.** Every value quoted must match the section, table or appendix it comes from.
- **Numbers come from what the figure shows.** A deviation quoted for a figure is
  computed over the plotted window and runs, not over a longer run or another table.
  A statement about an inset ("falls as 1/N until the sampling floor") must be visible
  in that inset. Check it in the data and the plotting code, not in the caption.
- **Every exception or failure the text states has a source and a cause.** A summary
  such as "except for a single spin at twice the critical coupling" points to the
  panel that shows it, and the paragraph that reports it gives the reason in one
  clause, with the evidence in the appendix. Authors asked "is this in the plots?"
  of an exception stated without either.
- **Improvement factors need a baseline.** "Reduces the deviation by a factor of 4.2"
  must say compared with what, and which measure (largest deviation, rms). Recompute it
  from the data when possible.

## 6. Main text vs. appendix
- Every section answers, in order: **why are we doing this**, **what is known**, **what
  are we doing**.
- Each section anticipates the next. Text and figures match 1:1: one figure, one piece of
  the argument.
- The appendix holds the detail, to show rigour. The body stays clean. When a passage is
  too detailed, move it to an appendix rather than deleting it.
- But results that matter go in the main text, even if their derivation stays in the
  appendix. Examples: recovering a known method as a limit, and how the work improves on
  the closest prior work.
- **The method contains everything the results use.** Every parameter of the physical
  setting that a results section uses (a temperature, a chemical potential, a coupling
  type) is introduced in the general method, with how it enters the equations and when
  it applies. The method figure shows it, and the appendix that derives the method
  carries it through the derivation. The results then only choose values and refer
  back. The converse also holds. **A parameter the results never vary does not belong
  in the paper.** For example, a bath parameter was carried through the method, the
  method figure, a table and the appendix because one results section mentioned it. A
  check of the code showed that every run used the trivial value, so it was removed
  everywhere. Before adding a parameter to the method, check in the code that some
  result uses a value other than the trivial one.
- **The results apply the method; they do not replace a step of it.** When a results
  section writes the equation of motion of a model, derive it from the general method
  and compare, and check the code that produced the figure. A form that agrees with the
  method only in a limit (for example a bosonised equation for a spin, which matches
  the spin bracket only at full polarisation) is an error in the text or in the code,
  not a detail to state. One paper divided a spin field by S^z so that a collective spin
  obeyed a bosonic equation; the authors wanted the spin equations, and the code and
  the figure had to be redone.
- **Derivations have the generality of the main text.** If the main text allows a
  parameter or a case, the appendix derivation includes it, and states where it does
  not apply (e.g. why a parameter is meaningful for one coupling and not the other).
- The method section says what each ingredient is and why it is there, not how well it
  performs. Accuracy figures ("reduces the deviation by a factor of four to six") belong
  in the results section that shows them.
- Overviews stay generic. "Section III B tests X" is enough at that level; the numbers and
  mechanisms belong in the subsection itself.
- **Explain top-down: the central equation first, then its terms.** A method section shows
  the equation the reader will use (the equation of motion, the estimator, the model)
  and then explains each of its terms, and only then gives the procedure that computes
  them. A co-author flagged a method that built the equation step by step: "the logical
  chain is to display Eq. (6) first, and then describe each term". The numbered
  procedure is the order of computing, not of understanding.
- **Length follows importance, not a budget.** The step that carries the main idea of the
  method, and the recovery of the known method as a limit, get the space they need to
  be understood, with the reasoning written out. Technical detail, conventions and
  special cases stay short or go to the appendix. A method trimmed to equal-length steps
  was flagged twice by the same reader: "this step has to be expanded and explained
  more clearly" (the central step) and "explain the reduction to Lindblad in more
  detail, because it helps the reader understand our approach". The space goes to the
  physical reasoning, not to definitions or to formulas read aloud. A later reader of
  the same expanded method found it "extremely pedantic and focusing on the wrong stuff
  at the wrong time": each paragraph should open with the physics it is for, and a
  revision that expands one part cuts another.
- **Introduce each object where it is used, not in passing.** A key quantity (a spectral
  density, the system operators) gets its own sentence at the point where the argument
  needs it. "Its effect is then fixed by T and the spectral density J(ω)=..." was
  flagged as "out of place and too fast", and three hatted symbols introduced in two
  sentences as "wasn't it Â above?".
- **Keep technical procedure steps short.** A reviewer wrote "too long, chop it!". Each step gives
  the action, its equation, and one or two sentences of why, in about 70 words or fewer.
  The first sentence of a step states what the step does or produces, as an instruction
  ("Compute the memory kernel", "Write the equations of motion of the closed system").
  The how follows. A step that opens with its technique ("Replace the operators by
  classical variables") and leaves its result for the end hides what it is for.
  If a definition makes a step long, replace the term by a plain description (section 3) or move
  the detail to the appendix.
- **Answers to review questions go where they belong.** A cold reader or referee asks
  "why?" about every factor, convention and special case. Answer in the main text only
  what the reader needs to follow the argument. Put derivation details, conventions,
  validity conditions and special cases in the appendix, with a pointer. A revision
  after a review should not leave the method longer than before. In one paper, answering
  every question in place turned a five-step method into a page of qualifications, and
  the authors had to move it all back to the appendix. Before answering a "why?" at all,
  ask whether a referee of the journal's field would ask it. If not, reject the finding:
  answering it makes the text pedantic.
- **Specialist terminology stays in the appendices.** When the main text can describe an
  object in plain words, it does. The appendix gives the technical name and links the
  two. Example: "a function O_W of these variables" in the method, and "the Weyl symbol,
  which is the function O_W of Sec. II" in the appendix. Typical candidates in physics are
  Weyl symbol, phase space, self-energy, star product and Hubbard–Stratonovich, and in
  statistics sufficient statistic, Fisher information and conjugate prior.
- Before relying on a known limitation of prior work, explain it so the reader understands
  why it matters.
- **Appendices follow the same rules as the main text.** Each opens with why it exists,
  what is known (with references) and what it does. Technical terms are allowed there,
  but each gets a one-clause definition at first use and a link to its main-text name
  ("In field theory the memory kernel is called the retarded self-energy"). No slogans
  ("the approximation enters here and nowhere else"), no dash
  asides, no italic sentences.

## 7. Captions and titles
- Captions are minimal but self-sufficient: a reader must be able to reproduce the figure
  from the caption alone. Parameters go in the caption; the explanation goes in the text.
- **Write captions in full sentences.** Don't chain verbless fragments ("Grey, individual
  trajectories. Shaded, their spread. Heavy line, their mean."). Put a list of line styles
  in one sentence with commas: "Grey lines show individual trajectories, the shaded band
  their spread, and the heavy line their mean." Replacing semicolons with full stops must
  not create fragments. Rewrite the sentence instead.
- **Figure labels and legends use the paper's terminology.** When a term changes in the
  text ("eliminated" to "integrated out"), change it in legends, axis labels and panel
  titles too, re-render the figure, and look at it. A caption that says one thing while
  the legend says another is a contradiction the reader sees at once.
- Section and subsection titles say what the section finds or does, not just label the
  setup ("General protocol" and "Memory against an exact solution" were flagged; "The
  memory kernel reproduces the exact dynamics" was accepted).

## 8. Mechanics (LaTeX)
- Cross-reference with a single mechanism (e.g. `\cref`/`\Cref`) and set the journal's
  spelling once in the preamble (for APS: Eq. (7), Fig. 2, Sec. III, Appendix A, Table I).
  Never type these by hand. Use `\Cref` at a sentence start.
- Setting `\crefname` also changes what `\Cref` prints. Set `\Crefname` explicitly as
  well (Equation, Figure, Section, Appendix, Table), and check the PDF text. Otherwise
  sentences start with "Sec." or "Eq.". Join the extracted text into one line before
  searching for ". Sec." or ". Eq.". Line wrapping produces false hits otherwise.
- New references go in the bibliography file. Tell the authors which entries were added,
  so they can verify the bibliographic details.
- Keep a backup of the file before large edits, and say where it is.

## 9. Style rules condensed from Celia Elliott's guides
Where Elliott allows em dashes, the ban in section 2 wins.

Paragraphs and flow
- Topic sentence first. Then explain or give evidence, then an example if one helps, then
  a sentence that leads into the next paragraph. Anything unrelated to the topic sentence
  gets cut or moved to its own paragraph.
- Test the structure: read only the first sentence of each paragraph in a section. It
  should tell the story with no gaps. If it doesn't, reorganise before polishing sentences.
- **Close each major section with a summary and a transition. Never drop the transition.**
  The summary states what the section established. The transition says why the next
  section follows: what question the reader should now have, and how the next section
  answers it. Keep it short, and in this order:
  1. Summary, one sentence (e.g. the inputs the method needs).
  2. What is new compared with the closest prior work, if not said already.
  3. The question the next section answers, and, for each new ingredient, why the test
     that follows isolates it, in one sentence together. Not what the tests find, not
     how they are done, and not a section-by-section list: repeating the content of
     later sections belongs in the introduction, and a co-author flagged it ("this thing
     of repeating the content of the sections doesn't sound right to me").
  4. The step after the tests (application), with a pointer.
  Physics remarks, validity conditions, generality and subtleties do not belong in the
  transition. They go in their own paragraph or a short "Remarks" subsection before it.
  A transition that also carried the zero-point part of the noise, the coupling
  generality and the roadmap was flagged: "this transition paragraph has to be
  rewritten. Many sentences should be put in a separate paragraph".
- Name the tests. "Tests the method against known results" was rejected as vague,
  because it hid the most interesting test. See examples.md, "Closing a section", for the
  accepted version.
- The transition is not the roadmap. If the next section opens with its own overview, the
  list of models, tests and subsections stays there. The transition gives only the logic
  that connects the two sections. Removing a transition to avoid overlapping with an
  overview disconnects the sections; the authors flagged it.

Sentences
- Aim for fewer than 25 words. More than three prepositions in a sentence means rewrite it.
- No stacks of nouns used as adjectives ("single-site memory-kernel boundary-term
  correction").
- Front-load the key word. Put the new point at the start of the sentence, not at the end
  of a dependent clause.
- Replace "is" verbs and nominalisations (-tion, -ment, -ance) with action verbs:
  "performs the integration of" becomes "integrates".
- State things positively. "The projection removes most of the error" beats "the error
  cannot be avoided without the projection".
- Restrictive clauses take "that" with no comma. Nonrestrictive clauses take ", which".
- Avoid "with" when you mean "having" or "using", "due to" (state the cause), and a bare
  "this" (write "this kernel", "this error").
- Use "compared with". "Three times smaller" and "twice the size" are ambiguous; give the
  ratio.

No fluff
- Cut "the fact that", "it is interesting to note", "in order to", "basically",
  "essentially", "very", and "It is…"/"There is…" openers.
- In results sections and appendices, quantify instead of qualifying: "agrees well" should
  give the number. The introduction is the exception (see below).
- No broad statements of wide applicability in the abstract or conclusions.
- A definition or example must tell the reader something new. If it doesn't, it's fluff.
- Tell what worked and what it means, not the history of the calculation.

Terminology and tense
- One name per object throughout the document. If K is "the memory kernel" in one
  section, it is not "the response function" in the next without saying so, and
  "damping" is not "friction" two paragraphs later. A new name signals a new object.
- Watch words that mean different things in different fields or contexts (e.g.
  "coherent", "flat", "stationary", "kernel" for both an integral kernel and a GPU kernel)
  and say which meaning you intend.
- Make it clear what is known (present tense, with citations) and what the paper does.
  Don't switch tenses at random.

Numbers, symbols, notation
- Don't start a sentence with a symbol, a numeral or an abbreviation, including the
  paper's own acronym.
- Counted numbers below ten are words ("two baths"); computed values are numerals.
  Leading zero on decimals (0.5), `\times` not x, a non-breaking space between number and
  unit.
- `\sim` means "of the order of" and `\approx` means "approximately equal to". Don't mix
  them.
- No "about" or "approximately" before exact numbers.
- Hyphenate compound modifiers ("rotating-wave coupling"), but not after -ly adverbs
  ("exactly solvable model").

Titles, abstract, introduction
- Title: fewer than 12 words, key words first, no "On", "Study of", "A novel", no
  qualitative adjectives (precise, efficient, powerful), no undefined acronyms or
  equations. Sentence case.
- Abstract (write it last): one or two sentences each on motivation, method, principal
  results with numbers, and what was learned. Plain text, no equations, little background.
- Introduction: what is known (with references), what question remains open, what was
  done, what was found, and what it means.
- In the introduction, state findings in words, one sentence per result, with a pointer to
  the section. No specific values or benchmark timings; numbers go in the sections and
  appendices.

References
- Cite the original work, not a later review, for the precise idea or result used.
- Cite fairly, including work that disagrees. When unsure whether something is common
  knowledge, cite it.

Revision order
1. Science and structure (first-sentence test, transitions, is the contribution clear,
   are assumptions justified, are reader objections anticipated).
2. Words (clarity, jargon, defined terms, simplest word).
3. Proofreading (headings, captions, table entries and figure labels too).

## 10. Maintaining the rules
- Every author correction becomes a rule here, or in the project files (CLAUDE.md,
  glossary.toml, paperlint.toml) if it only concerns one paper. State the general principle, then give one short example (flagged text and
  accepted text). Put it in the section where it belongs, not at the end.
- When a new rule conflicts with an old one, resolve the conflict in the text, and say
  which rule wins and when. Don't leave both.
- When the authors reject a fix, record why, so the rule doesn't push toward it again. For
  example, a redundancy cut that removed a premise, or dropping a transition to avoid
  overlapping with an overview.
- Keep examples current. If an example sentence is later rewritten, replace it with the
  accepted version.
