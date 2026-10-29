# Fable grading of the bank against the retired set (2026-10-29)

The maintainer asked for the 200 original questions to be graded, by Claude Fable 5.1, against the retired 83-question bank (verified by the maintainer before it was removed for licensing reasons; see [provenance.md](provenance.md)), and adapted to its form and difficulty; duplicates removed; the set rebalanced. One grader per exam domain read the domain's retired items and its current items and produced, per question: the nearest retired item, a style-match score, a difficulty estimate on the retired set's scale, concrete issues, duplicate pairs, and the revised text. The grades were applied by script (`tmp/merge.py`, not committed) and checked with `scripts/check-bank.py`, `npx quizmill validate .` and the admin eval lint.

## What changed

| Action | Questions |
|---|---|
| keep | 0 |
| tighten | 107 |
| rewrite | 82 |
| replace | 11 |

- **tighten**: same stem and key; options rewritten to the retired set's form (55–90 characters, parallel, no self-justifying clauses) and the explanation rebuilt as `Correct: X. … Why not the others: …`.
- **rewrite**: stem also changed. Most are first-hundred items whose scenario tracked a retired item too closely (the graders flagged them per domain below) and second-hundred items with 300+ character stems.
- **replace**: removed as a duplicate of another current question (table below) and replaced by a new question on the domain's least-covered concept, same answer type and same correct letter(s), so the domain counts, the select-two share and the letter balance are unchanged.

Difficulty was re-estimated per question on the retired set's scale; 3 labels changed. Mean option length moved from 110 to 84 characters (retired set: 69).

## Duplicates removed

| Removed | Duplicate of | Why | Replacement |
|---|---|---|---|
| ccar-p-d1-22 | ccar-p-d1-18 | Both ask for the pattern for a one-turn answer with context already supplied and both resolve to the single augmented LLM call; a learner who knows one knows the other. | ccar-p-d1-36 |
| ccar-p-d1-33 | ccar-p-d1-25 | d1-33's two keys are d1-25's answer (subagent contexts compress bulky exploration) and d1-16's answer (independent sub-tasks run in parallel); it adds no new substance. | ccar-p-d1-37 |
| ccar-p-d2-08 | ccar-p-d2-22 | Both test the same fix for drifted copies of shared prompt text: one versioned source (module/template) composed into each prompt. A learner who knows one answers the other; 22 is kept because it also covers variable separation. | ccar-p-d2-27 |
| ccar-p-d3-04 | ccar-p-d3-14 | Both test least-privilege scoping of an agent's tool surface, with the same distractor set (prompt rule, audit log, confirmation); knowing to narrow the tool set answers both. | ccar-p-d3-39 |
| ccar-p-d3-11 | ccar-p-d3-18 | Both test that progressive discovery wins when the tool and reference set is large and each request uses a small slice; 11 is the single-answer form of 18's select-TWO. | ccar-p-d3-40 |
| ccar-p-d3-19 | ccar-p-d3-33 | Both test that diagnosing a failing session needs one correlation/trace ID propagated across steps plus per-step records (spans); the substance of the correct answer is identical. | ccar-p-d3-41 |
| ccar-p-d4-13 | ccar-p-d4-01 | Both ask for the metric set a launch decision needs and both key on 'accuracy, latency, cost and safety, each with an agreed target'; a learner who knows one necessarily knows the other. | ccar-p-d4-33 |
| ccar-p-d5-24 | ccar-p-d5-04 | Both test that removing explicit demographic fields leaves proxy bias and that the answer is per-group outcome measurement with standing fairness tests; a learner who knows one answers the other. | ccar-p-d5-29 |
| ccar-p-d6-01 | ccar-p-d6-22 | Both test honest communication of probabilistic behaviour and the correct answer in both is a measured error rate plus controls; a learner who knows one answers the other. | ccar-p-d6-30 |
| ccar-p-d6-08 | ccar-p-d6-13 | d6-08's stem (review production eval results, choose next prompt changes = iteration) is the same activity as d6-13's key C; same concept, same substance. | ccar-p-d6-31 |
| ccar-p-d7-04 | ccar-p-d7-01 | Both resolve to committing the project instructions file (plus settings) so every session and teammate starts from the same conventions; a learner who knows one answers the other. | ccar-p-d7-15 |

## Per-domain grader notes

### solution-design

Style match before adaptation: mean 2.7/5 over 34 questions; 18 of 34 map to a retired item.

The domain covers the retired set's concepts well and adds sound newer material (handoffs, shared state, over-decomposition, SLA design, input and output gates), but almost every item misses the retired form: options average 100-140 characters with trailing justification clauses, stems of the newer items run 350-430 characters, and most explanations list distractors without the 'Why not the others:' frame. In 13 items the key was the single shortest option. I tightened options to 55-90 characters and rebuilt every explanation in the target form; the twelve newer items with long stems were also trimmed (rewrite) without changing the concept or the key. Two duplicates: d1-22 repeats d1-18 (single augmented call) and d1-33 is a composite of d1-25 and d1-16; both are replaced with items on the two least-covered concepts (human-in-the-loop placement, chunking and contextual retrieval). Multi-agent-and-decomposition still carries 11 of 34 items; the maintainer may want to move a future addition elsewhere. d1-08 and d1-35 both test the feedback loop but from different angles (missing stage vs. controlled loop elements) and were kept.

### models-context

Style match before adaptation: mean 2.5/5 over 26 questions; 25 of 26 map to a retired item.

The domain covers the right concepts at about the right difficulty (mostly 3, three 4s, four honest 2s), but its form is off the retired bar in two ways: options average 95 characters in ids 01-13 and 127 in ids 14-26 (target 55-90), and stems in 14-26 run 280-400 characters; no explanation used the 'Why not the others:' form. Every item was therefore at least tightened; I classed an item as 'tighten' when the scenario is kept (stems in 14-26 were condensed, options and explanations rewritten) and as 'rewrite' when the scenario itself changed. The maintainer should look at this: ids 01, 03, 04, 05, 06, 07, 11 and 12 were close paraphrases of retired items cca-p-2-1 to 2-8 (11 and 12 reuse the retired stems almost word for word), which is a licensing risk given why the retired set is going; I gave all eight fresh scenarios on the same concepts with the same correct letters, and checked that no six-word sequence is shared with the retired set. One duplicate pair (08 and 22, both 'drifted copies -> one versioned shared source'); 08 is replaced by a model-selection item (the least-covered concept) with the same key B. Eight keys were the single shortest or longest option (05, 09, 11, 12, 13, 20, 24, 26) and are rebalanced. In 15 and 26 an implausible distractor was replaced with a plausible one. Facts checked against current docs: cache hierarchy tools->system->messages, 5-minute default and 1-hour TTL, tool_choice and thinking changes invalidating message blocks, Skills metadata-first loading, token-counting endpoint, structured outputs where prefill is unsupported.

### integration

Style match before adaptation: mean 2.6/5 over 38 questions; 36 of 38 map to a retired item.

The domain is well aligned with the retired set on concept and difficulty, but the form drifts: the first 18 items average about 95 characters per option and the newer 20-38 about 140, against the 55-90 target, and almost no explanation uses the 'Why not the others:' form. Several of the first items are close paraphrases of retired scenarios (01, 02, 03, 05, 06, 07, 08, 10, 15 mirror cca-p-3-1 to 3-8 and 3-12 with the numbers shifted; 18's stem is word-for-word the retired cca-p-3-11), so those stems were rewritten with fresh settings given the licensing reason for retiring the originals. Three duplicate pairs were found and 04, 11 and 19 replaced with new items on the two least-covered concepts (cost-and-latency-optimisation now 4 items, context-window-management now 2). 18 and 38 are mirror images (what favours progressive vs. what favours monolithic); they were kept as different angles but the maintainer may want to keep only one. Items 10, 15 and 26 remain difficulty 2 by honest estimate; the bank has more 2s than the retired set.

### evaluation-testing

Style match before adaptation: mean 3.1/5 over 32 questions; 28 of 32 map to a retired item.

Conceptually the domain tracks the retired set closely: current 01-09 mirror retired 4-1 to 4-9 almost one-to-one, and 08/09/10 cover the retired scenario-matching set on model mismatch, hallucination and prompt failure. The gap is form, not substance: options average about 105 characters (the newer items 110-130), and no explanation uses the 'Why not the others:' pattern, so every item is at least tightened; seven newer items also had stems over 300 characters and are rewritten with shorter stems, concept unchanged. One duplicate pair was found (01 and 13 both test 'define the metric set with agreed targets'); 13 is replaced by a long-context evaluation item under context-window-management, the domain's thinnest concept. 03 and 31 both resolve to 'rubric plus human calibration' from different angles (choosing a methodology vs. repairing a biased judge) and were kept as distinct; the maintainer may want to confirm. In 15 the implausible on-call-roster distractor was replaced; in 28 the claim about a specific context-window stop reason was softened.

### governance-risk

Style match before adaptation: mean 2.5/5 over 28 questions; 21 of 28 map to a retired item.

The domain covers the retired set's concepts well and at similar difficulty, but no item is already in the target form: ids 01-14 run 80-120 characters per option and their explanations list distractors without the 'Why not the others:' lead-in, while ids 15-28 run 130-160 characters per option with 250-440 character stems and per-option explanations over 110 characters. The biggest change is therefore option compression to 55-90 characters and explanation restructuring across every question. Ids 01-06, 12 and 13 are close paraphrases of retired cca-p-5-1 to 5-8 (same scenario, same option set in a different order); since the retired set is being removed for licensing reasons I gave those fresh scenarios (different industry and details) while keeping concept and key letter, and the maintainer should confirm that is the intended policy. One duplicate pair: d5-04 and d5-24 both test proxy bias answered by per-group fairness measurement; d5-24 is replaced by ccar-p-d5-29 on authorization-below-the-model, the domain's least-covered concept. d5-20 carries conceptId rag-chunking-and-retrieval, which looks misfiled for this domain (it is about knowledge cutoff); I left it unchanged as instructed.

### stakeholder-lifecycle

Style match before adaptation: mean 2.6/5 over 28 questions; 25 of 28 map to a retired item.

Concept coverage tracks the retired set well, but form does not: 26 of 28 questions have options over 90 characters (the second-hundred items average 125-150 per option) and the older explanations never use the 'Why not the others:' form, so the main change is option compression everywhere and explanation restructuring. The maintainer should look hard at d6-01 to d6-08, d6-11 and d6-12: their scenarios mirror retired cca-p-6-1 to 6-9 almost line for line (same '100% accurate' sponsor, same cheapest-model-for-regulatory-filings dilemma, same sub-second latency demand, same fading-sponsor technical report, same scope-creep list, same discovery-outputs pair). Given the licensing reason for retiring the originals, I rewrote the stems of d6-02 to d6-07, d6-11 and d6-12 with fresh scenarios on the same concepts, and reworded d6-15's distractors, which quoted the retired classification scenarios. Two replacements: d6-01 (a near-copy of cca-p-6-1 and the same substance as d6-22) becomes d6-30 on leading versus lagging value indicators, the least-covered concept here; d6-08 (same substance as the iteration key of d6-13) becomes d6-31 on proof-of-concept scoping. Difficulty estimates move d6-23 and d6-28 from 4 to 3 and d6-02 and d6-17 from 2 to 3; d6-07, d6-15 and d6-21 remain the only genuine 2s.

### developer-enablement

Style match before adaptation: mean 2.6/5 over 14 questions; 11 of 14 map to a retired item.

The domain is well targeted on the exam objectives and factually sound, but every item overshoots the retired form: options average 110 characters (target 55-90), the newer items (08-14) carry 300-420 character stems and 420-490 character explanations, and no explanation uses the 'Why not the others:' marker. The largest change is therefore a full tightening of options, per-option notes and explanations on all 13 kept items. Four items (01, 02, 03, 07) are near-paraphrases of retired cca-p-7-1 to 7-4 (same scenario, same framing, same distractor set); since the retired set is leaving for licensing reasons I rewrote their stems onto fresh scenarios while keeping concept and correct letter, and the maintainer should confirm that distance is sufficient. 01 and 04 both test 'commit the shared project instructions file', so 04 (difficulty 2) is replaced by a cost-attribution item on the under-covered observability concept. 14's explanation referred to a named 'bare mode'; I kept the mechanism generic rather than assert a product flag.

## Per-question grades

| Id | Nearest retired | Style | Difficulty | Action | Issues |
|---|---|---|---|---|---|
| ccar-p-d1-01 | cca-p-1-1 | 3 | 3 | tighten | options 92-110 characters with justifying clauses; key is the single shortest option; explanation lacks the Why not the others frame; diffic |
| ccar-p-d1-02 | cca-p-1-2 | 3 | 3 | tighten | options 97-104 characters; key is the single shortest option; explanation lacks the Why not the others frame |
| ccar-p-d1-03 | cca-p-1-8 | 3 | 3 | tighten | options 96-102 characters; explanation discusses distractors out of letter order without the frame |
| ccar-p-d1-04 | cca-p-1-3 | 4 | 3 | tighten | option B 97 characters; explanation 503 characters without the frame |
| ccar-p-d1-05 | cca-p-1-4 | 2 | 4 | rewrite | stem 373 characters; options 95-106 characters; explanation 633 characters, far over target |
| ccar-p-d1-06 | — | 3 | 4 | tighten | options 85-101 characters with justifying clauses; key is the single shortest option; explanation lacks the frame |
| ccar-p-d1-07 | cca-p-1-5 | 4 | 3 | tighten | explanation lacks the Why not the others frame; difficulty 2 understates; retired equivalent is 3 |
| ccar-p-d1-08 | cca-p-1-6 | 3 | 3 | tighten | options 94-102 characters; explanation lacks the frame |
| ccar-p-d1-09 | cca-p-1-7 | 3 | 2 | tighten | options 92-103 characters; explanation lacks the frame; difficulty 3 overstates; the retired equivalent is 2 |
| ccar-p-d1-10 | cca-p-1-8 | 3 | 3 | tighten | options 96-102 characters; explanation groups A and D and lacks the frame |
| ccar-p-d1-11 | — | 3 | 3 | tighten | options 96-110 characters; explanation lacks the frame; difficulty 4 overstates; only B is defensible once the rules are described as precis |
| ccar-p-d1-12 | cca-p-1-5 | 4 | 3 | tighten | explanation lacks the Why not the others frame; stem 332 characters, slightly long; key C was the single longest option |
| ccar-p-d1-13 | — | 3 | 3 | tighten | options 94-108 characters; key is the single shortest option; explanation lacks the frame; difficulty 4 overstates; B is the only engineered |
| ccar-p-d1-18 | cca-p-1-11-s1 | 3 | 3 | tighten | options 102-111 characters; explanation lacks the frame; difficulty 2 understates; the retired equivalent is 3 |
| ccar-p-d1-15 | cca-p-1-9 | 3 | 3 | tighten | both keys (51 and 67 characters) are markedly shorter than every distractor (91-98); explanation groups B, D and E without the frame |
| ccar-p-d1-16 | cca-p-1-10 | 4 | 3 | tighten | key B is the longest and key D the shortest option; explanation groups A and E without the frame |
| ccar-p-d1-17 | — | 4 | 3 | tighten | option B 92 characters; explanation groups B, C and D without the frame |
| ccar-p-d1-19 | — | 2 | 3 | rewrite | stem 430 characters; options 135-146 characters; explanation 515 characters without the frame; per-option explanations over 110 characters |
| ccar-p-d1-20 | — | 2 | 3 | rewrite | stem 367 characters; options 130-137 characters; explanation 456 characters without the frame |
| ccar-p-d1-21 | — | 2 | 3 | rewrite | stem 358 characters; options 114-127 characters; key is the single shortest option; distractor C (fix by hand on customer reports) is implau |
| ccar-p-d1-22 | cca-p-1-11-s1 | 2 | 2 | replace | duplicate of ccar-p-d1-18: same concept (single augmented LLM call) and same substance of the key; stem 310 characters; options 111-117 char |
| ccar-p-d1-23 | — | 2 | 3 | rewrite | stem 352 characters; options 114-134 characters; explanation 456 characters without the frame |
| ccar-p-d1-24 | — | 2 | 4 | rewrite | stem 407 characters; options 124-142 characters; explanation 445 characters without the frame |
| ccar-p-d1-25 | — | 2 | 3 | rewrite | stem 374 characters; options 97-117 characters; key is the single shortest option; explanation lacks the frame |
| ccar-p-d1-26 | — | 2 | 3 | rewrite | stem 378 characters; options 114-117 characters; explanation 454 characters without the frame |
| ccar-p-d1-27 | — | 2 | 4 | rewrite | stem 396 characters; options 116-121 characters; explanation 477 characters without the frame |
| ccar-p-d1-28 | — | 2 | 3 | rewrite | stem 400 characters; options 113-121 characters; explanation lacks the frame |
| ccar-p-d1-29 | cca-p-1-3 | 2 | 3 | rewrite | stem 374 characters; options 107-125 characters; explanation lacks the frame; difficulty 4 overstates; only D is defensible |
| ccar-p-d1-30 | — | 2 | 3 | rewrite | stem 390 characters; options 103-128 characters; key is the single shortest option; explanation lacks the frame |
| ccar-p-d1-31 | cca-p-1-5 | 3 | 3 | tighten | options 108-127 characters; explanation lacks the frame; difficulty 2 understates; distinguishing outcome from activity metrics is applied j |
| ccar-p-d1-32 | — | 3 | 3 | tighten | options 125-130 characters; stem 333 characters, slightly long; explanation lacks the frame |
| ccar-p-d1-33 | cca-p-1-10 | 2 | 3 | replace | duplicate: key A restates ccar-p-d1-25 and key D restates ccar-p-d1-16's key D; options 118-134 characters; key D is the single shortest opt |
| ccar-p-d1-34 | — | 3 | 3 | tighten | options 98-110 characters; key A is the single shortest option; explanation groups C and E without the frame |
| ccar-p-d1-35 | cca-p-1-6 | 3 | 3 | tighten | options 112-130 characters; key C is the single shortest option; explanation lacks the frame |
| ccar-p-d2-01 | cca-p-2-1 | 3 | 3 | rewrite | Stem and option set closely paraphrase retired cca-p-2-1 (same ticket-classification scenario, same four option ideas); licensing risk; Opti |
| ccar-p-d2-02 | cca-p-2-1 | 3 | 3 | tighten | Options 88-107 characters, above target; A carries a self-justifying clause; Explanation lacks the 'Why not the others:' form |
| ccar-p-d2-03 | cca-p-2-2 | 3 | 4 | rewrite | Stem closely paraphrases retired cca-p-2-2 (timestamp and ID at the top of a long static system prompt); licensing risk; Options 89-104 char |
| ccar-p-d2-04 | cca-p-2-3 | 3 | 3 | rewrite | Stem closely paraphrases retired cca-p-2-3 (platform-wide chain-of-thought, complex feature improved, extraction endpoint slower); licensing |
| ccar-p-d2-05 | cca-p-2-4 | 3 | 3 | rewrite | Stem closely paraphrases retired cca-p-2-4 (pricing rule buried mid-prompt, rewording failed); licensing risk; Key B is the single longest o |
| ccar-p-d2-06 | cca-p-2-5 | 3 | 3 | rewrite | Stem closely paraphrases retired cca-p-2-5 (house-format report, prose instructions nearly right); licensing risk; Explanation lacks the 'Wh |
| ccar-p-d2-07 | cca-p-2-6 | 3 | 3 | rewrite | Stem closely paraphrases retired cca-p-2-6 (full engineering-standards corpus in context, mid-context answers weaker); licensing risk; Optio |
| ccar-p-d2-08 | cca-p-2-7 | 3 | 3 | replace | Duplicate of ccar-p-d2-22: same concept (drifted copies fixed by one versioned shared source) and same substance of the key; Options 90-108  |
| ccar-p-d2-09 | cca-p-2-7 | 3 | 3 | tighten | Key A is the single shortest option (90 vs 95-108 characters); Options above target length; Explanation 423 characters and lacks the 'Why no |
| ccar-p-d2-10 | cca-p-2-8 | 3 | 3 | tighten | Stem is thin at 178 characters with no concrete business context; Options 84-104 characters, above target; D is implausible as written; Expl |
| ccar-p-d2-11 | cca-p-2-7 | 3 | 3 | rewrite | Stem is almost identical to retired cca-p-2-7; licensing risk; Key C is the single shortest option (78 vs 87-96 characters); Stem 184 charac |
| ccar-p-d2-12 | cca-p-2-8 | 3 | 3 | rewrite | Stem is identical to retired cca-p-2-8; licensing risk; Key B is the single shortest option (82 vs 89-102 characters); Stem 163 characters w |
| ccar-p-d2-13 | cca-p-2-3 | 3 | 2 | tighten | Key A is the single shortest option (76 vs 84-91 characters); Explanation 434 characters and lacks the 'Why not the others:' form; Related t |
| ccar-p-d2-14 | cca-p-2-3 | 2 | 3 | tighten | Stem 373 characters, above target; Options 116-128 characters, far above target; Explanation 509 characters and lacks the 'Why not the other |
| ccar-p-d2-15 | cca-p-2-6 | 2 | 3 | tighten | Stem 345 characters, above target; Options 125-128 characters, far above target; Distractor D (send ten times, keep the longest) is implausi |
| ccar-p-d2-16 | cca-p-2-2 | 2 | 3 | tighten | Stem 357 characters, above target; Options 121-129 characters with self-justifying 'because' clauses; Explanation 442 characters and lacks t |
| ccar-p-d2-17 | cca-p-2-2 | 2 | 4 | tighten | Stem 396 characters, above target; Options 129-130 characters, far above target; Explanation 485 characters and lacks the 'Why not the other |
| ccar-p-d2-18 | cca-p-2-7 | 2 | 3 | tighten | Stem 384 characters, above target; Options 126-131 characters with self-justifying 'since/because' clauses; Explanation 463 characters and l |
| ccar-p-d2-19 | cca-p-2-6 | 2 | 3 | tighten | Stem 397 characters, above target; Options 128-129 characters, far above target; Explanation lacks the 'Why not the others:' form |
| ccar-p-d2-20 | cca-p-2-1 | 2 | 3 | tighten | Stem 342 characters, above target; Key B is the single shortest option (127 vs 129-131 characters); Options far above target; A and D carry  |
| ccar-p-d2-21 | — | 2 | 2 | tighten | Stem 296 characters, above target; Options 123-127 characters with self-justifying clauses; absolute words (always, never, every) only in di |
| ccar-p-d2-22 | cca-p-2-7 | 2 | 3 | tighten | Stem 341 characters, above target; Options 128-130 characters, far above target; Explanation 478 characters and lacks the 'Why not the other |
| ccar-p-d2-23 | cca-p-2-8 | 2 | 2 | tighten | Stem 292 characters, above target; Options 122-133 characters with self-justifying clauses; Explanation 448 characters and lacks the 'Why no |
| ccar-p-d2-24 | cca-p-2-5 | 2 | 3 | tighten | Stem 400 characters, above target; Key A is the single shortest option (119 vs 126-129 characters); Options far above target; Explanation la |
| ccar-p-d2-25 | cca-p-2-2 | 2 | 4 | tighten | Options 120-137 characters with self-justifying clauses; Explanation 526 characters, above target |
| ccar-p-d2-26 | cca-p-2-5 | 2 | 3 | tighten | Key C is the single shortest option (124 vs 130-132 characters); Options far above target with self-justifying clauses; Distractor E ('let e |
| ccar-p-d3-01 | cca-p-3-1 | 3 | 3 | rewrite | scenario closely paraphrases retired cca-p-3-1 (same shape, numbers shifted); options 87-110 characters; explanation lacks the 'Why not the  |
| ccar-p-d3-02 | cca-p-3-2 | 3 | 3 | rewrite | scenario closely paraphrases retired cca-p-3-2; key is the shortest option; options 87-100 characters; explanation lacks the 'Why not the ot |
| ccar-p-d3-03 | cca-p-3-3 | 3 | 4 | rewrite | scenario closely paraphrases retired cca-p-3-3; stem 300 characters; options 92-116 characters; explanation lacks the 'Why not the others:'  |
| ccar-p-d3-04 | cca-p-3-3 | 3 | 3 | replace | duplicate of ccar-p-d3-14 (same least-privilege lesson, same distractor pattern); key is the shortest option; explanation lacks the 'Why not |
| ccar-p-d3-05 | cca-p-3-4 | 3 | 3 | rewrite | scenario closely paraphrases retired cca-p-3-4; options 96-102 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-06 | cca-p-3-5 | 3 | 3 | rewrite | scenario closely paraphrases retired cca-p-3-5; options 91-103 characters with self-justifying clauses; explanation lacks the 'Why not the o |
| ccar-p-d3-07 | cca-p-3-6 | 3 | 4 | rewrite | scenario closely paraphrases retired cca-p-3-6 with numbers shifted; key is the shortest option; options 92-108 characters; explanation lack |
| ccar-p-d3-08 | cca-p-3-7 | 3 | 3 | rewrite | scenario closely paraphrases retired cca-p-3-7; options 85-122 characters, uneven; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-09 | cca-p-3-8 | 4 | 3 | tighten | options 94-105 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-10 | cca-p-3-12-s5 | 3 | 2 | rewrite | scenario is nearly verbatim from retired cca-p-3-12-s5; options 85-110 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-11 | cca-p-3-11 | 2 | 3 | replace | duplicate of ccar-p-d3-18 (same lesson: large sparsely used set favours progressive discovery); stem 312 characters with 'and why' double qu |
| ccar-p-d3-12 | cca-p-3-9 | 3 | 3 | tighten | key is the shortest option; options 85-103 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-13 | cca-p-3-10 | 3 | 3 | tighten | key is the shortest option; options 93-103 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-14 | cca-p-3-3 | 3 | 4 | tighten | options 88-108 characters with self-justifying clauses; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-15 | cca-p-3-12-s4 | 3 | 2 | rewrite | scenario is nearly verbatim from retired cca-p-3-12-s4; key is the shortest option; explanation 233 characters, too short, lacks the 'Why no |
| ccar-p-d3-16 | cca-p-3-5 | 3 | 3 | tighten | options 88-97 characters; explanation 274 characters, lacks the 'Why not the others:' form |
| ccar-p-d3-17 | cca-p-3-3 | 3 | 3 | tighten | keys are the longest and shortest options; option A 109 characters; explanation groups the distractors instead of naming each |
| ccar-p-d3-18 | cca-p-3-11 | 4 | 3 | rewrite | stem is word-for-word the retired cca-p-3-11 prompt; option D is the longest; keys C and D sit at the top of the length range; explanation l |
| ccar-p-d3-19 | cca-p-3-7 | 3 | 3 | replace | duplicate of ccar-p-d3-33 (correlation ID plus per-step records is the same answer as trace ID plus spans); key D is the shortest option; ex |
| ccar-p-d3-20 | cca-p-3-12-s1 | 2 | 3 | rewrite | stem 384 characters; options 146-159 characters with self-justifying clauses; explanation 523 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-21 | — | 2 | 3 | rewrite | stem 393 characters; options 147-151 characters with self-justifying clauses; explanation 553 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-22 | cca-p-3-3 | 2 | 3 | rewrite | stem 338 characters; options 145-148 characters with self-justifying clauses; explanation 482 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-23 | cca-p-3-3 | 2 | 4 | rewrite | stem 310 characters; options 142-148 characters with self-justifying clauses; explanation 466 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-24 | cca-p-3-3 | 2 | 3 | rewrite | stem 334 characters; options 127-147 characters with self-justifying clauses; explanation 470 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-25 | cca-p-3-2 | 2 | 3 | rewrite | stem 305 characters; options 143-147 characters with self-justifying clauses; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-26 | cca-p-3-10 | 2 | 2 | tighten | options 119-134 characters with self-justifying clauses; key is the shortest option; explanation 439 characters, lacks the 'Why not the othe |
| ccar-p-d3-27 | cca-p-3-4 | 2 | 3 | rewrite | stem 306 characters; options 139-140 characters with self-justifying clauses; explanation 461 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-28 | cca-p-3-9 | 2 | 3 | rewrite | stem 356 characters; options 139-151 characters with self-justifying clauses; key is the shortest option; explanation lacks the 'Why not the |
| ccar-p-d3-29 | cca-p-3-9 | 2 | 3 | rewrite | stem 322 characters; options 129-140 characters with self-justifying clauses; explanation 465 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-30 | cca-p-3-5 | 2 | 3 | rewrite | stem 336 characters; options 130-144 characters with self-justifying clauses; key is the shortest option; explanation lacks the 'Why not the |
| ccar-p-d3-31 | cca-p-3-12-s2 | 2 | 3 | rewrite | stem 372 characters; options 128-147 characters with self-justifying clauses; key is the shortest option; explanation 493 characters, lacks  |
| ccar-p-d3-32 | — | 2 | 3 | rewrite | stem 320 characters; options 141-153 characters with self-justifying clauses; explanation 438 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-33 | cca-p-3-7 | 2 | 3 | rewrite | stem 360 characters; options 133-142 characters with self-justifying clauses; explanation 490 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-34 | cca-p-3-6 | 2 | 4 | rewrite | stem 404 characters; options 145-149 characters with self-justifying clauses; explanation 464 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-35 | cca-p-3-11 | 2 | 3 | rewrite | stem 353 characters; options 97-115 characters; key E is the shortest option; explanation 438 characters, lacks the 'Why not the others:' fo |
| ccar-p-d3-36 | cca-p-3-7 | 2 | 3 | rewrite | stem 354 characters; options 112-119 characters with self-justifying clauses; key D is the longest option; explanation 451 characters, lacks |
| ccar-p-d3-37 | cca-p-3-4 | 3 | 3 | rewrite | stem 313 characters; options 92-109 characters; key C is the longest option; explanation lacks the 'Why not the others:' form |
| ccar-p-d3-38 | cca-p-3-11 | 3 | 4 | tighten | options 101-112 characters; key C is the longest option; explanation 446 characters, lacks the 'Why not the others:' form; mirror image of c |
| ccar-p-d4-01 | cca-p-4-1 | 3 | 3 | tighten | options 88-103 characters; key ties for longest option; explanation lacks the 'Why not the others:' form; difficulty 2 understates an applie |
| ccar-p-d4-02 | cca-p-4-2 | 3 | 3 | tighten | options 97-118 characters; key is the shortest option; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-03 | cca-p-4-3 | 3 | 3 | tighten | key is the shortest option; options up to 107 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-04 | cca-p-4-4 | 3 | 3 | tighten | options 90-98 characters; explanation lacks the 'Why not the others:' form and discusses distractors out of order |
| ccar-p-d4-05 | cca-p-4-5 | 3 | 3 | tighten | key is the shortest option; options up to 102 characters; absolute 'always' only in distractor B; explanation lacks the 'Why not the others: |
| ccar-p-d4-06 | cca-p-4-6 | 3 | 3 | tighten | options 87-107 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-07 | cca-p-4-7 | 4 | 3 | tighten | option A is 103 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-08 | cca-p-4-10-s1 | 3 | 3 | tighten | option A is 100 characters and not parallel with the others; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-09 | cca-p-4-10-s5 | 3 | 3 | tighten | key is the shortest option; option B is 114 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-10 | cca-p-4-10-s2 | 3 | 3 | tighten | options 90-107 characters; explanation is 287 characters and lacks the 'Why not the others:' form |
| ccar-p-d4-11 | cca-p-4-5 | 4 | 4 | tighten | stem is 300 characters; options A and B slightly over 90 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-12 | cca-p-4-5 | 3 | 3 | tighten | key is the longest option; options 91-99 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-13 | cca-p-4-1 | 3 | 2 | replace | duplicate of ccar-p-d4-01: same concept and same substance of key; key is the longest option; recall item with no applied reasoning; stem is |
| ccar-p-d4-14 | cca-p-4-8 | 3 | 4 | tighten | key C is the longest option (116) and key B the shortest; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-15 | cca-p-4-9 | 4 | 4 | tighten | key E is the single longest option; distractor C (on-call roster) is implausible; explanation is 417 characters and lacks the 'Why not the o |
| ccar-p-d4-16 | — | 3 | 3 | tighten | key B is the longest option; distractors C and D are implausible (send twice, replace with 'done'); explanation lacks the 'Why not the other |
| ccar-p-d4-17 | cca-p-4-3 | 3 | 2 | tighten | key is the shortest option; options 96-117 characters; stem is 285 characters; explanation is 429 characters and lacks the 'Why not the othe |
| ccar-p-d4-18 | cca-p-4-3 | 3 | 3 | rewrite | stem is 314 characters; options 110-114 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-19 | — | 3 | 4 | rewrite | stem is 326 characters; options 107-116 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-20 | cca-p-4-6 | 3 | 3 | tighten | options 119-122 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-21 | — | 3 | 4 | rewrite | stem is 357 characters; options 98-124 characters; key is the shortest option; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-22 | cca-p-4-7 | 3 | 3 | tighten | options 103-107 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-23 | cca-p-4-4 | 3 | 3 | tighten | stem is 295 characters; options 110-117 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-24 | cca-p-4-8 | 3 | 3 | tighten | stem is 284 characters; options 110-115 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-25 | cca-p-4-8 | 3 | 3 | tighten | stem is 296 characters; options 109-120 characters; key is the shortest option; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-26 | — | 3 | 2 | tighten | stem is 292 characters; options 105-110 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-27 | cca-p-4-5 | 3 | 3 | rewrite | stem is 318 characters; options 104-112 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-28 | cca-p-4-9 | 3 | 3 | rewrite | stem is 336 characters; options all exactly 108 characters; explanation is 499 characters and lacks the 'Why not the others:' form; distract |
| ccar-p-d4-29 | cca-p-4-2 | 3 | 3 | rewrite | stem is 327 characters; options 114-122 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-30 | cca-p-4-7 | 3 | 3 | tighten | stem is 288 characters; options 109-121 characters; key E is the shortest option; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-31 | cca-p-4-3 | 3 | 4 | rewrite | stem is 310 characters; options 114-131 characters; key A is the longest option; explanation lacks the 'Why not the others:' form |
| ccar-p-d4-32 | cca-p-4-4 | 3 | 3 | tighten | options 101-107 characters; explanation lacks the 'Why not the others:' form |
| ccar-p-d5-01 | cca-p-5-1 | 3 | 3 | rewrite | Close paraphrase of retired cca-p-5-1 (same scenario and option set); Key D is the single longest option (101 chars); Options A, C, D over 9 |
| ccar-p-d5-02 | cca-p-5-2 | 3 | 3 | rewrite | Close paraphrase of retired cca-p-5-2; Key C is the single longest option (119 chars); All options over 90 chars; Explanation lacks 'Why not |
| ccar-p-d5-03 | cca-p-5-3 | 3 | 3 | rewrite | Close paraphrase of retired cca-p-5-3; Key B is the single longest option, 54% over the mean distractor length; Explanation lacks 'Why not t |
| ccar-p-d5-04 | cca-p-5-4 | 3 | 4 | rewrite | Close paraphrase of retired cca-p-5-4; Key C is the single longest option (111 chars); Options A, C, D over 90 chars; Explanation lacks 'Why |
| ccar-p-d5-05 | cca-p-5-5 | 3 | 4 | rewrite | Close paraphrase of retired cca-p-5-5; All options over 90 chars; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-06 | cca-p-5-6 | 3 | 3 | rewrite | Close paraphrase of retired cca-p-5-6; Options A, B, D over 90 chars with 'so that' justifying clauses; Explanation lacks 'Why not the other |
| ccar-p-d5-07 | cca-p-5-9-s1 | 3 | 3 | tighten | Options C and D over 90 chars; Explanation lacks 'Why not the others:' lead-in and discusses distractors out of order |
| ccar-p-d5-08 | cca-p-5-9-s2 | 3 | 3 | tighten | Key C is the single shortest option; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-09 | cca-p-5-9-s3 | 3 | 3 | tighten | Key D is the single longest option (101 chars); All options over 90 chars; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-10 | — | 3 | 3 | tighten | All options over 90 chars; Distractors C and D are weak (self-evidently wrong); Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-11 | cca-p-5-9-s2 | 3 | 2 | tighten | Options C and D over 90 chars; A and B much shorter than C and D; Distractor D uses absolutes ('at all', 'any jurisdiction') found in no oth |
| ccar-p-d5-12 | cca-p-5-7 | 3 | 3 | rewrite | Close paraphrase of retired cca-p-5-7; Key B is the single shortest option (-30%) and key D the single longest (+48%); Explanation under 300 |
| ccar-p-d5-13 | cca-p-5-8 | 3 | 4 | rewrite | Close paraphrase of retired cca-p-5-8; Key C is the single shortest option (-17%); Options A, B, D over 90 chars; Explanation lacks 'Why not |
| ccar-p-d5-14 | cca-p-5-5 | 3 | 2 | tighten | Recognition item rather than applied judgement; Key D is the single longest option (93 chars); Explanation lacks 'Why not the others:' lead- |
| ccar-p-d5-15 | cca-p-5-2 | 2 | 3 | rewrite | Prompt 440 chars; Options 135-155 chars with justifying clauses; Key B is the single shortest option; Per-option explanations over 110 chars |
| ccar-p-d5-16 | — | 2 | 3 | rewrite | Prompt 342 chars; Options 147-155 chars with justifying clauses; Per-option explanations over 110 chars; Explanation 439 chars and lacks 'Wh |
| ccar-p-d5-17 | cca-p-5-1 | 2 | 3 | tighten | Options 144-156 chars with justifying clauses; Per-option explanations over 110 chars; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-18 | — | 2 | 4 | rewrite | Prompt 309 chars; Options 148-154 chars with justifying clauses; Per-option explanations over 110 chars; Explanation 440 chars and lacks 'Wh |
| ccar-p-d5-19 | — | 2 | 3 | tighten | Options 136-153 chars with justifying clauses; Key B is the single shortest option; Per-option explanation B over 110 chars; Explanation 426 |
| ccar-p-d5-20 | — | 2 | 2 | tighten | Options 130-143 chars with justifying clauses; conceptId rag-chunking-and-retrieval looks misfiled for this domain (item is about knowledge  |
| ccar-p-d5-21 | cca-p-5-9-s4 | 2 | 3 | rewrite | Prompt 317 chars; Options 139-141 chars with justifying clauses; Per-option explanations A and D over 110 chars; Explanation lacks 'Why not  |
| ccar-p-d5-22 | cca-p-5-8 | 2 | 3 | tighten | Options 129-133 chars with justifying clauses; Explanation 438 chars and lacks 'Why not the others:' lead-in |
| ccar-p-d5-23 | — | 2 | 2 | tighten | Options 135-142 chars with justifying clauses; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-24 | cca-p-5-4 | 2 | 3 | replace | Duplicate of ccar-p-d5-04: same concept (proxy bias) and same answer substance (per-group outcome measurement with fairness tests); Options  |
| ccar-p-d5-25 | — | 2 | 4 | rewrite | Prompt 293 chars; Options 142-147 chars with justifying clauses; Explanation 429 chars and lacks 'Why not the others:' lead-in |
| ccar-p-d5-26 | cca-p-5-3 | 2 | 3 | tighten | Options 125-144 chars with justifying clauses; Key A is the single shortest option; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-27 | cca-p-5-9-s4 | 2 | 3 | tighten | Options 130-160 chars with justifying clauses; Key B is the single shortest option; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d5-28 | cca-p-5-8 | 2 | 3 | rewrite | Prompt 364 chars; Options 132-151 chars with justifying clauses; Explanation lacks 'Why not the others:' lead-in |
| ccar-p-d6-01 | cca-p-6-1 | 3 | 3 | replace | stem and answer mirror retired cca-p-6-1 almost exactly (same '100% accurate' sponsor demand, same resolution); options 94-122 characters, C |
| ccar-p-d6-02 | cca-p-6-2 | 3 | 3 | rewrite | scenario mirrors retired cca-p-6-2 ('we need a chatbot' opener, run discovery first); options 83-101 characters; explanation does not use th |
| ccar-p-d6-03 | cca-p-6-3 | 3 | 4 | rewrite | scenario mirrors retired cca-p-6-3 (finance chief, cheapest model, regulatory filings); options 101-119 characters, B and C carry self-justi |
| ccar-p-d6-04 | cca-p-6-4 | 3 | 3 | rewrite | scenario mirrors retired cca-p-6-4 (sub-second demand, three-second pipeline, streaming and SLA); options 92-107 characters, B and C carry s |
| ccar-p-d6-05 | cca-p-6-5 | 3 | 3 | rewrite | scenario mirrors retired cca-p-6-5 (consultancy handoff, decision records and runbooks); options 89-114 characters; explanation groups the d |
| ccar-p-d6-06 | cca-p-6-6 | 3 | 3 | rewrite | scenario mirrors retired cca-p-6-6 (fading sponsor, fortnightly technical-only report); options 93-122 characters, B carries a self-justifyi |
| ccar-p-d6-07 | cca-p-6-9-s1 | 4 | 2 | rewrite | stem paraphrases retired cca-p-6-9-s1 (interviewing frontline staff about today's process and lost time); explanation lacks the 'Why not the |
| ccar-p-d6-08 | cca-p-6-9-s4 | 4 | 2 | replace | stem paraphrases retired cca-p-6-9-s4 (reviewing production evaluation trends, prioritising prompt improvements); same substance as ccar-p-d |
| ccar-p-d6-09 | cca-p-6-3 | 3 | 3 | tighten | options 96-116 characters; key C is the single longest option; explanation does not use the 'Why not the others:' form |
| ccar-p-d6-10 | cca-p-6-5 | 3 | 3 | tighten | options 83-113 characters; key B is the single longest option; explanation does not use the 'Why not the others:' form |
| ccar-p-d6-11 | cca-p-6-7 | 3 | 3 | rewrite | stem mirrors retired cca-p-6-7 (closing discovery, which TWO outputs before design); key E is the single longest option (104 characters); ex |
| ccar-p-d6-12 | cca-p-6-8 | 3 | 3 | rewrite | stem mirrors retired cca-p-6-8 (mid-build requests: new data sources, user groups, output formats); options 92-105 characters, A and E carry |
| ccar-p-d6-13 | cca-p-6-9-s4 | 3 | 3 | tighten | options 92-105 characters; key C is the single longest option; explanation is short (194 characters) and does not use the 'Why not the other |
| ccar-p-d6-15 | cca-p-6-9-s2 | 4 | 2 | tighten | distractors B, D and E quote the retired cca-p-6-9 scenarios almost verbatim; key C is the single shortest option (65 characters); explanati |
| ccar-p-d6-16 | cca-p-6-2 | 2 | 3 | tighten | options 133-145 characters with self-justifying clauses; stem is 277 characters, at the top of the target range; explanation 444 characters  |
| ccar-p-d6-17 | cca-p-6-7 | 2 | 3 | tighten | options 136-139 characters with self-justifying clauses; explanation groups B and D and does not use the 'Why not the others:' form; difficu |
| ccar-p-d6-18 | cca-p-6-7 | 2 | 3 | tighten | options 127-135 characters with self-justifying clauses; explanation groups A and C and does not use the 'Why not the others:' form |
| ccar-p-d6-19 | — | 2 | 3 | tighten | options 125-138 characters with self-justifying clauses; key B is the single shortest option; explanation does not use the 'Why not the othe |
| ccar-p-d6-20 | cca-p-6-3 | 2 | 3 | tighten | options 133-147 characters with self-justifying clauses; explanation 422 characters and does not use the 'Why not the others:' form |
| ccar-p-d6-21 | cca-p-6-5 | 2 | 2 | tighten | options 119-134 characters with self-justifying clauses; key C is the single longest option; explanation does not use the 'Why not the other |
| ccar-p-d6-22 | cca-p-6-1 | 2 | 3 | tighten | options 125-137 characters with self-justifying clauses; explanation 440 characters and does not use the 'Why not the others:' form |
| ccar-p-d6-23 | cca-p-6-4 | 2 | 3 | tighten | options 126-132 characters with self-justifying clauses; explanation does not use the 'Why not the others:' form; difficulty 4 overstates it |
| ccar-p-d6-24 | cca-p-6-9-s4 | 2 | 3 | tighten | options 124-153 characters with self-justifying clauses; explanation does not use the 'Why not the others:' form |
| ccar-p-d6-25 | cca-p-6-3 | 2 | 3 | tighten | options 133-135 characters with self-justifying clauses; explanation groups A and B and does not use the 'Why not the others:' form |
| ccar-p-d6-26 | — | 2 | 3 | tighten | options 122-143 characters with self-justifying clauses; explanation does not use the 'Why not the others:' form; conceptId model-selection  |
| ccar-p-d6-27 | cca-p-6-5 | 2 | 3 | tighten | options 129-137 characters with self-justifying clauses; explanation does not use the 'Why not the others:' form |
| ccar-p-d6-28 | cca-p-6-5 | 2 | 3 | tighten | options 130-153 characters with self-justifying clauses; explanation does not use the 'Why not the others:' form; difficulty 4 overstates it |
| ccar-p-d6-29 | — | 2 | 3 | tighten | options 125-137 characters with self-justifying clauses; explanation does not use the 'Why not the others:' form |
| ccar-p-d7-01 | cca-p-7-1 | 3 | 3 | rewrite | near-paraphrase of retired cca-p-7-1 (same rollout scenario, same distractor set); options 97-124 characters, well above target; explanation |
| ccar-p-d7-02 | cca-p-7-2 | 3 | 3 | rewrite | near-paraphrase of retired cca-p-7-2 (same self-review scenario and distractors); options 99-121 characters; key A carries a self-justifying |
| ccar-p-d7-03 | cca-p-7-3 | 3 | 3 | rewrite | near-paraphrase of retired cca-p-7-3 (same on-call scenario and distractor set); options 98-106 characters with self-justifying 'since ...'  |
| ccar-p-d7-04 | cca-p-7-1 | 3 | 2 | replace | duplicate of d7-01: same correct substance (commit the project instructions file); difficulty 2; distractors B, C and D are not credible to  |
| ccar-p-d7-05 | cca-p-7-4 | 3 | 3 | tighten | options 93-108 characters with 'so that' justifying clauses on A and D; explanation is 254 characters and lacks the 'Why not the others:' ma |
| ccar-p-d7-06 | — | 3 | 3 | tighten | options 100-117 characters; A and D carry justifying clauses; explanation 290 characters, lacks the 'Why not the others:' marker |
| ccar-p-d7-07 | cca-p-7-4 | 4 | 3 | rewrite | near-paraphrase of retired cca-p-7-4 (same platform-team scaling stem); explanation 254 characters, lacks the 'Why not the others:' marker |
| ccar-p-d7-08 | cca-p-7-4 | 2 | 3 | tighten | stem 333 characters; options 115-127 characters; key D is the single shortest option; per-option explanations 123-147 characters; explanatio |
| ccar-p-d7-09 | — | 2 | 3 | tighten | stem 329 characters; options 116-120 characters; per-option explanations 111-133 characters; explanation 422 characters, lacks the 'Why not  |
| ccar-p-d7-10 | cca-p-7-2 | 2 | 4 | tighten | stem 306 characters; options 122-131 characters; per-option explanations 131-146 characters; explanation 454 characters, lacks the 'Why not  |
| ccar-p-d7-11 | cca-p-7-1 | 2 | 3 | rewrite | stem 366 characters; options 116-125 characters with justifying clauses on A, B and D; per-option explanations 116-131 characters; explanati |
| ccar-p-d7-12 | cca-p-7-3 | 2 | 3 | tighten | stem 315 characters; options 124-130 characters; per-option explanations 118-148 characters; explanation 450 characters, lacks the 'Why not  |
| ccar-p-d7-13 | — | 2 | 3 | tighten | options 117-131 characters; per-option explanations 113-136 characters; explanation 421 characters, lacks the 'Why not the others:' marker;  |
| ccar-p-d7-14 | cca-p-7-4 | 2 | 3 | rewrite | stem 420 characters; options 122-132 characters; explanation 480 characters, lacks the 'Why not the others:' marker; explanation asserts a n |
