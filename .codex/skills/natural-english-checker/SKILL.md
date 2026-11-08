---
name: natural-english-checker
description: "Audit English for AI-sounding or overly academic vocabulary, passive voice, and formulaic transitions using natural undergraduate writing as the standard. Use when the user asks to check tone, identify an AI-written feel, or review text before submission. Strictly read-only: cite exact lines and suggest improvements without editing or rewriting the source."
---

# Natural English Checker

## What to do

Perform a read-only audit for inflated vocabulary, avoidable passive voice, formulaic AI transitions, and decorative phrases without concrete meaning. Compare against clear, direct writing by a real university student. List each supported finding and a concise revision suggestion, but never apply the suggestion to the input or its source file.

## Rules

- **Evidence:** Every finding must cite the source filename, a specific line number, and an exact excerpt. If any evidence is missing or does not support the label, do not report it. Never judge from a general impression alone.
- **Strictly read-only:** Report only. Never modify, overwrite, patch, replace, or rewrite any part of the input or source file. Suggestions may appear only as separate report text; never apply them, return a fully rewritten passage, or silently substitute edited text for the original.
- **Actionable suggestions:** Give one concise suggestion for each supported finding. Keep the quoted original unchanged and clearly separate it from the suggestion.
- **Baseline:** Use natural undergraduate assignment writing—not advertising, corporate copy, or academic-journal prose. Do not penalize simple vocabulary or a direct student voice.
- **Context:** Do not flag a target word when it is precise and natural in context.

## Target Patterns

- Inflated words: `delve`, `imperative`, `meticulously`, `testament`, `pivotal`, `underscore`, `realm`, `tapestry`, `multifaceted`, `robust`.
- Passive patterns: `was conducted`, `is demonstrated`, `has been shown`, or wording that hides the actor.
- Formulaic transitions: `Moreover`, `Furthermore`, `In conclusion`, `It is important to note that`, `It is worth mentioning that`, `This highlights the fact that`.

## Output Format

Use visible source line numbers. For pasted text without a filename, use `pasted-text`; if it has no line breaks, number sentences from 1. Write one line per finding:

```text
[AI-JARGON] File <filename>, Line <n>: "<exact original>" -> Suggestion: <concise replacement or revision advice>
```

Use only `[AI-JARGON]`, `[PASSIVE-VOICE]`, `[AI-TRANSITION]`, or `[UNNATURAL]`. Quote the smallest sufficient original phrase. End with exactly:

```text
SUMMARY: Total N | AI-JARGON X | PASSIVE-VOICE Y | AI-TRANSITION Z | UNNATURAL W
```

If there are no findings, output only:

```text
SUMMARY: Total 0 | AI-JARGON 0 | PASSIVE-VOICE 0 | AI-TRANSITION 0 | UNNATURAL 0
```
