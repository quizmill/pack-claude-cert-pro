# Claude Architect – Professional — quizmill practice pack

**Unofficial** practice question bank for the **Claude Certified Architect –
Professional (CCAR-P)** exam — the top tier of Anthropic's 2026 certification
program. Not affiliated with or endorsed by Anthropic.

This is a learning pack for [quizmill](https://github.com/quizmill/quizmill).
The pack is pure JSON; the engine turns it into an installable, offline-first
practice app.

| Domain | Weight |
|---|---|
| Solution Design & Architecture | 17% |
| Integration | 19% |
| Evaluation, Testing & Optimization | 16% |
| Governance, Safety & Risk Management | 14% |
| Stakeholder Communication & Lifecycle Management | 14% |
| Claude Models, Prompting & Context Engineering | 13% |
| Developer Productivity & Operational Enablement | 7% |

## Run it

```
git clone https://github.com/quizmill/quizmill
cd quizmill && npm install
npm run pack:use /path/to/pack-claude-architect-professional
npm run dev
```

## Sources & attribution

Questions are adapted from Matthew Purcell's free CCAR-P full practice set —
see [NOTICE.md](NOTICE.md). The exam's five **scenario-matching** items were
split into their individual sub-scenarios as single-answer multiple-choice
questions (the quizmill engine does not yet support a native matching type), so
63 source items are represented as 83 pack questions.
