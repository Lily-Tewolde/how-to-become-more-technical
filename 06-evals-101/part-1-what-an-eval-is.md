<sub>Lesson 6, Part 1 of 5 · about 10 min</sub>

# What an eval is

**In this part,** you'll see why an eval beats a vibe check, why you write it before the prompt, and what goes into each test case.

## Why this matters

When you change a prompt, you usually test it by typing a few messages and eyeballing the answers. That's a vibe check. It feels like testing, but it isn't repeatable, and you'll mostly try the questions you already know work.

An eval fixes three things:
1. **It's the same test every time.** You can compare this week's prompt with last week's.
2. **It covers the scary cases on purpose.** You won't forget to try the allergic reaction message.
3. **It gives you evidence.** "18 of 20 passed and here are the 2 that didn't" is something a team can act on.

For a PM, an eval is also the clearest way to say what "done" means for an AI feature. It's the acceptance criteria, written as real messages.

### Why write evals before or alongside the prompt

If you write the prompt first, you'll write tests your prompt already passes. That's very human, and it makes the eval decorative.

Writing the eval first makes you decide what good looks like before you're attached to a prompt. Then the eval becomes the thing that tells you when the prompt is good enough. You also get to rerun it every time something changes:
- the prompt
- the FAQ
- the model
- the rules

Anthropic's guide to agent evals says "20-50 simple tasks drawn from real failures is a great start" ([Anthropic, Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)). So 20 is a real starting size. You'll grow it in the next lesson.

## How it works

Every test case has the same parts. These are the columns in [`salon-golden-set.csv`](salon-golden-set.csv):

| Column | What it holds |
|---|---|
| `id` | A short name like `ME-03`, so you can talk about a case |
| `category` | Which group it's in |
| `customer_message` | Exactly what the customer types |
| `expected_behaviour` | What a good answer does, in plain words |
| `must_pass` | `yes` if this case has to pass every time |
| `must_include` | Words a good answer has to contain, split by `\|` |
| `must_not_include` | Words that mean the answer went wrong, split by `\|` |
| `notes` | Why the case is there, and what to watch for |

The 20 cases sit in four groups:

| Group | How many | What it tests |
|---|---|---|
| FAQ (`faq`) | 6 | Normal questions the FAQ answers |
| Not in the FAQ (`not_in_faq`) | 4 | Questions it should admit it can't answer, without making things up |
| Tricky wording (`tricky_wording`) | 3 | Typos, two questions in one, and a false alarm |
| Must escalate (`must_escalate`) | 7 | Safety and complaint messages that need a person right away |

The full list of test cases is often called a golden set. That's the next lesson.

<details>
<summary><strong>Go deeper (offline eval vs online metric)</strong></summary>

Everything in this lesson is an **offline eval**. You run a fixed set before anything reaches customers. It's a gate. It decides whether a version is good enough to try.

An **online metric** comes from real use after launch. For the salon, that could be how often the bot hands off, or how often customers rephrase the same question. Only real traffic tells you whether a change actually helped.

Two related ideas worth knowing:
- **Evaluation vs feedback loop.** Evaluation asks "is it good?" A feedback loop asks how real customer behaviour flows back into the next version. You can have one without the other. The best golden sets keep growing from real failures.
- **Confidence vs correctness.** What the model says about how sure it is isn't the same as being right. You can only use "hand off below a confidence score" if that score has been checked against real answers.

A small set also has limits. Twenty cases tell you when something is badly broken. They can't tell you a change made answers 5% better.
</details>

## Quick check

<details>
<summary>1. What four groups do the 20 cases sit in?</summary>

FAQ, Not in the FAQ, Tricky wording and Must escalate.
</details>

<details>
<summary>2. What does <code>must_pass</code> mean on a test case?</summary>

It's `yes` if the case has to pass every time.
</details>

---

**Next: [Part 2 (Write your 20 test cases)](part-2-write-your-test-cases.md)** | [Back to the lesson](README.md)
