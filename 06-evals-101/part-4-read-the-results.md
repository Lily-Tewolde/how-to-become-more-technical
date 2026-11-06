<sub>Lesson 6, Part 4 of 5 · about 10 min</sub>

# Read the results and rerun

**In this part,** you'll read the results group by group, decide whether this version ships, then fix one thing and run the whole set again.

### 7. Read the results

**Look at each group before you look at the total.** Here's a made-up example of a first run:

| Group | Cases | Passed | Pass rate |
|---|---|---|---|
| FAQ | 6 | 6 | 100% |
| Not in the FAQ | 4 | 4 | 100% |
| Tricky wording | 3 | 3 | 100% |
| **Must escalate** | **7** | **6** | **86%** |
| Total | 20 | 19 | 95% |

The total says 95%. The must-escalate row says the run failed, because ME-07 missed on one of its three runs. So this prompt doesn't ship yet.

Then read the fails themselves. Look for a pattern. If the bot misses the buried swelling but catches every direct "my finger is swollen", the allergy rule is fine. The prompt needs to tell it to read the whole message before it answers.

Two more things to check:
- **False alarms.** If TW-03 got the handoff, the bot is over-escalating. That's annoying for customers, and staff start ignoring handoffs.
- **A perfect score.** If everything passes on your first try, break something on purpose. Paste a bad answer into a row and make sure your grading catches it.

**You're done when** you can say in one sentence whether this version is good enough, and point to the rows that decide it.

### 8. Fix one thing and run everything again

**Change one thing, then rerun all 20.** A fix for ME-07 can break something else, like suddenly escalating TW-03. Rerunning the whole set is how you catch that. This is called regression testing.

Keep your old results. A small table of runs is enough:

| Run | What changed | FAQ etc. (13) | Must escalate (7, all runs) | Ships? |
|---|---|---|---|---|
| 1 | First prompt | 13 | 6 | No |
| 2 | Told it to read the whole message before answering | 13 | 7 | Yes |

**You're done when** your second run meets your pass bar, or you know exactly which row is stopping it.

## Common mistakes

- **Only testing questions the bot already answers well.** Write the scary and weird ones first.
- **Grading on gut feel.** Grade against the written expected behaviour, line by line.
- **Trusting one run of a safety case.** Run it more than once. A case that passes 2 of 3 runs is a fail.
- **Only checking that it escalates.** Also check that it doesn't escalate when it shouldn't.
- **Counting cases you didn't run as passes.** If you skipped a case, mark it "not run".

<details>
<summary><strong>Go deeper (held-out set)</strong></summary>

If you keep tweaking the prompt until all 20 pass, you can end up with a prompt that's great at these 20 messages and no better at anything else. That's overfitting.

A held-out set is a second batch of cases you never look at while you tune. You only run it at the end, to check the improvement is real. A few habits help:
- Keep the held-out cases in a separate file and don't read the fails while you're tuning.
- Keep a few hard cases you know the bot fails. A perfect score on everything usually means the test is too easy or the grader is broken.
- Show before and after numbers, on both sets.
</details>

<details>
<summary><strong>Go deeper (regression testing)</strong></summary>

Anthropic's guide splits evals into two kinds. Capability evals "should start at a low pass rate", so you have something to improve. Regression evals ask whether the system "still handle[s] all the tasks it used to" and "should have a nearly 100% pass rate" ([Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).

Your must-escalate group is a regression suite. Rerun it on every change to:
- the prompt
- the FAQ or the rules
- the model, including a model version update you didn't choose
- the output format

Cases also go stale. If the salon changes its handoff message, every must-escalate expected behaviour has to change with it.
</details>

## Quick check

<details>
<summary>1. Why rerun all 20 cases after fixing just one?</summary>

A fix for ME-07 can break something else, like suddenly escalating TW-03. Rerunning the whole set is how you catch that. It's called regression testing.
</details>

<details>
<summary>2. Everything passed on your first try. What do you do?</summary>

Break something on purpose. Paste a bad answer into a row and make sure your grading catches it.
</details>

---

**Next: [Part 5 (Wrap up)](part-5-wrap-up.md)** | [Back to the lesson](README.md)
