<sub>Lesson 8, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge and practise the questions you'd get in an interview.

## What I learned doing this

Checking the grader against my own judgment is the step that's easiest to skip, and it's the one that matters most. Until I've done it, I don't know if the judge's grades mean anything.

A few other things I'd tell myself at the start:
- **Grade blind.** I grade a batch myself before I look at the judge's grades. Once I've seen its answer, I start agreeing with it without meaning to.
- **Plant failures.** I make sure several replies in the check set are deliberately bad. Otherwise a grader that passes everything looks perfect.
- **Grade line by line.** When I graded on gut feel, I missed things. Going through the written rubric one line at a time caught them.
- **When the rules change, the answer key changes too.** If the salon changes a policy, my labels and the rubric examples have to change with it, or the judge gets checked against the wrong answers.
- **Use a stronger, different model as the judge.** The judge has the harder job, and a model grading its own writing is too kind.

## You're done when

- [ ] Every check in your golden set is marked "code" or "judge", with a reason
- [ ] Every must-pass case is checked by code, or marked for a person to read before release
- [ ] You have a rubric with two pass or fail criteria, each with pass and fail examples
- [ ] You have a judge prompt for each criterion, with worked examples from the `example` rows only
- [ ] You graded the check set yourself before you saw the judge's grades
- [ ] You know the judge's fail catch rate and pass match rate for each criterion
- [ ] Every disagreement on the `dev` rows has a written cause and a fix
- [ ] The judge passed your bar on the `test` rows, and you wrote down the model and prompt version

## Challenge

Add a third criterion to the rubric: **"Stays short."** The salon's rule is two or three sentences.

1. Write the pass and fail lines and two examples of each.
2. Before you build a judge for it, ask yourself whether code could check it instead. (Counting sentences is mostly code. Is there a part that isn't?)
3. Add four rows to the check set that test it, including one long reply that's otherwise perfect.

Which parts ended up in code, and which in the judge?

## Check yourself (interview style)

<details>
<summary><strong>1. When would you use an LLM as a judge, and when wouldn't you?</strong></summary>

I'd use one for things code can't check reliably, like tone, or whether an answer only uses facts from a source. I wouldn't use one for anything code can check, like a required phrase, a banned word or a real price. And I wouldn't let a judge be the only thing that passes a safety-critical case. Those stay deterministic where possible, and if they need judgment, a person reviews them before release.
</details>

<details>
<summary><strong>2. How do you know your LLM judge is right?</strong></summary>

I grade a set of outputs myself first, without seeing the judge's grades, and I plant some deliberately bad ones. Then I compare. I look at how many of my fails it caught and how many of my passes it matched, separately, because one agreement number can hide a judge that passes everything. I read every disagreement, fix the rubric or the prompt, and then test it once on examples it's never seen.
</details>

<details>
<summary><strong>3. Why pass or fail instead of a 1 to 10 score?</strong></summary>

Pass or fail forces a clear decision and is graded more consistently, by people and by models. Nobody agrees on what a 6 versus a 7 means, and an average score still doesn't tell you whether to ship. I keep the binary grade and add a one-line reason, so I get the decision and the detail.
</details>

<details>
<summary><strong>4. What biases do LLM judges have, and how do you handle them?</strong></summary>

Three well documented ones. Position bias, where it favours one slot in a comparison, so I swap the order and only count consistent wins. Verbosity bias, where it favours longer answers, so the rubric says length isn't a reason to pass and I plant long but wrong examples. Self-preference, where a model rates its own writing more kindly, so I use a different model as the judge.
</details>

<details>
<summary><strong>5. Your judge agrees with you 90% of the time. Is that good enough?</strong></summary>

It depends where the 10% is. If most replies pass, a judge that passes everything also scores high. I'd want to know its catch rate on the replies I failed. Missing real failures is much worse than being a bit strict. I'd also want to know how many examples that 90% is based on, because on a small check set it's a rough number.
</details>

## Further reading

**Start here**
- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/), Hamel Husain. The step-by-step method: a domain expert grades pass or fail with critiques, and the judge is built and checked against them.
- [AI Evals: Everything You Need to Know (FAQ)](https://hamel.dev/blog/posts/evals-faq/), Hamel Husain and Shreya Shankar. Read "How do I know if I can trust my automated eval?" next.

**Go deeper**
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), Anthropic. Choosing between code, human and model grading, with tips for LLM graders.
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/), Eugene Yan. A practitioner's review of the research.
- [An LLM-as-Judge Won't Save The Product, Fixing Your Process Will](https://eugeneyan.com/writing/eval-process/), Eugene Yan. Why the habit of looking at data matters more than the tool.

**Primary sources**
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685), Zheng et al. (2023). Names position, verbosity and self-enhancement bias, and measures how often strong judges agree with people.
- [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076), Panickssery, Bowman and Feng (2024). The self-preference study.
- [Who Validates the Validators?](https://arxiv.org/abs/2404.12272), Shankar et al. (2024). Aligning judges with people, and why criteria drift as you grade.

## Next lesson

**Next: [Lesson 9, Evals in CI](../09-evals-in-ci/).** You'll run the golden set automatically on every pull request with GitHub Actions, so a change that breaks a must-pass case can't merge.

[Back to the lesson](README.md) | ← [Lesson 7, Golden sets](../07-golden-sets/) | **Next: [Lesson 9, Evals in CI](../09-evals-in-ci/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
