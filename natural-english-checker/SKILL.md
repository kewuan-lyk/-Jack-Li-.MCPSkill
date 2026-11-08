---
name: natural-english-checker
description: "Audit English for AI-sounding or overly academic vocabulary, passive voice, and formulaic transitions using natural undergraduate writing as the standard. Use when the user asks to check tone, reduce an AI-written feel, or review text before submission. Read-only: report evidence and suggestions without editing the source."
---

# Natural English Checker

## What to do

Perform a read-only audit for inflated vocabulary, avoidable passive voice, formulaic AI transitions, and decorative phrases without concrete meaning. Compare against clear, direct writing by a real university student. Give short alternatives while preserving meaning and formality.

## Rules

- **Evidence:** Every finding must cite a specific line number and an exact excerpt. If either is missing or does not support the label, do not report it. Never judge from a general impression alone.
- **Read-only:** Never modify, overwrite, patch, or rewrite the source file or full text. Suggestions are allowed only after `->` in the report.
- **Baseline:** Use natural undergraduate assignment writing—not advertising, corporate copy, or academic-journal prose. Do not penalize simple vocabulary or a direct student voice.
- **Context:** Do not flag a target word when it is precise and natural in context.

## Target Patterns

- Inflated words: `delve`, `imperative`, `meticulously`, `testament`, `pivotal`, `underscore`, `realm`, `tapestry`, `multifaceted`, `robust`.
- Passive patterns: `was conducted`, `is demonstrated`, `has been shown`, or wording that hides the actor.
- Formulaic transitions: `Moreover`, `Furthermore`, `In conclusion`, `It is important to note that`, `It is worth mentioning that`, `This highlights the fact that`.

## Output Format

Use visible source line numbers; if the text has no line breaks, number sentences from 1. Write one line per finding:

```text
[标签] 行号: "原文" -> 替代建议
```

Use only `[浮夸词汇]`, `[被动语态]`, `[AI过渡句]`, or `[不自然表达]`. Quote the smallest sufficient original phrase. End with exactly:

```text
汇总: 共 N 处 | 浮夸词汇 X | 被动语态 Y | AI过渡句 Z | 不自然表达 W
```

If there are no findings, output only:

```text
汇总: 共 0 处 | 浮夸词汇 0 | 被动语态 0 | AI过渡句 0 | 不自然表达 0
```
