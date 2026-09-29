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

The test: read the paragraph aloud. If it sounds like a list, a press release or a
lecture on terminology, rewrite it until it sounds like one scientist explaining a
result to another.

## 3. The reader has no context
Terms
- **Standard vocabulary is not exempt.** At its first use in the document, every
  technical term gets a one-clause definition and a reference, even terms every expert
  knows. Cite the original work where possible, otherwise a standard textbook.
  Examples reviewers flag: master equation, rate equation, Langevin equation, white
  noise, coloured noise, convolution, Markovian, Wigner function, Poisson bracket,
  fluctuation–dissipation relation, order parameter, critical exponent, "integrating
  out", multiplicative noise, mean-field approximation, and named models. The same holds
  outside physics: likelihood, random effect, cross-validation, knockdown.
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

References
- Introduce every reference by what it did (authors, system, result) before leaning on
  it. "The rate equation of Ref. [12]" means nothing to someone who hasn't read [12].
- For every step of a method, cite where it was done first.
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
- **Claim only what holds in general.** Don't state a scaling or a bound (e.g. "the error
  is suppressed as 1/N") unless it is true for the case at hand.
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
  πJ(|ω|)coth(|ω|/2T).
- **A quantity given by a formula says what it is and why it has that value.** "The
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
  Wong–Zakai theorem). Such conventions are editorial fixes, not author decisions.
- **Use technical terms correctly and consistently.** Check that a word like
  "stationary" is the right one. Use the same verb for the same operation, and a
  different verb for a different operation (e.g. "integrated out" for an exact removal,
  "eliminated" for an approximate reduction).
- Schematic figure panels: say whether the shapes are generic or specific to a model.
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
- **Keep procedure steps short.** A reviewer wrote "too long, chop it!". Each step gives
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
  the authors had to move it all back to the appendix.
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
  answers it. Build the closing paragraph in this order:
  1. Summary, one sentence (e.g. the inputs the method needs).
  2. What is new compared with the closest prior work.
  3. For each new ingredient, the question it raises and the specific test that answers
     it, with the reason the test is meaningful, tied to an equation.
  4. The step after the tests (application), with a pointer.
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
