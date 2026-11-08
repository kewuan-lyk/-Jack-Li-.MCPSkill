# Step 2: Set Up the Skill Directory

## Skill location

Codex on this computer has no `CODEX_HOME` environment variable, so the verified user-level discovery directory is:

```text
/Users/yukuanli/.codex/skills/
```

The installed test skill is:

```text
/Users/yukuanli/.codex/skills/hw8-greeting/SKILL.md
```

A project-scoped copy is included in this repository at:

```text
.codex/skills/hw8-greeting/SKILL.md
```

## What the test skill does

When `$hw8-greeting` is invoked, the response must begin with:

```text
Skill recognized:
```

## Validation

The Skill Creator validator returned:

```text
Skill is valid!
```

An independent Codex CLI session was then started with this prompt:

```text
Use the $hw8-greeting skill to confirm that this skill is recognized. Reply in one short sentence.
```

The independent session read the installed `SKILL.md` and returned:

```text
Skill recognized: the `hw8-greeting` skill was loaded and followed.
```

This confirms that Codex discovered and followed the Skill before any real functionality was added.

## Official resources checked

- OpenAI Developers: https://developers.openai.com/blog/eval-skills
- OpenAI Developers skills overview: https://developers.openai.com/plugins/concepts/skills
