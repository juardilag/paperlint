"""Tests for the paperlint checks. Run with: python3 -m unittest discover tests"""
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "skills" / "scientific-writing" / "scripts"))

import lint  # noqa: E402

DOC = "\\begin{document}\n%s\n\\end{document}\n"


def codes(body: str, cfg: lint.Config | None = None) -> list[str]:
    cfg = cfg or lint.Config(banned=list(lint.DEFAULT_BANNED),
                             anthropomorphic=list(lint.DEFAULT_ANTHROPOMORPHIC))
    cfg.style = True
    return [f.code for f in lint.lint_text(DOC % body, "t.tex", cfg)]


class Fixtures(unittest.TestCase):
    def test_bad_fixture_finds_every_check(self):
        cfg = lint.load_config(HERE / "fixtures" / "bad.tex")
        cfg.style = True
        src = (HERE / "fixtures" / "bad.tex").read_text()
        found = {f.code for f in lint.lint_text(src, "bad.tex", cfg)}
        expected = {"PL001", "PL002", "PL003", "PL004", "PL005", "PL006", "PL007",
                    "PL008", "PL009", "PL010", "PL011", "PL012", "PL013", "PL014",
                    "PL016", "PL017", "PL018", "PL019", "PL020"}
        self.assertEqual(expected - found, set())

    def test_good_fixture_is_clean(self):
        cfg = lint.load_config(HERE / "fixtures" / "good.tex")
        cfg.style = True
        src = (HERE / "fixtures" / "good.tex").read_text()
        self.assertEqual(lint.lint_text(src, "good.tex", cfg), [])


class Defaults(unittest.TestCase):
    def test_only_errors_by_default(self):
        cfg = lint.load_config(HERE / "fixtures" / "bad.tex")
        src = (HERE / "fixtures" / "bad.tex").read_text()
        found = {f.code for f in lint.lint_text(src, "bad.tex", cfg)}
        self.assertTrue(found)
        self.assertLessEqual(found, lint.ERROR_CHECKS)

    def test_enable_one_style_check(self):
        cfg = lint.Config(enabled={"PL003"})
        found = [f.code for f in lint.lint_text(DOC % "One; two. We use a recipe.",
                                                 "t.tex", cfg)]
        self.assertEqual(found, ["PL003"])


class Sentences(unittest.TestCase):
    def test_abbreviations_do_not_end_sentences(self):
        self.assertNotIn("PL005", codes("See e.g. the model of Ref.~\\cite{a} and Eq. 3 here."))

    def test_sentence_ending_inside_math(self):
        # "... h.c.$ In this ..." is two sentences; neither is long.
        body = ("We write the coupling as $a b^\\dagger + \\mathrm{h.c.}$ In this coupling "
                "each term exchanges one quantum between the system and the bath.")
        self.assertNotIn("PL001", codes(body))

    def test_long_sentence(self):
        body = " ".join(["word"] * 30) + "."
        self.assertIn("PL001", codes(body))

    def test_display_math_does_not_count(self):
        body = ("The kernel is\n\\begin{equation}\na+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x\n"
                "\\end{equation}\nfor all times.")
        self.assertNotIn("PL001", codes(body))


class Texture(unittest.TestCase):
    def test_repeated_modifier(self):
        body = ("The bath is integrated out exactly. The model is then solved exactly "
                "for eight sites. This gives an exact reference for the kernel.")
        self.assertIn("PL018", codes(body))

    def test_repeated_noun_is_fine(self):
        body = ("The cavity loses photons. The cavity field decays. The cavity mode "
                "is harmonic and the cavity bath is flat.")
        self.assertNotIn("PL018", codes(body))

    def test_repetition_counts_per_paragraph(self):
        body = "The bath is exact.\n\nThe kernel is exact.\n\nThe noise is exact."
        self.assertNotIn("PL018", codes(body))

    def test_enumeration(self):
        body = ("We compare two results. The first result is an exact solution. "
                "The second result is an analytic exponent.")
        self.assertIn("PL019", codes(body))

    def test_single_ordinal_is_fine(self):
        self.assertNotIn("PL019", codes("The first result is an exact solution of the model."))

    def test_inanimate_agent(self):
        self.assertIn("PL020", codes("The Dicke model tests the memory kernel."))
        self.assertIn("PL020", codes("The simulation confirms that the kernel is causal."))

    def test_figure_shows_is_fine(self):
        self.assertNotIn("PL020", codes("This figure shows the kernel and the noise."))

    def test_section_as_agent_is_fine(self):
        self.assertNotIn("PL020", codes("Section III tests the memory kernel."))


class Openers(unittest.TestCase):
    def test_symbol_start(self):
        self.assertIn("PL005", codes("$N$ atoms couple to the lattice."))

    def test_numeral_start(self):
        self.assertIn("PL005", codes("50 samples were prepared."))

    def test_acronym_start(self):
        self.assertIn("PL005", codes("The method (TWA) is fast. TWA reaches large sizes."))

    def test_lowercase_cref_start(self):
        self.assertIn("PL006", codes("\\cref{eq:a} gives the kernel."))

    def test_capital_cref_start_ok(self):
        self.assertEqual(codes("\\Cref{eq:a} gives the kernel."), [])

    def test_expletive(self):
        self.assertIn("PL008", codes("It is clear that the bath is thermal."))
        self.assertIn("PL008", codes("There are two baths in the model."))

    def test_pronoun_passive_is_not_expletive(self):
        self.assertNotIn("PL008", codes("The commutator is not an average. It is obtained from a pulse."))

    def test_bare_demonstrative(self):
        self.assertIn("PL012", codes("The kernel decays. This means that the bath is fast."))
        self.assertNotIn("PL012", codes("The kernel decays. This kernel is short."))


class Punctuation(unittest.TestCase):
    def test_colon_and_semicolon(self):
        c = codes("The result is simple: it works; we use it.")
        self.assertIn("PL002", c)
        self.assertIn("PL003", c)

    def test_ratio_is_not_a_colon(self):
        self.assertNotIn("PL002", codes("The ratio is 1:4 in both runs."))

    def test_em_dash_but_not_en_dash(self):
        self.assertIn("PL004", codes("The bath --- a thermal one --- is fixed."))
        self.assertNotIn("PL004", codes("The range 2.1--2.6 follows Caldeira--Leggett."))

    def test_math_and_comments_are_ignored(self):
        body = "The map is $f: X\\to Y$ here.\n% note: ignore; this --- line\nThe end."
        self.assertEqual(codes(body), [])


class Words(unittest.TestCase):
    def test_parenthetical_pointers(self):
        self.assertIn("PL016", codes("A follows (\\cref{a}) and B follows (\\cref{b}) here."))
        self.assertNotIn("PL016", codes("A follows from the kernel (\\cref{a}) here."))

    def test_antithesis(self):
        self.assertIn("PL017", codes("The step is a consequence, not an extra assumption."))
        self.assertIn("PL017", codes("The method is not a fit but a derivation."))
        self.assertNotIn("PL017", codes("We do not use a cutoff, but the result converges."))

    def test_llm_openers(self):
        self.assertIn("PL007", codes("Notably, the kernel is causal."))
        self.assertIn("PL007", codes("The bath plays a key role in the relaxation."))

    def test_banned(self):
        self.assertIn("PL007", codes("We use a recipe to obtain the result."))

    def test_allow_overrides_default(self):
        cfg = lint.Config(banned=[b for b in lint.DEFAULT_BANNED if "very" not in b[0]])
        self.assertNotIn("PL007", codes("The result is very good.", cfg))

    def test_anthropomorphic_is_info(self):
        cfg = lint.Config(anthropomorphic=list(lint.DEFAULT_ANTHROPOMORPHIC), style=True)
        fs = lint.lint_text(DOC % "The bath remembers the past.", "t.tex", cfg)
        self.assertEqual([(f.code, f.severity) for f in fs], [("PL014", "info")])

    def test_long_emph(self):
        self.assertIn("PL009", codes("\\emph{The truncation is the only approximation here}."))
        self.assertNotIn("PL009", codes("We call it \\emph{memory kernel}."))


class Acronyms(unittest.TestCase):
    def test_defined_at_first_use(self):
        self.assertNotIn("PL011", codes("The graphics processing unit (GPU) is fast. The GPU works."))

    def test_used_before_defined(self):
        self.assertIn("PL011", codes("The GPU is fast."))

    def test_lowercase_prefix_acronym(self):
        self.assertIn("PL011", codes("We sample from the distribution of dTWA here."))
        self.assertNotIn("PL011", codes("The discrete method (dTWA) samples. The dTWA works."))
        self.assertNotIn("PL011", codes("The signal at 5 kHz and 3 mW is weak."))

    def test_known_acronym(self):
        cfg = lint.Config(known_acronyms={"GPU"})
        self.assertNotIn("PL011", codes("The GPU is fast.", cfg))

    def test_units_are_not_acronyms(self):
        cfg = lint.load_config(HERE / "fixtures" / "good.tex")
        fs = lint.lint_text(DOC % "The card has 12 GB of memory at 2 GHz.", "t.tex", cfg)
        self.assertNotIn("PL011", [f.code for f in fs])

    def test_roman_numerals(self):
        self.assertNotIn("PL011", codes("Table II lists the values."))


class References(unittest.TestCase):
    def test_hand_typed(self):
        self.assertIn("PL013", codes("As in Eq.~(\\ref{eq:a}) we find the kernel."))
        self.assertIn("PL013", codes("As in \\eqref{eq:a} we find the kernel."))

    def test_any_style_disables(self):
        cfg = lint.Config(reference_style="any")
        self.assertNotIn("PL013", codes("As in Eq.~(\\ref{eq:a}) we find the kernel.", cfg))


class Glossary(unittest.TestCase):
    def test_main_text_only(self):
        cfg = lint.Config(forbidden_terms=[{"pattern": "friction", "use": "damping",
                                            "scope": "main", "note": ""}])
        body = "The friction is small.\n\\appendix\nHere the friction is fine."
        fs = lint.lint_text(DOC % body, "t.tex", cfg)
        self.assertEqual([f.line for f in fs if f.code == "PL010"], [2])


class Length(unittest.TestCase):
    def test_prose_words(self):
        src = "\\section{A}\nThe atoms move $x$ fast.\n\\begin{equation}a=b\\end{equation}\n"
        self.assertEqual(lint.prose_words(src, 2, 3), 5)  # inline math counts as one word

    def test_paragraph_limit(self):
        cfg = lint.Config(max_paragraph_words=10)
        self.assertIn("PL022", codes("The atoms move. " * 5, cfg))
        self.assertNotIn("PL022", codes("The atoms move.", cfg))


class Sections(unittest.TestCase):
    def test_section_range(self):
        src = "\\section{Intro}\na\n\\subsection{Sub}\nb\n\\section{Method}\nc\n"
        self.assertEqual(lint.section_range(src, "intro"), (1, 5))
        self.assertEqual(lint.section_range(src, "Sub"), (3, 5))


if __name__ == "__main__":
    unittest.main()
