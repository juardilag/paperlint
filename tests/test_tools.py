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
                           "We use a recipe here.\n\\end{document}\n")
            (Path(d) / "paperlint.toml").write_text('[paper]\nfiles=["main.tex"]\n')
            out = self.run_hook({"tool_name": "Edit", "tool_input": {
                "file_path": str(tex), "old_string": "x",
                "new_string": "We use a recipe here."}})
            ctx = json.loads(out)["hookSpecificOutput"]["additionalContext"]
            self.assertIn("recipe", ctx)
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


if __name__ == "__main__":
    unittest.main()
