<sub>Lesson 3, Part 4 of 4 · about 15 min</sub>

# Wrap up

**In this part,** you'll check your PR against the list, try a second PR as a challenge and practise the questions you'd get in an interview.

## Common mistakes

- **Wrong:** opening the PR against my original repo by accident. **Instead:** check the base repository on the compare page. For this lesson it should be your fork.
- **Wrong:** a title that describes the edit ("Update README"). **Instead:** say what the change does for the work ("First FAQ addition: the assistant can answer gift card questions").
- **Wrong:** merging without opening Files changed. **Instead:** read the diff every time, even for two lines.
- **Wrong:** putting several unrelated changes in one PR. **Instead:** one PR, one purpose, small enough to review in one sitting.

## What I learned doing this

My PR titles used to describe the machinery. One of them was "Hold the frame still between screens, and move only the content". It was accurate, but nobody scanning a list of PRs could tell what it meant for the work. The better title was "Final pass: motion, with the full test and eval record". It says what the PR delivers and where it sits. If it's the PR someone will read first, I say that too.

Reading the diff has saved me more than once. It shows things the editor hides, like leftover blank lines. I open Files changed on every PR now, even the tiny ones.

## You're done when

- [ ] You have a fork of the hub under your own account
- [ ] Your PR has an outcome title and a description with What, Why, How I checked it and Not in this PR
- [ ] You've read the Files changed tab and left one line comment
- [ ] Your PR shows Merged and the branch is deleted
- [ ] The gift card section is on your fork's `main`

## Challenge

Open a second PR on your fork, this time as a draft. Add another answer a salon customer might want, like whether they can bring their own polish. Write the four-part description, then mark it **Ready for review**. Ask a friend to leave a comment on Files changed before you merge. If you want, share your PR title in the hub's Discussions.

Want to try it from the terminal? The [Extra credit](extra-credit.md) page (optional, Advanced) walks through the same PR on your own computer.

## Check yourself (interview style)

<details>
<summary>1. A stakeholder asks what a pull request is. What do you say in one sentence?</summary>

It's a proposal to change a project, with the change, the reason and the review in one place, so the team can check it before it's merged.
</details>

<details>
<summary>2. What's the difference between a fork and a branch?</summary>

A branch is a separate line of work inside one repo. A fork is your own copy of the whole repo under your account. You fork when you can't push to the original, and you branch inside whichever repo you're working in.
</details>

<details>
<summary>3. What's the difference between pushing and merging?</summary>

Pushing uploads your commits to GitHub, and you can do it as often as you like. An open PR updates every time you push. Merging brings the changes into the main branch, and it's the step that waits for approval.
</details>

<details>
<summary>4. You're reviewing a PR titled "Update handler logic". What would you ask the author for?</summary>

A title that says what the change does for the work and where it sits, plus a description covering what changed, why, how they checked it and what's left out. Then I'd read Files changed myself.
</details>

<details>
<summary>5. Why do teams prefer small PRs?</summary>

They're faster to review and get a more careful review. They cause fewer bugs and fewer merge conflicts, they're easier to roll back, and less work is lost if one gets rejected.
</details>

## Further reading

**Start here**
- [Introduction to GitHub](https://github.com/skills/introduction-to-github), GitHub Skills. A guided browser exercise where you branch, commit, open and merge a PR in under an hour. Good for a second rep.
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), GitHub Docs. The official explainer for the tabs on a PR, drafts and checks.
- [first-contributions](https://github.com/firstcontributions/first-contributions), firstcontributions. The classic first-PR tutorial using the terminal, with links to GUI versions. This guide follows its step shape.

**Go deeper**
- [Code review developer guide](https://google.github.io/eng-practices/review/), Google Engineering Practices. How reviewers and authors work together at Google.
- [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) and [Writing good CL descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html), Google Engineering Practices. Why small changes ship faster, and how to write a first line and body that make sense later.
- [How to write the perfect pull request](https://github.blog/developer-skills/github/how-to-write-the-perfect-pull-request/), Keavy McMinn, GitHub Blog. The PR description as communication, which is the part PMs are already good at.
- [Oh Shit, Git!?!](https://ohshitgit.com/), Katie Sylor-Miller. Plain-English fixes for when something goes wrong in the terminal.

**Primary sources**
- [Pro Git, 2nd edition](https://git-scm.com/book/en/v2), Scott Chacon and Ben Straub. The official free git book. Start with [Contributing to a Project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project) for forks and PRs.
- GitHub Docs on [editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files), [creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) and [merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request). The exact buttons, in case GitHub moves them.

---

[Back to the lesson](README.md) | [Back to the map](../README.md) | **Next lesson: [Why PRs matter for a PM](../04-why-prs-matter-for-pms/)**

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
