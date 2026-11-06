<sub>Lesson 5, Part 1 of 5 · about 15 min</sub>

# Plan it before you build it

**In this part,** you'll see how I go from an idea to a build, decide exactly what this little assistant does, and write the `CLAUDE.md` your agent will follow.

**Quick check before you start.** If you can answer both, skim this part and jump to [Part 2](part-2-set-up.md).
1. What's the difference between what goes in `CLAUDE.md` and what goes in the prompt you type?
2. Why would you ask an agent for a plan before it writes any code?

## Why this matters

A coding agent is very good at doing what you said. When you leave a gap, it fills it with a reasonable guess. Sometimes the guess is great. Sometimes you get a web server, a database and a login screen when you wanted one small script.

So the most useful thing you can do happens before the agent writes a line. Decide what you're building, what done looks like and what it must never do, and write it down where the agent will read it every time.

## How I build

My usual flow has three stops, and I skip the ones a build doesn't need:
1. **Brainstorm and spec in Claude Cowork.** I talk the idea through, push on the edge cases and end up with a written spec.
2. **Design specs in Claude Design.** For anything with screens, I work out the layout and look before any code exists.
3. **Build in Claude Code.** The agent works in my project folder, reads the spec, writes the code and runs the checks.

Planning, building and checking happen in different places on purpose. The chat where I made the plan isn't the one judging whether the build matches it.

This build has no screens, so you'll skip the design stop. You can do the brainstorm in any Claude chat.

Claude Code isn't the only coding agent. Cursor, GitHub Copilot and OpenAI's Codex work in a similar way, and many of them read a shared instructions file called [AGENTS.md](https://agents.md/). The steps in this lesson work with any of them. I use Claude Code, so that's what the commands show.

## How it works

`CLAUDE.md` is a plain Markdown file at the root of your project. Claude Code reads it at the start of every session, so it's where you put the things the agent can't work out by reading your files ([Claude Code docs, How Claude remembers your project](https://code.claude.com/docs/en/memory)):
- what you're building and what done looks like
- how to check the work, as exact commands
- decisions and rules that aren't written anywhere in the code
- anything you've had to correct twice

Keep it short. The docs say to "target under 200 lines per CLAUDE.md file", because longer files cost more and get followed less closely. The starter for this lesson is about 50.

The prompt you type in a session is for the task right now. `CLAUDE.md` is for what's true every time.

## Do it (step by step)

### 1. Brainstorm the scope

**Have a chat interview you until the build is small and clear.** Open a Claude chat and paste this:

```text
I want to build a tiny assistant for a made-up nail salon called Polish & Co.
It should answer customer questions using only the salon's FAQ, through the
Claude API. I'm going to build it with Claude Code and ship it as a pull
request. Interview me with short questions until you could write a one-page
spec. Push me to keep it as small as possible.
```

Answer its questions. These are the calls I made, so you can compare:
- **A command-line script, not a web page.** You type a question, it prints an answer. The smallest thing that proves the idea works.
- **One question at a time.** No conversation history yet.
- **Answers only from the FAQ.** If it isn't in the FAQ, it says so and offers to connect the customer with the salon.
- **A dry-run mode.** It prints the exact prompt without calling the API, so the agent and I can check the prompt for free.

You're done when you can describe the build in two sentences.

<details>
<summary>Stuck?</summary>

- **The chat keeps adding features.** Say "smaller". Booking, payments and a chat window can all be later PRs.
- **You're not sure what the FAQ is.** It's in the [running example](../example/README.md). Read it now. The assistant will read the same file.
</details>

### 2. Write down what done looks like

**Turn your scope into a short list you can check one line at a time.** Each line should be something you can see happen, not a feeling. "It's good" can't be checked. "With no API key set, it prints a clear message instead of crashing" can.

Mine is in the "Done looks like" section of the starter file. It's the acceptance criteria for this build, and you'll test it for real in [Evals 101](../06-evals-101/).

You're done when every line is something you could watch happen in the terminal.

### 3. Make the starter CLAUDE.md yours

**Copy the starter and read every line before you use it.** Open [`starter-CLAUDE.md`](starter-CLAUDE.md), click **Raw** and copy it into a note for now. You'll put it in your project in Part 2.

It has six short sections:
1. **What we're building.** Two sentences and one example.
2. **Done looks like.** Your list from step 2.
3. **Files.** What each file is for, and which one the agent must never touch (`faq.md`, because the salon owns its policies).
4. **Rules.** The things that must always or never happen, like where the API key comes from.
5. **How to check your work.** The exact commands, and a request to show the output.
6. **How we work.** Plan first, one step at a time, and you push and merge, not the agent.

Change at least one thing so it matches your scope. If you said "no tests" in your brainstorm, I'd push back and keep them, but it's your build.

You're done when you've read every line and can say why it's there.

<details>
<summary><strong>Go deeper (CLAUDE.md is context, not a lock)</strong></summary>

The Claude Code docs are clear that the agent "treats them as context, not enforced configuration" ([How Claude remembers your project](https://code.claude.com/docs/en/memory)). The more specific and short your instructions, the more consistently they're followed, but "consistently" isn't "always".

So for the rules that can't have exceptions, there are stronger tools:
- **Permission rules** can stop the agent reading certain files at all, like `.env`.
- **Hooks** run your own script at set moments, like before every commit, and can block the action.

[Extra credit](extra-credit.md) shows a permission rule for this project. The [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) page covers both.

A few related files you'll see in real projects:
- **`AGENTS.md`** is the shared format many coding agents read. Claude Code reads it when there's no `CLAUDE.md`.
- **`CLAUDE.local.md`** holds your personal preferences for a project. You add it to `.gitignore` so it isn't committed.
- **`SPEC.md`** or a build brief holds a bigger one-off plan. `CLAUDE.md` then stays short and points to it.
</details>

## Quick check

<details>
<summary>1. What belongs in CLAUDE.md, and what belongs in the prompt you type?</summary>

`CLAUDE.md` holds what's true every session: what you're building, what done looks like, the rules and how to check the work. The prompt holds the task for right now, like "do step 2 only".
</details>

<details>
<summary>2. Why is <code>faq.md</code> marked "never edit"?</summary>

Because the salon owns its policies. The agent's job is to write code that answers from the FAQ, not to change what the FAQ says. A rule in `CLAUDE.md` makes that explicit.
</details>

---

**Next: [Part 2 (Set up your project)](part-2-set-up.md)** | [Back to the lesson](README.md)
