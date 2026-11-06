<sub>Lesson 2, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll get a short look inside the model, see how fast long chats add up, and learn why some questions should never go to a search step. It's optional. Skip it if you're done for now.

<details open>
<summary><strong>Go deeper (what "attention" means, in one paragraph)</strong></summary>

Today's language models are built on the **transformer**, introduced in [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017). The key idea is **attention**: when the model works out the next token, it weighs every earlier token by how relevant it is. In "Sam booked a gel pedicure, and she wants to move it to 5pm", attention is what links "it" to the pedicure and "she" to Sam. That's also why the whole context window matters to every token it writes. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) walks through it with pictures, and 3Blue1Brown's [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) is a gentler start.
</details>

<details open>
<summary><strong>Go deeper (why long chats cost more than you'd think)</strong></summary>

Because the API is stateless, each turn resends everything before it. Say each customer message plus reply adds about 200 tokens, and leave out the system prompt to keep it simple:

| Turn | Tokens sent on this turn | Tokens sent so far |
|---|---|---|
| 1 | 200 | 200 |
| 2 | 400 | 600 |
| 5 | 1,000 | 3,000 |
| 10 | 2,000 | 11,000 |

Ten turns doesn't cost ten times one turn. It costs about 55 times, and the gap keeps growing, roughly with the square of the number of turns. Add a long system prompt with the whole FAQ and every row gets bigger.

**Prompt caching** is the main fix. The provider stores the start of the request so it doesn't have to process it again. Anthropic's docs say caching covers "`tools`, `system`, and `messages` (in that order)", and that "changes at each level invalidate that level and all subsequent levels" ([Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)).

That has a practical design rule hiding in it. Keep the parts that never change, like the tools, the rules and the FAQ, at the start and exactly the same every time. If you put something that changes on every request near the top, like today's date and time, you break the cache for everything after it.
</details>

<details open>
<summary><strong>Go deeper (search can't count)</strong></summary>

RAG is great for "find me the part of our documents about cancellations". It's the wrong tool for "how many gel pedicures did we do in October?"

Meaning search finds pieces of text that are *similar* to the question. It returns a handful of the closest matches, so it can't see every row, and it has no idea how to add things up. A count is a database question. It's the `SELECT` from [Lesson 1, Part 3](../01-how-software-works/part-3-databases.md), and it always was.

A useful habit before you design any AI feature that answers questions is sorting the questions people will actually ask:
1. **Lookup.** "What time do you open Sunday?" One fact, one place. A database read or the FAQ.
2. **Count or sum.** "How many no-shows last month?" A database query, maybe written by the model as a tool call, run by your code.
3. **Similar.** "Do you have anything like a French manicure?" Meaning search is good at this.
4. **Passage.** "What's your policy if I'm late?" Retrieve the section, then have the model answer from it. That's RAG.

Once you've sorted the questions, the design mostly falls out. You often end up with RAG for some, plain database tools for others, and no AI at all for a few.
</details>

---

[Back to the lesson](README.md) | [Part 5 (Wrap up)](part-5-wrap-up.md)
