<sub>Lesson 8, Part 2 of 5 · about 15 min</sub>

# Write the rubric

**In this part,** you'll pick what the judge grades, define pass and fail in plain words, and add examples so anyone (or any model) would grade the same way you do.

## Do it (step by step)

### 3. Pick one question per criterion

**Each criterion is one question with a yes or no answer.** For Polish & Co. there are two:
1. **Friendly tone.** Would a customer feel welcomed and respected reading this reply?
2. **Grounded in the FAQ.** Is every fact in this reply backed by the FAQ?

Keep them separate. "Is this a good reply?" mixes tone, facts and rules into one fuzzy grade. When it fails, you won't know which part to fix. Two clear questions give you two clear answers.

Start with one or two criteria. You can add more later, once these two work.

**You're done when** you've written each criterion as a single question.

### 4. Use pass or fail, not a 1 to 10 score

**Grade each criterion pass or fail.** A 1 to 10 scale feels more precise. In practice it causes three problems:
- **Nobody agrees on the middle.** Is a slightly stiff reply a 6 or a 7? You'll grade it differently on Monday and Friday, and the judge will pick its own number too.
- **You still have to decide.** A 6.4 average doesn't tell you whether to ship. Pass or fail does.
- **It hides the reason.** "6" says nothing. "Fail, it scolds the customer" tells you what to fix.

Hamel Husain and Shreya Shankar's [AI Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) puts it plainly: "Binary evaluations force clearer thinking and more consistent labeling." In his judge guide, Hamel describes the grade he wants from a domain expert as "just a clear pass or fail decision" ([Using LLM-as-a-Judge For Evaluation](https://hamel.dev/blog/posts/llm-judge/)).

To be fair, Anthropic's evals guide says either can work. You can tell a judge to output only "correct" or "incorrect", or a score from 1 to 5, as long as you're specific ([Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)). I stick with pass or fail plus a one-line reason. You get the decision and the detail.

**You're done when** every criterion has exactly two possible grades.

### 5. Define pass and fail, with examples

**Write what passes, what fails and a few real examples of each.** Open [`judge-rubric.md`](judge-rubric.md) next to this page. Each criterion has the same four parts:
1. **The question.** One line.
2. **Pass if all of these are true.** A short list.
3. **Fail if any of these are true.** A short list.
4. **Examples.** Real replies, graded, each with a one-line reason.

Then add the lines that stop the most common mistakes:
- **"Length isn't a reason to pass."** Judges tend to prefer longer answers (more in [Part 4](part-4-check-the-judge.md)), and the salon's rule is short. So the rubric says so out loud.
- **"When in doubt, fail."** For grounding, a plausible made-up fact is the worst kind, because customers believe it. If the judge isn't sure a fact is in the FAQ, it should fail the reply.
- **What the judge doesn't grade.** The rubric lists the checks code handles, so the judge doesn't try to grade the handoff.

**Use your own salon replies for the examples.** Generic examples like "a rude reply" don't help much. "Ha, nice try. No freebies." does, because it's exactly the kind of thing your bot might say to the birthday freebie request.

**You're done when** a friend could read your rubric, grade five replies and get the same grades you would, without asking you anything.

<details>
<summary><strong>Stuck?</strong></summary>

- **"Everything I write is vague, like 'be nice'."** Write the fail list first. It's easier to say what's wrong ("scolds", "sarcastic", "per our policy") than what's right.
- **"Is a reply that's friendly but long a pass?"** Decide, and write it down. The salon's call is that long isn't a tone fail on its own, unless the answer gets lost. Length is easier to check in code by counting sentences.
- **"My examples all pass."** Write a bad reply on purpose for each fail line. You'll need those in Part 4 anyway.
</details>

<details>
<summary><strong>Go deeper (your rubric will change, and that's normal)</strong></summary>

Expect to rewrite the rubric after you grade your first batch. In [Who Validates the Validators?](https://arxiv.org/abs/2404.12272), Shankar et al. found that people refine their criteria as they grade real outputs. They call it criteria drift. You think "friendly" is clear until you meet a reply that's warm but slightly pushy, and then you have to decide.

When that happens:
1. Make the call.
2. Add the reply as a new example in the rubric, with your reason.
3. Regrade anything the change affects.

That's also why the rubric lives in the repo next to the golden set. When the definition changes, the change has a history and a reason, like any other change to the product.
</details>

## Quick check

<details>
<summary>1. Why grade tone and grounding as two separate criteria?</summary>

So when a reply fails, you know which part to fix. A single "is this good?" grade mixes them up.
</details>

<details>
<summary>2. Why does the rubric say "length isn't a reason to pass"?</summary>

Because LLM judges tend to favour longer answers, and the salon wants short ones. Saying it out loud in the rubric pushes back on that bias.
</details>

---

**Next: [Part 3 (Write the judge prompt)](part-3-write-the-judge-prompt.md)** | [Back to the lesson](README.md)
