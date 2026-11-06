<sub>Lesson 5, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll turn two of your `CLAUDE.md` rules into limits Claude Code enforces itself, and share one instructions file between different coding agents. It's optional. Skip it if your build is done.

<details open>
<summary><strong>Go deeper (block the agent from reading secrets)</strong></summary>

A line in `CLAUDE.md` that says "never read .env" works most of the time. For a rule that can't have exceptions, use a permission rule instead. Claude Code applies it itself, so it doesn't depend on what the model remembers or decides.

Create `.claude/settings.json` in your project:

```json
{
  "permissions": {
    "deny": ["Read(./.env)", "Read(./.env.local)", "Read(./secrets/**)"]
  }
}
```

This is the example from [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices), which says `deny` rules hold in every permission mode. With it saved, asking Claude Code what's in `.env` fails, whether it tries to read the file directly or with a command like `cat`.

Commit `.claude/settings.json` in its own small PR, with a title like `Agent can't read secret files, enforced in settings`. Then try it. Make an empty `.env`, ask Claude Code to read it, and check it's refused.

The same docs cover **hooks**, which run your own script at set moments, like before a commit. A hook that scans for keys before every commit is a good next step once you're comfortable.
</details>

<details open>
<summary><strong>Go deeper (one instructions file for every agent)</strong></summary>

If you or your team use more than one coding agent, you don't want two instruction files drifting apart. [AGENTS.md](https://agents.md/) is an open format that many agents read, including OpenAI's Codex, GitHub's Copilot coding agent and Cursor.

Claude Code reads `AGENTS.md` when there's no `CLAUDE.md`. If you want both, keep the shared rules in `AGENTS.md` and import it at the top of `CLAUDE.md` with one line:

```markdown
@AGENTS.md

## Claude Code only
- Anything that only applies to Claude Code goes here.
```

The [memory docs](https://code.claude.com/docs/en/memory) explain which files load, and in what order.
</details>

<details open>
<summary><strong>Go deeper (run a check without opening a session)</strong></summary>

`claude -p "your question"` runs one request and exits, without the interactive window ([Claude Code quickstart](https://code.claude.com/docs/en/quickstart)). It's handy for one-off questions about your code, and it's the building block for running Claude Code in automation, like a GitHub Action that reviews every PR. You'll see the PR side of that in [Evals in CI](../09-evals-in-ci/).
</details>

---

[Back to the lesson](README.md) | [Part 5 (Wrap up)](part-5-wrap-up.md)
