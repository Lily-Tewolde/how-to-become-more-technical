<sub>Lesson 3, Part 2 of 4 · about 15 min</sub>

# Make your change on a branch

**In this part,** you'll add a gift card answer to the FAQ, save it to a new branch and point the PR at your own fork.

### 3. Add your FAQ answer

**Add a gift card answer under the Payment section.** Polish & Co. gets a lot of gift card questions, and right now the assistant has to say it doesn't know. Put your cursor after the Payment bullet, leave one blank line, and paste this in:

```markdown
**Gift cards**
- Gift cards come in any amount from $25. Buy them at the front desk or online.
- They never expire and can be used for any service.
```

Then click **Preview** above the text box. Check that "Gift cards" shows in bold like the other headings, with two bullets under it.

You're done when the preview looks like the rest of the FAQ.

<details>
<summary>Stuck?</summary>

- **The heading doesn't look bold in the preview.** Check there are two asterisks on each side of `Gift cards` and no spaces inside them.
- **The bullets run into the Payment section.** Add a blank line between the Payment bullet and `**Gift cards**`.
- **You'd rather add parking.** Go for it. Keep it short and in the same style as the other sections.
</details>

### 4. Save your change to a new branch

**Commit the change to a branch so your main version stays clean.** Click **Commit changes...** at the top right. A box opens.
- In **Commit message**, write `Add gift card answer to the FAQ`. Start with a verb and keep it short.
- Choose **Create a new branch for this commit and start a pull request**.
- Name the branch `docs/faq-gift-cards`. I start every branch name with the type of work (`docs/`, `fix/`, `copy/`), so the list of branches is easy to scan.
- Click **Propose changes**.

You're done when GitHub opens a page for opening a pull request.

<details>
<summary>Stuck?</summary>

- **You committed straight to main by accident.** No harm done, it's your fork. Make your next change (try a parking answer) and pick the new branch option this time. You'll still get your PR.
- **The branch option isn't there.** Check that you're in your fork, not my original. The two options sit under the commit message box.
</details>

### 5. Point the PR at your own fork

**Make sure the PR merges into your own fork.** Look at the bar at the top of the page. Because your copy is a fork, GitHub often sets the **base repository** to my original. Click it and choose `YOUR-USERNAME/how-to-become-more-technical`. Once you do, the bar shrinks to two dropdowns:
- **base:** `main` (where the change is going)
- **compare:** `docs/faq-gift-cards` (where the change is now)

You're done when the base is your fork's `main` and the compare is your new branch.

<details>
<summary>Stuck?</summary>

- **It says "There isn't anything to compare."** The two dropdowns are pointing at the same branch, or the wrong way round. Base is the destination and compare is your branch.
- **You already opened it against my original.** Close it with the **Close pull request** button at the bottom of the Conversation tab, then open a new one from your fork. Nothing is lost.
</details>

## Quick check

<details>
<summary>1. Why does your commit go on a new branch instead of main?</summary>

So your main version stays clean. The change waits on its branch until you merge it.
</details>

<details>
<summary>2. On the compare page, which dropdown is the destination?</summary>

**base** is the destination, your fork's `main`. **compare** is your branch, `docs/faq-gift-cards`, where the change is now.
</details>

---

**Next: [Part 3 (Open, review and merge your PR)](part-3-open-review-merge.md)** | [Back to the lesson](README.md)
