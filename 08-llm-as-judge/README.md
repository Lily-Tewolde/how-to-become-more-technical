# What is LLM-as-judge, and when can you trust it?

LLM-as-judge means using a second AI model to grade your AI's answers on things code can't check, like whether a reply is friendly or whether every fact came from your FAQ. You can trust it only after you've graded a batch of answers yourself and checked that the judge agrees with you, especially on the bad ones.

![Level: Intermediate](https://img.shields.io/badge/Level-Intermediate-yellow) ![Type: Learn and Build](https://img.shields.io/badge/Type-Learn%20%2B%20Build-blue) ![Time: 60 min](https://img.shields.io/badge/Time-60%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** Use code for anything code can check, like the handoff message or a real price. Use a judge for the rest. Write a short rubric with pass or fail for each criterion, put it in a judge prompt, and grade a batch of answers yourself before you look at the judge's grades. Make sure some of them are deliberately bad. Only trust the judge once it catches your bad ones. Judges have known biases, like favouring longer answers, so design around them.

> [!TIP]
> **New to this? Let me break it down.** The salon owner can't read every reply the booking assistant sends. So she trains a senior stylist to spot-check them. Before she trusts the stylist's grades, she grades the same 12 replies herself, and she slips in a few she knows are bad: one that's rude, one that makes up a price. If the stylist passes the rude one, the owner fixes the instructions before the stylist grades anything alone. The stylist is the judge. The owner's own grades are how you know whether to trust it.

**You'll need:**
- [Lesson 7: Golden sets](../07-golden-sets/), so you have a set with cases marked "read by hand"
- The [Polish & Co. running example](../example/) open in another tab
- Access to an AI chat app. For the Python parts, an Anthropic API key (optional)

**What you'll learn:**
- Which checks belong in code and which need a judge
- How to write a pass or fail rubric and a judge prompt
- How to check the judge against your own grades before you trust it
- The known biases of LLM judges, and how to design around them

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [What a judge is for](part-1-what-a-judge-is-for.md) | Sort checks into code and judge | 10 min |
| [ ] | [Write the rubric](part-2-write-the-rubric.md) | Define pass and fail for two criteria | 15 min |
| [ ] | [Write the judge prompt](part-3-write-the-judge-prompt.md) | Build the prompt and run it | 15 min |
| [ ] | [Check the judge](part-4-check-the-judge.md) | Compare its grades to yours, fix it | 15 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

The files you'll use:
- [`judge-rubric.md`](judge-rubric.md), the two criteria with pass and fail examples
- [`judge-prompt.md`](judge-prompt.md), the prompt you send the judge
- [`judge-check-set.csv`](judge-check-set.csv), 12 salon replies with my own grades, including planted bad ones

**[Start Part 1 →](part-1-what-a-judge-is-for.md)**
