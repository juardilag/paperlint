# Rules for scientific writing

These rules come from a supervisor's line-by-line review of an LLM-assisted physics
paper and from the co-authors' later corrections. They apply to any field. The examples
are taken from that paper; apply the principle, not the example.

**House defaults.** A few rules are strong preferences of the original authors rather
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
- **Aphorisms and slogans.** Examples: "the relation is an identity of the construction
  and not an assumption", "the coupling fixes A", "prices the two shortcuts", "the only
  approximation, and it acts on the system alone". Say the physics plainly.
- **Dash asides** ("– the bath is already carried by ξ –"). Use no em dashes at all.
  Rewrite with a comma or a full stop, not a colon or semicolon. En dashes only in ranges
  (2.1–2.6) and joined names (Caldeira–Leggett).
- **Meta phrases that do nothing**: "in the order it is carried out", "Applying the
  protocol.", "Table I gives both for…". Cut them.
- **Italic emphasis on whole sentences.** Don't use it.
- **Colloquial metaphors for technical quantities.** "How long the bath remembers" should
  be "the bath correlation time". Use scientific language.
- **Informal nouns and verbs for methods and results**: "the recipe", "the trick", "the
  engine", "buys", "prices", "the price of". Write "the method", "the procedure", "the
  formulation", "costs", "requires".
- **Compressed participle phrases** that pack a claim into a clause: "truncating the
  system sector alone", "with the system made semiclassical rather than exact". Write the
  claim as a full sentence with a subject and a verb.
- **Narrating a concept as a sequence of actions**: "the bath is traced out before the
  first trajectory is propagated". State what the method assumes or approximates instead.
- **Stiff, list-like, "student" prose**: short declarative sentences strung together
  without connecting logic. Paragraphs should flow and argue. Polish slowly; don't rush.
- **Placeholder words that name nothing**: "a microscopic model", "the corresponding
  equation", "a structured bath" with no structure given. Name the concrete object, for
  example "the Hamiltonian of the system and the bath, including their coupling (Eq. (2))".
- **Contrasts left implicit.** When the work differs from the closest prior work, say
  exactly what each side has, and show how the prior result is recovered as a limit.
  Example: "In Ref. [16] the damping depends only on the variables at the same instant and
  the noise is white. Here the damping is a convolution with a memory kernel and the noise
  is coloured. With a flat spectral density the kernels become δ(τ) and Ref. [16] is
  recovered."
- **Put the known or contrasted element first and the new element last.** "Instead of a
  master equation, we start from the Hamiltonian…" reads better than "We start from the
  Hamiltonian…, Eq. (2) below, instead of a master equation".
- **Losing context**: stating something as if it were obvious, or jumping to a quantity
  the reader wasn't prepared for ("the photon number decays at 2κ" in the middle of a
  kernel discussion: "do you mean the cavity photon?"). Set up each quantity before it
  appears.
- **Anthropomorphism.** Atoms don't "inherit" or "see", baths don't "remember", drives
  don't "move" things, and a coupling doesn't "fix" anything. Describe the physics that
  actually happens.

## 3. The reader has no context
Terms
- **Standard vocabulary is not exempt.** At its first use in the document, every
  technical term gets a one-clause definition and a reference, even terms every expert
  knows. Cite the original work where possible, otherwise a standard textbook.
  Examples a reviewer flagged in one paper: master equation, Lindblad equation, jump
  operator, Langevin equation, white noise, coloured noise, convolution. Other examples:
  Markovian, Wigner function, Poisson bracket, fluctuation–dissipation relation, soft
  mode, order parameter, critical exponent, rotating-wave coupling, "integrating out",
  multiplicative noise, sub-Ohmic, and named models.
- The definition goes where the term first appears (usually the introduction), not later.
- Spell out every acronym at first use, including common ones (QED, GPU).
- **Prefer a plain description to a term that needs defining.** If a term needs more
  than one clause to define in the main text, describe the object in plain words instead
  and keep the term for the appendix (see 6). Examples: "the kernel describes how the bath
  responds at time τ to a perturbation at time 0" instead of "the retarded response
  function"; "a function of these variables" instead of "a Weyl symbol on phase space".
- Unusual properties of familiar objects need one sentence saying what they mean and why
  they arise. For example, "the noise is then complex" provoked "how can a noise be
  complex?". Write "Because Â is not Hermitian, the bath force on it is a complex field,
  ξ = ξ₁ + iξ₂ with ξ₁ and ξ₂ real Gaussian noises", and give its correlation.
- Jargon ("exact c-number representations", "symmetrised correlators", "star-product
  correction") needs a one-line explanation. If it doesn't matter to the argument, drop it.
- If the document never uses something, don't mention it in the main text.

References
- Introduce every reference by what it did (authors, system, result) before leaning on
  it. "The Langevin equation of Ref. [16]" means nothing to someone who hasn't read [16].
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
  - "The same step underlies TWA" did not say which step, or the same as what. It became
    "This step is the same as in TWA without a bath".
  - In "The convolution adds up its past values", "its" read as the convolution. It became
    "the past values A(t′)".
  - In "θ(τ) makes it vanish, and its decay time…", the nearest noun was θ, not the kernel.
- Name the object when two candidates are in play ("its spectral density" with two baths).
- Don't use names that collide with better-known ones ("the standard model" for a
  physics model reads as the Standard Model). Name the model.

## 4. Say it once
- Don't restate the same idea in the introduction, the method and the results ("we have
  said that many times"). The introduction and the method must not share paragraphs.
- **No redundancy at any scale.** Each fact appears once.
  - Within a paragraph, don't repeat a quantity or claim in nearby sentences. "The bath
    starts at temperature T. It then enters only through T and J(ω)" states T twice.
    Write "a thermal bath is fully characterised by its temperature T and its spectral
    density J(ω)".
  - Don't define a term circularly ("the response function, the response of the bath").
  - Don't pair a term with its own paraphrase ("the damping is local in time, set by the
    variables at the same instant"). If the plain version is clear, use only that.
  - Don't assert something and then derive it again two sentences later (the noise is
    "real", ... "the correlation is therefore real").
  - A paragraph that opens with a claim about Ref. [X] doesn't close by restating it ("The
    result is the Langevin equation of Ref. [X]"). The topic sentence makes the claim once.
  - Across a section, once a concept is explained, refer back to it and don't explain it
    again. Each explanation lives in one place: the words where the concept first appears,
    the formula where it is used.
- **Premises.** Cutting a repetition must not cut a premise.
  - A section opening may briefly recall what it builds on or contrasts with, even if the
    introduction said it. That recall is context, not redundancy.
  - Keep the copy the argument needs where it needs it, and cut the others.
  - A "therefore" needs its reason in the sentence before.
  - After cutting, reread the paragraph from its first sentence. In the original paper,
    two redundancy cuts broke the method section: one made its opening meaningless and
    was reverted, the other left a "therefore" with no reason.

## 5. Be specific and correct
- **No vague qualifiers.** "A flat, memoryless bath" should say flat in what (the spectral
  density). "Methods that reach many spins [..]" should say which methods.
- **Tie each claim to the equation that realises it.** "We keep the bath at a microscopic
  level" must point to where that happens (the kernels computed from the spectral density
  in Eqs. (3) and (4)).
- **Claim only what holds in general.** Don't state a scaling or a bound (e.g. "suppressed
  in 1/S") unless it is true for the case at hand.
- Speculative extensions either get made specific or go to the conclusions as outlook.
- **Justify every structural feature of an equation when it appears**: odd-looking
  factors (a −2i that comes from a convention), step functions (causality), and choices
  such as a Poisson bracket where a reader expects a constant.
  Say also what a factor carries physically when the argument depends on it, for example
  that coth(ω/2T) = 1 + 2n_B(ω) carries the zero-point fluctuations through its term 1.
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
  in the paper.** For example, a chemical potential μ was introduced in the method, the
  figure, the kernel table and the appendix because one results section mentioned it.
  A check of the code showed that every run had μ = 0, so it was removed everywhere.
  Before adding a parameter to the method, check that some result uses a value other than
  the trivial one.
- **Derivations have the generality of the main text.** If the main text allows a
  parameter or a case, the appendix derivation includes it, and states where it does
  not apply (e.g. why μ is meaningful for one coupling and not the other).
- The method section says what each ingredient is and why it is there, not how well it
  performs. Accuracy figures ("reduces the deviation by a factor of four to six") belong
  in the results section that shows them.
- Overviews stay generic. "Section III B tests X" is enough at that level; the numbers and
  mechanisms belong in the subsection itself.
- **Keep procedure steps short.** A reviewer wrote "too long, chop it!". Each step gives
  the action, its equation, and one or two sentences of why, in about 70 words or fewer.
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
  which is the function O_W of Sec. II" in the appendix. Typical candidates are Weyl
  symbol, phase space, quasi-probability, self-energy, star product, Keldysh rotation and
  Hubbard–Stratonovich.
- Before relying on a known limitation of prior work, explain it so the reader understands
  why it matters.
- **Appendices follow the same rules as the main text.** Each opens with why it exists,
  what is known (with references) and what it does. Technical terms are allowed there,
  but each gets a one-clause definition at first use and a link to its main-text name
  ("In Keldysh field theory Σ^R and Σ^K are called the retarded and Keldysh
  self-energies"). No slogans ("the truncation enters here and nowhere else"), no dash
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
  setup ("General protocol" and "Cavity memory against an exact solution" were flagged).

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
- Name the tests. "Tests each kernel against a known result" was rejected as vague,
  because it hid the most interesting test. See examples.md, "Closing a section", for the
  accepted version.
- The transition is not the roadmap. If the next section opens with its own overview, the
  list of models, tests and subsections stays there. The transition gives only the logic
  that connects the two sections. Removing a transition to avoid overlapping with an
  overview disconnects the sections; the authors flagged it.

Sentences
- Aim for fewer than 25 words. More than three prepositions in a sentence means rewrite it.
- No stacks of nouns used as adjectives ("single-spin memory-kernel star-product
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
  section, it is not "the retarded self-energy" in the next without saying so, and
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
