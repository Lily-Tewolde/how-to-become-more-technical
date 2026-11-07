<sub>Lesson 9, Part 2 of 5 · about 15 min</sub>

# The eval script

**In this part,** you'll read the eval script in plain words, run it once yourself if you want to, and break the bot on purpose to watch the script catch it.

## Do it (step by step)

### 3. Read the script, top to bottom

**Open [`run_evals.py`](run_evals.py) next to this page.** It's about 110 lines. You don't need to write Python to follow it. Here's what each part does:

| Part of the script | What it does in plain words |
|---|---|
| The settings at the top | Which model the bot runs on, how many times each must-pass case runs (3), and how far the score can drop before the run fails (10 points) |
| `ask_bot` | Sends one customer message to the bot in a brand new conversation, wrapped in `<customer_message>` tags like in [Lesson 10](../10-prompt-injection/part-3-fence-it-off.md) |
| `check` | Runs the word checks from the golden set. Missing a `must_include` word or containing a `must_not_include` word is a fail. |
| The loop in `main` | Goes through every case. Must-pass cases run three times. Every other case runs once. It prints one line per case as it goes, like `FAQ-01 ... pass`, so you can see it's moving. |
| The score | The pass rate on the cases that aren't must-pass, compared with the number in `baseline.json` |
| The report | A table of every case, what the bot said on each fail, and a list of must-pass cases a person still has to read. It prints to the log and to the run's summary page. |
| The last two lines of `main` | Exit with an error if any must-pass case failed or the score dropped. This is what turns the check red. |

**Three choices in the script are worth knowing about.**

1. **A case with no word checks is "not checked", never "pass".** Some cases, like NIF-01 (parking), can't be graded with a word list. The script says so instead of quietly counting them as passes. It also lists any must-pass case with no word checks under "Read by hand before release". In the v2 golden set that's NIF-07, the diabetic customer. [Lesson 8](../08-llm-as-judge/) is how you'd grade those automatically.

2. **"Pass" in CI means "passed the word checks".** That's weaker than a full pass. It catches a missing handoff or a banned word. It won't catch a made-up parking lot. Be clear about this when you tell people what the green tick means.

3. **The score can drop 10 points before the run fails.** That sounds generous. Here's why. The v2 set has 17 cases that aren't must-pass and have word checks. One case is about 6 points. Remember from [Lesson 7, Part 4](../07-golden-sets/part-4-how-many-cases.md) that small sets wobble. A threshold tighter than one case would fail pull requests for noise. With the example baseline of 90%, the run fails below 80%. So up to three of the 17 can fail and the run still passes, and a fourth fails it. Must-pass cases have no allowance at all.

**You're done when** you can explain to someone what makes this script fail.

### 4. Run it yourself (optional)

**Run the script on your own computer once, before CI does.** It's the easiest way to see what CI will see. If you'd rather not use a terminal, skip to step 5 and you'll see the same output in Part 3.

From the top folder of your repo:

```bash
python -m pip install -r evals/requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
python evals/run_evals.py
echo $?
```

On Windows PowerShell, set the key with `$env:ANTHROPIC_API_KEY="your-key-here"` and check the exit code with `echo $LASTEXITCODE`.

While it runs, you'll see one line per case, like `FAQ-01 ... pass`. Then the report prints, and the last line prints the exit code: `0` if everything passed, `1` if something failed.

**Then set your baseline.** `baseline.json` ships with an example score of 90%. After your first full run on your main branch, replace it with your real score. From then on, you only update it in a pull request, when the score has genuinely improved.

**You're done when** you've seen a full report and an exit code, and your `baseline.json` holds your own score.

<details>
<summary><strong>Stuck?</strong></summary>

- **"No ANTHROPIC_API_KEY."** The `export` line only lasts for that terminal window. Run it again in the same window as the script.
- **"ModuleNotFoundError: No module named 'anthropic'."** The install step didn't run in the same Python. Try `python3` instead of `python` for both lines.
- **"It failed on a model name."** Model names change. Check Anthropic's [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) and set `EVAL_MODEL` to a current one, for example `export EVAL_MODEL="claude-haiku-5-5"`.
- **Never paste your key into a file in the repo.** Not the script, not a `.env` file you commit. If it ever gets committed, delete the key in the Claude Console and make a new one. Deleting the file isn't enough, because git keeps history.
</details>

### 5. Break it on purpose

**Make the bot worse and check the script notices.** A check that has never failed might not be able to fail. So:
1. In `bot-prompt.txt`, delete the line under rule 3 about "a burn, cut, bleeding or a possible infection after a visit".
2. Run the smoke set, which is just the must-pass cases: `python evals/run_evals.py --set smoke`
3. Some of ME-03, ME-04, ME-09 and ME-10 should fail, and the exit code should be `1`. Models sometimes hand off anyway out of caution. If nothing fails, delete all of rule 3 and try again.
4. Put the line back and run it again. It should pass.

If you're not using a terminal, do the same thing in Part 3 with a pull request. Open a PR that deletes the line and watch the check go red.

**You're done when** you've watched a must-pass case fail with the rule removed, and pass again once it's back.

<details>
<summary><strong>Go deeper (adding the judge, and what happens when the API is down)</strong></summary>

**Adding the Lesson 8 judge.** The cases marked "not checked" are exactly the ones a judge can grade. You'd add a second check that sends each reply to the judge prompt from [Lesson 8](../08-llm-as-judge/judge-prompt.md), and follow the same rules:
- a judge fail counts as a fail
- a judge pass on a must-pass case doesn't count on its own, so the case stays on the "read by hand" list
- only use a judge in CI after you've checked it against your own grades

This roughly doubles the number of model calls, so it's worth it for the cases that need it, not every case.

**When the API is down.** The SDK retries some errors twice by default, with a short wait between tries ([Anthropic Python SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python)). If it still fails, the script stops with an error, and the check goes red. That's on purpose. A run that didn't finish must never look like a pass.
</details>

## Quick check

<details>
<summary>1. NIF-01 has no word checks. How does the script count it?</summary>

As "not checked". It's left out of the score, and it never counts as a pass.
</details>

<details>
<summary>2. Why can the score drop up to 10 points before the run fails?</summary>

With 17 scored cases, one case is about 6 points, and small sets wobble. With the example baseline of 90%, the run fails below 80%. So up to three of the 17 can fail and the run still passes, and a fourth fails it. Must-pass cases get no allowance.
</details>

<details>
<summary>3. Why delete a rule on purpose?</summary>

To prove the check can fail. A check that has never failed might not be checking anything.
</details>

---

**Next: [Part 3 (Run it on every pull request)](part-3-run-it-on-every-pr.md)** | [Back to the lesson](README.md)
