<sub>Lesson 4, Part 4 of 5 · about 15 min</sub>

# Your PRs are your paper trail

**In this part,** you'll rewrite the cancellation PR so it works as a record, link it to a ticket, add a description template to your fork, and see why small PRs are worth the extra clicks.

## Why this matters

Every PR you open becomes part of the product's history. When someone asks "why did we change this?", they'll find the PR before they find you. If the title says "Update cancellation copy" and the description is one line, the answer is lost. If it says what changed, why, how it was checked and what was left out, the PR answers for you.

It works the other way too. A list of clear PRs is the easiest proof of what you've shipped.

## Titles name the outcome, not the mechanism

**A title gets read in a list, next to dozens of others, with no context.** So it should say what the PR delivers and where it sits in the work. How it does it goes in the description.

This is the mistake I make most, so I'll show you mine. I once titled a PR "Hold the frame still between screens, and move only the content". Every word was accurate. Nobody scanning the list could tell what it meant for the work. The better title was "Final pass: motion, with the full test and eval record". It says what the PR delivers (the motion work), where it sits (the final pass) and what a reviewer gets (the full record).

Here's the same idea on salon PRs:

| Mechanism (weak) | Outcome and position (better) |
|---|---|
| Update cancellation copy | Cancellation policy: 48 hours' notice to keep your deposit |
| Add two bullets under Payment | First FAQ addition: the assistant can answer gift card questions |
| Change system prompt wording | Must-escalate fix: buried swelling now gets the handoff |
| Add test file | Golden set runs on every PR, part 1 of 2 |

Three habits that help:
1. **Read it out loud.** If you stumble, it's probably describing machinery.
2. **Say the position** when the PR is one of several, like "part 1 of 2", "first pass" or "final pass".
3. **Flag the one to read first.** If this is the PR a reviewer should open before the others, say so in the title.

<details>
<summary><strong>Go deeper (three names, three jobs)</strong></summary>

A change usually gets three names, and each has a different reader.
- **Branch name.** The type of work, then a short name: `copy/cancellation-48h`, `fix/buried-swelling`, `docs/faq-gift-cards`. It makes a list of branches easy to scan.
- **Commit message.** One change, starting with a verb, about 50 characters and never over 72: `Update deposit line to match 48-hour rule`. Commits can describe the mechanism. That's their job.
- **PR title.** The outcome and the position, as above.

When you're the only reviewer, it can help to put the status in the title too, like "(draft)" or "waits on my OK". On a team, leave status to GitHub's badges and labels.
</details>

## Do it (step by step)

### 9. Fix the PR, then rewrite its title and description

**Make the PR match what a reviewer would approve, then make the page explain it.** On your `copy/cancellation-48h` branch:
1. Accept your own suggestion from Part 3, or edit the second bullet so it says `48 hours'` too.
2. Change the lateness line back to `15 minutes`. It wasn't asked for, so it doesn't belong here.
3. Open `06-evals-101/salon-golden-set.csv` on the same branch and update FAQ-05's `expected_behaviour` so it describes the 48-hour rule.

Commit each edit to the same `copy/cancellation-48h` branch, not a new one, so they all land in this PR. Then click **Edit** next to the PR title and change it to `Cancellation policy: 48 hours' notice to keep your deposit`. Open [`pr-description-template.md`](pr-description-template.md), click **Raw** to see the hidden notes, and copy it into the description. Here's what mine looks like filled in:

```markdown
## What
Customers now need to cancel or reschedule 48 hours ahead to keep their
deposit, up from 24. Both cancellation lines say 48 so they agree.

## Why
The owner asked for more notice so last-minute gaps can be filled.
- Ticket or spec: #12
Closes #12

## How I checked it
- Read the diff. Only the two cancellation lines and FAQ-05 changed.
- Updated FAQ-05 to expect the 48-hour rule, and the golden set check passes.

## Not in this PR
- What happens to bookings made under the 24-hour rule. Waiting on the owner.
- The lateness window. If it changes, it gets its own PR.
- The confirmation email and the front desk sign.
```

You're done when the title says the outcome, the description has all four sections, and Files changed only shows the cancellation lines and FAQ-05.

<details>
<summary>Stuck?</summary>

- **You don't see a Commit suggestion button.** No problem. Edit the file with the pencil on your branch instead. The PR updates on its own.
- **You don't have issue #12.** That's fine. Open an issue on your fork called "Owner wants 48 hours' notice for cancellations" and use its number, or delete the Closes line.
- **The golden set check isn't real yet.** Right, it's imaginary until [Evals in CI](../09-evals-in-ci/). Write what you actually checked. Never claim a check you didn't run.
</details>

### 10. Link it to the ticket and close it without merging

**Connect the PR to where the decision lives, then decide what happens to it.** If you used `Closes #12`, GitHub links the issue on the PR page. It would close the issue when the PR merges into your default branch. GitHub's closing words are close, closes, closed, fix, fixes, fixed, resolve, resolves and resolved, and they only work when the PR targets the default branch ([GitHub Docs, Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)).

For this course, Polish & Co. keeps the 24-hour rule, so the later lessons still match. Leave a comment saying "Closing. The owner decided to keep 24 hours for now." and click **Close pull request**.

That's a real decision, and the closed PR is part of the record. Anyone who suggests 48 hours later can find exactly what was tried, the discussion and why it didn't go ahead.

You're done when the PR shows a red **Closed** badge with your comment above it.

### 11. Add the template to your fork

**Make every new PR start from the four sections.** In your fork, click **Add file**, then **Create new file**. Name it `.github/pull_request_template.md`. Typing the slash creates the folder. Paste in the template, commit it on a new branch called `docs/pr-template`, and open a PR with the title `Every new PR starts from the four-part description template`. Merge it.

Now start any new PR on your fork. The description box fills in on its own.

GitHub only uses the template once it's on the default branch ([GitHub Docs, Creating a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)). That's why you merge it first.

You're done when a new PR on your fork opens with What, Why, How I checked it and Not in this PR already in the box.

## Small PRs beat big ones

Look at what step 9 did. Sam's PR had two policy changes in it. You took one out. That's the habit.

Small PRs are better for everyone. Google's guide on small changes lists the reasons:
- They're reviewed faster and more thoroughly.
- They're less likely to introduce bugs.
- They're easier to roll back.
- Less work is wasted if one gets rejected.

([Google Engineering Practices, Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html))

For a PM there's one more. A small PR is one decision. It can be approved, rejected or rolled back on its own, and its history is easy to read. A big PR mixes decisions, and you end up approving things nobody looked at closely.

My rule is one PR, one purpose, small enough to review in one sitting.

<details>
<summary><strong>Go deeper (when a PR has to be big)</strong></summary>

Sometimes the work really is big. A few ways to keep the review manageable:
- **Split by layer.** Data changes in one PR, the screen in the next.
- **Split by step.** "Part 1 of 3: the FAQ loader", "Part 2 of 3: the answer", "Part 3 of 3: the tests". Say the position in each title.
- **Open a draft early.** Share the direction before it's finished, so nobody spends a week on the wrong approach.
- **Stack carefully.** A PR can target another PR's branch. Merge them in order and keep the stack to one level. If the children merge first, they land in the parent's branch and never reach `main`.
- **Write the map.** In the first PR's description, list the whole plan so reviewers can see where each piece fits.
</details>

## Quick check

<details>
<summary>1. Rewrite "Change system prompt wording" as an outcome title.</summary>

Something like "Must-escalate fix: buried swelling now gets the handoff". It says what the change delivers and what kind of work it is. The wording change goes in the description.
</details>

<details>
<summary>2. Why close the 48-hour PR instead of deleting the branch and forgetting it?</summary>

A closed PR with a comment is part of the record. It shows what was tried, the discussion and why it didn't go ahead, so the next person who suggests it can see the decision.
</details>

<details>
<summary>3. Why didn't <code>Closes #12</code> close the issue?</summary>

Closing words only work when the PR merges into the default branch. This PR was closed without merging, so the issue stays open.
</details>

---

**Next: [Part 5 (Wrap up)](part-5-wrap-up.md)** | [Back to the lesson](README.md)
