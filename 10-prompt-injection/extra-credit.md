<sub>Lesson 10, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll see how the defences in this lesson line up with OWASP's guidance. It's optional. Skip it if you're done for now.

<details open>
<summary><strong>Go deeper (OWASP LLM01 and its neighbours)</strong></summary>

[LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) lists seven mitigation strategies:
1. Constrain model behavior
2. Define and validate expected output formats
3. Implement input and output filtering
4. Enforce privilege control and least privilege access
5. Require human approval for high-risk actions
6. Segregate and identify external content
7. Conduct adversarial testing and attack simulations

Steps 5 to 9 in [Part 3](part-3-fence-it-off.md) and [Part 4](part-4-rules-approvals-retests.md) map onto these. A few other entries in the [Top 10](https://genai.owasp.org/llm-top-10/) sit right next to injection:
- **LLM05 Improper Output Handling.** Trusting what the model returns, like rendering its links. See the exfiltration section in [Part 4](part-4-rules-approvals-retests.md).
- **LLM06 Excessive Agency.** Giving the model more tools or permissions than the job needs.
- **LLM07 System Prompt Leakage.** Getting the bot to reveal its instructions. Assume your system prompt will leak and keep secrets out of it.

For a sense of where the best models are, Anthropic reported in [Mitigating prompt injections in browser use](https://www.anthropic.com/research/prompt-injection-defenses) (Nov 2025) that about 1% of attacks still succeeded against Claude Opus 4.5 in its browser testing. That's a big improvement, and it's still not zero.
</details>

---

[Back to the lesson](README.md) | [Part 5 (Wrap up)](part-5-wrap-up.md)
