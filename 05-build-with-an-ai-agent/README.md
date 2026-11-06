# How do I build something with an AI coding agent?

You write down what you want in a short spec file, then give the agent one small step at a time and check its work after each one. In this lesson you'll use Claude Code to build a tiny Polish & Co. assistant that answers customer questions from the FAQ using the Claude API, and ship it as a pull request.

![Level: Intermediate](https://img.shields.io/badge/Level-Intermediate-blue) ![Type: Build](https://img.shields.io/badge/Type-Build-blue) ![Time: 75 min](https://img.shields.io/badge/Time-75%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** Plan first, then build. Write a `CLAUDE.md` that says what you're building, what done looks like, the rules and how to check the work. Ask the agent for its plan before any code. Then give it one step at a time, read the diff, run the check yourself, and commit. Keep your API key in an environment variable so it never lands in a file. When it works, push the branch and open a PR that says what you checked and which parts the agent wrote.

> [!TIP]
> **New to this? Let me break it down.**
> Picture a talented new nail tech on her first day at Polish & Co. She's fast and she's good, but she's never seen this salon. You wouldn't say "do the customers" and walk away. You'd hand her the service menu and the house rules, ask her to talk you through the first set before she starts, then check each hand before she moves on.
>
> A coding agent is that new tech. `CLAUDE.md` is the service menu and the house rules. The small steps are the one-hand-at-a-time check. The pull request is the owner looking over the finished set before the customer leaves.

**You'll need:**
- [Lesson 3: Your first pull request](../03-your-first-pull-request/) and [Lesson 4: Why PRs matter for a PM](../04-why-prs-matter-for-pms/), so you can open and describe a PR
- [Lesson 2: How LLMs and agents work](../02-how-llms-and-agents-work/) helps, but isn't required
- A Mac, Windows or Linux computer where you can open a terminal. Never used one? Start with the [Claude Code terminal guide for new users](https://code.claude.com/docs/en/terminal-guide).
- Git and Python 3.10 or newer installed
- A free GitHub account
- A Claude subscription (Pro, Max, Team or Enterprise) or a Claude Console account, to use Claude Code
- A Claude Console account with some prepaid credit and an API key, for the assistant's own calls to the Claude API. The API is paid for separately from a Claude subscription. This lesson only makes a handful of short calls with a small model, so it uses very little. Check the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) for current prices.

**What you'll learn:**
- How I go from idea to spec to build, and where Claude Code fits
- How to write a short `CLAUDE.md` an agent can actually follow
- How to give an agent small steps and check each one yourself
- How to keep an API key out of your code and out of git
- How to review what an agent wrote and ship it as a PR with a good description

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [Plan it before you build it](part-1-plan-it.md) | Write your `CLAUDE.md` | 15 min |
| [ ] | [Set up your project](part-2-set-up.md) | Repo, branch, Claude Code and your API key | 15 min |
| [ ] | [Build it in small steps](part-3-build-in-small-steps.md) | Plan, build, check and commit, one step at a time | 20 min |
| [ ] | [Review it and ship it as a PR](part-4-review-and-ship.md) | Review the agent's work, push, open the PR | 15 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

**Copy this:** [`starter-CLAUDE.md`](starter-CLAUDE.md), the spec file you'll start from.

**Stuck on the code?** A working version is in [`reference/`](reference/). Compare against it, don't copy it. The point is to see what your agent does.

**Optional, Advanced:** [Extra credit](extra-credit.md), hard limits on what the agent can read, and one instructions file for every agent.

**[Start Part 1 →](part-1-plan-it.md)**
