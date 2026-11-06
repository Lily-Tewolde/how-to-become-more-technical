# How do LLMs and AI agents work?

A large language model (LLM) writes by predicting the next small chunk of text, over and over, based on everything it's been given. An AI agent is that same model running in a loop where it can ask your code to use tools, like checking the salon's appointment book, then read the result and decide what to do next.

![Level: Beginner](https://img.shields.io/badge/Level-Beginner-brightgreen) ![Type: Learn](https://img.shields.io/badge/Type-Learn-blue) ![Time: 60 min](https://img.shields.io/badge/Time-60%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** An LLM reads text as tokens and predicts the next token, one at a time, until the reply is done. It only knows what's in its context window right now: your system prompt, the conversation, and anything you paste in. It doesn't remember anything between requests, so your app sends the whole conversation every time. It's built to sound plausible, not to be right, so it can make things up, and it can answer the same question differently twice. That's why evals exist. Tools let it ask your code to do things, and an agent is a model using tools in a loop until the job's done. RAG is looking up the right part of your documents, like the salon FAQ, and handing it to the model just before it answers.

> [!TIP]
> **New to this? Let me break it down.**
> Picture a brilliant temp at the Polish & Co. front desk who's read millions of conversations but has never worked at this salon.
> - Every time a customer speaks, she gets handed a fresh folder with the owner's rules, the FAQ and the whole conversation so far. That folder is the **context window**. She forgets everything the moment she hands it back.
> - She answers by saying whatever sounds most like a good front desk reply. Usually that's right. Sometimes she confidently makes up a parking lot. That's a **hallucination**.
> - She can't open the appointment book herself. She can pass a note to the back room saying "check Saturday at 3", and someone hands her the answer. That's a **tool**.
> - If she keeps passing notes and reading answers until the booking's done, she's working as an **agent**.
>
> That's the whole idea. The rest of this lesson is the real version.

**You'll need:**
- [Lesson 1: How software works](../01-how-software-works/), especially APIs and JSON. Calling a model is just another API request.
- The [Polish & Co. running example](../example/) open in another tab
- Any AI chat app, like Claude, for two short experiments. No code needed.

**What you'll learn:**
- What tokens are and how next-token prediction builds a whole reply
- What a context window is, and the difference between a system prompt and a user message
- Why models make things up and answer differently each time, and why that means you need evals
- How tool calls work, what makes something an agent, and what RAG is in plain words
- Three distinctions that help a PM make better calls about AI features

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [Tokens and prediction](part-1-tokens-and-prediction.md) | See how a reply is built, one token at a time | 10 min |
| [ ] | [Context and prompts](part-2-context-and-prompts.md) | Build the request the salon sends to the model | 15 min |
| [ ] | [Tools, agents and RAG](part-3-tools-agents-and-rag.md) | Follow a booking through the agent loop | 15 min |
| [ ] | [Three distinctions](part-4-three-distinctions.md) | Evaluation, confidence and launch decisions | 10 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

**Optional, Advanced:** [Extra credit](extra-credit.md), how the model pays attention, why long chats cost more, and why search can't count.

**[Start Part 1 →](part-1-tokens-and-prediction.md)**
