---
name: blindtest
description: "Measure how much a paper's prose reads like published prose. Mixes paragraphs of the paper with held-out paragraphs of the house-style corpus, has the blind judge agent give each one, on its own, a probability of being human-written, and reports the separation (AUC: 0.5 means indistinguishable, 1.0 always told apart; lower is better) and the tells it used. Use when the user asks whether the text reads as generated, to compare two versions of a section, or before and after a rewrite."
argument-hint: "<file.tex> [--section <title>] [-n 10] [--seed 1]"
---

S="${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts"

1. If `python3 $S/corpus.py jobs` says there is no corpus, run `python3 $S/corpus.py build`.
2. `python3 $S/blindtest.py make <file.tex> [--section <title>] -n <n> --seed <seed>`.
   It prints a work directory. Use the same seed for every version you compare; a
   section too short for `n` paragraphs gets fewer, and the score is then coarse.
3. Launch the `judge` agent with the path of `<workdir>/blind.md`. It must not see
   `key.json`.
4. `python3 $S/blindtest.py score <workdir>`.
With `--budget`, run only `blindtest.py budget <file.tex>` and show the table: each
section's length against the corpus median and limit for its job.

5. Report the separation, the mean probability of being human for the paper's and the
   published paragraphs, and the judge's five tells in one line each. With `--stats`, also run
   `blindtest.py stats <file.tex>` and show the table; its measures are diagnostics of
   where to look, never targets.

One run of 20 paragraphs has a large error bar (an AUC of 0.8 and 0.9 are not reliably
different). The judge never balances its labels: with a quota it could find the
published paragraphs by their typos and idioms and label the rest by elimination, and
the score would not move whatever the paper says. Compare versions with the same seed, and run two seeds before concluding
that a change helped.
