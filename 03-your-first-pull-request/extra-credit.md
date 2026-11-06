<sub>Lesson 3, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll make the same kind of PR from your own computer, using the terminal. It's optional. Skip it if the browser route did what you needed.

<a name="go-deeper-terminal-route"></a>
<details open>
<summary><strong>Go deeper (Advanced): the terminal route</strong></summary>

Same PR, made from your own computer. You'll need git installed and a way to sign in to GitHub from the terminal. GitHub no longer accepts your account password for git, so use a personal access token, a credential helper like Git Credential Manager, or `gh auth login` if you have the [GitHub CLI](https://cli.github.com/).

This time, add a parking answer so you have something new to change.

```bash
# 1. Copy your fork to your computer
git clone https://github.com/YOUR-USERNAME/how-to-become-more-technical.git
cd how-to-become-more-technical

# 2. Make a branch (older git versions: git checkout -b docs/faq-parking)
git switch -c docs/faq-parking

# 3. Edit example/README.md in any editor, then check what changed
git diff

# 4. Stage and commit the one file
git add example/README.md
git commit -m "Add parking answer to the FAQ"

# 5. Push the branch to your fork on GitHub
git push -u origin docs/faq-parking

# 6. Open the PR against your fork's main
gh pr create --repo YOUR-USERNAME/how-to-become-more-technical --base main \
  --title "Second FAQ addition: the assistant can answer parking questions" \
  --body "What, Why, How I checked it, Not in this PR"
```

No GitHub CLI? After step 5, open your fork on GitHub and click **Compare & pull request** in the yellow banner. Then carry on from [step 5 of the browser route](part-2-make-your-change.md#5-point-the-pr-at-your-own-fork).

Push and merge are different steps. Pushing uploads your commits whenever you like, and an open PR updates each time you push. Merging is the one step that waits for someone's OK.

To pull my latest lessons into your fork later, click **Sync fork** on your fork's main page, then **Update branch**. From the terminal, add my repo as `upstream` once, then fetch and merge it:

```bash
git remote add upstream https://github.com/Lily-Tewolde/how-to-become-more-technical.git
git fetch upstream
git checkout main
git merge upstream/main
git push
```
</details>

---

[Back to the lesson](README.md) | [Part 4 (Wrap up)](part-4-wrap-up.md)
