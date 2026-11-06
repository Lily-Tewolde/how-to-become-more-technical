<sub>Lesson 7, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge and practise the questions you'd get in an interview.

## What I learned doing this

The question that finds the most useful cases for me is "who's missing?" The person booking for someone else. The parent writing about their kid. The person who mentions the important thing at the very end of a cheerful message. A first draft of a golden set tends to be full of people who write like whoever wrote it.

A few other things I'd tell myself at the start:
- **Cases are cheap, so add them freely.** A new case is a few lines and a few cents per run. A new behaviour in the product takes real build time. When in doubt, add the case.
- **Cases go stale.** A copy change or a new flow can quietly shift every expected answer. I re-check the set every time the product changes, not just when something breaks.
- **A perfect score should make me suspicious.** If everything passes, the set might be too easy, or the checker might be broken. Keeping a few hard cases I know the bot struggles with keeps me honest.
- **Hold some back.** A golden set with no held-out cases can't tell me whether I improved the bot or just taught it the test.

## You're done when

- [ ] You have a coverage grid with rules down the side and the four kinds across
- [ ] Your set has about 40 cases, covering every kind, including at least two false alarms
- [ ] Every case has a `source`, and at least one came from a bug
- [ ] Every expected behaviour starts with its type (answer, decline and offer to connect, or hand off)
- [ ] About a fifth of the cases are marked `held_out`, spread across every group
- [ ] The CSV lives in your repo, with a short changelog next to it
- [ ] You can explain why 18 of 20 isn't a precise 90%
- [ ] Your must-pass results are reported on their own line, never averaged in

## Challenge

Run your v2 set against your bot, dev cases first. Fix one thing in the prompt based only on the dev fails. Then run the held-out cases for the first time.

1. Did the held-out cases do as well as the dev cases?
2. If not, which pattern did the dev cases miss?
3. Write one new dev case for that pattern, and add a line to your changelog.

## Check yourself (interview style)

<details>
<summary><strong>1. What makes a test set a golden set?</strong></summary>

The expected behaviour for every case is agreed by whoever owns the outcome, it's the reference every new version is compared against, and it only changes on purpose through a reviewed change. It also covers the full range of what matters: happy paths, edge cases, must-escalate cases and adversarial ones.
</details>

<details>
<summary><strong>2. Where do good test cases come from?</strong></summary>

Real conversations, cleaned of personal details. The people who answer customers, and support tickets. Every bug, which becomes a case before it's fixed. Attack lists from red teaming. And deliberate gap-filling, where you vary who's writing, what they want and how they write.
</details>

<details>
<summary><strong>3. How do you stop your prompt overfitting to your eval?</strong></summary>

Keep a held-out set you never tune against. Fix failures using dev cases, then check the held-out set to confirm the improvement is real. Refresh the held-out cases once you've looked at them too often.
</details>

<details>
<summary><strong>4. How many test cases do you need?</strong></summary>

It depends what you're trying to learn. Twenty to fifty is a solid start, and it'll catch something badly broken. To tell two good versions apart you need far more, because the score on a small set has a wide range. A 90% on 20 cases could really be anywhere from about 70% to 97%. I grow the set until new cases stop finding new problems, and every important rule has cases on both sides.
</details>

<details>
<summary><strong>5. All your safety cases pass. What do you tell your stakeholders?</strong></summary>

That nothing is obviously broken, not that it's safe. With a small number of safety cases, a real miss rate well above zero can't be ruled out. I'd say how many cases and runs it's based on, keep must-pass results separate from the overall score, keep adding safety cases, and have a plan to watch real conversations after launch.
</details>

<details>
<summary><strong>6. Why keep the golden set in the repo instead of a spreadsheet?</strong></summary>

So every change has a history and a review, and the automatic eval check reads the same file everyone agreed on. When a case's expected behaviour changes, the reason is in the pull request.
</details>

## Further reading

**Start here**
- [AI Evals: Everything You Need to Know (FAQ)](https://hamel.dev/blog/posts/evals-faq/), Hamel Husain and Shreya Shankar. Read "How many examples do I need for an eval?" and "What should I do when my gold eval dataset becomes stale?" first.
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/), Hamel Husain. If you skipped it in Evals 101, it's the best story for why this matters.

**Go deeper**
- [Golden dataset evaluation: build and maintain LLM test sets](https://langfuse.com/resources/engineering/golden-dataset-evaluation), Langfuse. Practical advice on versioning, adding production failures and comparing prompt versions. It's written by a tool vendor, but the advice works with any tool.
- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), Anthropic. Balanced problem sets, saturation, and how evals graduate into regression suites.

**Primary sources**
- [Who Validates the Validators?](https://arxiv.org/abs/2404.12272), Shankar et al. (2024). Why you can't fully define "good" before you grade real outputs.
- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640), Evan Miller (2024). The statistics behind reading an eval score as a range. Anthropic's [plain-language summary](https://anthropic.com/research/statistical-approach-to-model-evals) is a gentler start.

## Next lesson

**Next: [Lesson 8, LLM-as-judge](../08-llm-as-judge/).** Some cases in your set say "read by hand", like whether a reply is warm or whether it made up a parking lot. You'll write a rubric and a judge prompt so a second AI can grade those, then check the judge against your own grades before you trust it.

[Back to the lesson](README.md) | ← [Lesson 6, Evals 101](../06-evals-101/) | **Next: [Lesson 8, LLM-as-judge](../08-llm-as-judge/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
