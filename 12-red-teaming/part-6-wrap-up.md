<sub>Lesson 12, Part 6 of 6 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge and practise the questions you'd get in an interview.

## What I learned doing this

The habit that changed how I test is checking two ways. A reply can look fine while the thing behind it went wrong. With an agent, that means reading the tool log every time, not just the chat. A single observation isn't a pass.

A few other things I'd tell myself at the start:
- **A quiet session isn't proof.** A search that finds nothing only means something if you've checked it can find the thing when it's there. A red team that found nothing might mean the bot is solid, or that the tests were too gentle. Plant a known problem and make sure you'd catch it.
- **Hide attacks inside normal text.** The cases that taught me the most weren't the loud "ignore your instructions" ones. They were the attack tucked into a friendly message, and the plain request to show the instructions.
- **Fixes break things too.** Review the fix the same way you reviewed the original. Rerunning the whole set after every fix is how you catch the new problem before a customer does.
- **Independent only counts if the inputs are.** Three reviewers who all got the same incomplete picture will agree with each other and still be wrong. Bring in someone who didn't build it.

## You're done when

- [ ] You have a written threat model: what the assistant can touch, who'd attack, what they'd want, and your top three risks
- [ ] Rules of engagement are written down, with a test environment and made-up data
- [ ] Your attack plan has at least three attacks per category, plus multi-turn and harmful advice attacks
- [ ] You've mapped every path from untrusted text to a tool
- [ ] You've checked the tool log, not just the replies
- [ ] You've tried to use every tool on another customer's data from a normal account
- [ ] Every finding is in the log with a severity, a likelihood and a reason
- [ ] Every finding has an exact case, a variation and a control in the golden set
- [ ] Every Critical and High finding has a fix in code, an approval or a removed ability
- [ ] Every fix has been retested, and the full golden set has been rerun
- [ ] The next session has a date or trigger, and an owner

## Challenge

Run a 60-minute red team session on an AI feature you own, or on version 2 of the salon if you've built it. Use the [findings log](red-team-findings-log.csv) as your template. Find at least three things, rate them, and turn each one into golden set cases. Then fix the worst one and retest it six times. If you'd like, share your anonymized log in Discussions. No real customer data, please.

Want more? The [Extra credit](extra-credit.md) page (optional, Advanced) maps red teaming onto OWASP, MITRE ATLAS and NIST, and covers automated tools.

## Check yourself (interview style)

<details>
<summary><strong>1. How would you plan a red team for an AI agent that can issue refunds?</strong></summary>

I'd start with a threat model: what the agent can read and do, who'd want to misuse it, and what would hurt most. For refunds, that's refunds outside policy, refunds on someone else's order, and refunds triggered by injected text in something the agent reads. Then I'd set rules of engagement with a test environment and test accounts, write attacks in every category, and focus on the refund tool: claims the agent should check instead of believe, multi-turn setups, injections in order notes or emails, and attempts from one account on another's orders. I'd check the tool log on every run, rate findings by severity and likelihood, and turn each into golden set cases.
</details>

<details>
<summary><strong>2. What's the difference between red teaming and evals?</strong></summary>

Evals test the cases you already know about, the same way every time, so you can compare versions. Red teaming is a focused effort to find the cases you don't know about. They feed each other. Red team findings become new eval cases, and the eval suite makes sure old findings stay fixed.
</details>

<details>
<summary><strong>3. How do you rate the severity of a finding?</strong></summary>

I look at impact and likelihood separately. Impact is who gets hurt and how badly: someone's safety, money, private data, or just embarrassment. Likelihood is how easy it is to repeat, which I measure by rerunning it several times and noting how much effort it took. Then I combine them. I also set floor rules. For example, anything that exposes another user's data or blocks a required safety handoff starts at High.
</details>

<details>
<summary><strong>4. How is prompt injection different in an agent that uses tools?</strong></summary>

A successful injection can cause an action, not just a bad reply. Tool calls are text the model writes, so anything that steers the model can steer its tools. I'd map every path from untrusted content to a tool, plant injections there, and check the tool log. The defences that hold up are structural: tools scoped to the current user and checked on the server, approvals for anything costly or permanent where the approver sees the real tool call, and separating the parts that read outside content from the parts that act.
</details>

<details>
<summary><strong>5. Your red team found nothing. What do you conclude?</strong></summary>

Not much yet. I'd check the session could have found something: was the tool log recording, were we on normal accounts, did we cover every category and every untrusted source? I'd plant a known issue and see if we catch it. Then I'd bring in someone who didn't build it. If it still holds up, I'd report what we tested and what we didn't, rather than calling it safe.
</details>

## Further reading

**Start here**
- [Challenges in red teaming AI systems](https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems), Anthropic (2024). A readable overview of the kinds of red teaming a model maker does and why there's no standard yet.
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), Simon Willison (2025). The mental model for when an agent can be tricked into leaking data.
- [AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs), Microsoft. Hands-on challenges for direct and indirect injection, prompt extraction and multi-turn attacks. You'll need to run them yourself.

**Go deeper**
- [GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/), OWASP (2025). A full practitioner guide across model, implementation, infrastructure and runtime testing.
- [Lessons From Red Teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238), Bullwinkel et al., Microsoft (2025). Eight lessons from real product red teams.
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/), Simon Willison (2025). The structural fixes you'll reach for after a session.
- [Red team quickstart](https://www.promptfoo.dev/docs/red-team/quickstart/), Promptfoo. Automated red teaming you can run against your own app.

**Primary sources**
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/). The standard risk list. Log every finding against it.
- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). The risk list for agents that plan and use tools.
- [MITRE ATLAS](https://atlas.mitre.org/). A knowledge base of attacker tactics and techniques against AI systems.
- [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST (2024). Twelve generative AI risks with suggested actions, including red teaming.
- [AgentDojo](https://arxiv.org/abs/2406.13352), Debenedetti et al. (2024). A benchmark of agent tasks with injected tool results.

## Next lesson

**Next: [Lesson 13, When AI mistakes are expensive](../13-when-ai-mistakes-are-expensive/).** You'll take the must-escalate idea into health, finance and insurance, where one miss outweighs a great average, and learn how crisis protocols, audit trails and human sign-off work.

[Back to the lesson](README.md) | ← Previous: [Guardrails](../11-guardrails/) | **Next: [When AI mistakes are expensive](../13-when-ai-mistakes-are-expensive/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
