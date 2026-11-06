<sub>Lesson 4, Part 2 of 5 · about 15 min</sub>

# Read a PR like a PM

**In this part,** you'll review a made-up PR that changes the Polish & Co. cancellation policy, using the five places from Part 1, and write down what you'd raise.

## The PR you're reviewing

Sam, a teammate, opened this PR on the salon's repo. The owner asked for a longer cancellation window, and there's a ticket for it. Here's what you see when you open the PR.

> **Update cancellation copy** #14
>
> `copy/cancellation` into `main` · opened by Sam
>
> **Description**
> Updates the cancellation section.

**Files changed** · 1 file, 2 lines added, 2 removed · `example/README.md`

```diff
 **Cancellations and lateness**
-- Cancel or reschedule at least 24 hours ahead to keep your deposit.
+- Cancel or reschedule at least 48 hours ahead to keep your deposit.
 - Less than 24 hours' notice, or a no-show, and the deposit isn't refunded.
-- More than 15 minutes late and we may need to shorten or move your appointment.
+- More than 10 minutes late and we may need to shorten or move your appointment.
```

**Checks**

```text
Spell check          passed
Golden set evals     failed   FAQ-05 (1 of 20 cases)
```

Imagine the repo already runs the golden set from [Evals 101](../06-evals-101/) on every PR. You'll set that up for real in [Evals in CI](../09-evals-in-ci/).

## Do it (step by step)

### 1. Read the title and description first

**Before you look at any changes, ask what this PR says it does and why.** The title and description are the author's claim. Everything else on the page is evidence for or against it.

Here, the title says "Update cancellation copy". That's the mechanism. It doesn't tell you the outcome (customers now need 48 hours' notice) or that this is a policy change, not a typo fix. The description is one line with no reason, no link to the ticket and nothing on how it was checked.

Write down two things you'd want added. You're done when you have them.

### 2. Compare the diff with the description

**Check that the change does what the description says, and nothing more.** Open Files changed in your head and go line by line. You don't need to know code for this one, but the habit is the same on a code PR. Read the file names and the line counts first, then the changes.

Ask yourself:
1. Is every change in the diff mentioned in the description?
2. Does anything nearby now contradict the change?
3. Are there numbers, prices or customer-facing words? Those are always worth a PM's eye.

You're done when you've found two problems in the diff itself. Look at the lines that didn't change too.

<details>
<summary>Stuck?</summary>

- **"I don't see anything wrong."** Read the second bullet, the one with no `+` or `-` in front. It didn't change. Does it still agree with the line above it?
- **"The lateness line looks fine to me."** It might be fine. The question is whether anyone asked for it. It isn't in the title or the description.
</details>

### 3. Read the checks, then ask what the failure means

**A failing check doesn't always mean the change is wrong. Sometimes the test needs updating.** FAQ-05 is the golden set case about cancelling tomorrow morning. Its expected behaviour still describes the 24-hour rule. So the eval failed because the policy changed, which is exactly what it should do.

That leaves a decision, and it's a product one:
- If 48 hours is right, the PR should update FAQ-05 in the same PR, so the record shows the test changed on purpose.
- If nobody meant to change the rule that much, the eval just caught a real problem.

Either way, nobody should merge with a red check and no comment explaining it.

You're done when you can say in one sentence why FAQ-05 failed.

### 4. Think past the diff

**Ask what else has to change for this to be true for customers.** A PR only shows what's in the repo. The real world has more:
- Customers who already booked under the 24-hour rule. Does the old rule still apply to them?
- The booking confirmation email, the website and the sign at the front desk
- Staff, who'll get asked about it
- When it takes effect

You don't need answers to all of these in the PR. You do need the PR to say which ones are handled and which aren't. That's what a "Not in this PR" section is for.

You're done when you have at least one question about something outside the diff.

### 5. Write down your findings

**Make a short list before you leave any comments.** Sort it into "must fix before merge" and "nice to have". You'll turn it into review comments in Part 3.

<details>
<summary><strong>What I found (open after you've made your list)</strong></summary>

Must fix before merge:
1. **The policy now contradicts itself.** You keep your deposit with 48 hours' notice, and lose it with less than 24. What happens at 30 hours? The second line needs to say 48 too, or the rule needs rewriting.
2. **There's an unexplained change.** Lateness went from 15 minutes to 10. It's not in the title or description. It might be intended, but it should be its own PR with its own reason.
3. **FAQ-05 is red with no explanation.** Update the eval case in this PR if 48 hours is the new rule.

Nice to have:
1. **A title that says the outcome**, something like "Cancellation policy: 48 hours' notice to keep your deposit".
2. **A description with the why and a ticket link**, plus how existing bookings are handled and what's not in this PR.
</details>

## What to look for without reading every line

Here's the list I run on any PR, whether it's copy or code:
1. **Title.** Can I tell the outcome from the title alone?
2. **Description.** Is there a reason, a link to the ticket or decision, and a "How I checked it"?
3. **Size.** How many files and lines? A small copy change that touches 30 files is a question.
4. **File names.** Do they match the description? A pricing change shouldn't touch the login code.
5. **Customer-facing words and numbers.** Prices, policies, error messages and emails. Read every one.
6. **Tests next to code.** If code changed, did tests or evals change with it? If not, ask how it was checked.
7. **Checks.** Did the checks you expect run, and are they green? If one's red, is there a comment?
8. **Conversation.** Are earlier questions answered? Who approved?

<details>
<summary><strong>Go deeper (reading a code PR you didn't write)</strong></summary>

When the diff is code you can't fully read, you can still review it well:
- **Ask the author where to start.** "Which file is the heart of this?" is a normal question. Good authors say it in the description.
- **Read the tests first.** Test names often read like plain sentences ("rejects a booking without a deposit"). They tell you what the author thinks the code does.
- **Click the preview link** if there is one, and try the change like a customer would.
- **Ask an AI to explain the diff in plain words.** Then check its explanation against the description and the tests. An AI can describe code confidently and still get it wrong, so treat its summary as a lead, not a verdict.
- **Leave design and correctness to the engineers, and own the product questions.** Google's review guide says "The most important thing to cover in a review is the overall design of the CL" ([What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)). CL is Google's word for a PR. For a PM, the product version of design is: does this solve the right problem for the right customer?
</details>

## Quick check

<details>
<summary>1. The eval FAQ-05 failed on Sam's PR. Does that mean the PR is wrong?</summary>

Not necessarily. FAQ-05 still expects the 24-hour rule, so it failed because the policy changed. If 48 hours is the new rule, the PR should update FAQ-05 too. Either way, it shouldn't merge with a red check and no explanation.
</details>

<details>
<summary>2. Why flag the lateness change if it might be fine?</summary>

Because nobody said it was happening. It's not in the title or the description, so it hasn't been decided on purpose. It should be its own PR with its own reason.
</details>

---

**Next: [Part 3 (Leave a review that helps)](part-3-leave-a-useful-review.md)** | [Back to the lesson](README.md)
