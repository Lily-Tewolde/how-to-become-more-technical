# What are AI guardrails, and which ones does your product need?

Guardrails are checks that run around an AI model, before it reads a message and after it writes a reply, so a bad answer gets caught before a customer sees it. The important ones live in code, not in the prompt, and every one of them has a cost you should know before you add it.

![Level: Intermediate](https://img.shields.io/badge/Level-Intermediate-yellow) ![Type: Learn and Build](https://img.shields.io/badge/Type-Learn%20%2B%20Build-blue) ![Time: 60 min](https://img.shields.io/badge/Time-60%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** A prompt asks the model to behave. A guardrail checks whether it did. Put checks before the model (catch must-escalate messages, keep it on topic) and after it (prices must match the price list, no medical advice, a tone rule). Hard rules that touch money, safety or the law go in code. When a check fires, hand off to a person or refuse kindly, and log what happened. Each check can wrongly block real customers and can slow replies down, so measure that too.

> [!TIP]
> **New to this? Let me break it down.**
> Think about how Polish & Co. handles the till. The front desk person is lovely and knows the prices. But the card machine still only charges what's in the system, and a manager signs off on any refund. Nobody thinks that's rude to the front desk person. It's just how you run a business where mistakes cost money. Guardrails are the card machine and the manager's sign-off for your AI. The prompt is the training. The guardrails are the systems that don't depend on anyone remembering their training.

**You'll need:**
- The [running example](../example/), the Polish & Co. booking assistant
- [Evals 101](../06-evals-101/), so you know the must-escalate group
- [Prompt injection, plainly](../10-prompt-injection/), so you know why a line in the prompt isn't a defence
- Python 3 if you want to run the code (optional). Everything else works in a spreadsheet.

**What you'll learn:**
- The difference between a check before the model, a check after it, and an instruction in the prompt
- How to build three salon guardrails: a must-escalate detector, a price check and a tone rule
- How to escalate, refuse kindly and log, and how to measure what each guardrail costs you

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [Rules in code vs rules in the prompt](part-1-code-vs-prompt.md) | Sort the salon's rules | 10 min |
| [ ] | [Checks before the model](part-2-checks-before.md) | Build the must-escalate detector | 15 min |
| [ ] | [Checks after the model](part-3-checks-after.md) | Build the price check and tone rule | 15 min |
| [ ] | [Escalate, refuse kindly, log, and count the cost](part-4-escalate-refuse-log.md) | Write the fallbacks, measure false refusals | 10 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

**Files in this lesson:**
- [`salon_guardrails.py`](salon_guardrails.py), all four checks in one small file you can run
- [`guardrails-checklist.md`](guardrails-checklist.md), a one-page checklist to copy into your own project

**Optional, Advanced:** [Extra credit](extra-credit.md), the guardrail tools you'll hear about and what they're good for.

**[Start Part 1 →](part-1-code-vs-prompt.md)**
