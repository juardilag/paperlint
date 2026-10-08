# What readers objected to

Two kinds of entries, both from real readers. Neither is a model to imitate: the model
for how a paragraph should read is a real paragraph that does the same job, retrieved
from the corpus (`scripts/corpus.py retrieve <job> <text>`). Earlier versions of this
file paired each objection with an "accepted" rewrite; those rewrites were written by
the model itself, and imitating them taught paperlint its own voice, so they are gone.

- **Tells of generated prose**: what the blind `judge` used to tell paperlint's
  paragraphs from published ones (all 20 of 20 in the first two tests, Oct 2026). A
  draft that shows these tells is redrafted, not patched.
- **Objections**: a pattern a supervisor, co-author or referee flagged, with their
  words. The examples are anonymised onto an imaginary paper (atoms in an optical
  lattice coupled to phonons).

New entries come from `/paperlint:learn` (an author's own edits, recorded as pairs in
the paper's `author_edits.md`) or from a reviewer's remark, never from a draft.

## Tells of generated prose

1. **An even rhythm, either way.** One fact per short sentence ("The correction helps
   less at stronger coupling. Iterating it does not converge."), or, after a first
   attempt to fix that, every sentence chained with ", so that ...", ", which ..." and
   a colon until it carries a whole argument. Published paragraphs vary: a long
   sentence, a short one, a new sentence started with "However," or "Of course,".
2. **A thesis sentence first, then the support as a list.** "The other two cases change
   the noise." "The dependence on the system size is set by the coupling." Published
   paragraphs open from the setting or from the previous point ("In Fig. 2a we
   show ...", "According to the above considerations ...", "Nevertheless, one can ...").
3. **A reason or a pointer attached to every step.** "because", "so", "therefore" and
   "(Sec. III)" in most sentences; counted lists ("Three details keep ..."). Published
   prose gives the reason where a reader would ask for it and lets the rest follow from
   the order.
4. **No voice.** No narrating "we" ("we have recently investigated", "we note that"),
   no evaluation ("remarkably", "crucially", "a prominent example"), no aside to the
   reader ("notice the logarithmic term"), no stock phrase of the field ("has been
   extensively studied", "see, e.g., Refs."). The house style uses all of these.
5. **Definitions slipped in as appositives**, one after another: "the two polaritons,
   the normal modes of cavity and spins at $g_c$, are strongly mixed".

## Objections, by kind

### Content and correctness
- **Slogan instead of the physics.** "Detailed balance is a property of the
  construction, not an assumption." Say what holds, why, and where it is shown.
- **Placeholder words.** "derives the corresponding equation from a microscopic model"
  *(Reviewer: "which equation? what is microscopic here?")*
- **Prior work invoked, not stated.** "the natural generalisation of Ref. [12]" with no
  word on what Ref. [12] does; or its limitation saved for the end of the paragraph
  *(Author: "only at the end of the paragraph you talk about that it has no memory")*.
- **Anthropomorphism and colloquial metaphor.** "the lattice remembers its past", "the
  trick that buys the speed-up", "the two engines", "our recipe".
- **A statement narrower or wider than the method.** "each atom is sampled from a
  discrete distribution" *(Authors: "not true, the dense lattices use a Gaussian")*;
  a general step written for one system *(Authors: "this is a general method, not
  only for ...")*.
- **Contribution framed as someone else's plan.** "Ref. [12] outlined the extension,
  which we carry out." *(Co-author: "this can give the referee the impression that the
  work is incremental")*
- **A semiclassical statement in quantum words**, or the reverse *(Author: "This is a
  semiclassical statement")*.
- **A limitation without its consequence.** "the error grows with the interactions"
  *(Co-author: "Of order 1/S for a spin of length S.")*
- **A circular "because".** "... is a first-order differential equation, so Eq. (6) is
  unambiguous." *(Author: "this makes no sense")*
- **A comparison the argument does not need.** Initial-state fluctuations set against
  those of the reservoir *(Senior author: "it is confusing and can attract
  criticism")*.
- **A historical citation where the field cites a modern source.** The 1925 paper for
  the classical correspondence of commutators *(Senior author: "good to cite the
  review, no human would cite the original")*.
- **Words that do not fit the physics.** "a weakly damped transition" *(Senior author:
  "how can a transition be damped physically?")*; "the bath cannot respond before it
  is perturbed" for causality *(Senior author: "say it as a physicist")*.
- **A property the formula does not show, left unexplained.** "The noise is then
  complex." *(Reviewer: "how can a noise be complex?")*; a correlator claimed real next
  to an explicit i/2.

### Density: both directions were objected to
- **Too little:** terms the argument turns on used bare. "their noise is white"
  *(Reviewer: "what is white noise? reference?")*; "what is Γ? why 2πJ?"
- **Too much:** the fix for it. Definition sentences in a row, formulas read aloud,
  mechanisms in the main text. *(Co-author: "waaay too pedantic. The point is to
  explain the physical meaning of mathematical formulas, not to put them in words.")*;
  *(Co-author: "You shouldn't put formulas into words.")*; *(Authors: "too much
  technical detail")*; a name coined and used once *(Co-author: "Do we care about
  this?")*.
- **Too little, for notation:** an index pair, a subscript or a new argument used
  without a word *(Senior author: "it is assumed the reader will figure out but he
  won't"; "each notation adds overhead to reading")*; two averages behind one overline
  *(Senior author: "a clear conceptual clash")*.
- **The balance** *(Author: "we must try not to assume anything of the reader ... this
  is important, find a balance")*: a reference for every term, a clause of meaning
  only for the terms the argument turns on, the mechanism in an appendix.
- **A departure explained by its mechanism.** A step that does not follow the method
  explained with joint ground states and negative frequencies *(Author: "I think for
  not confuse the reader, just say that because the cavity loss is of Lindblad type,
  the noise is white, and reference")*; earlier, *(Author: "more direct, better
  explained, because this is the first test of the method, so it is really strange
  that we set up a list of steps, and then it does not work")*; and of the one-sentence
  remainder, *(Author: "this is not necessary ... the important thing is to say that
  this Lindblad loss produces a white noise that is filtered with the cavity because
  we integrated it out")*: say what the step does, point to the appendix for why.
- **Another paper's results re-derived** *(Author: "These results come from another
  paper, maybe just state them more direct and concisely")*.
- **A particular number without its support** *(Author: "This is a particular result,
  right? Maybe we can quit this and just state the general result")*.
- **Every fix right, the whole too long.** An introduction revised from 1519 to 1764
  words, each change justified *(Author: "the text is too dense, is too large ... a
  human seeks to communicate all the ideas in a concise readable way, not wasting space
  or time")*. Answers to review questions go where the result is shown, or to an
  appendix, not into the sentence that raised them.

### Structure
- **A step that says what it does only at its end** *(Authors: "the step never says
  directly what it does")*.
- **The central equation too early or too late** *(senior author: the equation
  "arrives too quickly")*: name its actors in words first, then show it.
- **A "Remarks" subsection**, struck by the senior author: a remark stands where its
  subject is, or goes.
- **A thin section opening.** An abrupt first sentence about "the existing methods",
  then a second paragraph that assumes the reader knows the background *(Senior
  author: "starting of sections are always difficult ... expand ... a concise yet
  longer and deeper summary at a conceptual level. Do not be shallow")*.
- **A compressed technical paragraph in the main text** *(Senior author: "decide
  whether this section is for a short show off or to deliver real content")*: expand
  it with intuition and references, or move it to an appendix.
- **A placeholder caption** *(Senior author: "a caption has still to be understood
  and not just be a placeholder")*, and its opposite, a caption that repeats the
  text and every setting *(Author: "we need a more concise and direct caption")*.
- **A closing that lists the sections again** (flagged by a second co-author).
