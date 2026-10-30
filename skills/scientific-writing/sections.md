# Rules by section type

`rules.md` holds the rules that apply to every sentence of a paper. This file holds
what is specific to one kind of section: what its parts are, in which order, and what
each part does. Each rule generalizes comments that co-authors and reviewers made on
real papers; like `rules.md`, it is checked, not stylistic, and the deletion test of
`rules.md`, section 8, decides when a rule here would add text.

Each section type carries its **review status**: which kind of reviewer has shaped its
rules so far. A type marked *provisional* has rules from the author only, or none, and
is filled in as review rounds reach it (`/paperlint:comments --train` adds the
comments of a round to the type they concern). A rule a paper's authors decide
against is recorded as a decision in that paper's `CLAUDE.md`, not deleted here.

Every section type also follows the general rule for openings: an opening (of a
section, subsection or appendix) is a bird's-eye view in words the reader already has.
Particular numbers, system sizes and new symbols wait for the part that uses them, and
a claim of the opening a reader would question carries its reason. Before writing an
opening or a closing, retrieve corpus paragraphs that do the same job (`rules.md`,
section 10).

## Abstract
*Provisional: author comments only.*
- Four moves, in order: what the method or result is, where its power comes from,
  what it was tested on and against which reference, and where it fits. No phrase of
  the closest prior paper is reused.
- A limit is stated as the scope of the claim, with the hedge the body uses, never as
  a failure of the method.
- No numerical settings, sample counts or system sizes.

## Introduction
*Reviewed by co-authors on the opening and the description of other methods.*
- Each term of art the argument relies on (a critical exponent, a soft mode, a
  sideband, a quasiprobability distribution) is explained in plain words at first use,
  for the broad reader of the journal, not only named.
- Technical parameters (an expansion parameter, a fit window) stay out; the
  introduction says what they measure in words, with a reference.
- Each claim about another method is checked against its source and states its scope
  ("the weak-coupling derivation", "in the cases where"), not a universal.
- The motivation comes from the physics, never from carrying out another paper's
  outlook.
- The closing roadmap says what each section tests, one sentence per section, and
  names the reference each comparison is made against; it gives no outcomes or
  numbers and does not copy the abstract.

## Method
*Reviewed by co-authors in three rounds.*
- The section opens with a conceptual summary that assumes nothing: what the parent
  method does and how the closest prior method extends it, in a few lines, then a
  bird's-eye view of what follows. No abrupt start ("The existing methods ...").
- The actors of the central equation (a force, a kernel, a noise) are introduced
  physically, in two words each, before the equation; the equation is then explained
  term by term, and each label and index is defined accurately for what it ranges
  over.
- The assumptions the method rests on are stated, and two statements of the method
  never contradict each other.
- A main-text summary says the method plainly ("white noise, uncorrelated at
  different times"); a convention, a derivation's lineage ("derived from the path
  integral of ...") and a sign or factor that only the derivation explains go to the
  appendix. A cryptic aside is either explained with its consequence or moved.
- An estimator formula shows what it averages over, and the words say the same.
- A recipe step says what it does at once and lists every input it needs.
- The limit that recovers the prior method is shown with its condition stated
  physically and the timescale on which it holds, briefly.
- No "Remarks" subsection and no closing paragraph that relists the inputs: a remark
  stands where its subject is introduced, and a fact appears once.
- Field vocabulary is cited to authoritative modern sources (textbooks, reviews), not
  to historical originals.

## Results
*Reviewed by co-authors and the principal reviewer in several rounds.*

**Section opening.** A plain roadmap: one sentence per subsection, each named by its
physical purpose, with no restated physics, numbers or method details. Subsections
are organized by physical setting; an introduction paragraph that the subsection
structure already says is cut.

**Subsection opening.** The subsection opens with the question its figure answers,
why the method's answer is not guaranteed there, and what measurement or comparison
decides it, naming every mechanism its Result discusses so that none appears for the
first time later. The question is posed in the field's register, as the physics at
stake and the test it gives ("A system coupled to a thermal bath relaxes to ... In
the method ... this is not guaranteed ... is therefore a test"), not announced ("Here we
ask whether"). An opening that only announces a comparison ("we compare X with Y on
Z") is an error. Where the regime is part of the point (Markovian or not, weak or
strong coupling), the opening says in which sense, at the subsection's parameters.
Where the parent section's introduction already poses the question, the subsection
opens with its Model and does not repeat it.

**Parts.** The subsections share the structure the authors approved first (its parts,
named in `CLAUDE.md`, typically Model, Equations of motion, Initial state, Result),
but a part that fails the deletion test is dropped rather than kept for symmetry, and
a part the first subsection lacks (a Measurement) is added only when the Result
cannot be followed without it.

**Model.**
- The Hamiltonian is a numbered equation introduced as such ("We consider ... with
  the Hamiltonian"), followed by each operator and parameter named physically.
- The dissipation channels and the spectral density are stated as assumptions, with
  what the exponent and cutoff characterize. A lossy mode used as a bath is described
  by its loss and its effective spectral density, never by the environment of that
  environment.
- Each parameter value comes with one reason, only where the argument uses it or a
  reader would doubt it.
- Physics the Result relies on (a resonance condition, an instability, a critical
  point) is stated as a known result with its reference, in one or two sentences; its
  derivation goes to the appendix. One job per sentence: a model paragraph that also
  derives its mechanism is split.
- The references the Result compares against are named where the comparison is set
  up, with a pointer to the appendix that describes how they are computed; a
  sentence describing the reference's method belongs there, not in the main text.

**Equations of motion.**
- Shown directly, as the method's general equation for these variables ("Eq. (3)
  with $A = S^x$"), with the method's names and notation (a special case keeps the
  general symbol with a label), no counting of steps and no intermediate equation a
  later one replaces. Scaling factors stay visible in the displayed equation.
- A force or field is defined after the equation that uses it, by pointing to the
  method's equation, not by writing the general expression again.
- An ingredient that does not follow from the method's general step (a noise not
  given by the fluctuation-dissipation relation, a correction, a counterterm) is
  quoted with its reference and its purpose in one clause; the mechanism goes to the
  appendix. An expression the paper neither derives nor cites is an error.
- Where the results depart from a step of the method, they say so at that step, with
  the physical reason and when the general step would apply.

**Initial state.** The main text gives only the sampling a reader needs to follow the
result (which variables are Gaussian, or which discrete values with which
probabilities); the prepared state's parameters (its direction, the cavity's vacuum,
a fixed component) go to the appendix with the run settings. A special-case scheme
gets one sentence. The part is cut when the text does not use it and an appendix
states it.

**Measurement.** The observable is defined before the Result: what it characterizes,
its scaling form where one is tested, the meaning of the sign of the control
parameter, and why this quantity decides the question of the opening. How it is
estimated goes to the appendix, unless the reader needs it to trust the verdict.

**Result.**
- States the verdict its figure shows. Numbers, precise deviations and settings go to
  an appendix, which the paragraph points to.
- When the figure compares cases, the paragraph walks through them one comparison per
  sentence, in the order the figure presents them, saying what each case changes and
  what the comparison shows. Several cases packed into one sentence are an error,
  however short the paragraph; verdict-only limits numbers, not the explanation.
- The story starts where agreement is best and moves toward the hardest case, named
  physically.
- An agreement claim is recomputed from the saved data, holds over the range the data
  covers, and names its reference where it is made. A case that does not test the
  claim sharply (where the compared forms barely differ) is said to be weak.
- A departure is reported with the mechanism it is consistent with, cited, and with
  what the data do not exclude; never as a failure the data do not show.
- Nothing the figure itself makes obvious is narrated, and the result is credited to
  the method as a whole. Results of other work are quoted with their reference, not
  re-derived.

## Figure captions
*Reviewed by the principal reviewer.*
- A caption says what is plotted against what, what each line, marker and visible
  band or error bar is, one sentence per panel naming its quantities physically, and
  the physical parameters, those shared by all panels once. It carries no equation
  references, no initial state, no numerical settings (time step, cutoffs, sample
  sizes, fit windows) and no pointer to them; before one leaves a caption, check that
  the text or an appendix states it. It does not repeat a value the text derives (a
  critical coupling) or a parameter the figure itself shows.
- Whether a caption states the takeaway follows the caption the authors approved
  first, in every caption, and must match the text and the data.
- Legends and axis labels use the text's terms; a key that only repeats the caption
  is dropped. Every drawn element (a line, an arrow, an inset, markers) is explained
  or removed. A schematic is redrawn after the text it illustrates is settled.
- Each panel varies one thing; data that adds nothing to a comparison is dropped.
- The figures share one language, checked across all of them: the same object in the
  same color and marker, one marker size in panels and insets, the same role drawn
  the same way, one grid style; no tick label touches a frame, and no inset or legend
  hides data. The colored series of every figure take one fixed palette in order (the
  first series the first color, and so on, in legend order), and every panel's axes
  box has the same height, measured on the rendered figure.

## Conclusions
*Provisional: no reviewer comments yet.*
- No new facts, no mechanism explained again and no list of the sections: the
  conclusions state what was shown, with the body's hedges, and point back.
- Limitations are stated as scope, each with its consequence.
- The outlook is the paper's own, not the fulfilment of another paper's outlook.

## Appendices
*Provisional: author comments and the principal reviewer's citation remark.*
- An appendix is cited as an appendix, with its full number, never as a section.
- Lean: equations with the sentences that connect them, the main text's notation,
  and no restated motivation or main-text repeats.
- A derivation is one ordered chain: the model and its terms first, each step from
  the ones before, the approximation last, remarks after.
- Every numerical step the results rely on (sampling, discretization, truncation,
  boundary terms, the integrator) is described well enough to reimplement and agrees
  with the code; numerical settings and checks are collected in one appendix, and
  hardware and timings stay out of the main text.
- What no main-text pointer, figure or claim needs goes to the code's README.
