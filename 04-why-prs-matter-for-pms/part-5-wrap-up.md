<sub>Lesson 4, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge, see how PRs come up in interviews and practise the questions.

## Common mistakes

- **Wrong:** treating green checks as approval. **Instead:** read the description and diff yourself. Checks only test what someone told them to test.
- **Wrong:** reviewing only the lines that changed. **Instead:** read the lines around them too. Sam's contradiction was in a line that didn't change.
- **Wrong:** comments with no label or reason, like "hmm" or "fix this". **Instead:** label it, say why, suggest a next step.
- **Wrong:** a mechanism title like "Update handler logic". **Instead:** the outcome and the position, like "Must-escalate fix: buried swelling now gets the handoff".
- **Wrong:** one PR with three decisions in it. **Instead:** one PR, one purpose. Split it.
- **Wrong:** "How I checked it" that claims a check you didn't run. **Instead:** write exactly what you did, and say what you didn't check.

## How PRs come up in interviews

For technical PM and AI builder roles, PRs show up in interviews in a few ways:
1. **As proof of work.** Some interviewers ask how many PRs you shipped recently, or ask you to walk through one. Have two or three real PRs you can link to and explain, and an honest count.
2. **As a process question.** "Walk me through what happens from a ticket to production" is common. The PR is the middle of that answer.
3. **As a judgment question.** "Tell me about a time you caught something in review" or "How do you review code an AI agent wrote?"
4. **As a build exercise.** If you're given something to build, your PRs are part of what gets read. The open one, or the last one, is the one a reviewer is sure to open. Make it carry the summary.

You don't have to be an engineer to answer these well. You have to show you understand the change well enough to be responsible for it.

## What I learned doing this

I'm not trying to prove I could write every line alone. I'm trying to prove I understand a change well enough to be responsible for it. Reading PRs carefully is how I get there.

A few things I'd tell myself at the start:
- **The PR someone opens first should carry the summary.** It's the one page a reviewer is guaranteed to read, so I put what changed, how I checked it and the test results there.
- **Write the PR in first person.** "I checked the preview on my phone." In my own repos I never write about myself in third person. It reads like someone else did the work.
- **Mechanism is my default.** When I write from inside the work, my titles describe the machinery. I catch it now by reading the title out loud next to the other PRs in the list.
- **Closed PRs are useful.** A PR that didn't go ahead, with a comment saying why, has saved me from having the same debate twice.

## You're done when

- [ ] You can name the five places on a PR page and the PM question for each
- [ ] You found the contradiction, the unexplained change and the stale eval in Sam's PR
- [ ] You left three labelled line comments and submitted a review
- [ ] Your cancellation PR has an outcome title and a four-part description, linked to an issue
- [ ] You closed it with a comment explaining the decision
- [ ] Your fork has `.github/pull_request_template.md` on `main`, and new PRs fill in with it

## Challenge

Do the lateness change properly, as its own PR. Open an issue first that says why the salon might want 10 minutes instead of 15. Then make the change on a new branch, write an outcome title, fill in the template and link the issue with `Closes`. Ask a friend to review it on Files changed with at least one labelled comment. Decide together whether to merge or close it, and write the decision in a comment either way. If you merge it, remember the golden set may need a new case.

## Check yourself (interview style)

<details>
<summary><strong>1. Why should a PM read pull requests?</strong></summary>

Because the PR is where the details of a product decision actually get settled, like the exact number, the wording and the edge cases. Review is the last cheap moment to catch "that's not what I meant". The PR is also the record of why something changed, and it's where AI coding agents hand work back for review.
</details>

<details>
<summary><strong>2. How do you review a PR when you can't read all the code?</strong></summary>

I check that the title, description, diff, checks and conversation tell the same story. I read the file names and size first, then any customer-facing words and numbers, then whether tests changed alongside the code. I ask the author where to start, read the test names, and click the preview link if there is one. I own the product questions and leave correctness to the engineers, and I say which part I reviewed.
</details>

<details>
<summary><strong>3. All the checks on a PR are green. Is it safe to merge?</strong></summary>

Not on that alone. Checks only cover what someone wrote a test for. They don't know whether the change solves the right problem, whether the copy is right, or whether the checks you expected even ran. I'd still read the description and diff, and check that nothing important is untested.
</details>

<details>
<summary><strong>4. What makes a good PR description?</strong></summary>

It says what changed for the user, why, how the author checked it, and what's deliberately not included. It links to the ticket or decision. A reviewer should be able to understand the change without messaging the author.
</details>

<details>
<summary><strong>5. Why do teams prefer small PRs?</strong></summary>

They get reviewed faster and more carefully, they cause fewer bugs, they're easier to roll back, and less work is lost if one is rejected. For a PM, a small PR is one decision, so it can be approved or reversed on its own and the history stays readable.
</details>

<details>
<summary><strong>6. Walk me through what happens from a ticket to production.</strong></summary>

Someone picks up the ticket and makes the change on a branch, in small commits. They open a PR that links the ticket and explains what, why and how they checked it. Automated checks run, like tests, linting and evals. A reviewer reads it and approves or asks for changes. Once checks pass and it's approved, it merges into main. Then it deploys, either automatically on merge or in the next release, and sometimes behind a feature flag. After launch, we watch the metrics and errors.
</details>

## Further reading

**Start here**
- [How to write the perfect pull request](https://github.blog/developer-skills/github/how-to-write-the-perfect-pull-request/), Keavy McMinn, GitHub Blog. The PR as communication. Short, friendly and still right.
- [Conventional Comments](https://conventionalcomments.org/). The label format I use for review comments, with examples of each label.
- [Introduction to GitHub](https://github.com/skills/introduction-to-github), GitHub Skills. A free guided exercise if you want another rep at opening and merging a PR.

**Go deeper**
- [What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html), Google Engineering Practices. The full list a reviewer runs, from design to tests to saying what's good.
- [How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html), Google Engineering Practices. Courtesy, explaining why, and labelling severity.
- [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) and [Writing good CL descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html), Google Engineering Practices. Why small changes ship faster, and how to write a description that still makes sense a year later.

**Primary sources**
- [Pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) and [Reviewing proposed changes in a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request), GitHub Docs. Comment, Approve and Request changes, and the exact buttons.
- [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue), GitHub Docs. The closing keywords and when they work.
- [Creating a pull request template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository), GitHub Docs. Where the template file can live.
- [Status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks), GitHub Docs. What checks are and what each state means.

## Next lesson

**Next: [Lesson 5, Build something with an AI agent](../05-build-with-an-ai-agent/).** You'll write a short spec, have Claude Code build a tiny Polish & Co. FAQ assistant one step at a time, review what it wrote, and ship it as a PR using this template.

[Back to the lesson](README.md) | ← [Lesson 3, Your first pull request](../03-your-first-pull-request/) | **Next: [Lesson 5, Build something with an AI agent](../05-build-with-an-ai-agent/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
