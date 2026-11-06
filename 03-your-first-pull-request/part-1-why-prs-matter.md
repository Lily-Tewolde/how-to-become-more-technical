<sub>Lesson 3, Part 1 of 4 · about 10 min</sub>

# Why PRs matter, and your own copy

**In this part,** you'll see why the PR matters to a PM, then make your own copy of the hub and open the file you'll change.

**Quick check before you start.** If you can answer both of these, skip to the [terminal route](extra-credit.md#go-deeper-terminal-route) in Extra credit.
1. What's the difference between pushing a change and merging it?
2. Why would you make a branch for a two-line change?

## Why PRs matter for a PM

Here's the short version. The PR is where a change is:
1. described, so anyone can see what changed and why
2. reviewed by someone who isn't the author
3. tested, because automated checks and evals run on it
4. discussed and approved before it reaches users

That makes it the paper trail of product decisions. It's also where AI coding agents hand their work back to you for review. And builder roles are starting to ask how many PRs you shipped last month. The full story is in the next lesson, [Why PRs matter for a PM](../04-why-prs-matter-for-pms/).

## Do it (step by step)

You'll make a real PR inside your own copy of the hub. That way you get to be the author, the reviewer and the person who merges, all in one sitting.

### 1. Fork the hub

**Make your own copy of the hub so you can change it.** You can't edit my copy directly, and that's normal. A fork is a copy that lives under your account, where you're the owner. Go to [Lily-Tewolde/how-to-become-more-technical](https://github.com/Lily-Tewolde/how-to-become-more-technical), click **Fork** in the top right corner, check your account is selected under **Owner**, keep the repository name, and click **Create fork**.

You're done when the top left of the page shows `YOUR-USERNAME/how-to-become-more-technical` with "forked from Lily-Tewolde/how-to-become-more-technical" under it.

<details>
<summary>Stuck?</summary>

- **GitHub took you to a repo instead of the fork form.** You've probably forked it before. That's your fork, so carry on from there.
- **You don't see a Fork button.** Make sure you're signed in. The button sits at the top right of the repo page, next to Watch and Star. On a narrow screen it can be tucked into a menu.
</details>

### 2. Open the FAQ file

**Find the file the assistant answers from.** In your fork, click the `example` folder, then click `README.md`. This is the Polish & Co. FAQ. Click the pencil icon at the top right of the file to start editing.

You're done when the file opens in a text box you can type in.

<details>
<summary>Stuck?</summary>

- **GitHub says you need to fork the repository to make changes.** You're on my original. Check the name at the top left. It should start with your username.
- **You don't see a pencil.** Make sure you clicked into the file itself, not the folder.
</details>

<details>
<summary><strong>Go deeper (Advanced): what's going on under the hood</strong></summary>

- **A PR is a GitHub feature.** Git itself has no pull request button. Developers used to email a project's maintainer asking them to pull changes from their branch. GitHub turned that request into a web page with a diff, a comment thread and checks.
- **Fork or branch.** A branch lives inside one repo. A fork is a whole second repo. Teams with write access usually branch inside the main repo. Outside contributors fork, because they can't push to the original.
- **Merge, squash or rebase.** A merge commit keeps every step of the PR on main. Squash folds the PR into one commit on main, and the steps stay on the PR page. Rebase replays each commit on top of main with no merge commit. Squashing doesn't hide old commit messages or titles once a repo is public, because the PR page keeps them.
- **Drafts.** A draft PR can't be merged and doesn't ask code owners for review. Use one to share work in progress.
- **Keep PRs small.** Google's guide on small changes lists the reasons: faster and more thorough reviews, fewer bugs, easier rollbacks, and less work lost if a change is rejected.
</details>

## Quick check

<details>
<summary>1. Name the four things that happen to a change in a PR.</summary>

It's described, reviewed by someone who isn't the author, tested, and discussed and approved before it reaches users.
</details>

<details>
<summary>2. Why can't you edit my copy of the hub directly?</summary>

You're not the owner of my copy. A fork is a copy that lives under your account, where you're the owner, so that's where you make your change.
</details>

---

**Next: [Part 2 (Make your change on a branch)](part-2-make-your-change.md)** | [Back to the lesson](README.md)
