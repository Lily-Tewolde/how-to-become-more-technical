<sub>Lesson 12, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll see how a red team session lines up with the main security frameworks, and where automated tools fit. It's optional. Skip it if you're done for now.

<details open>
<summary><strong>Go deeper (mapping your findings to OWASP)</strong></summary>

Tagging every finding with an OWASP ID makes your log easy to compare across sessions and easy to explain to a security team. Here's how the categories from Part 2 line up with the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/):

| OWASP entry | What it covers | Salon findings |
|---|---|---|
| LLM01 Prompt Injection | Direct and indirect injection, jailbreaks | RT-001, RT-007 |
| LLM02 Sensitive Information Disclosure | Leaking private data | RT-003 |
| LLM03 Supply Chain | Risky models, libraries or plugins from outside | Not tested |
| LLM04 Data and Model Poisoning | Bad data in training or fine-tuning | Not tested (no fine-tuning) |
| LLM05 Improper Output Handling | Trusting model output downstream | Covered in [Guardrails](../11-guardrails/) |
| LLM06 Excessive Agency | Too many tools or permissions | RT-002, RT-004 |
| LLM07 System Prompt Leakage | Revealing instructions | RT-006 |
| LLM08 Vector and Embedding Weaknesses | Attacks on retrieval systems | Not tested (no retrieval) |
| LLM09 Misinformation | Made-up facts and harmful advice | RT-005 |
| LLM10 Unbounded Consumption | Runaway cost and abuse | Not tested in S1 |

The "not tested" rows are worth keeping in your report. They're the honest edge of what you checked.

For agents, the [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) adds:
1. ASI01 Agent Goal Hijack
2. ASI02 Tool Misuse and Exploitation
3. ASI03 Identity and Privilege Abuse
4. ASI04 Agentic Supply Chain Vulnerabilities
5. ASI05 Unexpected Code Execution
6. ASI06 Memory and Context Poisoning
7. ASI07 Insecure Inter-Agent Communication
8. ASI08 Cascading Failures
9. ASI09 Human-Agent Trust Exploitation
10. ASI10 Rogue Agents

ASI09 is a good one for PMs to know. It's about the trust people put in an agent being used against them, like a staff member approving a refund because the agent's summary sounded sure, when an injection wrote that summary. That's the approval screen problem from [Part 3](part-3-agents-with-tools.md).
</details>

<details>
<summary><strong>Go deeper (MITRE ATLAS and NIST)</strong></summary>

- [MITRE ATLAS](https://atlas.mitre.org/) is a knowledge base of tactics and techniques used against AI systems, built from real attacks and research. Security teams use it to check coverage. If your team already uses MITRE ATT&CK, ATLAS will feel familiar.
- [NIST AI 600-1, the Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (July 2024) lists twelve generative AI risks, including confabulation, data privacy, information security and human-AI configuration. Its suggested actions include AI red teaming. It sits under the broader [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). It's the reference regulated teams tend to cite, which is why it comes up again in [Lesson 13](../13-when-ai-mistakes-are-expensive/).
</details>

<details>
<summary><strong>Go deeper (automated red teaming tools)</strong></summary>

Automated tools generate many attacks, run them against your app and score the results. They're good for coverage and for running between human sessions.

- [Promptfoo](https://www.promptfoo.dev/docs/red-team/quickstart/) is an open-source eval and red team tool. You describe your app and it generates attacks across many categories, and it can run in CI.
- [garak](https://github.com/NVIDIA/garak) from NVIDIA is an open-source LLM vulnerability scanner with a large library of probes.
- [PyRIT](https://microsoft.github.io/PyRIT) from Microsoft is an open-source framework for building your own automated red teaming, including multi-turn attacks.

How I'd use them:
1. Run a human session first, so you know what matters for your product.
2. Point an automated tool at the same test environment to widen coverage.
3. Read a sample of what it flags by hand. Automated graders make mistakes too.
4. Treat anything real it finds exactly like a human finding: log it, rate it, turn it into cases, fix and retest.
</details>

---

[Back to the lesson](README.md) | [Part 6 (Wrap up)](part-6-wrap-up.md)
