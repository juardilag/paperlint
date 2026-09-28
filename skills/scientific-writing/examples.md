# Examples: flagged text and accepted rewrites

Each pair shows a sentence a reviewer or co-author flagged, and a rewrite of the kind
they accept. The pairs are invented, modelled on real reviews of LLM-assisted papers.
Most follow one imaginary physics paper, a stochastic method for atoms in an optical
lattice coupled to a phonon bath. A few come from other fields, to show that the rules
do not depend on the subject. Read each pair for its rule, which is named in the
heading.

When writing, match the accepted versions in tone and density: plain words, sentences
joined by the logic between them, every term defined, every claim tied to an equation,
a figure or a reference.

---

## Slogans and aphorisms (rules.md, section 2)

**Flagged:** "Detailed balance is a property of the construction, not an assumption."

**Accepted:** "Because the phonons start in thermal equilibrium, the noise and the
damping obey the fluctuation–dissipation relation [refs], and the atoms relax to the
thermal state of the lattice (App. B)." *(Say what holds, why, and where it is shown.)*

**Flagged:** "The coupling fixes everything; the phonons enter only through their
spectrum."

**Accepted:** "The phonons couple to the atomic density on each site. A continuum of
such modes in thermal equilibrium affects the atoms only through its temperature T and
its spectral density J(ω)."

## Placeholder words (section 2)

**Flagged:** "This section derives the corresponding equation from a microscopic model."
*(Reviewer: "which equation? what is microscopic here?")*

**Accepted:** "Instead of a rate equation, we start from the Hamiltonian of the atoms,
the phonons and their coupling (Eq. (2)), and derive a stochastic equation for the site
occupations."

## Implicit contrast with prior work (section 2)

**Flagged:** the method is "the natural generalisation of Ref. [12]", with no statement
of what Ref. [12] does.

**Accepted:** "Smith et al. [12] describe the phonons by a single relaxation rate, so the
damping of an atom depends only on its state at the same instant. Here the damping
depends on the past of the atom over the phonon correlation time. For a phonon bath with
a flat spectral density this memory vanishes, and the equation of Ref. [12] is
recovered."

## Colloquial metaphor, anthropomorphism (section 2)

**Flagged:** "the time over which the lattice remembers its past"

**Accepted:** "the correlation time of the phonons"

**Flagged:** "the proteins sense the crowding and decide to fold"

**Accepted:** "at high crowding the folded state has the lower free energy, and the
folding rate increases"

## Informal words for methods (section 2)

**Flagged:** "Our recipe", "the trick that buys the speed-up", "the two engines",
"this prices the approximation".

**Accepted:** "our procedure", "the step that makes the calculation faster", "the two
formulations", "this measures the cost of the approximation".

## Standard vocabulary still needs defining (section 3)

**Flagged:** "master equation", "white noise", "Langevin equation", "convolution", all
used without definition or reference. *(Reviewer: "what is white noise? reference?")*

**Accepted, each inside the sentence that first uses it:**
- "The standard description is a master equation, an equation of motion for the density
  matrix of the atoms alone, from which the phonons have been eliminated [refs]."
- "Each atom obeys a Langevin equation [refs], in which the deterministic motion is
  supplemented by a damping term and a random force, the noise."
- "The damping becomes a convolution, (K ∗ n)(t) = ∫dt′ K(t−t′) n(t′), which adds up the
  past occupations n(t′), each weighted by the memory kernel K at the time difference."

## Plain description instead of jargon (section 3)

**Flagged:** "We represent each operator by its Weyl symbol on phase space." *(Reviewer:
"what is the phase space here?")*

**Accepted:** "Each operator is replaced by a function of the classical variables, chosen
so that its average over the initial distribution equals the quantum expectation value."
The appendix then adds: "This function is known as the Weyl symbol of the operator
[refs]."

## Formulas and corrections need their why (section 5)

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

## A property the formula does not show (section 5)

**Flagged:** "The noise has the correlation ⟨ξξ⟩ = −(i/2)K(t − t′). Its correlation is
real and its spectrum is non-negative." *(Authors: "there is an i/2, so it is not clear
why it is real")*

**Accepted:** "Because K is purely imaginary (Eq. (3)), the factor −i/2 makes the
correlation real. Its spectrum, πJ(|ω|)coth(|ω|/2T), is non-negative." The reason is one
clause, and the spectrum is written in a form whose sign the reader can see.

## Unusual property of a familiar object (section 3)

**Flagged:** "The noise is then complex." *(Reviewer: "how can a noise be complex?")*

**Accepted:** "Because the atoms couple to the phonons through a hopping operator, which
is not Hermitian, the force on them is a complex field. The noise is then complex,
ξ = ξ₁ + iξ₂, with ξ₁ and ξ₂ real Gaussian noises of equal variance."

## Notation introduced with a full clause (section 3)

**Flagged:** "occupations n_j, collectively n"

**Accepted:** "occupations n_j, and we denote the set of all n_j by n."

**Flagged:** a caption saying "with K the memory kernel" while the text never introduced
K.

**Accepted:** the text defines K where the convolution first appears, and the caption
uses it without defining it.

## Back-references (section 3)

**Flagged:** "The same step underlies the method for fermions." *("the same as what?")*

**Accepted:** "This sampling step is the same as in the method without phonons [refs]."

**Flagged:** "The convolution adds up its past values." *("its? the convolution's?")*

**Accepted:** "The convolution adds up the past occupations n(t′)."

## Redundancy (section 4)

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

## Cutting a premise (section 4), a fix that was rejected

A redundancy pass removed "Smith et al. describe the phonons by a single relaxation
rate" from the opening of the method, because the introduction said it already. The
authors reverted the cut: "now the method does not say what it improves on". A section
opening may recall what it builds on. Keep that recall.

## Method vs. results (section 6)

**Flagged:** in the method, "the correction reduces the error by a factor of four to
six" *("this belongs to the results")*.

**Accepted:** the number moves to the results section that shows it. The method says
only "App. C derives a correction for this error."

**Flagged:** a parameter that the method, its figure and its table carry, while every
simulation in the paper sets it to zero.

**Accepted:** the parameter is removed everywhere, after checking the simulation input
files.

## Scope of a method statement (section 5)

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

## Procedure steps too long (section 6)

**Flagged:** steps of 110 to 125 words *("too long, chop it!")*.

**Accepted:** each step gives the action, its equation and one or two sentences of why,
in about 70 words. The definitions that made the steps long became plain descriptions,
and the details moved to the appendix.

## A step opens with what it does (section 6)

**Flagged:** a step that begins "Replace the occupation operators by classical numbers
and every operator by its Weyl symbol" and states the equations of motion of the
isolated lattice only in its last sentence. *(Authors: "the step never says directly
that it computes the dynamics without phonons")*

**Accepted:** "Write the classical equations of motion of the lattice without the
phonons. Replace the occupation operators by classical numbers, ... The isolated lattice
then obeys ṅ_j = {n_j, H}." The action comes first, as in the other steps.

## Answering review questions in place (section 6)

**Flagged:** after a review, every step of the method carried its own qualifications:
the Fourier convention, the validity of an approximation, a special case, and three
pointers in parentheses. *(Authors: "too many technical details for the main text")*

**Accepted:** the method keeps the argument and one pointer per step. The conventions,
validity conditions and special cases moved to the appendix, which the pointers name.

## Closing a section (section 9)

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

## Captions (section 7)

**Flagged:** "Grey, individual trajectories. Shaded, their spread. Black, the mean."

**Accepted:** "Grey lines show individual trajectories, the shaded band their spread,
and the black line their mean."

## Introduction (section 9)

**Flagged:** an introduction paragraph full of values ("agrees to 6 × 10⁻³ for 30 sites",
"2.6 s for 8192 sites") *("too many numbers for an introduction")*.

**Accepted:** one sentence per result, in words, with a pointer: "For eight sites the
method agrees with the exact solution at all interaction strengths (Sec. IV A)."

## Smoother word order (section 2)

**Flagged:** "We start from the Hamiltonian of the atoms, the phonons and their coupling,
Eq. (2) below, instead of a rate equation." *("put the known thing first")*

**Accepted:** "Instead of a rate equation, we start from the Hamiltonian of the atoms,
the phonons and their coupling (Eq. (2))."

## Rhythm and texture (section 2b)

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
