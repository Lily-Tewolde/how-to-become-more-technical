# How do you red team an AI assistant?

Red teaming is attacking your own AI on purpose, in a planned way, before someone else does it for real. You decide who might attack and what they'd want, try every kind of attack against it, rate what gets through, and turn each finding into a test that runs forever after.

![Level: Advanced](https://img.shields.io/badge/Level-Advanced-red) ![Type: How-to](https://img.shields.io/badge/Type-How--to-green) ![Time: 80 min](https://img.shields.io/badge/Time-80%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** Start with a threat model: what the assistant can touch, who'd want to misuse it, and what they'd be after. Then attack it across the main categories: direct and indirect prompt injection, jailbreaks, data leaks, tool misuse and harmful advice. Pay extra attention to tools, because an agent that can book or refund turns a bad sentence into a bad action. Log every finding with a severity rating, turn it into golden set cases, fix it, and retest. Then do it again whenever the assistant changes.

> [!TIP]
> **New to this? Let me break it down.**
> Picture the Polish & Co. owner before opening a second location. She asks a friend to come in and try to get a free manicure, any way she can. Sweet-talk the front desk. Leave a fake note from "the owner". Ask what time another client's appointment is. Pretend to be someone's sister and cancel her booking. The friend writes down what worked, and the owner fixes it before real customers try. That's a red team. The friend isn't there to be mean. She's there so the salon finds its gaps first.

**You'll need:**
- [Prompt injection, plainly](../10-prompt-injection/), for direct and indirect injection
- [Guardrails](../11-guardrails/), so you know the defences you're testing
- [Evals 101](../06-evals-101/) or [Golden sets](../07-golden-sets/), so findings have somewhere to go
- An assistant you own, or written permission to test someone else's

**What you'll learn:**
- How to write a threat model for an AI assistant in plain words
- The main attack categories, with a salon example for each, and how they map to the OWASP Top 10 for LLM Applications
- Why prompt injection is worse in agents that can use tools, and what to test there
- How to run a session, rate severity, log findings, and retest after a fix

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [Who would attack, and what they'd want](part-1-threat-model.md) | Write a threat model | 15 min |
| [ ] | [The attack categories](part-2-attack-categories.md) | Plan attacks in every category | 15 min |
| [ ] | [Injection in agents that use tools](part-3-agents-with-tools.md) | Test what injected text can make tools do | 15 min |
| [ ] | [Run a session and rate what you find](part-4-run-and-rate.md) | Run it, rate severity, log findings | 15 min |
| [ ] | [Turn findings into tests, then retest](part-5-findings-to-tests.md) | Golden set cases, fixes, retests | 10 min |
| [ ] | [Wrap up](part-6-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

**Files in this lesson:**
- [`red-team-findings-log.csv`](red-team-findings-log.csv), a findings log template with worked salon examples
- [`red-team-cases.csv`](red-team-cases.csv), those findings turned into golden set cases

**Optional, Advanced:** [Extra credit](extra-credit.md), how red teaming lines up with OWASP, MITRE ATLAS and NIST, plus automated tools.

**[Start Part 1 →](part-1-threat-model.md)**
