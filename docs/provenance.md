# Provenance audit — 2026-10-10

Every question in `questions.json` carries a `source` and a `sourceRef`.
This audit walks all of them and records what each source permits, so the
bank can leave `reviewStatus: draft` with its attribution in order.

## Summary

| sourceRef | Questions | Source items | Licence found | Status |
|---|---|---|---|---|
| Matthew Purcell, *CCAR-P Full Practice Exam Question Set* (LinkedIn post `ugcPost-7482585280751824896`) | 83 of 83 | 63 (five scenario-matching items split into 25 single-answer questions) | **None.** The post and its attached PDF carry no licence, Creative Commons mark, or reuse statement. The author describes the set as free and original, written against Anthropic's public exam guide. | **Not clearly licensed** — included under attribution only; no written permission on file. |

There are no other sources: no hand-authored questions, no questions from
MIT-licensed community banks, and no `conceptId` links (the pack has no
`concepts.json` yet).

## What "not clearly licensed" means here

"Free" on a social post is not a licence. Absent an explicit grant, the
text stays under the author's copyright, and adapting it (splitting,
re-keying, rewording rationales) does not change that. The sibling pack
`quizmill/pack-claude-cert` draws the same line: its MIT-licensed banks
are included, while a bank with no upstream licence is excluded until one
appears. By that rule, **every question in this pack is flagged.**

Removing all 83 would leave an empty pack, so this audit flags rather than
removes. The options, in recommended order:

1. **Ask the author for a written licence** (CC BY 4.0 or a direct
   permission note covering adaptation and redistribution), record it in
   `NOTICE.md`, and keep the bank.
2. **Replace the bank with original questions** written against
   Anthropic's public exam guide and Claude documentation, keeping the
   seven-domain blueprint and the question ids where the topic survives.
3. Keep the bank under attribution only. Not recommended for anything
   beyond personal practice.

Until one of these is chosen, every question stays `reviewStatus: draft`.

## Other checks run in the same pass

- **Blueprint weights.** `pack.json` category weights sum to 1.00 and match
  the seven-domain table in `README.md` (17 / 13 / 19 / 16 / 14 / 14 / 7).
  The bank is distributed close to those weights, with Models & Prompting
  (10% of the bank vs 13%) and Dev Enablement (5% vs 7%) slightly under.
  The weights were not re-checked against Anthropic's exam guide in this
  pass; the guide's page could not be fetched.
- **Explanations.** Present on all 83 questions; none shorter than 80
  characters.
- **Engine validation.** `npm run pack:validate` on the engine reports a
  valid pack, 83 questions.
- **Bundle.** `quizmill bundle` produces a single bundle file from the pack
  (83 questions, 0 images, 111 KiB). Bundles are gitignored
  (`*.bundle.json`) so one is never committed here by accident.
- **Concept cards.** None yet. The plan is cards for the weakest topics
  measured from real practice history, which needs a progress export from
  the app (Settings → Move progress) rather than a guess from tag counts.

## Reproduce

```
npm --prefix <engine checkout> run pack:validate -- <this directory>
npm --prefix <engine checkout> run pack:bundle   -- <this directory> --out claude-architect-pro.bundle.json
```
