<sub>Lesson 3, Part 3 of 4 · about 20 min</sub>

# Open, review and merge your PR

**In this part,** you'll write a title and description, read your own diff like a reviewer, then merge and tidy up.

### 6. Write the title and description

**Write a title someone can understand in a list with no context.** A PR title gets read next to dozens of others. Say what the change does for the work and where it sits. Leave the mechanics for the description. Compare these:
- Good: `First FAQ addition: the assistant can answer gift card questions`
- Weak: `Add two bullets under Payment`

The weak one is accurate. It just doesn't tell anyone why they should care.

For the description, I use the same four parts every time. Paste this in and edit it to match what you did:

```markdown
## What
Adds a Gift cards section to the Polish & Co. FAQ.

## Why
Customers ask about gift cards and the assistant can only answer from the FAQ.
Right now it has to say it doesn't know.

## How I checked it
- Previewed the file. The new section matches the others.
- Read the diff. Only the new lines changed.

## Not in this PR
- Gift card balance checks. The assistant can't look those up.
```

Click **Create pull request**.

You're done when you land on your new PR, with a green **Open** badge under the title.

<details>
<summary>Stuck?</summary>

- **You can't find the description box.** It's the large box under the title, with Write and Preview tabs.
- **You picked draft by mistake.** That's fine. A draft can't be merged until you click **Ready for review** near the bottom of the Conversation tab.
</details>

> **Pause and think.** Your PR has a "How I checked it" section. If an AI agent had written this change for you, what would you want in that section before you trusted it?

### 7. Review your own diff

**Read exactly what changed before you merge anything.** Click the **Files changed** tab. This is the diff. Lines in green were added and lines in red were removed. You should see your new lines in green and nothing in red.

Now try leaving a comment like a reviewer would. Hover over one of your green lines, click the blue comment icon next to the line number, write a note to yourself, and click **Comment**.

You're done when you've read every changed line and left one comment.

<details>
<summary>Stuck?</summary>

- **There's red you didn't expect.** You changed or deleted something by accident. Go back to the file on your branch, fix it with the pencil, and commit to the same branch. The PR updates on its own.
- **You see an extra blank line in green.** The editor hides these. The diff doesn't. Fix it the same way if you want it clean.
</details>

### 8. Merge it and tidy up

**Accept your own change, then delete the branch.** Go back to the **Conversation** tab and scroll to the bottom. Click **Merge pull request**, then **Confirm merge**. After it merges, click **Delete branch**. The branch has done its job, and the PR keeps the full record of what happened.

You're done when the PR shows a purple **Merged** badge and `example/README.md` on your `main` branch has the gift card section.

<details>
<summary>Stuck?</summary>

- **You don't see Merge pull request.** Check that you're on your own fork's PR. On someone else's repo, only people with write access can merge.
- **You deleted the branch and want it back.** There's a **Restore branch** button on the PR.
</details>

Congrats, you just shipped your first pull request.

**Prefer a different tool?**

| Browser | Terminal | Desktop app |
|---|---|---|
| This guide | [The terminal route](extra-credit.md#go-deeper-terminal-route) in Extra credit | [GitHub Desktop docs](https://docs.github.com/en/desktop) |

<details>
<summary><strong>Go deeper (Advanced): how teams run PRs at scale</strong></summary>

- **Merge gates.** Branch protection can require passing checks and an approving review before anything merges. A useful bar is checks green, one reviewer's sign-off, and every comment fixed or answered.
- **Checks that didn't run.** CI workflows can be filtered by file path. If your PR didn't trigger the checks you expected, look at the workflow's `paths:` setting before you assume everything passed.
- **PR templates.** A `pull_request_template.md` fills in the description for every new PR, but only once it's on the default branch.
- **Stacked PRs.** A PR can target another PR's branch instead of main. Merge them in order, and keep the stack to one level. If you merge the children before the parent, they land in the parent's branch and never reach main.
- **Public history.** In a public repo, every PR stays visible after its branch is deleted. Check branches and PRs for secrets before you make a repo public.
</details>

## Quick check

<details>
<summary>1. What do green and red lines mean on the Files changed tab?</summary>

Green lines were added and red lines were removed. For this PR you should see your new lines in green and nothing in red.
</details>

<details>
<summary>2. Which is the better PR title, and why? "Add two bullets under Payment" or "First FAQ addition: the assistant can answer gift card questions"</summary>

The second one. A PR title gets read next to dozens of others, so it should say what the change does for the work and where it sits. The first one is accurate, but it doesn't tell anyone why they should care.
</details>

---

**Next: [Part 4 (Wrap up)](part-4-wrap-up.md)** | [Back to the lesson](README.md)
