#!/usr/bin/env python3
"""PostToolUse hook: report ERRORS in the paragraphs of a .tex file Claude just edited.

Opt-in: it runs only when the edited file sits under a directory that contains a
paperlint.toml (create one with the init script). It never modifies anything. The
report reaches Claude as additional context; when the edited paragraphs are clean
the hook prints nothing.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint  # noqa: E402

MAX_FINDINGS = 25


def _config_dir(path: Path) -> Path | None:
    for d in [path.parent, *path.parent.parents]:
        if (d / "paperlint.toml").is_file():
            return d
    return None


def _paragraph_range(src: str, a: int, b: int) -> tuple[int, int]:
    """Expand the character span [a, b) to whole paragraphs; return line numbers."""
    start = src.rfind("\n\n", 0, a)
    start = 0 if start < 0 else start + 2
    end = src.find("\n\n", b)
    end = len(src) if end < 0 else end
    return src.count("\n", 0, start) + 1, src.count("\n", 0, end) + 1


def _edited_ranges(src: str, tool_input: dict) -> list[tuple[int, int]] | None:
    """Line ranges touched by the edit, or None for 'the whole file'."""
    pieces = []
    if "new_string" in tool_input:
        pieces.append(tool_input["new_string"])
    for e in tool_input.get("edits", []) or []:
        if "new_string" in e:
            pieces.append(e["new_string"])
    if not pieces:
        return None
    ranges = []
    for piece in pieces:
        piece = piece.strip()
        if not piece:
            continue
        pos = src.find(piece)
        if pos < 0:
            # fall back to the first line of the new text
            first = piece.splitlines()[0]
            pos = src.find(first)
            if pos < 0:
                continue
        ranges.append(_paragraph_range(src, pos, pos + len(piece)))
    return ranges or None


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except Exception:
        return 0
    tool_input = event.get("tool_input") or {}
    fname = tool_input.get("file_path") or tool_input.get("path") or ""
    if not fname.endswith(".tex"):
        return 0
    path = Path(fname)
    if not path.is_absolute():
        path = Path(event.get("cwd", ".")) / path
    if not path.is_file() or _config_dir(path) is None:
        return 0

    src = path.read_text(encoding="utf-8")
    cfg = lint.load_config(path)
    # Errors only, whatever the paper's config: style notes are for the author to read,
    # not for the writer to patch paragraph by paragraph.
    cfg.style, cfg.enabled = False, set()
    findings = lint.lint_text(src, str(path), cfg)
    ranges = _edited_ranges(src, tool_input)
    if ranges is not None:
        findings = [f for f in findings if any(a <= f.line <= b for a, b in ranges)]
    if not findings:
        return 0

    where = "the edited paragraphs" if ranges is not None else "the file"
    report = (f"paperlint found {len(findings)} error(s) in {where} of {path.name}. "
              "Fix each with the smallest edit, or say why it is a false positive. "
              "Do not rewrite the paragraph for this.\n"
              + lint.format_findings(findings, MAX_FINDINGS))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                             "additionalContext": report}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
