<sub>Lesson 2, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check what you've got against the list, design the salon assistant's tools as the challenge, and practise the questions you'd get in an interview.

## What I learned doing this

The biggest shift for me was remembering that the model is predicting, not checking. That changed how I read its answers, including answers about my own work. An AI will happily describe a method it didn't actually use, or tell you a file says something it doesn't. So I check claims against the source, the file or the database, not against what the AI says it did. A self-reported pass isn't a pass.

A few other things I'd tell myself at the start:
- **Start with a workflow.** If I can draw the flowchart, I build that first. I can test every path, and I only reach for an agent when the steps really can't be known ahead of time.
- **Keep the scary decisions out of the model's hands.** Anything that must happen every time, like a handoff when someone's hurt, gets a rule in code as well as a line in the prompt.
- **Let results pick the model.** I start with a faster, cheaper model where speed matters, and move up only if it misses the cases that have to pass. The eval tells me, not my gut.

## You're done when

- [ ] You can explain tokens and next-token prediction in two sentences
- [ ] You've asked the same question in two fresh chats and seen different answers
- [ ] You can say what's in the context window and why the whole conversation is sent every time
- [ ] You can tell a system prompt from a user message, with a salon example of each
- [ ] You can walk through a tool call from `tool_use` to `tool_result` to the final reply
- [ ] You can say whether something is a chatbot, a workflow or an agent, and why
- [ ] You can explain RAG using the salon FAQ, and the two ways it can go wrong
- [ ] You can name the three distinctions and the question to ask for each

## Challenge

**Design the salon assistant's tools.** Write a short list of every tool you'd give the Polish & Co. assistant. For each one, write down:
1. What it does
2. Whether it **reads** or **writes**
3. What the back end checks before running it
4. Whether a person has to approve it

Then decide: is the assistant a workflow, an agent, or a bit of both? Finally, trace the loop for "can you move my Saturday 3pm to 5pm?" the way you did in [Part 3](part-3-tools-agents-and-rag.md).

<details>
<summary>One good answer</summary>

| Tool | Reads or writes | Back end checks | Person approves? |
|---|---|---|---|
| `check_availability` | Reads | The service exists and the date is a day the salon's open | No |
| `create_booking` | Writes | The time is still free, the price comes from `services`, the deposit rule | No, but the customer confirms on screen first |
| `move_booking` | Writes | It's her booking, the new time is free, the 24-hour rule for the deposit | No |
| `hand_off` | Writes (a message to staff) | Nothing that could stop it | No. It also fires from a word check in code, so it doesn't depend on the model choosing it |

Things that get **no tool at all:** refunds, discounts and anything medical. Those go to a person through `hand_off`. If the assistant can't do it, a trick message can't make it do it.

It's a bit of both. The must-escalate check runs first as a fixed workflow step in code. Only normal booking chats go to the agent loop.

The loop for the move: the model calls `check_availability` for Saturday, your code returns the free times, the model sees 5pm is open and calls `move_booking`, your code checks it's her booking and the time is still free, saves it, and returns the result. The model replies "Done, you're now at 5pm on Saturday."
</details>

## Check yourself (interview style)

<details>
<summary><strong>1. Explain how an LLM writes an answer to someone who isn't technical.</strong></summary>

It reads everything it's been given in small chunks called tokens, then predicts the most likely next chunk, adds it, and repeats until the reply is done. It's very good at producing text that sounds like a good answer. It isn't looking anything up while it does it, unless we give it the information or a tool.
</details>

<details>
<summary><strong>2. Why do LLMs hallucinate, and what would you do about it in a product?</strong></summary>

They're trained to produce plausible text, and research suggests training and scoring reward a confident guess more than "I don't know". In a product I'd give the model the facts it needs, like the FAQ, tell it to say when the answer isn't there, ask it to quote or cite its source, and test for it with cases where the right answer is "I don't know". I wouldn't assume any of that takes the risk to zero.
</details>

<details>
<summary><strong>3. The same prompt gives different answers. What does that mean for testing?</strong></summary>

One good answer only shows the model can get it right, not that it will every time. So I'd use a fixed set of test cases, run the important ones several times, and require the safety cases to pass every run. Then I'd rerun the whole set whenever the prompt, the model or the data changes.
</details>

<details>
<summary><strong>4. What's a context window, and why do long conversations cost more?</strong></summary>

It's everything the model can see for one reply: the system prompt, the conversation, any documents or tool results, and the reply itself. The API doesn't remember anything between requests, so the app sends the whole conversation every turn. Each turn is bigger than the last, which costs more, slows things down and can make answers worse as the context gets long.
</details>

<details>
<summary><strong>5. How does tool calling work?</strong></summary>

You describe the tools in the request. When the model wants one, it replies with a structured request naming the tool and its inputs instead of a normal answer. Your code checks it, runs it and sends the result back in the next request. The model then either asks for another tool or writes the final reply. The model never runs anything itself. Your code is in charge of the loop.
</details>

<details>
<summary><strong>6. When would you not use an agent?</strong></summary>

When I can write the steps down ahead of time. A workflow with fixed steps is easier to test, cheaper and more predictable. I'd also keep high-stakes decisions, like safety handoffs or anything with money, in code rather than leaving them to the model's choice at runtime. I'd use an agent where the steps really depend on what it finds along the way.
</details>

<details>
<summary><strong>7. Explain RAG to a stakeholder.</strong></summary>

The model doesn't know our documents. When a question comes in, we search our documents for the most relevant parts and hand them to the model along with the question, so it answers from our material instead of from memory. If the answer's wrong, I'd check two things separately: did the search find the right part, and did the model use it correctly?
</details>

<details>
<summary><strong>8. What's the difference between confidence and correctness?</strong></summary>

Confidence is how sure the model says it is. Correctness is whether it's actually right, which you can only check against a known answer. Calibration is whether they line up. I wouldn't build a rule like "hand off below 80% confidence" until someone had checked the confidence against real answers for our use case.
</details>

## Further reading

**Start here**
- [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs), 3Blue1Brown (video). A short, visual intro to next-token prediction.
- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), Andrej Karpathy (video). The classic one-hour explainer for general audiences, including an early look at prompt injection.
- [Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial), Anthropic. Hands-on chapters on roles, separating data from instructions, and avoiding hallucinations.
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners), Microsoft. A free course of 21 lessons, each with a video.

**Go deeper**
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), Andrej Karpathy (video). Over three hours on how models are trained, from raw text to an assistant.
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents), Anthropic. Workflows vs agents, the common patterns, and when not to build an agent.
- [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/), Simon Willison. The agent loop explained plainly, including why the conversation is resent every time.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), Jay Alammar. The best-known visual walkthrough of what's inside a model.
- [LLM Course](https://huggingface.co/learn/llm-course), Hugging Face. Free and hands-on, for when you want to touch real models.

**Primary sources**
- [Glossary](https://platform.claude.com/docs/en/about-claude/glossary), [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) and [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), Anthropic docs. The definitions and API behaviour I used in this lesson.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762), Vaswani et al. (2017). The paper that introduced the transformer.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), Lewis et al. (2020). The paper that named RAG.
- [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664), Kalai et al. (2025). Why training and scoring reward guessing.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599), Guo et al. (2017), and [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221), Kadavath et al. (2022). The two calibration papers from Part 4.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml), Google. Practical rules on offline tests, launches and the gap between them.

## Next lesson

**Next: [Lesson 3, Your first pull request](../03-your-first-pull-request/).** You'll make a real change to the Polish & Co. FAQ, the same FAQ the model reads in this lesson, and ship it as a pull request in your browser in about an hour.

After that:
- [Lesson 5, Build something with an AI agent](../05-build-with-an-ai-agent/) puts the agent loop to work on code.
- [Lesson 6, Evals 101](../06-evals-101/) turns "it answers differently every time" into a test you can run.

[Back to the lesson](README.md) | ← [Lesson 1, How software works](../01-how-software-works/) | **Next: [Lesson 3, Your first pull request](../03-your-first-pull-request/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
