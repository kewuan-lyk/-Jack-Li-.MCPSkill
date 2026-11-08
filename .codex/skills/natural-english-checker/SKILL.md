---
name: natural-english-checker
description: "Audit English for AI-sounding or overly academic vocabulary, passive voice, and formulaic transitions using natural undergraduate writing as the standard. Use when the user asks to check tone, identify an AI-written feel, or review text before submission. Read-only: report evidence without editing or rewriting the source."
---

# Natural English Checker

## What to do

Perform a read-only audit for inflated vocabulary, avoidable passive voice, formulaic AI transitions, and decorative phrases without concrete meaning. Compare against clear, direct writing by a real university student.

## Rules

- **Evidence:** Every finding must cite the source filename, a specific line number, and an exact excerpt. If any evidence is missing or does not support the label, do not report it. Never judge from a general impression alone.
- **Read-only:** Do not fix anything. Report only. Never modify, overwrite, patch, or rewrite any source file or source text, and do not provide replacement wording.
- **Baseline:** Use natural undergraduate assignment writing—not advertising, corporate copy, or academic-journal prose. Do not penalize simple vocabulary or a direct student voice.
- **Context:** Do not flag a target word when it is precise and natural in context.

## Target Patterns

- Inflated words: `delve`, `imperative`, `meticulously`, `testament`, `pivotal`, `underscore`, `realm`, `tapestry`, `multifaceted`, `robust`.
- Passive patterns: `was conducted`, `is demonstrated`, `has been shown`, or wording that hides the actor.
- Formulaic transitions: `Moreover`, `Furthermore`, `In conclusion`, `It is important to note that`, `It is worth mentioning that`, `This highlights the fact that`.

## Output Format

Use visible source line numbers. For pasted text without a filename, use `pasted-text`; if it has no line breaks, number sentences from 1. Write one line per finding:

```text
[AI-JARGON] File <filename>, Line <n>: "<exact original>" — <brief reason>
```

Use only `[AI-JARGON]`, `[PASSIVE-VOICE]`, `[AI-TRANSITION]`, or `[UNNATURAL]`. Quote the smallest sufficient original phrase. End with exactly:

```text
SUMMARY: Total N | AI-JARGON X | PASSIVE-VOICE Y | AI-TRANSITION Z | UNNATURAL W
```

If there are no findings, output only:

```text
SUMMARY: Total 0 | AI-JARGON 0 | PASSIVE-VOICE 0 | AI-TRANSITION 0 | UNNATURAL 0
```
