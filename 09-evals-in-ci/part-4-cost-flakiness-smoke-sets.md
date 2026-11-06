<sub>Lesson 9, Part 4 of 5 · about 10 min</sub>

# Cost, flaky results and smoke sets

**In this part,** you'll work out what each run costs, decide what to do when a case passes sometimes and fails sometimes, and choose when to run the full set and when a smaller smoke set is enough.

## Do it (step by step)

### 10. Work out what a run costs

**Count the model calls, then multiply by the price.** Unlike normal tests, every eval case costs a little money, because it calls a model.

For the v2 golden set:
- 23 cases aren't must-pass, and each runs once. That's 23 calls.
- 17 cases are must-pass, and each runs three times. That's 51 calls.
- So a full run is 74 calls.

Each call sends the bot's prompt plus one customer message. That's well under 1,000 input tokens. Replies are short, a few hundred tokens at most. Anthropic's [pricing page](https://platform.claude.com/docs/en/about-claude/pricing) listed Claude Haiku 5.5 at $0.10 per million input tokens and $0.50 per million output tokens (for prompts under 100,000 tokens) when I checked in November 2026. Using those prices and my rough token guesses, a full run costs about one or two cents.

That's cheap. It adds up when:
- the set grows to hundreds of cases
- you add the Lesson 8 judge, which doubles the calls and uses a bigger model
- people push ten times per pull request

The workflow already helps. `concurrency` cancels old runs when you push again, `timeout-minutes` stops stuck runs, and `max_tokens` in the script caps how long a reply can be.

**You're done when** you can say roughly what one run costs, and how many runs a busy week would have.

<details>
<summary><strong>Go deeper (cutting the bill for big sets)</strong></summary>

- **Batch the nightly run.** Anthropic's pricing page lists Batch API prices at half the normal rate for both input and output. Batches don't come back instantly, so they suit a nightly full run better than a pull request someone is waiting on.
- **Run the cheap checks first.** If the smoke set fails, there's no point paying for the full set. Make the full run a second job that only starts when the smoke job passes.
- **Cache the prompt.** The bot's prompt is the same on every call. Prompt caching can make repeated input cheaper. It's worth it once your prompt is long.
</details>

### 11. Decide what to do about flaky results

**The same message can get a different reply on the next run.** AI models don't give identical output every time. So a case can pass on Monday and fail on Tuesday with nothing changed. That's called a flaky result.

You may see older guides say "set temperature to 0" to make replies repeatable. Anthropic's [migration guide for Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) tells you to "omit `temperature`, `top_p`, and `top_k`" on that model, and adds: "If you were using `temperature = 0` for determinism, note that it never guaranteed identical outputs on prior models." So don't design around a setting that makes the variation go away. Design for the variation.

Here's how the script and the workflow handle it:
1. **Must-pass cases run three times and must pass all three.** That's pass^k from [Evals 101, Part 3](../06-evals-101/part-3-run-and-grade.md). Every customer gets one try, so the bot has to get it right every time.
2. **The score has an allowance.** One flaky non-must-pass case can flip without failing the PR (Part 2).
3. **API errors are retried. Wrong answers aren't.** The SDK retries things like a dropped connection or "too many requests" automatically. That's fine, because those aren't the bot's fault. A wrong answer is the bot's fault.

**Don't re-run until it goes green.** GitHub has a "re-run failed jobs" button, and it's tempting when a check fails for no obvious reason. But re-running until it passes turns "passes every time" into "passed once out of several tries". That's pass@k, and it's the wrong measure for a safety case. A must-pass case that fails one run in three is failing one customer in three.

When a case is flaky:
1. Read the failed answer in the report.
2. Treat it as a real failure that happens some of the time.
3. Fix the prompt, and add a case or two with similar wording to the golden set.
4. If you're sure it's the check that's wrong (a word check catching a good answer), fix the check in its own pull request, with a reason.

**Pin the model, and upgrade on purpose.** The script reads the model name from `EVAL_MODEL`. When you want a new model, change it in a pull request, so the upgrade runs the full golden set like any other change.

**You're done when** your team has agreed that a flaky must-pass case is a failure, not bad luck.

### 12. Pick when to run the full set and when to run a smoke set

**A smoke set is a small, fast set you run often.** In this script, `--set smoke` runs only the must-pass cases. The full set runs everything.

With 40 cases, running the full set on every pull request is fine. That's what `evals.yml` does. As the set grows, split it up:

| When | What to run | Why |
|---|---|---|
| Every push to a pull request | Smoke set | Fast and cheap, and it catches the worst failures right away |
| Before a pull request merges, or when the prompt, model or rules change | Full set | Catches the quieter problems |
| Every night or every week | Full set, with extra runs of must-pass cases | Catches changes you didn't make, like a provider updating a model |
| Before a release | Full set, including held-out cases, plus a person reading the "read by hand" list | The last gate before customers see it |

You can always start a run by hand. In the **Actions** tab, pick **Evals**, click **Run workflow**, and choose `full` or `smoke`.

**You're done when** you've decided which set runs when, and written it in your repo's README or PR template.

<details>
<summary><strong>Go deeper (a smoke set on pull requests and a nightly full run)</strong></summary>

Once your set is big, you could change the top of `evals.yml` to run the smoke set on pull requests and the full set every night:

```yaml
on:
  pull_request:
  schedule:
    - cron: "23 9 * * *"  # every day at 09:23 UTC
  workflow_dispatch:
```

Then pick the set from the event that started the run:

```yaml
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          EVAL_SET: ${{ github.event_name == 'pull_request' && 'smoke' || 'full' }}
```

Scheduled runs use your default branch (usually `main`), so they test what's live, not what's being proposed. If a nightly run goes red and nobody changed anything, that's the most useful red you'll get. Something outside your code changed.
</details>

## Quick check

<details>
<summary>1. A must-pass case fails, you click re-run, and it passes. Can you merge?</summary>

No. Re-running until it passes is pass@k. The case just showed it fails some of the time, which means some customers would get the wrong answer. Fix the prompt.
</details>

<details>
<summary>2. Why not set temperature to 0 and stop worrying about flaky results?</summary>

Because it never guaranteed identical outputs, and some of Anthropic's newest models don't accept the setting at all. Design for variation by running must-pass cases several times instead.
</details>

<details>
<summary>3. When is a smoke set enough?</summary>

On every push to a pull request, once the full set is big or slow. The full set still runs before merging, on a schedule, and before a release.
</details>

---

**Next: [Part 5 (Wrap up)](part-5-wrap-up.md)** | [Back to the lesson](README.md)
