# Examples: author corrections, before and after

Each pair is a sentence a supervisor, co-author or referee flagged, and the rewrite they
accepted. The pairs are invented, modelled on real reviews of LLM-assisted papers; most
follow one imaginary physics paper (atoms in an optical lattice coupled to a phonon
bath), a few come from other fields.

These pairs, and the paper's own `style_examples.md`, carry paperlint's sense of style.
Read them before drafting and match the accepted versions in tone and density. They are
examples, not rules: a pair shows what one reader objected to, and what a scientist
wrote instead. When a pair and the paper's `style_examples.md` disagree, the paper's
examples win.

New author corrections about style are added here (or to `style_examples.md`) as a
pair, never as a rule.

---

## Slogans and aphorisms

**Flagged:** "Detailed balance is a property of the construction, not an assumption."

**Accepted:** "Because the phonons start in thermal equilibrium, the noise and the
damping obey the fluctuation–dissipation relation [refs], and the atoms relax to the
thermal state of the lattice (App. B)." *(Say what holds, why, and where it is shown.)*

**Flagged:** "The coupling fixes everything; the phonons enter only through their
spectrum."

**Accepted:** "The phonons couple to the atomic density on each site. A continuum of
such modes in thermal equilibrium affects the atoms only through its temperature T and
its spectral density J(ω)."

## Placeholder words

**Flagged:** "This section derives the corresponding equation from a microscopic model."
*(Reviewer: "which equation? what is microscopic here?")*

**Accepted:** "Instead of a rate equation, we start from the Hamiltonian of the atoms,
the phonons and their coupling (Eq. (2)), and derive a stochastic equation for the site
occupations."

## Implicit contrast with prior work

**Flagged:** the method is "the natural generalisation of Ref. [12]", with no statement
of what Ref. [12] does.

**Accepted:** "Smith et al. [12] describe the phonons by a single relaxation rate, so the
damping of an atom depends only on its state at the same instant. Here the damping
depends on the past of the atom over the phonon correlation time. For a phonon bath with
a flat spectral density this memory vanishes, and the equation of Ref. [12] is
recovered."

## Colloquial metaphor, anthropomorphism

**Flagged:** "the time over which the lattice remembers its past"

**Accepted:** "the correlation time of the phonons"

**Flagged:** "the proteins sense the crowding and decide to fold"

**Accepted:** "at high crowding the folded state has the lower free energy, and the
folding rate increases"

## Informal words for methods

**Flagged:** "Our recipe", "the trick that buys the speed-up", "the two engines",
"this prices the approximation".

**Accepted:** "our procedure", "the step that makes the calculation faster", "the two
formulations", "this measures the cost of the approximation".

## Terms defined for the audience

**Flagged:** "master equation", "white noise", "Langevin equation", "convolution", all
used without definition or reference. *(Reviewer: "what is white noise? reference?")*

**Also flagged, later:** the fix for it, a method opening made of definition sentences.
"A Langevin equation is an equation of motion that contains, besides the deterministic
dynamics, a damping term and a random force, the noise." and "The convolution adds up
the past values of A, each weighted by the memory kernel at the time difference."
*(Co-author: "waaay too pedantic. The point is to explain the physical meaning of
mathematical formulas, not to put them in words.")*

**Flagged after that fix went too far:** "their noise is white" and "its noise is
coloured", with references but no meaning, in a paper whose point is the contrast between
the two. *(Author: "we must try not to assume anything of the reader ... this is
important, find a balance")*

**Accepted, a reference for every term, a clause for every term the argument turns on,
and nothing more, inside the sentence that uses the term:**
- "Their damping depends only on the state at the same instant, and their noise is
  white, uncorrelated between different times." ... "its noise is coloured, correlated
  over that time [ref]." 
- "The standard description is a master equation for the atoms alone [refs], from which
  the phonons have been eliminated."
- "Ref. [12] derived from it a Langevin equation [refs] whose damping and white noise
  are both set by the jump operators, so it cannot describe phonons with memory."
- "Integrating out the phonons makes the damping depend on the past occupations over the
  phonon correlation time, and the noise coloured [ref]." The convolution itself is left
  to the displayed equation.

## Plain description instead of jargon

**Flagged:** "We represent each operator by its Weyl symbol on phase space." *(Reviewer:
"what is the phase space here?")*

**Accepted:** "Each operator is replaced by a function of the classical variables, chosen
so that its average over the initial distribution equals the quantum expectation value."
The appendix then adds: "This function is known as the Weyl symbol of the operator
[refs]."

## Formulas and corrections need their why

**Flagged:** "The damping is instantaneous, with the rate Γ = 2πJ(ω₀). Smith et al.
absorb the accompanying frequency shift into ω₀." *(Authors: "what is Γ? why 2πJ? the
last sentence is not needed")*

**Accepted:** "The damping is instantaneous. Its rate is the rate Γ of the jump operator
in Eq. (1), and equals 2πJ(ω₀), the golden-rule rate of decay into the phonons resonant
with the atoms [refs]."

**Flagged:** "For a single atom, Eq. (B5) replaces the damping term." *("why?")*

**Accepted:** "For a single atom the classical damping term shifts the atom's level
spuriously, and Eq. (B5) replaces it (App. B)." Later sections point back to this
sentence instead of explaining again.

**Rejected alternative:** four sentences on why the shift appears (the damping term
contains the square of the occupation, the operator obeys n̂² = n̂, the classical number
does not, so ...). *(Authors: "too much technical detail")* That mechanism is App. B's.

## A property the formula does not show

**Flagged:** "The noise has the correlation ⟨ξξ⟩ = −(i/2)K(t − t′). Its correlation is
real and its spectrum is non-negative." *(Authors: "there is an i/2, so it is not clear
why it is real")*

**Accepted:** "Because K is purely imaginary (Eq. (3)), the factor −i/2 makes the
correlation real. Its spectrum, πJ(|ω|)coth(|ω|/2T), is non-negative." The reason is one
clause, and the spectrum is written in a form whose sign the reader can see.

**Later flagged by a co-author:** the same passage grown to four sentences, with a case
for the complex noise and a pointer for non-negativity, was struck out of the method
step. A reason longer than a clause, or split into cases, goes to the appendix; and a
unified definition of the noise (a co-author's paper) made the case split unnecessary.

## Unusual property of a familiar object

**Flagged:** "The noise is then complex." *(Reviewer: "how can a noise be complex?")*

**Accepted:** "Because the atoms couple to the phonons through a hopping operator, which
is not Hermitian, the force on them is a complex field. The noise is then complex,
ξ = ξ₁ + iξ₂, with ξ₁ and ξ₂ real Gaussian noises of equal variance."

## Notation introduced with a full clause

**Flagged:** "occupations n_j, collectively n"

**Accepted:** "occupations n_j, and we denote the set of all n_j by n."

**Flagged:** a caption saying "with K the memory kernel" while the text never introduced
K.

**Accepted:** the text defines K where the convolution first appears, and the caption
uses it without defining it.

## Back-references

**Flagged:** "The same step underlies the method for fermions." *("the same as what?")*

**Accepted:** "This sampling step is the same as in the method without phonons [refs]."

**Flagged:** "The convolution adds up its past values." *("its? the convolution's?")*

**Accepted:** "The convolution adds up the past occupations n(t′)."

## Redundancy

**Flagged:** "The phonons start at temperature T. They then enter the dynamics only
through T and J(ω)." *(T twice)*

**Accepted:** "A thermal phonon bath affects the atoms only through its temperature T
and its spectral density J(ω)."

**Flagged:** "In Ref. [12] the damping is instantaneous, set by the state at the same
time." *(a term and its own paraphrase)*

**Accepted:** "In Ref. [12] the damping depends only on the state at the same time."

**Flagged:** a paragraph that opens "The rate equation of Ref. [12] is the memoryless
limit of Eq. (6)" and closes "The result is the rate equation of Ref. [12]."

**Accepted:** the closing sentence is cut. The topic sentence makes the claim once.

## Cutting a premise, a fix that was rejected

A redundancy pass removed "Smith et al. describe the phonons by a single relaxation
rate" from the opening of the method, because the introduction said it already. The
authors reverted the cut: "now the method does not say what it improves on". A section
opening may recall what it builds on. Keep that recall.

## Method vs. results

**Flagged:** in the method, "the correction reduces the error by a factor of four to
six" *("this belongs to the results")*.

**Accepted:** the number moves to the results section that shows it. The method says
only "App. C derives a correction for this error."

**Flagged:** a parameter that the method, its figure and its table carry, while every
simulation in the paper sets it to zero.

**Accepted:** the parameter is removed everywhere, after checking the simulation input
files.

## Scope of a method statement

**Flagged:** "The atoms are sampled from the discrete distribution of Ref. [7]."
*(Authors: "not true, the dense lattices use a Gaussian and the phonon modes their Wigner
function")* The sentence came from a rewrite of the fragment "..., and the atoms as in
App. B", which had pointed to all the cases.

**Accepted:** "App. B gives the distributions used here for the phonon modes, single
atoms and dense lattices."

**Flagged**, in step 1 of the same general method: "For an atom, the occupation becomes
a classical number (App. B)." *(Authors: "this is a general method, not only for
atoms")*

**Accepted:** "App. B gives these functions for the phonon modes and the atoms." The
step keeps its general statement and points to the cases, as the sampling step does.

## Procedure steps too long

**Flagged:** steps of 110 to 125 words *("too long, chop it!")*.

**Accepted:** each step gives the action, its equation and one or two sentences of why,
in about 70 words. The definitions that made the steps long became plain descriptions,
and the details moved to the appendix.

## A step opens with what it does

**Flagged:** a step that begins "Replace the occupation operators by classical numbers
and every operator by its Weyl symbol" and states the equations of motion of the
isolated lattice only in its last sentence. *(Authors: "the step never says directly
that it computes the dynamics without phonons")*

**Accepted:** "Write the classical equations of motion of the lattice without the
phonons. Replace the occupation operators by classical numbers, ... The isolated lattice
then obeys ṅ_j = {n_j, H}." The action comes first, as in the other steps.

## Answering review questions in place

**Flagged:** after a review, every step of the method carried its own qualifications:
the Fourier convention, the validity of an approximation, a special case, and three
pointers in parentheses. *(Authors: "too many technical details for the main text")*

**Accepted:** the method keeps the argument and one pointer per step. The conventions,
validity conditions and special cases moved to the appendix, which the pointers name.

## Closing a section

**Flagged:** "Section IV therefore tests the method against known results and then
applies it." *(vague; it hid the most interesting test)*

**Accepted:**
> The method needs the lattice Hamiltonian, the coupling to the phonons, their spectral
> density and their temperature. Compared with a rate equation, it adds a memory kernel
> and a coloured noise, and each needs its own test. The memory kernel must reproduce
> dynamics in which the past of an atom matters, so Sec. IV A compares it with an exact
> solution for eight sites. The noise must drive the atoms to the thermal state of the
> lattice, although each trajectory is classical, and Sec. IV B tests that. Section V
> then applies both to a driven lattice, where no rate equation is consistent.

**Rejected alternative:** dropping the transition because the next section opens with
its own overview ("the reader needs the connection between the sections").

**Flagged later by a second co-author:** the section-by-section version ("Sec. IV A
compares it with an exact solution ... Sec. IV B tests that") *("this thing of
repeating the content of the sections, which is usually a thing for the intro, doesn't
sound right to me")*, and the claim that the two tests are separate without the reason
*("bizarre statement")*.

**Accepted after both:**
> The method needs the lattice Hamiltonian, the coupling to the phonons, their spectral
> density and their temperature. What it adds to a rate equation is a memory kernel
> and a coloured noise. Section IV tests the kernel on a large lattice, where the noise
> is suppressed, and the noise on a small one, where it dominates, before applying both
> to a driven lattice.

**Also flagged:** the same transition grown with the zero-point part of the noise, the
generality of the coupling and the roadmap of the tests *("out of place", "this
transition paragraph has to be rewritten; add a subsection, e.g. Remarks")*. The
remarks moved to their own paragraph; the transition kept the four short parts.

## Method explained top-down

**Flagged:** a five-step method that computes the kernels in step 2, the noise in step 3
and shows the equation of motion only in step 4 *("the logical chain is to display the
equation first, and then describe each term")*.

**Accepted:** the method opens with the Langevin equation of the atoms, then explains
its three terms (the dynamics without phonons, the noise, the memory integral), each
with its equation and reason, and ends with the procedure as a short list.

## Contribution framed as someone else's plan

**Flagged:** "Smith et al. outlined this extension in an appendix of Ref. [12], and we
carry it out." *(Smith, a co-author: "this can give the referee the impression that the
work is incremental")*

**Accepted:** the introduction says what Ref. [12] does (a memoryless bath) and what the
paper adds (the memory kernel and the coloured noise); the method sentence is cut.

## Captions

**Flagged:** "Grey, individual trajectories. Shaded, their spread. Black, the mean."

**Accepted:** "Grey lines show individual trajectories, the shaded band their spread,
and the black line their mean."

## Introduction

**Flagged:** an introduction paragraph full of values ("agrees to 6 × 10⁻³ for 30 sites",
"2.6 s for 8192 sites") *("too many numbers for an introduction")*.

**Accepted:** one sentence per result, in words, with a pointer: "For eight sites the
method agrees with the exact solution at all interaction strengths (Sec. IV A)."

## Smoother word order

**Flagged:** "We start from the Hamiltonian of the atoms, the phonons and their coupling,
Eq. (2) below, instead of a rate equation." *("put the known thing first")*

**Accepted:** "Instead of a rate equation, we start from the Hamiltonian of the atoms,
the phonons and their coupling (Eq. (2))."

## Rhythm and texture

**Flagged**, a paragraph that passes the linter and still reads as generated:
> The lattice is coupled to a phonon bath. The bath is harmonic (Sec. II). The coupling
> is linear (App. A). The bath can therefore be integrated out exactly, which means that
> no approximation is made. Notably, the result is a consequence of the model, not an
> additional assumption. The damping is a convolution. The noise is coloured, which means
> that its correlations extend over a finite time.

**Accepted:**
> Because the phonon bath is harmonic and couples linearly to the lattice, it can be
> integrated out exactly (App. A). What remains for the atoms is a damping term that is a
> convolution over their past, and a noise whose correlations extend over the correlation
> time of the phonons.

What changed: sentences joined by the relation between them ("Because"), one pointer
instead of two, no "which means that" definitions in a row, no "Notably", no "not an
additional assumption", and the claim that no approximation is made is left to the
appendix, which shows it.

**Flagged**, a paragraph patched by three rounds of review:
> At low density, the rate equation of Ref. [12] is the memoryless limit of Eq. (6).
> Take a flat spectral density around the lattice frequency ω₀. Here ω₀ is the
> frequency of the mode that the phonons damp. Both kernels are then proportional to
> δ(τ) (Table I). The damping then depends only on the same instant. The rate is Γ.
> It equals 2πJ(ω₀).

**Accepted:**
> The rate equation of Ref. [12] is the memoryless limit of Eq. (6) at low density. The
> limit requires a spectral density flat around ω₀, the frequency of the damped mode.
> Both kernels are then proportional to δ(τ), so the damping depends only on the
> occupations at the same instant (Table I). The damping rate 2πJ(ω₀) is the
> golden-rule rate of decay into the resonant phonons [refs].

What changed: the condition moved behind the claim, the instruction "Take" became "the
limit requires", the definition of ω₀ went into the sentence that uses it, the two
"then" sentences were joined by "so", and the rate got its meaning in the same sentence.

**Flagged**, from an ecology paper:
> Notably, predation plays a key role in the dynamics. The predator density is high. The
> prey density is low. This underscores the importance of top-down control.

**Accepted:**
> Where predators are dense the prey density falls by half within one season (Fig. 3),
> which is the top-down control that the model predicts for this food web.

**Flagged**, the opening of a results section that passed the cold reader three times
*(authors: "not human-like writing")*:
> The lattice model tests the memory kernel in two independent ways. In the first, the
> phonons are integrated out exactly, because they are harmonic. The atoms then feel a
> force that depends on their past. With phonon loss as the only dissipation, the model
> can be solved exactly for eight sites, which gives an exact reference (Sec. IV A). The
> second test uses the critical exponent at the melting transition. With a second bath on
> the atoms, the critical exponent depends on the low-frequency shape of its spectral
> density (Sec. IV B).

**Accepted:**
> We test the memory kernel on the lattice model, where two known results constrain it
> from different sides. The phonons are harmonic and couple linearly to the atoms, so they
> can be integrated out like the bath of Sec. II, and for eight sites the full model can
> still be solved numerically (Sec. IV A). The second result concerns the melting
> transition. When a second bath acts on the atoms, the density diverges there with an
> exponent set by the low-frequency shape of its spectral density. Reproducing this
> exponent, known analytically for an infinite lattice, tests the kernel at arbitrarily
> low frequencies and at sizes that no exact method reaches (Sec. IV B).

What changed: the authors are the agent instead of the model ("We test", not "The model
tests"); the enumeration "In the first ... The second test" became one claim about why
the two results are useful; "exact" appears once instead of three times; the paragraph
says why the exponent is a test (low frequencies, large sizes), which the flagged version
never did. The rewrite was drafted fresh from a note of what the paragraph must say, not
patched sentence by sentence.

## Formulas read aloud

**Flagged:** "Its first term is the classical dynamics of the system. The second is the
force exerted by the bath." and "The step function θ(τ) enforces causality." next to the
displayed equations. *(Co-author: "You shouldn't put formulas into words.")*

**Accepted:** cut both; keep the sentence the equation cannot say, "The force at time t
depends on the whole past of the atoms, over the correlation time of the phonons."

## Counterfactual instead of the consequence

**Flagged:** "The noise kernel carries the zero-point fluctuations of the bath through
the term 1 of coth(ω/2T), which remains at T = 0. With the classical noise, 2T/ω in
place of coth(ω/2T), the trajectories would relax to classical statistics. Section IV B
tests whether they reach the quantum ones."

**Accepted (the co-author's version):** "The noise carries the zero-point fluctuations
of the bath through the coth factor of Eq. (4). So, although the equations of motion
are classical, the method relaxes the system to the quantum thermal state, which
Sec. IV B shows through the fluctuation–dissipation relation."

## A limitation without its consequence

**Flagged:** "Their size is set by the semiclassical parameter, of order 1/N for a
collective spin of N spins one-half. The corrections accumulate at long times and grow
with the strength of interactions." *(Co-author: "Of order 1/S for a spin of length S."
and "Draw a conclusion: does it invalidate the dynamics? What are the timescales in
which we expect the method to work?")*

**Accepted:** the general parameter first (1/S for a spin of length S, 1/N for the
collective spins used here), then the conclusion: until which time, in units the reader
can check, the dropped corrections stay small, and where the paper tests it.

## A name that does not pay

**Flagged:** "We call this the quadrature coupling, because the Hermitian operator
couples to a quadrature of the bath modes." *(Co-author: "Do we care about this
nomenclature? Does it help?")*

**Accepted:** "The coupling operators may be Hermitian, such as a spin component, or not,
such as a lowering operator." The two cases are named only in the table that lists them.

## Circular "because" and a word without its problem

**Flagged:** "Because the noise multiplies the bracket {φ,A}, a function of the system
variables, it is multiplicative. With coloured noise every trajectory solves an ordinary
differential equation, so Eq. (6) is unambiguous." *(Author: "this makes no sense.
'is unambiguous' also makes no sense. What is that?")* The first sentence gives the
definition as the reason; the second copied a referee's "the Itô/Stratonovich ambiguity
is absent" without the ambiguity.

**Accepted:** "The noise enters multiplied by the bracket {φ,A}, which depends on the
state of the system. In the white-noise limit the equation must then specify at which
point of a time step the bracket is evaluated. The finite correlation time of a physical
bath selects the midpoint, the Stratonovich rule [refs]."

## Too long although every fix was right

**Flagged:** an introduction revised from 1519 to 1764 words. Every change fixed a real
problem: an overstated claim got its conditions, a term its gloss, a list of methods its
missing entries, a result its caveat. *(Author: "the text is too dense, is too large ...
a human seeks to communicate all the ideas in a concise readable way, not wasting space
or time")*

**Accepted approach:** each fix rewrites the sentence it corrects instead of adding one;
the caveats ("at large N, within the statistical error, while the order parameter still
relaxes") move to the results section and the introduction keeps the finding in one
clause; the survey names representative methods; the section is cut to the budget
derived from its idea inventory, with every idea kept.

**Flagged:** "The quantum fluctuation--dissipation relation ties the fluctuations of an
observable in equilibrium to its response, and it distinguishes quantum from classical
statistics. ... the Dicke model relaxes ... At large N the fluctuations obey it within
the statistical error, even while the order parameter of the ordered phase is still
relaxing." (61 words in an introduction)

**Accepted:** "... relaxes to a state whose fluctuations obey the quantum
fluctuation--dissipation relation [refs] (Sec. III B)." (the conditions are in III B)
