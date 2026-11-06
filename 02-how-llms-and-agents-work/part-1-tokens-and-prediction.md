<sub>Lesson 2, Part 1 of 5 · about 10 min</sub>

# Tokens and prediction

**In this part,** you'll see what tokens are, how a model builds a whole reply by predicting one token at a time, and why that makes it sound right even when it's wrong.

**Quick check before you start.** If you can answer both of these, skip ahead to the "Go deeper" sections.
1. Why can the same question get two different answers from the same model?
2. Why does a model sometimes make up a fact that sounds completely real?

## Why this matters

Almost every surprise people have with AI comes back to one fact: the model is predicting likely text, not looking up true answers. Once that clicks, a lot of other things make sense:
- why it's priced and limited in tokens
- why it can make things up so confidently
- why you can't test it once and call it done
- why the salon's rule "answer only from the FAQ" matters so much

## How it works

### 1. See text as tokens

**Picture the model reading in small chunks, not letters or whole words.** Those chunks are called **tokens**. Anthropic's glossary says tokens "can correspond to words, subwords, characters, or even bytes" ([Claude glossary](https://platform.claude.com/docs/en/about-claude/glossary)).

So a sentence like "Polish & Co. is open Tuesday to Saturday" might get split into something like:

```text
Pol | ish |  & |  Co | . |  is |  open |  Tuesday |  to |  Saturday
```

That split is just to show the idea. Every model family splits text its own way. Anthropic's glossary gives a rough size: on its earlier models "a token represents approximately 3.5 English characters", and its newer tokenizer makes about 30 percent more tokens for the same text.

Tokens matter to you because:
1. **Pricing is per token.** Both what you send and what the model writes back.
2. **Limits are in tokens.** How much the model can read at once, and how long its reply can be.
3. **Languages differ.** The glossary notes the count "depends on the model and the language", so the same message can cost more in one language than another.

### 2. Play the prediction game

**Watch how a reply gets built one token at a time.** Finish this sentence in your head:

> "Thanks for booking with Polish & Co.! See you on ___"

You probably thought of a day of the week. A model does the same thing with numbers. For every possible next token, it works out how likely it is. It picks one, adds it to the end, and does it again. A two-sentence reply is a few dozen of those picks in a row.

That's what Anthropic's glossary means when it says the model is "pretrained to predict the next word, given the previous context". Everything else the model seems to do, like answering, summarising or writing code, comes out of that one move repeated very fast.

Now try it for real. **Open a fresh chat in any AI app and ask "What are Polish & Co.'s opening hours?"** without pasting in the FAQ. Polish & Co. is made up, so there's no right answer to find. Watch what happens:
- If it says it doesn't know, that's good behaviour. It was trained to admit when it's missing information.
- If it gives you hours that sound real, that's a **hallucination**. It predicted what a salon's hours usually look like.

Either way, the point is the same. The model can only give you this salon's real hours if you give them to it. That's what the FAQ and rule 1 in the [running example](../example/) are for, and it's how you'll see RAG work in [Part 3](part-3-tools-agents-and-rag.md).

### 3. Ask the same thing twice

**Send the same message in two fresh chats and compare the answers.** Try "Write a two-sentence welcome message for a nail salon called Polish & Co." The two replies will almost certainly be worded differently.

That's because the model doesn't always pick the single most likely next token. It picks from the likely ones with a bit of randomness, so one different word early on sends the rest of the reply somewhere new.

Many model APIs have had a setting called **temperature** for how adventurous those picks are. Low is safer and more repetitive. High is more varied. Two things are worth knowing about it:
1. **Turning it down never made answers identical.** Anthropic's glossary says: "Even with temperature set to 0, the results will not be fully deterministic, and identical inputs might produce different outputs across API calls."
2. **On the newest Claude models you can't set it at all.** Anthropic's docs say to leave it out and "use prompting to guide the model's behavior instead" ([Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)).

So plan for variety. For a welcome message, variety is charming. For "my lips are swelling after my appointment", it's a risk. One good answer only shows the model *can* get it right. It doesn't show it *will* every time. That's the whole reason [Evals 101](../06-evals-101/) runs the must-escalate cases more than once.

<details>
<summary><strong>Stuck?</strong></summary>

- **"My two answers were the same."** Short, very predictable prompts can come out the same. Ask for something more open, like a short poem about gel nails, and try again.
- **"The app remembered my first answer."** Make sure you started a brand new chat, not a follow-up in the same one. You'll see why that matters in [Part 2](part-2-context-and-prompts.md).
</details>

## Why models make things up

A model is trained to produce text that sounds like a good answer. Most of the time, sounding right and being right line up. When the model doesn't have the information, they come apart, and it can produce something fluent and false.

A 2025 paper by Adam Tauman Kalai and colleagues puts it well:

> "Like students facing hard exam questions, large language models sometimes guess when uncertain."
> [Kalai et al., Why Language Models Hallucinate (2025)](https://arxiv.org/abs/2509.04664)

They argue models guess because the way they're trained and scored rewards a confident guess more than "I don't know". Anthropic's [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) guide suggests the fixes you'll see all through this hub:
1. Give the model explicit permission to say "I don't know".
2. Have it work from direct quotes of the source.
3. Have it cite where each claim came from, and drop any claim it can't support.

None of these take the risk to zero, so you still test for it. The "Not in the FAQ" group in the Evals 101 golden set exists to catch exactly this.

<details>
<summary><strong>Go deeper (how a model learns, and what it can't know)</strong></summary>

- **Pretraining.** The model is trained on a huge amount of text to predict the next token. Anthropic's glossary is frank that these pretrained models "are not inherently good at answering questions or following instructions".
- **Fine-tuning and RLHF.** Further training on examples of good behaviour, plus feedback from people (reinforcement learning from human feedback), turns a text predictor into an assistant that follows instructions.
- **It has a cutoff.** A model only knows what was in its training data, which stops at some date. It doesn't know your salon, today's prices or yesterday's news unless you put them in the request, or give it a tool to look them up.
- **It doesn't look things up by default.** Nothing in plain next-token prediction checks a fact. Any checking has to come from what you add around the model: the FAQ in the prompt, a search tool, a rule in code, or an eval.
</details>

## Quick check

<details>
<summary>1. What is a token, in one sentence?</summary>

A small chunk of text, often a word or part of a word, that the model reads and writes in.
</details>

<details>
<summary>2. If you set temperature to 0, will you always get the same answer?</summary>

No. Anthropic's docs say results still won't be fully deterministic, and the newest Claude models don't take a temperature setting at all.
</details>

<details>
<summary>3. Why might a model give a made-up salon's hours with total confidence?</summary>

It's predicting what a good answer usually looks like. Without the real hours in front of it, a plausible guess can come out sounding just as confident as a fact.
</details>

---

**Next: [Part 2 (Context and prompts)](part-2-context-and-prompts.md)** | [Back to the lesson](README.md)
