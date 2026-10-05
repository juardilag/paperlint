# House style: J. Marino, H. Hosseinabadi, M. Stefanini

paperlint writes like these three physicists. The style is learned from their real
paragraphs, retrieved from the corpus by the job a paragraph does
(`scripts/corpus.py retrieve`, papers in `corpus_ids.txt`); this file only describes it
in a few lines and keeps a handful of paragraphs for when the corpus is not built. It
is the same for every paper and is not a setting. A description of a style is not a
recipe: do not write toward the lines below, read the retrieved paragraphs.

## In a few lines

Sentence length varies a lot, from a few words to a long sentence with several
clauses, and it follows the content rather than a pattern. A paragraph opens from its setting, its figure or the previous point ("In Fig. 2a
we show ...", "We consider ...", "Despite ...") and arrives at its claim, rather than
stating a thesis and listing support. "We" narrates throughout ("we benchmark", "we
note that", "we have recently investigated"). Evaluation is welcome where it is earned
("remarkably", "in sharp contrast", "excellent agreement"), and so are the field's
stock phrases ("has been extensively studied", "see, e.g., Refs."). Reasons are given
where a reader would ask, often by a colon or a dash, and otherwise left to the order of
the sentences. Prior work is credited in clusters of citations by platform or mechanism.
Introductions open on the big picture or by defining the phenomenon, state the gap, and
announce "In this work, we ..."; conclusions summarise in one or two sentences and turn
to experiments and open directions. Captions run three to six sentences, panel by panel,
and may state the takeaway. Where the three differ, Marino sets openings, framing and
conclusions, and Hosseinabadi and Stefanini methods, derivations and approximations;
Stefanini gives a physical picture for every mechanism and states each limitation with
the advantage that compensates it.

The paragraphs below are verbatim from the arXiv versions; inline math lost in
extraction is marked `[math]`.

## Examples

1. Introduction opening (2608.10075, Introduction)
> Lasers with ultra-narrow linewidths and long-term phase stability are central to precision metrology, from optical atomic clocks [47, 15] to gravitational-wave detection [4, 26]. In conventional lasers, thermal fluctuations of the cavity mirrors ultimately limit phase stability [33, 37, 16, 32, 73]. On the other hand, superradiant (SR) lasers operating in the bad-cavity regime circumvent this limitation by storing coherence in the atomic medium rather than in the cavity field: the emission frequency is pinned to the atomic transition, and cavity-induced noise is strongly suppressed [50, 42, 20].

2. Introduction opening, gap stated (2605.05343, Introduction)
> Despite intense theoretical activity and a rapidly expanding toolbox of reservoir-engineering strategies [...], scalable experimental implementations remain challenging, with only a few notable exceptions [48, 41]. In this work, we build a framework connecting superradiance and many-body dissipative state preparation, with the goal of leveraging modern experimental advances in the former to develop new strategies for quantum state engineering in open systems.

3. Announcement of the contribution (2608.10075, Introduction)
> Existing strategies therefore trade reduced recoil heating against optical coherence. In this Letter, we consider incoherent correlated pump to connect the local and collective limits directly. [...] Any intermediate [math] breaks permutation invariance, so no exact solution is available: correlated pumping bridges the two solvable limits through a regime that has so far remained uncharted.

4. Abstract with numbers (2608.10075, Abstract)
> Our findings indicate that ultra-narrow emission persists for all [math], while the coherence improves as the pump becomes shorter ranged, with [math] surviving at least down to [math], indicating that fully coherent light thus does not require local pumping. The drive strength needed for lasing is reduced by a factor [math] for [math], and by [math] as [math], parametrically suppressing recoil heating.

5. Results paragraph (2504.06267, Thermalization dynamics)
> In Fig. 2 a, we show the time dependence of the low-frequency effective temperatures for three choices of parameters starting from the same initial condition [math]. [...] As a consistency check, we have benchmarked our simulations with dynamics truncated at the semiclassical level [92, 93], and found good agreement on short time scales. [...] Regime I is characterized by strong long-range interactions; the system demonstrates fast thermalization, with matter and light quickly reaching the same temperature.

6. Method paragraph (2503.17443, Sec. II.1)
> We consider the dynamics of Lindblad systems as given by the general expression in Eq. (1). Taking [math] as the set of basic operator degrees of freedom in the system, e.g. spins or boson creation and annihilation operators, the semi-classical dynamics can be obtained using the following prescription (see Appendix A for a derivation): 1. Replace quantum operators with the classical dynamical variables [...]

7. Caption (2503.17443, Fig. 3)
> The evolution of the normalized photon population in the dissipative Tavis-Cummings model with [math], starting with the photonic vacuum with fully inverted atoms. TWA demonstrates excellent agreement with the exact solution, whereas the second-order CE becomes inaccurate beyond short times.

8. Limitation and outlook (2608.10075, Perspectives)
> The TWA appears to be a powerful tool for predicting the properties of such systems at low computational cost, while GPU acceleration enables significant speed-ups in simulating the dynamics of thousands of atoms. At the same time, the method must be applied with care, since a semiclassical approach cannot correctly describe intrinsically quantum systems that lack a well-defined mean-field order parameter [31].

9. Conclusion (2504.06267, Perspectives)
> We have demonstrated that the two-dimensional quantum Ising model can exhibit prethermalization for a broad range of parameters when its transverse field becomes dynamic and is self-consistently determined by light-matter interactions. In particular, light and matter can equilibrate at distinctly different temperatures, and notably, matter may sustain negative temperatures over extended periods of time.

10. Conclusion opening, summary (2505.10531, Discussion)
> We studied the non-equilibrium dynamics of a spin system on a two-dimensional square lattice subject to a harmonic parametric drive. Combining physical arguments with numerical simulations, we predicted the emergence of two distinct dynamical instabilities induced by the drive.

11. Keldysh derivation (1606.00452, Sec. II C)
> In order to develop the quantum dynamical field theory at inspection in this work, we convert the evolution encoded in the quantum master equation, (1) into a Keldysh partition function, in view of renormalization group applications. The procedure is detailed in a number of works, and we will not repeat here all the technical steps, although we outline its main logic. [...] For practical convenience, we then express the driven-dissipative microscopic action, [math], associated to the Lindblad dynamics (1), in terms of the so-called classical and quantum fields of the Keldysh formalism, [math].

12. Benchmark against a limit where another method is exact (2312.11624, Introduction)
> We benchmark 2PI with a semi-classical phase space approximation [44, 96] and demonstrate excellent agreement in the limit of large spins between the two, where the latter becomes exact. This indicates the viability of 2PI

13. Key results announced as a list (1508.02723, Introduction)
> Our results establish a new driven quantum universality class in one dimension, which we characterize by computing the full set of static and dynamical critical exponents. In particular, we obtain the following key results: (i) New non-equilibrium fixed point. The fixed point (FP) associated to quantum NEQ condensation cannot be mapped to the classical FP of driven-dissipative condensation

14. Gap as questions (1508.02723, Introduction)
> This sparks a natural and fundamental set of questions: Given the intrinsic quantum origin, together with the flexibility in designing such systems, to which extent can effects of quantum mechanical coherence persist asymptotically at the largest distances in the vicinity of a critical point? [...] In other words, is there a driven analogue of quantum critical behavior?

15. Outlook tied to experiments (1904.01026, Outlook)
> The Dicke model is currently engineered in several experimental platforms [58-63]. We expect our results to be qualitatively insensitive to the details of the microscopic structure of the interaction term [math], and to hold in a broader set of models, and thus would be relevant for experiments where collectivity of the system is inevitably broken by inhomogeneous fields [...]. We believe that the outreach of our results has the potential to motivate a new generation of experiments on TCs in many-body systems

16. Introduction opening (M. Stefanini, 2406.03527, Sec. I)
> The Kondo effect [1] is one of the simplest and most iconic phenomena in the physics of strongly correlated systems. It emerges when an interacting impurity exchanges particles with a gapless fermionic reservoir. The hybridization of the impurity levels with the bath's states causes the emergence of a very narrow many-body resonance (the Kondo, or Abrikosov-Suhl resonance) pinned at the chemical potential of the reservoir, whose properties dominate the low-energy physics and lead to a number of fascinating phenomena

17. Gap and contribution (M. Stefanini, 2310.00039, Introduction)
> In this Letter, we embark on an initial exploration in this direction by proposing a model of non-unitary dynamics where non-perturbative effects beyond bosonization manifest in a controlled fashion, and where at the same time the mechanisms for the breakdown of bosonization can be traced back to a transparent physical picture. The latter feature is highly nontrivial, since there are only a few cases [34, 36] in which the breakdown is physically well understood.

18. Introducing the central object of a method (M. Stefanini, 2506.22436, Sec. 4.3)
> In this section we introduce the main object determining the Markovian properties of a bath—the Fourier transform of its correlation function(s) [math], known as spectral density or spectral function. A fundamental condition for a bath to provide dissipation is that it has to be large enough (in the thermodynamic sense) that its spectrum can be considered to be continuous. [...] If this condition is not fulfilled—for instance, in a small bath—the information of the previous states of the system will be able to feed back on it, providing memory and thus breaking Markovianity.

19. Caption (M. Stefanini, 2310.00039, Fig. 1)
> Absolute value of the return amplitude as a function of the rescaled time for L = 1000, J = 0.5, γ = 0.3 and increasing density. The plot shows the absence of particle-hole symmetry as the low-density curves (in shades of red) decay faster than those at the conjugate densities 1 − n̄ (shades of blue) because of an additional exponential envelope caused by the post-selected measurements.

20. Limitation with its advantage (M. Stefanini, 2206.13478, Sec. VII)
> We studied the problem from the perspective of the impurity and of the baths themselves, employing an improved perturbative technique. Albeit a priori limited to small couplings, the method we used is rather simple, and has the advantage of providing analytical results for the whole system-bath state.

21. Conclusion (M. Stefanini, 2310.00039, Conclusions)
> From a fundamental point of view, our research unveils a novel mechanism for departures from bosonization. The mechanism is distinct from more traditional explanations rooted in the effects of band curvature of the dispersion relation [34], and in this regard it illustrates transparently the profound difference between unitary and dissipative systems when it comes to the breakdown of low-energy collective descriptions.
