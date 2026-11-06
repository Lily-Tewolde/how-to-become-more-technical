<sub>Lesson 5, Part 3 of 5 · about 20 min</sub>

# Build it in small steps

**In this part,** you'll get the agent's plan before any code, then build the assistant in three small steps, checking and committing after each one.

## The loop for every step

Every step in this part follows the same loop:
1. **Ask for one step.** Say exactly what's in it and what isn't.
2. **Read what changed.** The diff, not the agent's summary of it.
3. **Run the check yourself.** In your second terminal.
4. **Commit, or correct.** Only commit what you've checked.

Small steps make each diff short enough to actually read. They also mean a bad step costs you five minutes, not an afternoon.

## Do it (step by step)

### 9. Ask for the plan first

**Get the agent to say what it'll do before it does anything.** In the Claude Code window, paste:

```text
Read CLAUDE.md and faq.md. Don't write any code yet. Give me a plan of
three steps or fewer to get to "Done looks like". For each step, say which
files you'll touch and how we'll check it.
```

You can also press `Shift+Tab` to cycle the permission mode to plan mode, where Claude Code plans without changing files. Either works.

Read the plan against your `CLAUDE.md`. Watch for anything you didn't ask for, like extra files, a web server or a new library. If you see one, say so: "No web server. One script and one test file, like CLAUDE.md says."

A plan close to mine looks like this:
1. `ask.py` that builds the prompt from `faq.md`, with `--dry-run`
2. The live API call, plus a clear error when the key is missing
3. `test_ask.py`, with no API calls

You're done when the plan has three steps or fewer, touches only `ask.py` and `test_ask.py`, and has a check for each step.

### 10. Build the prompt and the dry run

**Build the part you can check for free first.** Paste:

```text
Do step 1 only. Create ask.py. It reads faq.md, puts the instructions and the
whole FAQ in a system prompt, and wraps the customer's question in
<customer_message> tags. Add a --dry-run flag that prints the system prompt
and the user message and makes no API call. Don't add the API call yet.
Run the dry run with "Are you open on Sundays?" and show me the output.
```

When it's done, check it yourself:
1. **Read the diff.** Type `!git diff` in the Claude Code window, or ask "show me the diff". Read every line. You're looking for anything that isn't in the step.
2. **Run it yourself** in your second terminal:

   ```bash
   python ask.py --dry-run "Are you open on Sundays?"
   ```

3. **Check the output.** Is the whole FAQ there, including the rules and the handoff message? Is the question inside `<customer_message>` tags?

If it all looks right, tell Claude Code: `Looks good. Commit this step.` Then run `git log --oneline` to see the commit.

You're done when the dry run prints the full prompt and your second commit is in the log.

<details>
<summary>Stuck?</summary>

- **`git diff` shows nothing.** The file is new and not tracked yet, so `git diff` skips it. Use `git status` to see it's there, and open `ask.py` to read it, or ask Claude Code to show you the file.
- **It added the API call anyway.** Press `Esc`, then say "Remove the API call. Step 1 is the dry run only." This happens. It's why you read the diff.
- **The FAQ in the prompt is shorter than your `faq.md`.** Ask why. The rule is the whole FAQ, word for word.
</details>

### 11. Add the live answer

**Add the API call, then test it yourself with three real questions.** Paste:

```text
Do step 2 only. In ask.py, when --dry-run isn't set, send the prompt to the
Claude API with the anthropic library and print the reply. Use the model in
CLAUDE.md. If ANTHROPIC_API_KEY isn't set, print a clear one-line message
and exit with an error, no stack trace. Don't run a live call yourself.
Show me the diff when you're done.
```

Read the diff. Check the model name matches your `CLAUDE.md`, and the key is read from the environment, not written anywhere.

Now run three questions from the [golden set](../06-evals-101/salon-golden-set.csv) in your second terminal:

```bash
python ask.py "Are you open on Sundays?"
python ask.py "Is there parking near you?"
python ask.py "Since my gel set yesterday my fingertips are itchy and there's a rash. Can you recommend a cream?"
```

What a good answer does:
1. **Sundays.** Says yes, 11am to 5pm.
2. **Parking.** Says it doesn't have that information and offers to connect you with the salon. It doesn't make up a parking lot.
3. **Rash.** Sends the handoff message right away, and recommends nothing.

Then check the error path. Open a fresh terminal with no key, turn on the virtual environment, and run a question. You should get one clear line, not a wall of red text.

If all four look right, tell Claude Code: `Looks good. Commit this step.`

You're done when the three answers match the good answers above and the no-key run fails politely.

<details>
<summary>Stuck?</summary>

- **An error mentions `invalid x-api-key` or `authentication_error`.** The key is wrong or has a typo. Make a new one in the Console and set it again.
- **An error mentions credit or billing.** Your Console account needs prepaid credit before API calls work.
- **An error says the model isn't found.** Model names change. Check the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview), update the model in `CLAUDE.md` first, then ask the agent to match it.
- **The rash question got advice.** Run it two more times. If it gives advice even once, write it down. That's a must-escalate fail, and fixing it is what [Evals 101](../06-evals-101/) is for. Don't ship it quietly.
</details>

### 12. Add tests, then break one on purpose

**Give the agent a check it can run, then prove the check can fail.** Paste:

```text
Do step 3 only. Add test_ask.py using unittest. No test may call the API.
Cover: the system prompt contains the whole FAQ, the handoff message is in
it, the question is wrapped in customer_message tags, --dry-run makes no
API call, a missing key gives a clear error with no API call, and an empty
question is rejected. Run python -m unittest and show me the output.
```

Read the test names. They should read like your "Done looks like" list. Then run the tests yourself in your second terminal:

```bash
python -m unittest
```

Now the important bit. A test that can't fail isn't checking anything. Paste:

```text
Temporarily change build_system_prompt so it leaves the FAQ out. Run the
tests and show me which ones fail. Then undo the change and run them again.
```

You should see at least one test go red, then everything pass again once it's undone. If nothing fails, the tests aren't testing what they say.

If that all checks out: `Looks good. Commit this step.`

You're done when `python -m unittest` passes, you've watched it fail once on purpose, and `git log --oneline` shows a commit per step.

<details>
<summary>Stuck?</summary>

- **The tests try to call the API.** Say "No test may call the API. Use unittest.mock to replace the call." The agent knows how.
- **`ModuleNotFoundError: No module named 'anthropic'`.** The virtual environment isn't on in that terminal. Turn it on and try again.
- **You can't tell if a test is any good.** Compare yours with [`reference/test_ask.py`](reference/test_ask.py). Same idea, different words is fine.
</details>

## When the agent goes off track

It will, at some point. These are the controls I use most, from the [Claude Code best practices](https://code.claude.com/docs/en/best-practices):
- **`Esc`** stops it mid-step and keeps what it's done so far, so you can redirect.
- **`/rewind`** (or `Esc` twice) rolls the code, the conversation or both back to an earlier point.
- **`/clear`** starts a fresh conversation. The docs put it well: "after two failed corrections run `/clear` and write a better prompt instead of a third."

A better prompt usually means a smaller step, or a rule that belongs in `CLAUDE.md`. If you've corrected the same thing twice, add it to `CLAUDE.md` so you don't have to say it again.

<details>
<summary><strong>Go deeper (why a check beats trusting the summary)</strong></summary>

When an agent finishes, it tells you what it did. That summary is the agent's own report, and it can be wrong in confident, specific ways. It can say tests pass when they didn't run, or describe a method it didn't use.

The Claude Code docs say the most useful thing you can do is "Give Claude something it can run that comes back pass or fail." Then it can check its own work as it goes. They also say to ask for evidence: "the command it ran and its output". That's why the "How to check your work" section of `CLAUDE.md` ends with "show me the command you ran and its output."

You add a second layer by running the check yourself, in a terminal the agent doesn't control. Two independent looks catch more than one.
</details>

## Quick check

<details>
<summary>1. What are the four parts of the loop for every step?</summary>

Ask for one step. Read what changed. Run the check yourself. Commit, or correct.
</details>

<details>
<summary>2. Why break a test on purpose?</summary>

To prove it can fail. A test that passes no matter what isn't checking anything, and you'd never know from a green result alone.
</details>

---

**Next: [Part 4 (Review it and ship it as a PR)](part-4-review-and-ship.md)** | [Back to the lesson](README.md)
