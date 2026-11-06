<sub>Lesson 2, Part 2 of 5 · about 15 min</sub>

# Context and prompts

**In this part,** you'll see what's in a model's context window, the difference between a system prompt and a user message, and you'll build the actual request the salon's back end sends to the model.

## Why this matters

The model only knows what's in the request you send it, right now. It doesn't remember last week's chat with the same customer, or even the message before this one, unless your app sends it again.

That one fact explains:
- why long chats get slower and cost more
- why an assistant can "forget" something you told it earlier
- why the rules you write for the model are so easy to argue with
- why you need to test with the same fixed inputs every time

## How it works

### 4. Open the folder

**Picture everything the model can see as one folder.** That's the **context window**. Anthropic describes it as the model's "working memory":

> "The 'context window' refers to all the text a language model can reference when generating a response, including the response itself."
> [Anthropic, Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)

The same page says "everything in the request counts toward the context window": the system prompt, every message, any tool definitions, and the reply the model writes.

What goes in the folder comes in three roles:

| Role | Who writes it | At Polish & Co. |
|---|---|---|
| **System prompt** | You, the builder. It's the same for every customer. | "You're the booking assistant for Polish & Co." plus the rules and the FAQ |
| **User message** | The customer | "Are you open on Sundays?" |
| **Assistant message** | The model, on earlier turns | "Yes! Sundays we're open 11am to 5pm." |

The system prompt is the owner's rules in the temp's folder, from the TIP box on the [lesson home](README.md). The user message is whatever the customer types, so you don't control it. Anthropic's API docs describe the system prompt as "a way of providing context and instructions to Claude, such as specifying a particular goal or role" ([Create a Message](https://platform.claude.com/docs/en/api/messages/create)).

### 5. Build the salon's request

**Write out the request the back end sends to the model.** Remember from [Lesson 1](../01-how-software-works/part-2-apis-json-and-status-codes.md) that a request is a method, an endpoint and a JSON body. Calling a model works exactly the same way. The salon's back end sends a `POST` to the model provider's messages endpoint with a body like this:

```json
{
  "model": "claude-opus-5-5",
  "max_tokens": 300,
  "system": "You're the booking assistant for Polish & Co., a nail salon. Answer only from the FAQ below. If the answer isn't there, say so and offer to connect the customer with the salon. Never give medical advice. Be warm and short.\n\n<faq>\nHours: Tuesday to Saturday, 10am to 7pm. Sunday 11am to 5pm. Closed Mondays.\n...\n</faq>",
  "messages": [
    { "role": "user", "content": "Are you open on Sundays?" }
  ]
}
```

Line by line:
1. **`model`** says which model to use. The names change as new models come out.
2. **`max_tokens`** caps how long the reply can be. Remember, tokens.
3. **`system`** is the system prompt, with the FAQ wrapped in `<faq>` tags so the model can tell where it starts and ends.
4. **`messages`** is the conversation so far. Right now it's one customer message.

The response comes back as JSON too. Its content is the reply text, something like "Yes! We're open Sundays from 11am to 5pm." It also carries a `stop_reason`. `end_turn` means the model finished its reply on its own.

Notice where this request comes from. It's built on the salon's back end, not on the customer's phone. The system prompt, the FAQ and the key that pays for the model all stay on the server, for the same reason the price did in Lesson 1.

### 6. Send the second turn

**Add a second customer message and see what the request has to carry.** The customer replies "great, and how much is a gel pedi?" Here's the new `messages` list:

```json
"messages": [
  { "role": "user", "content": "Are you open on Sundays?" },
  { "role": "assistant", "content": "Yes! We're open Sundays from 11am to 5pm." },
  { "role": "user", "content": "great, and how much is a gel pedi?" }
]
```

The whole conversation goes again, plus the system prompt. That's not a quirk of this example. Anthropic's docs say it plainly:

> "The Messages API is stateless, which means that you always send the full conversational history to the API."
> [Anthropic, Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

So the model's "memory" is really your app re-sending the folder every time. Here's what that means for you as a PM:
1. **Long chats cost more and get slower.** Every turn sends everything before it again. [Extra credit](extra-credit.md) shows how fast that adds up.
2. **Forgetting is a product decision.** When a chat gets too long, something has to be dropped or summarised. Anthropic notes chat apps "can also manage the context window on a rolling 'first in, first out' basis", which means the oldest messages go first.
3. **More context isn't always better.** The same page warns that "as token count grows, accuracy and recall degrade", which it calls context rot. A short, relevant folder often beats a huge one.
4. **The model reads it all as one stream.** Your rules and the customer's text arrive together, and there's no hard wall between them. That's the root of [prompt injection](../10-prompt-injection/), and it's why nothing secret should go in a system prompt.

<details>
<summary><strong>Stuck?</strong></summary>

- **"Then how does a chat app remember me across days?"** The app saves your past chats, or notes about you, and puts the relevant parts back into the folder. The model itself still starts blank every time.
- **"What's the `\n` in the system prompt?"** It means "new line". JSON text has to fit on one line, so line breaks are written that way.
</details>

## Why this means you need evals

Put Part 1 and Part 2 together:
1. The same request can come back worded differently, or even decided differently.
2. A small change to anything in the folder, like the system prompt, the FAQ or the model name, can change every answer.

So you can't check an AI feature once and call it done. You need a fixed set of test messages that you send the same way every time, with a written idea of what a good answer does. That's an eval, and it's the next big section of this hub, starting with [Evals 101](../06-evals-101/).

<details>
<summary><strong>Go deeper (writing the system prompt like a spec)</strong></summary>

- **The system prompt is a product spec.** It's where your rules, tone and edge cases live. Anthropic's [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) covers being clear and direct, giving examples, and using tags like `<faq>` to separate parts.
- **History can be written by anyone who sends the request.** The Messages API docs point out that earlier turns "don't necessarily need to actually originate from Claude". That's useful for testing. It's also a reason to keep the conversation on your back end and not trust a history the phone sends you.
- **A rule in the prompt can still be broken.** The model usually follows it, which isn't the same as always. Anything that must never happen, like a free booking, gets enforced in code too. [Prompt injection](../10-prompt-injection/) and [Guardrails](../11-guardrails/) go further.
- **Try Anthropic's tutorial.** The free [Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) has hands-on chapters on roles, separating data from instructions, and avoiding hallucinations.
</details>

## Quick check

<details>
<summary>1. What's the difference between a system prompt and a user message?</summary>

The system prompt is written by the builder and is the same for every customer. It holds the rules and the FAQ. The user message is whatever the customer types, so the builder doesn't control it.
</details>

<details>
<summary>2. On the customer's fifth message, what does the request to the model contain?</summary>

The system prompt plus all five customer messages and the four replies before it. The API is stateless, so the whole conversation goes every time.
</details>

<details>
<summary>3. Why should the request to the model be built on the back end?</summary>

So the system prompt, the FAQ and the key that pays for the model stay on the server, where customers can't read or change them.
</details>

---

**Next: [Part 3 (Tools, agents and RAG)](part-3-tools-agents-and-rag.md)** | [Back to the lesson](README.md)
