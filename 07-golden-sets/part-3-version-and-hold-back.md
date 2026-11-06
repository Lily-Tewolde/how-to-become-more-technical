<sub>Lesson 7, Part 3 of 5 · about 15 min</sub>

# Version it and hold some back

**In this part,** you'll put the golden set in your repo so every change has a history, split off a held-out group you don't tune against, and set a habit for keeping it fresh.

## Do it (step by step)

### 9. Put the set in your repo

**Keep the golden set as a file in the same repo as the bot.** A CSV in a folder like `evals/golden-set.csv` works well. Living next to the code gives you three things:
1. **History.** Git remembers every version. You can see who changed a case, when and why.
2. **Review.** A change to the set goes through a pull request, just like a change to the prompt. Someone else gets to say "wait, is that really the right answer?"
3. **One source of truth.** In [Lesson 9](../09-evals-in-ci/), the automatic check reads this exact file. No copies in someone's Google Drive drifting out of date.

If you haven't opened a pull request before, [Lesson 3](../03-your-first-pull-request/) walks you through it in the browser.

**Follow a few house rules.** These keep your history honest:
- **Never reuse or renumber an ID.** ME-07 means the same case forever. If you retire it, the number stays retired.
- **Changing an expected behaviour needs a reason.** Write it in the PR description and in the case's `notes`.
- **Don't delete a case to make a run pass.** If a case is wrong, fix the case in its own PR and say why. If the bot is wrong, fix the bot.
- **Keep a short changelog.** A `CHANGELOG.md` next to the CSV is enough.

Here's what the changelog for this lesson's set might look like:

```markdown
## v2 (2026-11)
- Added 20 cases. Sources: staff notes, rewritten real messages, one bug, Lesson 10 attacks.
- New columns: split, source, added_in.
- 7 cases marked held_out.
- NIF-07 (diabetic customer): owner decided no medical advice, offer to connect, no handoff.

## v1 (2026-11)
- First 20 cases from Evals 101.
```

**You're done when** the CSV lives in your repo, and your next change to it goes through a pull request.

<details>
<summary><strong>Stuck?</strong></summary>

- **"My team works in a spreadsheet, not GitHub."** That's fine for drafting. Export to CSV when a version is agreed, and commit that. The repo copy is the one that counts.
- **"The diff for a CSV is hard to read."** It is a bit. Keep one case per line and don't reorder rows, so the diff only shows what really changed.
</details>

### 10. Split off a held-out group

**Pick about one case in five and mark it `held_out`.** These are cases you don't look at while you're tuning the prompt. Here's why they matter.

When you change the prompt, rerun, read the fails and change it again, you're slowly fitting the prompt to those exact messages. Do it enough and the prompt gets great at the test without getting better at real customers. That's called overfitting. The held-out group is your check. If the dev cases go up and the held-out cases don't, the improvement isn't real.

How I pick them:
- At least one from every group, including must escalate and adversarial
- Cases that test the same rules as dev cases, with different wording. ME-10 is a chemical burn, while ME-03 is a foot bath burn.
- Never the case you just fixed a bug for. That one stays in dev.

In v2, 7 of the 40 are held out: FAQ-09, NIF-06, TW-06, TW-08, ME-10, ME-12 and INJ-07.

**Follow the held-out rules.**
1. **Held-out cases still have to pass to ship.** You run them before every release, and must-pass ones are still hard gates.
2. **Don't tune while staring at them.** When a held-out case fails, find a dev case with the same pattern, or write a new one, and fix the prompt against that. Then check the held-out case again.
3. **Refresh them now and then.** Once you've read a held-out case's fails a few times, it isn't really held out anymore. Move it to dev and write a fresh one.

**You're done when** about a fifth of your cases say `held_out`, spread across every group.

<details>
<summary><strong>Go deeper (the same idea for judges, and pinning a version)</strong></summary>

**For judges.** When you build an AI grader in [Lesson 8](../08-llm-as-judge/), the same problem shows up. Hamel Husain and Shreya Shankar's [AI Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) recommends you "split these examples into train, dev, and test sets", and warns that overfitting "can happen even if you never put the dev examples directly in the prompt." Just reading them while you edit is enough.

**Pinning a version.** When you compare two prompts, run both against the same version of the set. If you add five cases between runs, the scores aren't comparable anymore. Tools like Langfuse version datasets automatically. Their guide says "every addition, update, deletion, or archival of items creates a new version" ([Golden dataset evaluation](https://langfuse.com/resources/engineering/golden-dataset-evaluation)). In plain git, the commit is your version. Write it next to every score you report.
</details>

### 11. Re-check the set after every product change

**Cases go stale when the product changes.** If Polish & Co. rewrites its handoff message, every must-escalate case that checks for "passing this to our team" is now wrong. If gel goes up to $55, FAQ-02 fails for a good reason.

Make it a habit. Any PR that changes the FAQ, the rules or the handoff message also updates the golden set in the same PR. Reviewers should ask "did the golden set change too?"

**You're done when** you've written that habit down somewhere your team will see it, like your PR template.

## Quick check

<details>
<summary>1. Your prompt now passes every dev case. The held-out cases didn't improve. What does that tell you?</summary>

The prompt probably got better at the test, not at real customers. That's overfitting.
</details>

<details>
<summary>2. A held-out case fails. Do you fix the prompt while reading that case?</summary>

No. Find or write a dev case with the same pattern, fix the prompt against that, then check the held-out case again.
</details>

<details>
<summary>3. The salon changes its prices. What else changes in the same PR?</summary>

The golden set. Any case that checks a price needs updating, or it'll fail for the wrong reason.
</details>

---

**Next: [Part 4 (How many cases is enough)](part-4-how-many-cases.md)** | [Back to the lesson](README.md)
