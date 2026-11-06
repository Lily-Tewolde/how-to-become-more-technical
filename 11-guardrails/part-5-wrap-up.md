<sub>Lesson 11, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge and practise the questions you'd get in an interview.

## What I learned doing this

The guardrails I trust most are the boring ones. A strict output format, where anything that doesn't match falls back to a plain answer with no retry. A rule in code that makes the decisions that matter, so the model never gets a vote. And two safety layers that run separately, where either one can escalate and neither can switch the other off.

A few other things I'd tell myself at the start:
- **I won't let AI run unsupervised anywhere it can fail quietly.** If a mistake would go unnoticed until a customer complains, that step gets a check or a person.
- **Give every flag a reason.** When I built a checker that sorted content into approved, soft flag and hard flag, each flag came with a short reason. Without the reason, people stopped reading the flags.
- **Drop what you can't back up.** If an AI output includes a fact it can't point to a source for, it's safer to remove the fact than to hope it's right.
- **Put a person in front of anything you can't take back.** Drafts are cheap. Sends, refunds and bookings get an approval step.

## You're done when

- [ ] Every salon rule has a "where it lives" answer: prompt, before the model, or after it
- [ ] Your must-escalate detector catches all 7 must-escalate cases in the golden set
- [ ] You've tested at least three false alarms and three unusual wordings, and written down the results
- [ ] Either layer can escalate, and neither can cancel the other
- [ ] The price check passes and fails the six example replies correctly
- [ ] A reply with medical advice gets replaced with the handoff message
- [ ] Tone flags are logged, not blocked
- [ ] Every refusal acknowledges, explains plainly and offers a next step
- [ ] Every guardrail decision writes a log line
- [ ] You have a false refusal rate, and you know which way each guardrail fails when it breaks

Copy [`guardrails-checklist.md`](guardrails-checklist.md) into your own project and tick it off there too.

## Challenge

Polish & Co. wants to let the bot book appointments. Write the guardrails for the new booking tool before anyone builds it:
1. What does code check before a booking is made? (Think about the price, the time slot, opening hours and the deposit.)
2. Which bookings need a staff member to approve them?
3. What does a kind refusal look like when a slot is taken?
4. What gets logged?

Then add three golden set cases that would catch a broken booking guardrail. Share your list in Discussions if you like.

Want more? The [Extra credit](extra-credit.md) page (optional, Advanced) covers the guardrail tools and frameworks you'll hear about.

## Check yourself (interview style)

<details>
<summary><strong>1. What's the difference between a guardrail and an instruction in the system prompt?</strong></summary>

An instruction asks the model to behave. A guardrail checks whether it did, in code that doesn't depend on the model. Instructions make good answers more likely. Guardrails catch the bad ones before a user sees them, or stop risky messages before the model sees them at all.
</details>

<details>
<summary><strong>2. How do you decide which rules go in code?</strong></summary>

I ask what happens if the model breaks the rule once. If it costs money, could hurt someone, or creates legal or privacy trouble, it gets a check in code, often in more than one place. Style and helpfulness rules stay in the prompt and get measured with evals.
</details>

<details>
<summary><strong>3. Your safety guardrail is blocking a lot of real users. What do you do?</strong></summary>

First I'd measure it: run a set of normal messages through and get a false refusal rate, then look at the actual blocked messages for a pattern. Then I'd tune the specific trigger, or add a second, smarter layer so the first one can be narrower. I wouldn't just loosen a safety check, though. I'd compare the cost of a false alarm with the cost of a miss. For must-escalate cases a false alarm is usually the cheaper mistake.
</details>

<details>
<summary><strong>4. Design guardrails for a support bot that can issue refunds.</strong></summary>

The model can propose a refund, but code decides. Code checks the order exists, belongs to the person asking, is within policy, and is under a set amount. Anything over the limit or outside policy goes to a person to approve. The refund tool can only refund the current customer's own orders. I'd log every proposed and approved refund with who approved it, add injection cases that try to trigger refunds, and fail closed if any check breaks.
</details>

<details>
<summary><strong>5. How do you know your guardrails actually work?</strong></summary>

I test both directions. Bad inputs and outputs should get caught, and normal ones shouldn't. I break each check on purpose to make sure the test goes red. I track the false refusal rate and the miss rate over time, run the guardrail tests in CI on every change, and turn every real miss from the logs into a new golden set case.
</details>

## Further reading

**Start here**
- [Safe and reliable AI via guardrails](https://www.deeplearning.ai/short-courses/safe-and-reliable-ai-via-guardrails/), DeepLearning.AI with Shreya Rajpal (Guardrails AI). A short video course with code. The page says access is free for a limited time.
- [Errors + Graceful Failure](https://pair.withgoogle.com/chapter/errors-failing/), Google People + AI Guidebook. How to design what users see when the AI gets it wrong.

**Go deeper**
- [Guardrails](https://openai.github.io/openai-agents-python/guardrails/), OpenAI Agents SDK docs. Input and output guardrails, tripwires, and the parallel vs blocking trade-off explained clearly.
- [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), Anthropic. Harmlessness screens, input validation and layered defences.
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), Anthropic. Letting the model say "I don't know", grounding in quotes, and citing sources.
- [NeMo Guardrails documentation](https://docs.nvidia.com/nemo-guardrails/), NVIDIA. An open-source toolkit for adding programmable guardrails to an app.

**Primary sources**
- [LLM05:2025 Improper Output Handling](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/), OWASP. Why model output needs checking before it reaches people or other systems.
- [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), OWASP. Giving a model more tools and permissions than the job needs.
- [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674), Inan et al. (Meta, 2023). A model trained to classify inputs and outputs against safety categories.
- [XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models](https://arxiv.org/abs/2308.01263), Röttger et al. How to measure over-refusal.
- [Constitutional Classifiers: Defending against universal jailbreaks](https://www.anthropic.com/research/constitutional-classifiers), Anthropic (2025). A large guardrail system with its refusal and compute costs reported.

## Next lesson

**Next: [Lesson 12, Red teaming](../12-red-teaming/).** You've built the guardrails. Now you'll plan a proper attack on them, rate what gets through, and turn every finding into a golden set case.

[Back to the lesson](README.md) | ← Previous: [Prompt injection, plainly](../10-prompt-injection/) | **Next: [Red teaming](../12-red-teaming/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
