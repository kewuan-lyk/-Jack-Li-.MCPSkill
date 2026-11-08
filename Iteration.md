This document shows one  failure during the development of the toolkit and related details.

# Failure (Version 1)

# The Setup
During initial testing of the `$natural-english-checker` skill, Version 1 of `SKILL.md` had a very basic frontmatter configuration:

```yaml
---
name: natural-english-checker
description: Checks text for natural English style.
---
```

I opened a fresh Codex session and issued a natural, everyday user prompt:

"Can you review the text in my README.md and tell me if the tone sounds good?"

Codex completely ignored the `$natural-english-checker` skill. Instead of loading the skill's instructions, Codex responded using its standard default system prompt. It directly edited the file and gave a vague, unformatted paragraph saying the tone "looks fine and professional."
The initial description was far too brief and vague. Agents rely exclusively on the skill's description field  to determine intent matching. Since the info I provided lacked explicit triggers like AI jargon, the agent did not recognize the prompt as a match for the custom skill and defaulted to standard text generation.




# Revision Applied (Version 2)
I updated the frontmatter of SKILL.md to explicitly define both what the tool does and when the agent should trigger it

```yaml
---
name: natural-english-checker
description: Reviews written documents, reports, or code comments to identify overly academic, verbose, or unnatural "AI jargon" (e.g., delve, imperative, meticulously, testament). Suggests simple, direct alternatives suited for a college student. Use when reviewing text for tone, or before submitting documentation.
---
```

In addition, I tightened the Rules section to explicitly enforce Read-Only mode. Then I restarted Codex with a fresh context and issued the same ambiguous prompt:
"Can you review the text in my README.md and tell me if the tone sounds good?"
Codex automatically recognized and loaded the $natural-english-checker skill before generating a reply. It did NOT edit any local files. It outputted the exact flagged lines with line numbers, quotes, and suggested replacements.