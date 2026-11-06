<sub>Lesson 5, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your build against the list, try the challenge and practise the questions you'd get in an interview.

## Common mistakes

- **Wrong:** "Build me a salon chatbot" as the first prompt. **Instead:** a `CLAUDE.md` with scope, done, rules and checks, then a plan, then one step.
- **Wrong:** accepting "all tests pass" from the agent's summary. **Instead:** read the diff and run the check yourself, in your own terminal.
- **Wrong:** pasting your API key into the chat or a file "just for now". **Instead:** an environment variable in a terminal the agent doesn't use.
- **Wrong:** one giant commit at the end. **Instead:** one commit per checked step, so any step can be undone on its own.
- **Wrong:** correcting the same mistake a third time in the same conversation. **Instead:** `/clear`, and a better prompt or a new line in `CLAUDE.md`.
- **Wrong:** a PR that says "works" and hides the case that failed. **Instead:** say exactly what you ran, what passed, what didn't and what's next.

## What I learned doing this

I learn the judgment, and the AI does the typing. My job on a build like this is to decide what it should do, notice when it's drifting, and check that it actually does the thing. That's still real work, and it's the part I can't hand off.

A few things I'd tell myself at the start:
- **Nothing counts on a self-reported pass.** An agent can describe a method it didn't use, and do it confidently. I check claims against the file and the running thing, not the summary.
- **Write "OPEN QUESTION", not a guess.** When my spec has a gap, I'd rather the agent stop and ask than fill it in for me. Saying so in `CLAUDE.md` makes that happen more often.
- **Plan, build and check in different places.** The conversation that made the plan isn't the one I trust to judge the build. A fresh session or a second terminal keeps me honest.
- **Don't switch branches under a working agent.** The folder shows whatever branch is checked out. If I need another branch while the agent's working, I use a second folder (a git worktree) instead.

## You're done when

- [ ] Your repo has a `CLAUDE.md` you've read line by line and changed to fit your scope
- [ ] Your API key has never been in a file, a commit or a chat, and `git log -S "sk-ant"` prints nothing
- [ ] `python ask.py --dry-run "..."` prints the full prompt
- [ ] `python ask.py "..."` answers from the FAQ in your second terminal
- [ ] `python -m unittest` passes, and you've watched a test fail on purpose
- [ ] Your branch has one commit per step, each one checked before it went in
- [ ] Your PR has an outcome title, says what you checked and what failed, and says which parts the agent wrote
- [ ] The PR is merged and the branch is deleted

## Challenge

Make a tiny web page version as a second PR. A box to type a question, a button, and the answer underneath. Keep the same rules. The key stays on the server side, never in the page.

Do it the same way:
1. Update `CLAUDE.md` first, in its own commit. What does done look like for the page?
2. If you want, sketch the page in Claude Design or on paper before you build.
3. Ask for a plan, then build it in small steps, checking each one.
4. Open the PR with an outcome title, like `Second pass: customers can ask the FAQ assistant from a web page`.

Share your PR title in the hub's Discussions if you like.

## Check yourself (interview style)

<details>
<summary><strong>1. How do you work with an AI coding agent?</strong></summary>

I write a short spec first, with what we're building, what done looks like, the rules and how to check the work. I ask the agent for a plan before any code. Then I give it one small step at a time, read the diff, run the check myself and commit only what I've checked. When it's done, a fresh reviewer checks it against the spec, and I ship it as a PR that says what I checked and which parts the agent wrote.
</details>

<details>
<summary><strong>2. What goes in a CLAUDE.md or AGENTS.md file?</strong></summary>

The things the agent can't work out by reading the code. What we're building and what done looks like, the exact commands to check the work, decisions and rules that aren't written down anywhere else, and anything I've had to correct twice. I keep it short, because long files get followed less closely. And it's guidance, not enforcement, so rules that can never be broken go in permission rules or hooks.
</details>

<details>
<summary><strong>3. How do you know the code an agent wrote actually works?</strong></summary>

I don't take its word for it. I read the diff, run the checks myself, and make sure the checks can fail by breaking something on purpose. For an AI feature, I also run real test questions, including the safety cases several times, and I write down the results. A second reviewer that didn't write the code checks it against the spec.
</details>

<details>
<summary><strong>4. How do you handle API keys and secrets when building with an agent?</strong></summary>

Keys live in environment variables, never in code or committed files. The agent runs in a session where the key isn't set, so it can't leak it. `.env` and similar files are in `.gitignore` before they exist, and I block the agent from reading them with a permission rule. Before I push, I search the files and the git history for keys. If one ever gets committed, I revoke it and make a new one, because deleting the file doesn't remove it from history.
</details>

<details>
<summary><strong>5. An agent opens a PR on your team's repo. What do you check before approving?</strong></summary>

The same things as any PR, with a bit more suspicion. Does the description match the diff, with nothing extra? Are there new libraries, files or permissions nobody asked for? Did the checks I expect actually run, and can they fail? Are customer-facing words and numbers right? And does the "How I checked it" section describe checks that were really run, not just claimed?
</details>

## Further reading

**Start here**
- [Claude Code 101](https://academy.claude.com/courses/claude-code-101), Claude Academy. Anthropic's free self-paced intro course.
- [Terminal guide for new users](https://code.claude.com/docs/en/terminal-guide), Claude Code docs. How to open a terminal and paste a command, if you've never done it.
- [Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/), MIT Missing Semester (2026). A free lecture on how coding agents work, with notes and exercises.

**Go deeper**
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices), Anthropic. Tell it what it can't see, give it a check to run, and enforce the rules that can't have exceptions.
- [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/), Simon Willison. Practical patterns from someone who builds with agents every day. Start with [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/).
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents), Anthropic. When to use an agent, when a simple workflow is better, and why.

**Primary sources**
- [Claude Code quickstart](https://code.claude.com/docs/en/quickstart) and [How Claude remembers your project](https://code.claude.com/docs/en/memory), Claude Code docs. Install, first session, and how `CLAUDE.md` and `AGENTS.md` load.
- [Get started with Claude](https://platform.claude.com/docs/en/get-started) and [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages), Claude Platform docs. Your first API call, and how system prompts and messages work.
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview), Claude Platform docs. Current model names and prices.
- [AGENTS.md](https://agents.md/). The open instructions format many coding agents share.
- [Ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files), GitHub Docs. How `.gitignore` works, and what it can't do for files already committed.

## Next lesson

**Next: [Lesson 6, Evals 101](../06-evals-101/).** You'll write 20 test cases for the assistant you just built, including the must-escalate group, run them, and decide whether it's ready to ship.

[Back to the lesson](README.md) | ← [Lesson 4, Why PRs matter for a PM](../04-why-prs-matter-for-pms/) | **Next: [Lesson 6, Evals 101](../06-evals-101/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
