#!/usr/bin/env python3
"""Curation checks for questions.json that the engine validator does not do.

The engine's `quizmill validate` checks the schema and cross-references.
This script checks the things a test-wise candidate exploits instead:

  * the correct option must not be systematically the longest one
  * the correct letter must be spread across A–D (A–E for select-two)
  * no absolute-language tells ("always", "never") only in distractors
  * every question has a difficulty, tags, and an explanation that names
    the correct option and at least one distractor
  * the bank's domain split tracks the manifest weights

Run from the pack root:  python3 scripts/check-bank.py
Exit code is non-zero when a hard check fails.
"""
import collections
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
qs = json.loads((ROOT / "questions.json").read_text())
manifest = json.loads((ROOT / "pack.json").read_text())
weights = {c["key"]: c["weight"] for c in manifest["categories"]}

failures: list[str] = []
warnings: list[str] = []
n = len(qs)

# --- answer-position balance ------------------------------------------------
single = [q for q in qs if "correctKey" in q]
multi = [q for q in qs if "correctKeys" in q]
letters = collections.Counter(q["correctKey"] for q in single)
print(f"questions: {n}  single-answer: {len(single)}  select-many: {len(multi)}")
print("correct letter (single-answer):", dict(sorted(letters.items())))
if single:
    top = max(letters.values()) / len(single)
    if top > 0.40:
        failures.append(f"one letter is correct in {top:.0%} of single-answer questions (limit 40%)")
# The engine shows options in file order, so a dominant key pair on the
# select-many items is just as exploitable as a dominant single letter.
pairs = collections.Counter("+".join(sorted(q["correctKeys"])) for q in multi)
print("correct pair (select-many):", dict(sorted(pairs.items())))
if multi:
    top_pair = max(pairs.values()) / len(multi)
    if top_pair > 0.40:
        failures.append(f"one key pair is correct in {top_pair:.0%} of select-many questions (limit 40%)")

# --- length tell -------------------------------------------------------------
# Rank 0 = the correct option is the longest of its question.
longest = 0
shortest = 0
ratios = []
for q in single:
    lengths = {o["key"]: len(o["text"]) for o in q["options"]}
    ck = q["correctKey"]
    ordered = sorted(lengths.values(), reverse=True)
    if lengths[ck] == ordered[0] and ordered[0] > ordered[1]:
        longest += 1
    if lengths[ck] == ordered[-1] and ordered[-1] < ordered[-2]:
        shortest += 1
    others = [v for k, v in lengths.items() if k != ck]
    ratios.append(lengths[ck] / statistics.mean(others))
share = longest / max(len(single), 1)
print(f"correct option is the single longest: {longest}/{len(single)} ({share:.0%}); "
      f"single shortest: {shortest}; mean length ratio correct/others: {statistics.mean(ratios):.2f}")
if share > 0.35:
    failures.append(f"correct option is the longest in {share:.0%} of single-answer questions (limit 35%)")
if statistics.mean(ratios) > 1.15:
    failures.append(f"correct options average {statistics.mean(ratios):.2f}x the length of distractors (limit 1.15)")

for q in multi:
    lengths = {o["key"]: len(o["text"]) for o in q["options"]}
    correct = [lengths[k] for k in q["correctKeys"]]
    wrong = [v for k, v in lengths.items() if k not in q["correctKeys"]]
    if min(correct) > max(wrong):
        warnings.append(f"{q['id']}: every correct option is longer than every distractor")

# --- wording tells -----------------------------------------------------------
ABSOLUTE = re.compile(r"\b(always|never|all|none|every|only|guarantee[sd]?)\b", re.I)
HEDGE = re.compile(r"\b(usually|typically|generally|often|may|might|can)\b", re.I)
abs_in_correct = abs_in_wrong = 0
for q in qs:
    keys = {q["correctKey"]} if "correctKey" in q else set(q["correctKeys"])
    for o in q["options"]:
        if ABSOLUTE.search(o["text"]):
            if o["key"] in keys:
                abs_in_correct += 1
            else:
                abs_in_wrong += 1
print(f"absolute words — in correct options: {abs_in_correct}, in distractors: {abs_in_wrong}")
if abs_in_wrong > 0 and abs_in_correct == 0 and abs_in_wrong >= 8:
    warnings.append("absolute language appears only in distractors — a test-wise tell")

# --- per-question hygiene ----------------------------------------------------
for q in qs:
    keys = [q["correctKey"]] if "correctKey" in q else q["correctKeys"]
    exp = q["explanation"]
    if not all(re.search(rf"\b{k}\b", exp) for k in keys):
        failures.append(f"{q['id']}: explanation does not name the correct option(s) {keys}")
    wrong = [o["key"] for o in q["options"] if o["key"] not in keys]
    if not any(re.search(rf"\b{k}\b", exp) for k in wrong):
        failures.append(f"{q['id']}: explanation does not discuss any distractor")
    if len(exp) < 160:
        warnings.append(f"{q['id']}: explanation is short ({len(exp)} chars)")
    if "correctKeys" in q and not re.search(r"Select (TWO|THREE|all)", q["prompt"]):
        failures.append(f"{q['id']}: select-many question does not say how many to select")
    if "correctKey" in q and len(q["options"]) != 4:
        warnings.append(f"{q['id']}: single-answer question with {len(q['options'])} options")
    if not q.get("tags"):
        failures.append(f"{q['id']}: no tags")
    texts = [o["text"].strip().lower() for o in q["options"]]
    if len(set(texts)) != len(texts):
        failures.append(f"{q['id']}: duplicate option text")
    for o in q["options"]:
        if re.search(r"all of the above|none of the above", o["text"], re.I):
            failures.append(f"{q['id']}: 'all/none of the above' option")

# --- distribution ------------------------------------------------------------
by_cat = collections.Counter(q["categoryKey"] for q in qs)
print("domain split vs blueprint:")
for key, w in weights.items():
    have = by_cat.get(key, 0) / n
    flag = "" if abs(have - w) <= 0.03 else "  <-- off blueprint by >3pt"
    print(f"  {key:24s} bank {have:5.1%}  blueprint {w:4.0%}{flag}")
    if abs(have - w) > 0.03:
        failures.append(f"{key}: bank share {have:.1%} is more than 3 points from blueprint {w:.0%}")
diff = collections.Counter(q["difficulty"] for q in qs)
print("difficulty:", dict(sorted(diff.items())))
print("reviewStatus:", dict(collections.Counter(q["reviewStatus"] for q in qs)))
print("source:", dict(collections.Counter(q["source"] for q in qs)))

for w in warnings:
    print("warning:", w)
for f in failures:
    print("FAIL:", f)
print("OK" if not failures else f"{len(failures)} failure(s)")
sys.exit(1 if failures else 0)
