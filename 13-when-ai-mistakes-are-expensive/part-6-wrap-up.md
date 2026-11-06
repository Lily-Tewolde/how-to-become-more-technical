<sub>Lesson 13, Part 6 of 6 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge and practise the questions you'd get in an interview.

## What I learned doing this

The biggest shift for me was deciding, before writing a single prompt, which decisions the model would never get a vote on. On a health-related build, rules decided who was eligible, and the model only turned messy answers into fields the rules could read. That one choice made everything else easier to test and easier to explain.

A few other things I'd tell myself at the start:
- **Keep safety out of reach of the thing you're protecting.** The crisis check ran separately from the main conversation, with two layers that could each escalate and couldn't clear each other. Tricking the conversation couldn't switch safety off.
- **Five runs, every one passing.** A crisis case that passes four of five times isn't done.
- **Grade it yourself first.** I scored safety cases by hand before looking at the AI grader, with some deliberately wrong outputs mixed in. Any disagreement on a safety case meant fixing the grader before trusting it.
- **Write the gaps down, with a reason.** When a gap is written down with a reason, nobody assumes it was handled. And if a case wasn't run, I say it wasn't run. I never count it as a pass.

## You're done when

- [ ] Every behaviour is either must-pass or averaged, and your results table leads with the gates
- [ ] Every must-pass case runs at least five times, and one failed run fails the case
- [ ] You measure both misses and false alarms, in every language you support
- [ ] You've blind-graded a sample with planted failures before trusting a model grader on safety
- [ ] Your crisis protocol has tiers, two detection layers, a full stop to the normal flow, a tested handoff, and a fixed, signed-off resource message
- [ ] The crisis flow fails closed when the model check breaks
- [ ] Every decision has an owner: rules, the model or a person
- [ ] Look-alike inputs are kept as typed and marked unclear
- [ ] Your never list has owners, enforcement points and must-pass tests
- [ ] Every important event writes an audit record, and sensitive text is access-controlled
- [ ] Sign-off owners are named for every item
- [ ] Monitoring measures have thresholds and written responses, set before launch

## Challenge

Pick a high-stakes AI feature, real or made up. A bank's chat assistant, an insurance claims helper or a pharmacy's refill bot all work. Write a one-page safety plan for it:
1. The must-pass groups and the averaged ones
2. The crisis or emergency tiers, and the four steps for each
3. A never list with five lines, each with where it's enforced
4. The audit record fields
5. Who signs off on what
6. Three monitoring measures, each with a threshold and a response

Use [`never-list-template.md`](never-list-template.md) for step 3. Share your plan in Discussions if you like. Keep it made up, with no real company or customer details.

Want more? The [Extra credit](extra-credit.md) page (optional, Advanced) maps this lesson onto NIST, health device guidance and the EU AI Act.

## Check yourself (interview style)

<details>
<summary><strong>1. How would you approach AI risk in a regulated product?</strong></summary>

I'd start by sorting every behaviour into must-pass and averaged, and agreeing with the risk owners which ones are must-pass. Then I'd keep any decision with a right answer in a policy in rules, not the model, and write a never list with an enforcement point and tests for each line. I'd design a crisis protocol, an audit trail and a sign-off list before launch, and set monitoring thresholds with written responses. I'd anchor it in frameworks the compliance team already knows, like the NIST AI RMF.
</details>

<details>
<summary><strong>2. Your model scores 98% overall but missed one crisis case. Do you ship?</strong></summary>

No. Crisis handling is a hard gate, so one miss fails the run, whatever the average. I'd look at why it missed, add the case and variations to the must-pass set, fix it in the strongest layer I can (detection or structure, not just the prompt), rerun everything five times, and ship only when every gate passes.
</details>

<details>
<summary><strong>3. Design crisis handling for an AI intake assistant.</strong></summary>

Four steps. Detect with two independent layers, a phrase list on the raw message and a separate model check, where either can escalate, neither can cancel the other, and the flow fails closed if the model check breaks. Stop the normal flow completely, with no more questions and no model-written reply. Hand off to a named on-call person with the original message, the tier and a target pickup time, with an out-of-hours plan. Show a fixed resource message, written and signed off by clinical experts, with the local emergency number and the right crisis line. I'd test every step, including the handoff end to end, and I wouldn't let the AI try to counsel anyone.
</details>

<details>
<summary><strong>4. What goes in an audit trail for an AI product?</strong></summary>

For every important event: what was asked, what the AI said or proposed, what the user was actually shown, which rule or guardrail fired, what action happened, the model and prompt versions, and who reviewed it, when and what they decided. Full sensitive text lives once in an access-controlled store, referenced by ID, with a retention period, and sensitive labels stay out of general analytics.
</details>

<details>
<summary><strong>5. Which decisions should never be left to the model?</strong></summary>

Anything with a right answer in a policy, like eligibility, prices, coverage and deadlines, which belong to rules in code. Anything that needs professional judgment or can't be undone, like a diagnosis, a dose or a claim denial, which belongs to a person. The model is great at the language around those decisions, like extracting fields and writing summaries, with checks after.
</details>

<details>
<summary><strong>6. How do you monitor a high-stakes AI feature after launch?</strong></summary>

I'd pick a few measures, like escalation rate, confirmed misses, time to human pickup, override rate and fallback rate, and set a threshold and a written response for each before launch. I'd review every escalation, a random sample of non-escalated conversations and every override. Any confirmed must-pass miss is an incident that can pause the AI flow. Every miss and false alarm becomes a new must-pass case, and the full set reruns on every change, including model updates.
</details>

## Further reading

**Start here**
- [People + AI Guidebook](https://pair.withgoogle.com/guidebook), Google PAIR. Practical, plain guidance on designing AI products people can trust, including what happens when the AI gets it wrong.
- [WHO releases AI ethics and governance guidance for large multi-modal models](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models), World Health Organization (2024). A short summary of the WHO's guidance on generative AI in health.
- [Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents), Anthropic. Where pass@k and pass^k come from, and why repeated runs matter.

**Go deeper**
- [Good Machine Learning Practice for Medical Device Development: Guiding Principles](https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices/good-machine-learning-practice-medical-device-development.html), Health Canada, US FDA and UK MHRA. Ten short principles, including human-AI teams and monitoring after launch.
- [Lessons From Red Teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238), Bullwinkel et al., Microsoft (2025). Why domain experts and people matter in testing high-stakes systems.
- [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), Anthropic. Includes layered safeguards and continuous monitoring.

**Primary sources**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). The shared language for AI risk: Govern, Map, Measure, Manage.
- [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST (2024). Twelve generative AI risks with suggested actions.
- [Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models](https://www.who.int/publications/i/item/9789240084759), WHO (2024). The full guidance.
- [EU AI Act, Article 12, Record-keeping](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12) and [Article 14, Human oversight](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14), European Commission AI Act Service Desk.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599), Guo et al. (2017). Why a model's confidence isn't the same as being right.

**If you or someone you know needs help now:** call your local emergency number. In Canada, call or text [9-8-8](https://988.ca/about). In the US, call or text the [988 Suicide & Crisis Lifeline](https://988lifeline.org/).

## What's next

You've finished the main path. The reference section, with a glossary and common interview questions, is coming soon. For now, head back to the [hub home](../README.md) to pick a lesson to revisit, or try the challenges you skipped.

[Back to the lesson](README.md) | ← Previous: [Red teaming](../12-red-teaming/) | **[Back to the hub home](../README.md)**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
