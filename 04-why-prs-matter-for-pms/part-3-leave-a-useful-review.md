<sub>Lesson 4, Part 3 of 5 · about 15 min</sub>

# Leave a review that helps

**In this part,** you'll recreate Sam's PR in your own fork, leave review comments the author can act on, and submit a review.

## What makes a review comment useful

A useful comment does four things:
1. **It's about the change, not the person.** Google's review guide puts it simply: make comments about the code and never about the developer ([How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html)).
2. **It says why.** "This contradicts the line below, so a customer at 30 hours won't know where they stand" gets fixed. "This is wrong" gets a reply asking what you mean.
3. **It says how much it matters.** The author needs to know which comments block the merge and which are ideas.
4. **It suggests a next step.** A question, a fix or a suggested wording.

I start each comment with a label so the author can sort them at a glance. These come from [Conventional Comments](https://conventionalcomments.org/), and I only use a few:

| Label | What it means |
|---|---|
| `issue (blocking):` | Has to be fixed before this merges |
| `question:` | I'm not sure, and I need an answer before I can approve |
| `suggestion (non-blocking):` | A better way, but the author can say no |
| `nit:` | Tiny and optional, like a typo or wording preference |
| `praise:` | Something done well. Say it. It's how good habits stick |

## Do it (step by step)

### 6. Recreate Sam's PR in your fork

**Make the same change in your fork so you can practise on a real PR page.** In your fork, open `example/README.md`, click the pencil, and in the Cancellations section change:
- `24 hours ahead` to `48 hours ahead` in the first bullet
- `15 minutes late` to `10 minutes late` in the third bullet

Leave the second bullet alone. That's the contradiction you'll comment on.

Click **Commit changes...**, choose **Create a new branch for this commit and start a pull request**, name the branch `copy/cancellation-48h`, and click **Propose changes**. Point the base at your fork's `main` like you did in Lesson 3. Use Sam's title and description on purpose, `Update cancellation copy` and `Updates the cancellation section.` You'll fix them in Part 4.

You're done when your PR is open and Files changed shows two red lines and two green lines.

<details>
<summary>Stuck?</summary>

- **The base is my original repo.** Click the base repository dropdown and choose your fork. Lesson 3, [step 5](../03-your-first-pull-request/part-2-make-your-change.md#5-point-the-pr-at-your-own-fork), has the details.
- **Your fork is behind.** If the FAQ in your fork looks different from the running example, click **Sync fork** on your fork's main page first.
</details>

### 7. Leave three line comments

**Comment on the exact line, with a label, the reason and a next step.** On Files changed, hover over a line number, click the blue comment icon, write your comment and click **Start a review**. For the next comments, the button says **Add review comment**. They all wait in one review until you submit it.

Here are the three I'd leave. Write yours in your own words.

On the new 48-hours line:

```markdown
issue (blocking): This now contradicts the next line. You keep your deposit
with 48 hours' notice but only lose it under 24, so a customer cancelling at
30 hours doesn't know where they stand. Can the next line say 48 too?
```

On the lateness line:

```markdown
question: Was the lateness change from 15 to 10 minutes intended? It isn't in
the title or description. If it is, could it go in its own PR with the reason,
so each policy change has its own record?
```

On the 48-hours line and the line under it, using GitHub's suggestion feature, so the author can accept your wording with one click. Click the first line number and drag down to the second before you click the comment icon, so the comment covers both lines:

````markdown
suggestion (non-blocking): One way to make both lines agree.

```suggestion
- Cancel or reschedule at least 48 hours ahead to keep your deposit.
- Less than 48 hours' notice, or a no-show, and the deposit isn't refunded.
```
````

A suggestion block replaces the lines your comment covers with the text inside it. That's why it has both lines in it.

You're done when you have three pending comments on Files changed.

<details>
<summary>Stuck?</summary>

- **The comment posted on its own instead of joining a review.** You clicked **Add single comment**. That's fine. It just notifies the author right away instead of all at once.
- **The suggestion shows as plain text.** Check the three backticks and the word `suggestion` are on their own line, with the closing backticks on their own line too.
</details>

### 8. Submit the review

**Send all your comments at once, with a short summary and a decision.** Click **Review changes** at the top of Files changed. Write a one or two line summary, like "Two things to fix before this goes out: the 24/48 contradiction and the unexplained lateness change. FAQ-05 will need updating too." Then pick one:
- **Comment.** General feedback, no decision.
- **Approve.** Ready to merge.
- **Request changes.** The author has to address your feedback before merging.

Click **Submit review**.

On a team PR with a blocking issue, you'd choose **Request changes**. On your own PR, GitHub won't let you approve or request changes, so choose **Comment**.

You're done when your review shows on the Conversation tab with all three comments under it.

> **Pause and think.** If an AI agent had opened this PR, would any of your comments change? Would you trust its description more or less than Sam's?

<details>
<summary><strong>Go deeper (reviewing as the PM on a real team)</strong></summary>

- **Know which hat you're wearing.** On most teams the PM isn't the required code reviewer. Say what you're reviewing ("Reviewing the copy and the policy, not the code") so engineers know your approval doesn't cover their part.
- **Answer fast.** A PR waiting on the PM is a blocked engineer. If you can't review today, say when you can.
- **Comment, then talk.** If a thread goes back and forth more than twice, hop on a call, then write the outcome in the PR so the record stays complete.
- **Don't redesign in review.** If the PR shows the ticket was wrong, that's a conversation about the ticket. Fix the spec, then the PR.
- **Say what's good.** Google's guide says "If you see something nice in the CL, tell the developer" ([What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)).
</details>

## Quick check

<details>
<summary>1. What are the four things a useful review comment does?</summary>

It's about the change, not the person. It says why. It says how much it matters. It suggests a next step.
</details>

<details>
<summary>2. You found a blocking issue on a teammate's PR. Which review option do you pick?</summary>

**Request changes.** It tells the author they need to address your feedback before merging.
</details>

---

**Next: [Part 4 (Your PRs are your paper trail)](part-4-your-paper-trail.md)** | [Back to the lesson](README.md)
