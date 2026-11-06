# What is a golden set, and how do you build one that lasts?

A golden set is the list of test cases you trust enough to judge every new version of your AI against. It lasts when it covers every kind of message that matters, grows from real conversations and every bug you fix, lives in your repo with a history, and keeps a few cases aside so you can tell whether a better score is real.

![Level: Intermediate](https://img.shields.io/badge/Level-Intermediate-yellow) ![Type: Learn and Build](https://img.shields.io/badge/Type-Learn%20%2B%20Build-blue) ![Time: 60 min](https://img.shields.io/badge/Time-60%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** Grow the 20 cases from Evals 101 to about 40. Cover happy paths, edge cases, must-escalate cases and attacks. Pull new cases from real messages, from the people who answer customers, and from every bug. Keep the file in your repo so every change is reviewed. Hold some cases back so you don't tune your prompt to the test. And read every score as a rough range, because 40 cases is a small sample, which is why must-pass cases are never averaged in.

> [!TIP]
> **New to this? Let me break it down.** In Evals 101 the salon manager ran a new hire through 20 pretend calls. A golden set is the binder she keeps after that. Every time a real call goes badly, she adds it as a new page. She dates every page, so she knows which version of the rules it was written for. And she keeps a few calls in a sealed envelope that nobody practises with. On review day, she opens the envelope. If the new hire only memorised the binder, the envelope is where it shows.

**You'll need:**
- [Lesson 6: Evals 101](../06-evals-101/) finished, with your 20 cases in [`salon-golden-set.csv`](../06-evals-101/salon-golden-set.csv)
- The [Polish & Co. running example](../example/) open in another tab
- A spreadsheet or text editor. A GitHub account helps for Part 3 ([Lesson 3](../03-your-first-pull-request/) shows you how).

**What you'll learn:**
- How to check your set covers every kind of message that matters
- Where good cases come from, and who decides what the right answer is
- How to keep the set versioned in your repo, with a held-out group you don't tune against
- How many cases is enough, and why a score on a small set is a rough reading

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [What makes a set golden](part-1-what-makes-it-golden.md) | Map your coverage and find the gaps | 10 min |
| [ ] | [Where good cases come from](part-2-where-cases-come-from.md) | Grow the set to 40 and label each case | 15 min |
| [ ] | [Version it and hold some back](part-3-version-and-hold-back.md) | Put it in the repo and split it | 15 min |
| [ ] | [How many cases is enough](part-4-how-many-cases.md) | Read a score honestly | 10 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

The finished set is in [`salon-golden-set-v2.csv`](salon-golden-set-v2.csv). It keeps all 20 cases from Evals 101 and adds 20 more.

**[Start Part 1 →](part-1-what-makes-it-golden.md)**
