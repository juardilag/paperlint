"""Offline tests for check_refs parsing and the PostToolUse hook."""
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "skills" / "scientific-writing" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import check_refs  # noqa: E402

BIB = r"""
@article{Wigner1932,
  author  = {Wigner, E.},
  title   = {On the quantum correction for thermodynamic {E}quilibrium},
  journal = {Phys. Rev.}, volume = 40, pages = {749--759}, year = {1932},
}
@misc{code, author = "Someone", title = "A code", year = 2020}
@comment{ignored}
"""


class Bib(unittest.TestCase):
    def test_parse(self):
        es = {e["key"]: e for e in check_refs.parse_bib(BIB)}
        self.assertEqual(set(es), {"Wigner1932", "code"})
        w = es["Wigner1932"]
        self.assertEqual(w["volume"], "40")
        self.assertEqual(check_refs.first_page(w["pages"]), "749")
        self.assertEqual(check_refs.first_author_family(w["author"]), "wigner")
        self.assertEqual(es["code"]["title"], "A code")

    def test_plain_strips_markup_and_html(self):
        self.assertEqual(check_refs.plain("Semigroups of\n <i>N</i>\n -level {S}ystems"),
                         check_refs.plain("Semigroups of {N}-level systems"))

    def test_compare_flags_wrong_volume(self):
        e = check_refs.parse_bib(BIB)[0]
        work = {"title": ["On the quantum correction for thermodynamic equilibrium"],
                "author": [{"family": "Wigner"}], "volume": "41",
                "page": "749-759", "issued": {"date-parts": [[1932]]}}
        issues = check_refs.compare(e, work)
        self.assertEqual(len(issues), 1)
        self.assertIn("volume", issues[0])


class Hook(unittest.TestCase):
    def run_hook(self, event):
        p = subprocess.run([sys.executable, str(SCRIPTS / "hook_postedit.py")],
                           input=json.dumps(event), capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        return p.stdout

    def test_reports_only_edited_paragraph(self):
        with tempfile.TemporaryDirectory() as d:
            tex = Path(d) / "main.tex"
            tex.write_text("\\begin{document}\nThe first paragraph is fine.\n\n"
                           "As in Eq.~\\ref{x} we go on.\n\\end{document}\n")
            (Path(d) / "paperlint.toml").write_text('[paper]\nfiles=["main.tex"]\n')
            out = self.run_hook({"tool_name": "Edit", "tool_input": {
                "file_path": str(tex), "old_string": "x",
                "new_string": "As in Eq.~\\ref{x} we go on."}})
            ctx = json.loads(out)["hookSpecificOutput"]["additionalContext"]
            self.assertIn("PL013", ctx)
            out2 = self.run_hook({"tool_name": "Edit", "tool_input": {
                "file_path": str(tex), "old_string": "x",
                "new_string": "The first paragraph is fine."}})
            self.assertEqual(out2, "")

    def test_silent_without_config_or_for_other_files(self):
        with tempfile.TemporaryDirectory() as d:
            tex = Path(d) / "main.tex"
            tex.write_text("\\begin{document}\nWe use a recipe.\n\\end{document}\n")
            self.assertEqual(self.run_hook({"tool_input": {"file_path": str(tex)}}), "")
        self.assertEqual(self.run_hook({"tool_input": {"file_path": "/tmp/x.py"}}), "")
        self.assertEqual(self.run_hook({}), "")

    def test_silent_for_round_notes(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "paperlint.toml").write_text("[paper]\n")
            notes = Path(d) / "review" / "2026-10-03"
            notes.mkdir(parents=True)
            tex = notes / "summary.tex"
            tex.write_text("\\begin{document}\nThe TWA; a recipe: here.\n\\end{document}\n")
            self.assertEqual(self.run_hook({"tool_input": {"file_path": str(tex)}}), "")


if __name__ == "__main__":
    unittest.main()


class PdfComments(unittest.TestCase):
    def test_reads_annotation_with_marked_text(self):
        try:
            from pypdf import PdfWriter
            from pypdf.annotations import Highlight, Text
            from pypdf.generic import ArrayObject, FloatObject
        except ImportError:
            self.skipTest("pypdf not installed")
        import pdf_comments
        w = PdfWriter()
        w.add_blank_page(200, 200)
        w.add_annotation(0, Text(text="say who?", rect=(10, 10, 30, 30)))
        h = Highlight(rect=(50, 50, 90, 60), quad_points=ArrayObject(
            [FloatObject(v) for v in (50, 60, 90, 60, 50, 50, 90, 50)]))
        w.add_annotation(0, h)
        with tempfile.TemporaryDirectory() as t:
            pdf = str(Path(t) / "a.pdf")
            w.write(pdf)
            rows = pdf_comments.comments(pdf)
        self.assertEqual([r["type"] for r in rows], ["Text", "Highlight"])
        self.assertEqual(rows[0]["comment"], "say who?")
        self.assertEqual(rows[1]["page"], 1)
