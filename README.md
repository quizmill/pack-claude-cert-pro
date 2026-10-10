# Claude Architect – Professional — quizmill practice pack

**Unofficial** practice question bank for the **Claude Certified Architect –
Professional (CCAR-P)** exam — the top tier of Anthropic's 2026 certification
program. Not affiliated with or endorsed by Anthropic.

This is a learning pack for [quizmill](https://github.com/quizmill/quizmill).
The pack is pure JSON; the engine turns it into an installable, offline-first
practice app.

## What's in it

- **100 original questions** — 81 single-answer and 19 "select TWO" items,
  written against the objectives in Anthropic's public
  [exam guide](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf)
  (v1.0, July 2026). Every question has a rationale that says why the
  answer is right and why each distractor is wrong.
- **Blueprint weighting** — the bank's domain split matches the exam
  blueprint to the question, and the manifest carries the same weights so
  the engine's readiness estimate is blueprint-weighted.
- **24 concept cards** — one per objective cluster, shown after a wrong
  answer. Every question links to one.

| Domain | Weight | Questions |
|---|---|---|
| Solution Design & Architecture | 17% | 17 |
| Claude Models, Prompting & Context Engineering | 13% | 13 |
| Integration | 19% | 19 |
| Evaluation, Testing & Optimization | 16% | 16 |
| Governance, Safety & Risk Management | 14% | 14 |
| Stakeholder Communication & Lifecycle Management | 14% | 14 |
| Developer Productivity & Operational Enablement | 7% | 7 |

The real exam has 63 items, 120 minutes, and a scaled pass mark of 720 on a
100–1,000 scale; the manifest's `exam` block records this so the app can
show an estimate (raw accuracy, not the scaled score).

## Run it

```
npx quizmill run quizmill/pack-claude-cert-pro
```

or from a clone of the engine:

```
git clone https://github.com/quizmill/quizmill
cd quizmill && npm install
npm run pack:use /path/to/pack-claude-cert-pro
npm run dev
```

## Checking the bank

Two checks, run from the pack root:

```
npx quizmill validate .          # schema + cross-reference checks (engine)
python3 scripts/check-bank.py    # curation checks (this repo)
```

The curation script guards against the things a test-wise candidate
exploits rather than knowledge: the correct option being the longest,
one letter dominating, absolute wording only in distractors, and
explanations that do not discuss the distractors. It also checks the
domain split against the manifest weights.

## Sources & attribution

All questions are original; see [NOTICE.md](NOTICE.md) and
[docs/provenance.md](docs/provenance.md).
