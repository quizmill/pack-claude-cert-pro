# Notices

## Questions and concept cards — original

Every question in `questions.json` and every card in `concepts.json` was
written for this pack. Each question's `source` is `original` and its
`sourceRef` points at the document the question was written against:
Anthropic's public *Claude Certified Architect – Professional Exam Guide*
(v1.0, July 2026), which lists the seven content domains, their weights,
and the objectives each domain measures. The questions test those
objectives with scenarios, options and rationales of our own; none are
drawn from the live exam, which is under NDA, and none reproduce the
guide's three sample items. Where a question turns on a product
behaviour (prompt caching, Skills, MCP, Claude Code configuration), the
behaviour was checked against Anthropic's public documentation.

Apart from the Purcell paper below, the pack carries no third-party
question content. The history of an earlier, since-removed bank is
recorded in [docs/provenance.md](docs/provenance.md).

## Matthew Purcell — CCAR-P Practice Question Set, Second Edition (paper `purcell-ccar-p`)

**These questions are not covered by the MIT licence.** The 43 questions
with `paperId: purcell-ccar-p` (ids `ccar-p-purcell-v2-*`) are
adapted from Matthew Purcell's *Claude Certified Architect – Professional:
Full Practice Question Set — Second Edition* (revised 3 November 2026,
written following Exam Guide v1.0, July 2026), © Matthew Purcell,
licensed under the
[Creative Commons Attribution-NonCommercial 4.0 International Licence (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).
They are excluded from the MIT licence, and from any other licence that
covers the rest of this repository, and remain under CC BY-NC 4.0: you
may share and adapt them for non-commercial purposes, with credit to the
author and a link to the licence.

- Author: <https://www.linkedin.com/in/purcellmatthew>
- Source: <https://www.linkedin.com/posts/purcellmatthew_ccar-p-practice-exam-question-set-ugcPost-7522215192798142464-zF9t/>

The author states the set is original material written against
Anthropic's public exam guide, **not** actual exam content, which is
under NDA.

**What was changed:**

- **Format.** Converted from the PDF to the pack's JSON format. Stems,
  options and answer keys are his, in his order (questions 1.1–7.3).
  Each stem and its question line are joined into one prompt, and the
  multiple-response line "Each correct answer presents part of the
  solution" (or "a complete solution") is dropped.
- **Rationales.** Each question's `explanation` is his rationale for the
  correct answer. His "Why not the others" note is split per option
  into `options[].explanation`, lightly reworded so each note reads on
  its own (a note shared by two options, such as "A and C pay for…",
  appears on both).
- **Matching items left out.** The set has 63 questions; 20 of them are
  matching items (Yes/No review and classify-each-row: 1.9–1.11,
  2.6–2.8, 3.9–3.12, 4.8–4.10, 5.7–5.9, 6.7–6.9 and 7.4). The quizmill
  engine cannot show matching questions yet, so they are left out
  rather than rewritten into a different format. The paper is labelled
  "43 of 63" to say so.
- **Key corrections.** None; every answer key is as published.

## Trademarks

"Claude" and "Claude Certified Architect" are trademarks of Anthropic,
PBC. This project is not affiliated with or endorsed by Anthropic.
