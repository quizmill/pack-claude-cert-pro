# Coverage map: removed bank → current bank

The bank this pack carried until October 2026 (83 questions, see
[provenance.md](provenance.md)) was removed for licensing reasons, but it
was a reasonable proxy for what the exam asks. This map records, item by
item, which question in the current bank tests the same concept, so the
replacement is at least as complete as what it replaced. Scenarios,
options and rationales in the current bank are original; what is matched
here is the concept under test.

Removed ids are `cca-p-<domain>-<n>`; scenario-matching sets were stored
as five sub-items `-s1`…`-s5`. Current ids are `ccar-p-d<domain>-<nn>`.

## Format

| | Removed bank | Current bank |
|---|---|---|
| Items | 63 (44 single-answer, 14 select-two, 5 scenario-matching sets of 5) | 100 (80 single-answer, 20 select-two) |
| Domain split | 15 / 8 / 16 / 14 / 13 / 13 / 4 by sub-item (not blueprint-weighted) | 17 / 13 / 19 / 16 / 14 / 14 / 7, exactly the blueprint |
| Scenario matching | 5 sets, each a list of scenarios classified against 3–4 shared labels | Each scenario is a stand-alone question with its own distractors; the engine has no matching item type |
| Mock exam | n/a | The manifest's `exam` block draws 63 items weighted by domain |

## Domain 1 — Solution Design & Architecture

| Removed | Concept | Current | Note |
|---|---|---|---|
| 1-1 | Fixed workflow for stable, repeated steps | d1-01 | |
| 1-2 | Autonomous agent when the path emerges mid-task | d1-02 | |
| 1-3 | Decompose an overloaded single prompt into sequenced steps | d1-04 | |
| 1-4 | Orchestrator in sequence: ordered audit trail, halt on exception | d1-05 | Stem now states the ordered record and the halt |
| 1-5 | Choosing the first use case on value, data and risk | d1-07 | |
| 1-6 | Feedback loop closes the input–processing–output cycle | d1-08 | |
| 1-7 | Retrieval for daily-changing reference data | d1-09 | |
| 1-8 | Split an overloaded agent behind a router | d1-10 | |
| 1-9 (select two) | Properties that favour a workflow | d1-15 | |
| 1-10 (select two) | Properties that warrant multiple agents | d1-16 | |
| 1-11 s1, s5 | Single augmented LLM call | d1-18 | Added in this pass |
| 1-11 s2 | Fixed workflow | d1-01 | |
| 1-11 s3 | Autonomous agent | d1-02 | |
| 1-11 s4 | Multi-agent system | d1-16 | |
| — | Routing; evaluator-optimizer; orchestrator-workers cost; agent stopping conditions and idempotent tools; business-value pillars; translating the business problem | d1-03, d1-11, d1-06, d1-13, d1-12, d1-17 | Objectives in the exam guide the removed bank did not reach |

## Domain 2 — Claude Models, Prompting & Context Engineering

| Removed | Concept | Current | Note |
|---|---|---|---|
| 2-1 | Smallest model that meets the accuracy target | d2-01 | |
| 2-2 | Prompt caching needs a stable prefix | d2-03 | |
| 2-3 | Chain-of-thought selectively, by task | d2-04 | |
| 2-4 | Critical rule buried in reference content | d2-05 | |
| 2-5 | Few-shot examples for exact format | d2-06 | |
| 2-6 | Retrieve relevant sections instead of the whole corpus | d2-07 | |
| 2-7 (select two) | Cost: cacheable prefix, on-demand instructions | d2-11, d2-09 | Caching + model tiering in d2-11; on-demand Skills in d2-09 |
| 2-8 (select two) | Instruction adherence: structure and explicit cases | d2-12 | |
| — | Evidence-based model choice at low volume; modular shared prompts; guardrail prompt design; zero-shot first | d2-02, d2-08, d2-10, d2-13 | Guide objectives not in the removed bank |

## Domain 3 — Integration

| Removed | Concept | Current | Note |
|---|---|---|---|
| 3-1 | MCP for many systems, many consumers, frequent churn | d3-01 | |
| 3-2 | Capability bloat: prune and scope tools | d3-02 | |
| 3-3 | Authorization enforced below the model | d3-03 | |
| 3-4 | Structure-aware chunking | d3-05 | |
| 3-5 | Hybrid retrieval for exact identifiers | d3-06 | |
| 3-6 | Accuracy vs latency decided against the SLA | d3-07 | |
| 3-7 | Observability at scale: traces, sampling, capture on error | d3-08 | |
| 3-8 | Agent-to-agent across an organisational boundary | d3-09 | |
| 3-9 (select two) | Stale index after refresh: validated rebuild, versioning | d3-12 | Single-answer in the current bank |
| 3-10 (select two) | Tool-selection errors: distinct descriptions, consolidate | d3-13 | Single-answer in the current bank |
| 3-11 (select two) | Progressive discovery vs monolithic context | d3-18, d3-11 | |
| 3-12 s1, s4 | MCP server | d3-01, d3-15 | |
| 3-12 s2, s5 | Direct API integration | d3-10 | |
| 3-12 s3 | Agent-to-agent protocol | d3-09 | |
| — | Least-privilege tool scoping; narrow tool interfaces; retrieval per query pattern; authentication gaps; what tracing needs | d3-04, d3-14, d3-16, d3-17, d3-19 | Guide objectives not in the removed bank |

## Domain 4 — Evaluation, Testing & Optimization

| Removed | Concept | Current | Note |
|---|---|---|---|
| 4-1 | Define task-specific metrics and thresholds first | d4-01 | |
| 4-2 | Evaluation set: real queries plus constructed edge cases | d4-02 | |
| 4-3 | Model-as-judge with human calibration | d4-03 | |
| 4-4 | A/B test before replacing a prompt | d4-04 | |
| 4-5 | Cost reduction from trace-level analysis | d4-05 | |
| 4-6 | Model migration: full suite, then canary | d4-06 | |
| 4-7 | Leading indicators in RAG telemetry | d4-07 | |
| 4-8 (select two) | Regulated evaluation: expert golden set plus adversarial cases | d4-14 | Adversarial component restored in this pass |
| 4-9 (select two) | Diagnosing degradation: traces plus input drift | d4-15 | Input-drift source restored in this pass |
| 4-10 s1, s4 | Model mismatch | d4-08 | |
| 4-10 s2 | Prompt failure (conflicting instructions) | d4-10 | |
| 4-10 s3, s5 | Hallucination | d4-09 | |
| — | Latency from the critical path; batch processing; the five metric dimensions; context management on long sessions | d4-11, d4-12, d4-13, d4-16 | Guide objectives not in the removed bank |

## Domain 5 — Governance, Safety & Risk Management

| Removed | Concept | Current | Note |
|---|---|---|---|
| 5-1 | Human-in-the-loop gate before irreversible actions | d5-01 | |
| 5-2 | GDPR: data minimisation before export | d5-02 | |
| 5-3 | Health-data compliance decided at architecture time | d5-03 | |
| 5-4 | Proxy variables and fairness evaluation | d5-04 | |
| 5-5 | Retrieved content is untrusted data | d5-05 | |
| 5-6 | Transparency: disclose, state limits, route to a human | d5-06 | |
| 5-7 (select two) | No incorrect commitment reaches the customer | d5-12 | |
| 5-8 (select two) | Injection hardening: delimit plus least privilege | d5-13 | |
| 5-9 s1, s4 | Preventative guardrail | d5-07 | |
| 5-9 s2 | Human-in-the-loop validation | d5-08 | |
| 5-9 s3 | Monitoring and audit (reconstruction) | d5-09 | |
| 5-9 s5 | Monitoring and audit (fleet trends) | d4-07, d6-13 | Tested as monitoring in the evaluation and lifecycle domains |
| — | FedRAMP boundary; confident-error limitation; LLM failure modes on a risk register | d5-10, d5-11, d5-14 | Guide objectives not in the removed bank |

## Domain 6 — Stakeholder Communication & Lifecycle Management

| Removed | Concept | Current | Note |
|---|---|---|---|
| 6-1 | "100% accurate" → measurable criteria and controls | d6-01 | |
| 6-2 | Discovery before architecture | d6-02 | |
| 6-3 | Cheapest-model instruction vs evidence | d6-03 | |
| 6-4 | Sub-second demand vs pipeline reality | d6-04 | |
| 6-5 | Handoff artefacts | d6-05 | |
| 6-6 | Report business outcomes, not only technical metrics | d6-06 | |
| 6-7 (select two) | Discovery outputs before design | d6-11 | |
| 6-8 (select two) | Change management mid-build | d6-12 | |
| 6-9 s1, s5 | Discovery phase | d6-07 | |
| 6-9 s2 | Design phase | d6-15 | Added in this pass (select two: design-phase activities) |
| 6-9 s3 | Handoff phase | d6-15, d6-05 | |
| 6-9 s4 | Monitoring and iteration | d6-08, d6-13 | |
| — | Communicating a decision in the audience's terms; implementation guidance | d6-09, d6-10 | Guide objectives not in the removed bank |

## Domain 7 — Developer Productivity & Operational Enablement

| Removed | Concept | Current | Note |
|---|---|---|---|
| 7-1 | Shared, versioned team configuration | d7-01 | |
| 7-2 | Independent review context, human on the merge | d7-02 | |
| 7-3 | Traces before changing the prompt | d7-03 | |
| 7-4 (select two) | Scale safely: shared standards plus execution limits | d7-07 | |
| — | Project instructions file; branch-and-review workflow; robust structured output | d7-04, d7-05, d7-06 | Guide objectives not in the removed bank |

## Result

All 63 removed items (every scenario of the five matching sets included)
have a current question testing the same concept. Two concepts had no
item of their own before this pass and were added by replacing two
near-duplicates (a second feedback-loop definition, a second SLA item), so
the blueprint counts are unchanged; two select-two items had lost a
component of the removed item's key and have it back. 73 of the 100
current questions map to a removed item; the remaining 27 test guide
objectives the removed bank did not reach.
