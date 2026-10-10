# Provenance audit

Every question in `questions.json` carries a `source` and a `sourceRef`.
This audit records what each source permits, so the bank can leave
`reviewStatus: draft` with its attribution in order.

## Current bank (from 2026-10-10)

| sourceRef | Questions | Licence | Status |
|---|---|---|---|
| Anthropic, *Claude Certified Architect – Professional Exam Guide* v1.0 (public PDF linked from the Anthropic Partner Academy certification page) | 100 of 100 | The guide is the public reference for the exam. The questions are **original**: written against the guide's domain objectives with new scenarios, options and rationales. Nothing from the guide's three sample items is reproduced. | Clear — original work; `source: original`. |

`concepts.json` (24 cards) is original in the same way.

## Earlier bank — removed 2026-10-10

| sourceRef | Questions | Licence found | Outcome |
|---|---|---|---|
| Matthew Purcell, *CCAR-P Full Practice Exam Question Set* (LinkedIn post `ugcPost-7482585280751824896`) | 83 of 83 | **None.** Checked again on 2026-10-10: the post body, its attached document and the visible comments carry no licence, Creative Commons mark or reuse statement. The author invites readers to repost, which is not a grant to adapt or redistribute. The author's profile returned an HTTP 999 (LinkedIn blocks unauthenticated fetches), so no further statement could be found there; no written permission is on file. | **Not clearly licensed → removed.** The sibling pack `quizmill/pack-claude-cert` applies the same rule (no upstream licence → excluded). The maintainer chose to replace the bank with original questions rather than seek a licence. |

The old questions had ids `cca-p-*`; the new bank uses `ccar-p-*`, so no
attempt-history row can be mistaken for a different question.

## Other checks (2026-10-10)

- **Blueprint weights.** Confirmed against the exam guide itself (section
  6): 17 / 13 / 19 / 16 / 14 / 14 / 7. `pack.json` weights match and sum
  to 1.00. The bank has exactly those percentages (100 questions).
- **Exam block.** The guide gives 63 items, 120 minutes, multiple-choice
  and multiple-response, scaled pass mark 720 on 100–1,000. The manifest
  carries `questionCount: 63`, `passPct: 72`, `scaled: true`.
- **Explanations.** Present on 100/100, each naming the correct option and
  discussing the distractors (`scripts/check-bank.py` enforces this).
- **Answer-key tells.** `scripts/check-bank.py` reports the correct option
  as the single longest in 10 of 80 single-answer questions (12%) and the
  mean length ratio of correct to distractor options at 1.02. The engine
  shows options in file order, so letter balance matters: correct letters
  are A 20 / B 21 / C 20 / D 19, and the 20 select-two items use each of
  the ten possible key pairs exactly twice.
- **Coverage of the removed bank.** Every concept the removed bank tested
  is tested here with original scenarios; the item-by-item map is in
  [coverage.md](coverage.md).
- **Concept cards.** 24, one per objective cluster across all seven
  domains; every question links to one via `conceptId`.
- **Engine validation.** `npm run pack:validate` on the engine reports a
  valid pack, 100 questions.
- **Bundle.** `quizmill bundle` builds a single bundle file from the pack.
  Bundles are gitignored (`*.bundle.json`) so one is never committed here.

## Reproduce

```
npm --prefix <engine checkout> run pack:validate -- <this directory>
npm --prefix <engine checkout> run pack:bundle   -- <this directory> --out claude-architect-pro.bundle.json
python3 scripts/check-bank.py
```
