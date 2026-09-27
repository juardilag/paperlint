# Examples: flagged text and accepted rewrites

Every pair below comes from a real review of an LLM-assisted physics paper. The left
side was flagged by the supervisor or a co-author; the right side is the version they
accepted. The paper was about open quantum systems, but each pair illustrates a rule
that holds in any field. Read the pair for its rule, which is named in the heading.

When writing, match the accepted versions in tone and density: plain words, one idea
per sentence, every term defined, every claim tied to an equation or a reference.

---

## Slogans and aphorisms (rules.md, section 2)

**Flagged:** "The bath's fluctuation–dissipation relation is an identity of the
construction and not an assumption."

**Accepted:** "The fluctuation–dissipation relation of the thermal bath then gives the
noise kernel in terms of the Fourier transform Σ^R(ω)." *(State what the relation does,
where it is used, and cite it.)*

**Flagged:** "The coupling fixes Â, and the modes enter only through their spectral
density."

**Accepted:** "Here H_S is the system Hamiltonian and Â is the Hermitian system operator
that couples to the bath. … A continuum of such modes in thermal equilibrium is fully
characterised by its temperature T and its spectral density J(ω)."

## Placeholder words (section 2)

**Flagged:** "This section derives the corresponding equation from a microscopic model
of the bath." *(Reviewer: "What is a microscopic equation?")*

**Accepted:** "Here we derive a Langevin equation that keeps the memory of the bath.
Instead of a master equation, we start from the Hamiltonian of the system and the bath,
including their coupling (Eq. (2))."

## Implicit contrast with prior work (section 2)

**Flagged:** the method is "the non-Markovian generalisation anticipated in Ref. [16]",
with no statement of what Ref. [16] has.

**Accepted:** "Hosseinabadi et al. obtained from the Lindblad equation, Eq. (1), a
Langevin equation for the classical spin variables. … In their equation the damping
depends only on the spin variables at the same instant. The noise is white, which means
that its correlations are proportional to δ(t−t′) and its spectrum is flat. Both the
damping and the noise are determined by the jump operators." And later: "At zero
temperature, the Markovian TWA of Ref. [16] is the memoryless limit of Eq. (6)."

## Colloquial metaphor, anthropomorphism (section 2)

**Flagged:** "whose decay in τ sets how long the bath remembers"

**Accepted:** "The decay time of Σ^R(τ) is the bath correlation time."

**Flagged:** "what the atoms inherit once the mode between them and the bath is
eliminated"

**Accepted:** "The atoms are then driven by a field that depends on their own past over
the cavity decay time."

## Informal words for methods (section 2)

**Flagged:** "The recipe of Hosseinabadi et al. …", "this is what eliminating the cavity
buys", "the two engines", "prices the two shortcuts".

**Accepted:** "the procedure", "the correction is available only because the cavity has
been integrated out", "the cavity-kept and integrated-out formulations", "measures the
cost of each approximation".

## Standard vocabulary still needs defining (section 3)

**Flagged:** "white noise", "jump operators", "Langevin equation", "master equation",
"convolution", "coloured noise", all used without definition or reference.
*(Reviewer: "what is white noise? … what are those? reference??")*

**Accepted, one clause each at first use:**
- "a master equation. A master equation is an equation of motion for the density matrix
  ρ of the system alone, from which the bath has been eliminated [refs]."
- "The jump operators L_j describe the processes through which the bath changes the
  state of the system. An example is L = √Γ a for the loss of cavity photons at rate Γ."
- "A Langevin equation is an equation of motion that contains, besides the deterministic
  dynamics, a damping term and a random force, the noise [refs]."
- "The damping then becomes a convolution, (Σ^R ∗ A)(t) = ∫dt′ Σ^R(t−t′)A(t′). Here A is
  the system variable that couples to the bath. The convolution adds up the past values
  A(t′), each weighted by the memory kernel Σ^R at the time difference t − t′."
- "The noise becomes coloured, which means that its correlations extend over a finite time
  and its spectrum depends on frequency [ref]."

## Plain description instead of jargon (section 3)

**Flagged:** "by its Weyl symbol 𝒪_W(φ)" … "the phase-space function" *(Reviewer: "what is
the phase space?")*

**Accepted:** "Replace every operator 𝒪̂ by a function 𝒪_W(φ) of these variables. The
function is chosen so that the expectation value ⟨𝒪̂⟩ equals the average of 𝒪_W over the
Wigner function ρ_W of the density matrix. For a spin, the spin operators become the
components of a classical vector." The appendix then says "The function 𝒪_W of step 1 is
known as the Weyl symbol of 𝒪̂ [refs]."

## Unusual property of a familiar object (section 3)

**Flagged:** "The noise is then complex." *(Reviewer: "how can a noise be complex?")*

**Accepted:** "Because Â is not Hermitian, the bath force on it is a complex field. The
noise is then complex, ξ(t) = ξ₁(t) + iξ₂(t) with ξ₁ and ξ₂ real Gaussian noises, and its
correlation is \overline{ξ(t)ξ*(t′)} = −2iΣ^K(t−t′)."

## Notation introduced with a full clause (section 3)

**Flagged:** "classical variables φ_α, collectively φ" *("what is this? it's a bit odd")*

**Accepted:** "classical variables φ_α, and denote the set of all φ_α by φ."

**Flagged:** a figure caption saying "with ∗ the convolution" while the text never
introduced ∗.

**Accepted:** the text defines (Σ^R ∗ A)(t) where the convolution first appears, and the
caption no longer defines anything.

## Back-references (section 3)

**Flagged:** "The same step underlies TWA for bosons and for spins." *("I don't
understand this.")*

**Accepted:** "This step is the same as in TWA without a bath [refs]."

**Flagged:** "The convolution adds up its past values" *("its past values? of what?")*

**Accepted:** "The convolution adds up the past values A(t′)".

## Redundancy (section 4)

**Flagged:** "The bath starts in thermal equilibrium at temperature T. For a continuum of
modes it then enters the system dynamics only through T and the spectral density."

**Accepted:** "A continuum of such modes in thermal equilibrium is fully characterised by
its temperature T and its spectral density J(ω)."

**Flagged:** "In the equation of Ref. [31] the damping is local in time, set by the spin
variables at the same instant." *(term + its own paraphrase)*

**Accepted:** "In their equation the damping depends only on the spin variables at the
same instant."

**Flagged:** a paragraph opening "The Markovian TWA of Ref. [31] is the memoryless limit
of Eq. (6)" and closing "The result is the Langevin equation of Ref. [31]."

**Accepted:** the closing sentence is cut; the topic sentence makes the claim once.

## Cutting a premise (section 4) — a fix that was rejected

A redundancy pass removed "Hosseinabadi et al. obtained from the Lindblad equation a
Langevin equation …" from the opening of the method section, because the introduction
already said it. The authors reverted the cut: "now it does not make any sense". A section
opening may recall what it builds on. Keep that recall.

## Method vs. results (section 6)

**Flagged:** in the method section, "In the Rabi model of Sec. III B1 … the correction
reduces the deviation from the exact solution by a factor of four to six."
*("this is not necessary")*

**Accepted:** the sentence moves to the results; the method says only "Appendix A3
derives a correction for this precession."

**Flagged:** a chemical potential μ used first in the results, never mentioned in the
method or its figure.

**Accepted:** a method paragraph saying why μ is allowed and how it enters ("The
rotating-wave coupling also allows a chemical potential μ for the bath. … The factor
coth(ω/2T) in Eq. (4) then becomes coth[(ω−μ)/2T]"), plus μ in the figure label, the
kernel table and the appendix derivation.

## Procedure steps too long (section 6)

**Flagged:** steps of 110–125 words *("too long, chop it!")*.

**Accepted:** each step gives the action, its equation, and one or two sentences of why,
about 70 words. Definitions that made steps long were replaced by plain descriptions.

## Closing a section (section 9)

**Flagged:** "Section III therefore tests each kernel against a known result, and then
applies both to a driven system." *(vague; it hid the most interesting test)*

**Accepted:**
> The inputs of the method are the system Hamiltonian H_S, the coupling operator Â, the
> spectral density J(ω) and the bath temperature T. Compared with the Markovian TWA, it
> adds two ingredients, the memory kernel and the noise kernel, and each has to be tested.
> The memory kernel must reproduce dynamics in which the past of the system matters.
> Section III A tests it against an exact solution and an analytic theory. The noise
> kernel carries the zero-point fluctuations of the bath through the factor coth(ω/2T) in
> Eq. (4), while each trajectory is classical. Section III B tests whether the
> trajectories nevertheless relax to a state that obeys the quantum
> fluctuation–dissipation relation. Section III C then applies both kernels to a driven
> model, for which no consistent Lindblad description exists.

**Rejected alternative:** dropping the transition entirely because the next section had
an overview ("we have to connect all the sections to the reader").

## Captions (section 7)

**Flagged:** "Grey, individual trajectories. Shaded, their spread. Heavy line, their
mean."

**Accepted:** "Grey lines show individual trajectories, the shaded band their spread,
and the heavy line their mean."

## Introduction (section 9)

**Flagged:** a results paragraph in the introduction full of values ("agree to
5.9 × 10⁻³ for 30 atoms", "2.61 s at N = 8192") *("I don't like that we put a ton of
results in the intro")*.

**Accepted:** one sentence per result in words, each with a pointer: "In the Dicke model
it agrees with the exact solution across the superradiant transition (Sec. III A1)."

## Smoother word order (section 2)

**Flagged:** "We start from the Hamiltonian of the system, the bath and their coupling,
Eq. (2) below, instead of a master equation." *("This can be written more smoothly")*

**Accepted:** "Instead of a master equation, we start from the Hamiltonian of the system
and the bath, including their coupling (Eq. (2))."
