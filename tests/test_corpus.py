"""Offline tests for corpus.py, blindtest.py and learn.py."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "skills" / "scientific-writing" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import blindtest  # noqa: E402
import corpus  # noqa: E402
import learn  # noqa: E402

PAGE = """
<div class="ltx_abstract"><h6>Abstract</h6><p class="ltx_p">We study a thing. It is new. It matters a lot for many reasons in physics today.</p></div>
<section id="S1" class="ltx_section"><h2 class="ltx_title ltx_title_section">1 Introduction</h2>
<p id="S1.p1.1" class="ltx_p">Lasers are central to metrology <cite class="ltx_cite">[1]</cite>. In conventional lasers the mirrors limit the phase stability, and superradiant lasers store coherence in the atoms instead.</p>
<p id="S1.p2.1" class="ltx_p">In this work, we consider a correlated pump with <math alttext="N" display="inline"><mi>N</mi></math> atoms. We find that coherence survives for every pump range we study here.</p></section>
<section id="S2" class="ltx_section"><h2 class="ltx_title ltx_title_section">2 Model</h2>
<p id="S2.p1.1" class="ltx_p">We consider spins coupled to a cavity mode. The cavity decays at a rate kappa, and the spins are pumped incoherently.</p>
<p id="S2.p1.2" class="ltx_p">Here the second part of the same paragraph follows the equation. It continues the thought.</p></section>
<section id="A1" class="ltx_appendix"><h2 class="ltx_title">Appendix A Derivation</h2>
<p id="A1.p1.1" class="ltx_p">We derive the equations of motion. Each step follows from the previous one by standard algebra.</p></section>
<figure><figcaption class="ltx_caption">Figure 1: Photon number against time for three pump ranges. The curves collapse at late times.</figcaption></figure>
"""


class Corpus(unittest.TestCase):
    def test_parse_jobs_and_math(self):
        rows = {r["pid"]: r for r in corpus.parse(PAGE, "0000.00000", min_words=5)}
        self.assertEqual(rows["S1.p1"]["job"], "opening")
        self.assertEqual(rows["S1.p2"]["job"], "intro")
        self.assertEqual(rows["S2.p1"]["job"], "method")
        self.assertEqual(rows["A1.p1"]["job"], "appendix")
        self.assertEqual(rows["caption0"]["job"], "caption")
        self.assertIn("[ref]", rows["S1.p1"]["text"])
        self.assertIn("$N$", rows["S1.p2"]["text"])
        self.assertIn("[equation]", rows["S2.p1"]["text"])   # a split paragraph is joined
        self.assertTrue(all(r["split"] in ("train", "test") for r in rows.values()))

    def test_retrieve_never_returns_test_split(self):
        with tempfile.TemporaryDirectory() as d:
            rows = [dict(arxiv=f"a{i}", pid="p", job="results", split="test" if i % 2 else "train",
                         text=f"cavity photons laser number {i}. Second sentence here.", words=30,
                         author="", section="") for i in range(6)]
            idx = Path(d) / "corpus.jsonl"
            idx.write_text("".join(json.dumps(r) + "\n" for r in rows))
            old = corpus.INDEX
            corpus.INDEX = idx
            try:
                got = corpus.retrieve("results", "cavity photons", k=5)
            finally:
                corpus.INDEX = old
            self.assertTrue(got and all(r["split"] == "train" for r in got))
            self.assertEqual(len({r["arxiv"] for r in got}), len(got))


class Blind(unittest.TestCase):
    def test_tidy_hides_latex(self):
        p = blindtest.tidy(r"We use $\hat H$ in \cref{eq:H}~\cite{X}, see \emph{this}.")
        self.assertNotIn("\\", p)
        self.assertIn("[math]", p)
        self.assertIn("[ref]", p)

    def test_score(self):
        with tempfile.TemporaryDirectory() as d:
            w = Path(d)
            (w / "key.json").write_text(json.dumps({"key": ["llm", "human", "llm", "human"]}))
            (w / "labels.txt").write_text("1 20 x\n2 90 y\n3 70 z\n4 60 w\n")
            self.assertAlmostEqual(blindtest.score(w), 0.75)


class Budget(unittest.TestCase):
    def test_sections_get_their_jobs(self):
        words = " ".join(["word"] * 50) + ". Second. Third."
        tex = (r"\begin{document}\section{Introduction}" + "\n\n" + words +
               r"\section{Method}\subsection{Recipe}" + "\n\n" + words +
               r"\section{Results}\subsection{A test}" + "\n\n" + words +
               r"\appendix\section{Numerical performance}" + "\n\n" + words + r"\end{document}")
        rows = {r["title"]: r for r in blindtest.section_lengths(tex)}
        self.assertEqual(rows["Introduction"]["job"], "intro")
        self.assertEqual(rows["Recipe"]["job"], "method")      # a subsection takes its section's job
        self.assertEqual(rows["A test"]["job"], "results")
        self.assertEqual(rows["Numerical performance"]["job"], "appendix")
        self.assertEqual(rows["Recipe"]["level"], 1)


class Learn(unittest.TestCase):
    def test_pairs_only_real_changes(self):
        old = "The noise is white. It has no memory.\n\nWe test it. It works well."
        new = "The noise is white. Its correlations vanish between different times.\n\nWe test it.  It works well."
        got = learn.pairs(old, new)
        self.assertEqual(len(got), 1)
        self.assertIn("no memory", got[0][0])


if __name__ == "__main__":
    unittest.main()
