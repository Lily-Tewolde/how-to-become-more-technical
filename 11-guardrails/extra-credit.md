<sub>Lesson 11, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll get a quick map of the guardrail tools and frameworks you'll hear about, and what each kind is good for. It's optional. Skip it if you're done for now.

<details open>
<summary><strong>Go deeper (the guardrail tools you'll hear about)</strong></summary>

You don't need any of these to follow the lesson. Plain code got the salon a long way. But when someone on your team says "let's use a guardrails framework", it helps to know the main kinds.

**Guardrails built into agent frameworks.** The [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/) has input guardrails, output guardrails and tool guardrails. A guardrail sets a "tripwire", and the run stops. Good when your app already runs on that framework, because the checks live next to the agent code.

**Programmable guardrail toolkits.** [NeMo Guardrails](https://docs.nvidia.com/nemo-guardrails/) from NVIDIA is open source. You describe allowed topics, flows and checks, and it sits between your app and the model. Good when you have lots of rules and want them in one place, outside the prompt.

**Safety classifier models.** [Llama Guard](https://arxiv.org/abs/2312.06674) from Meta is a model trained to label an input or output as safe or unsafe against a list of categories. You run it as the second layer before or after your main model. Good for broad harm categories. It won't know your salon's price list, so you still need your own checks for that.

**Model-maker guardrails.** Anthropic's [Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers) are classifiers trained to block jailbreaks on the model provider's side. Anthropic's docs on [mitigating jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) also describe a pattern you can build yourself: a lightweight model screens input with a structured yes or no answer before the main model runs.

**How I'd choose:**
1. Start with plain code for anything with one right answer (prices, formats, required handoffs). It's fast, cheap and easy to test.
2. Add a classifier or a second model call when you need meaning, not words, like spotting a health message worded in a way your list doesn't cover.
3. Reach for a framework when the number of rules makes plain code hard to keep track of, or when your team already uses one.
4. Whatever you pick, test it with your own golden set and your own false refusal set. Don't trust a vendor's accuracy number on its own.

**Where guardrails sit in the standards.** In the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/), the guardrails in this lesson mainly answer:
- **LLM01 Prompt Injection**, by not relying on the prompt for hard rules
- **LLM05 Improper Output Handling**, with the checks after the model and plain text output
- **LLM06 Excessive Agency**, with approvals and least privilege for tools
- **LLM09 Misinformation**, with the price check and "answer only from the FAQ"
- **LLM10 Unbounded Consumption**, with length and rate limits
</details>

---

[Back to the lesson](README.md) | [Part 5 (Wrap up)](part-5-wrap-up.md)
