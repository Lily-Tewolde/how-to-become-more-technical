<sub>Lesson 2, Part 4 of 5 · about 10 min</sub>

# Three distinctions

**In this part,** you'll learn three pairs of ideas that sound alike and aren't. Mixing them up is one of the most common ways AI features ship with a gap nobody noticed.

## Why this matters

You now know a model predicts likely text, can make things up, and can answer differently each time. The next question is how you decide whether it's good enough, and how you keep it good after launch. These three distinctions are the vocabulary for that conversation:
1. Evaluation vs feedback loop
2. Confidence vs correctness
3. Offline eval vs online metric

## How it works

### 11. Evaluation vs feedback loop

**Ask whether the team is only testing the assistant, or also learning from it.**
- **Evaluation** asks "is it good?" You run a fixed set of test messages and grade the answers.
- **A feedback loop** asks "how does what real customers do flow back in and make the next version better?"

You can have one without the other. Lots of teams build a solid eval before launch and then never add to it. The test set slowly stops looking like real customers, and it keeps passing while the product gets worse.

At Polish & Co., a feedback loop could look like this:
1. A customer asks about parking and the assistant makes something up.
2. Someone at the salon notices, or the customer complains.
3. That message becomes a new test case in the golden set, marked with what a good answer does.
4. Every future version is tested on it before it ships.

**The question to ask in a review:** "When a real customer gets a bad answer, how does it get into our tests?" [Golden sets](../07-golden-sets/) covers how to keep that set growing.

### 12. Confidence vs correctness

**Don't treat how sure the model sounds as how right it is.**
- **Confidence** is how sure the model says or seems it is.
- **Correctness** is whether it's actually right. You can only check that against a known right answer.
- **Calibration** is whether the two match. A well calibrated system that says it's 90% sure is right about 90% of the time.

This matters because a common design idea is "hand off to a person whenever the model is less than 80% sure". That only works if the confidence number has been checked against real answers. If it hasn't, you've built a rule on a number nobody's tested.

The research is mixed, which is exactly why you check for your own use case:
- A 2017 study found that "modern neural networks, unlike those from a decade ago, are poorly calibrated" ([Guo et al., On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)).
- A 2022 study found that "larger models are well-calibrated on diverse multiple choice and true/false questions", when the questions are put in the right format ([Kadavath et al., Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221)).

A salon chat isn't a multiple choice test. So for the must-escalate messages, like a rash or trouble breathing, I wouldn't lean on the model's confidence at all. Those get a rule in code and a handoff every time.

**The question to ask in a review:** "Has anyone checked this confidence score against real answers?"

### 13. Offline eval vs online metric

**Treat the pre-launch test as a gate, not the final answer.**
- **An offline eval** runs on a fixed test set before anything reaches customers. It decides whether a version is good enough to try.
- **An online metric** comes from real use after launch. It tells you whether the change actually helped.

For the salon, online metrics could be:
- the share of chats that end in a booking
- how often the assistant hands off to a person
- how often a customer asks the same thing twice in one chat
- how often staff have to fix a booking the assistant made

A version can pass every offline test and still do worse with real customers, because real customers ask things nobody wrote a test for. Teams often run an A/B test, where some customers get the new version and some get the old one, so the online numbers can be compared fairly. Google's Rules of Machine Learning is honest about how messy that comparison gets:

> "The only easy launch decisions are when all metrics get better (or at least do not get worse)."
> [Google, Rules of Machine Learning, Rule #39](https://developers.google.com/machine-learning/guides/rules-of-ml)

**The question to ask in a review:** "What number will we watch after launch, and what would make us roll it back?"

## All three on one page

| Distinction | The trap | The question to ask |
|---|---|---|
| Evaluation vs feedback loop | A test set that never learns from real customers | How do real failures get into our tests? |
| Confidence vs correctness | Trusting "I'm 90% sure" without checking it | Has the confidence score been checked against real answers? |
| Offline eval vs online metric | Calling it done because the tests passed | What will we watch after launch, and what triggers a rollback? |

<details>
<summary><strong>Go deeper (measuring calibration, and why offline and online drift apart)</strong></summary>

- **Measuring calibration.** Group the model's answers by how confident it was, then check how often each group was right. If the "90% sure" group is right 70% of the time, it's overconfident. Guo et al. use expected calibration error (ECE), which averages that gap across the groups.
- **Asking a model how sure it is** gives you text, not a measured probability. It can be useful, and it still has to be checked the same way.
- **Why offline and online drift apart.** Real traffic changes over time, and your test set was a snapshot. Google's Rules of Machine Learning, Rule #33, says that when you test a model on newer data than it was built on, you should expect it to do somewhat worse, but it "shouldn't be radically worse".
- **This is where evals get statistical.** How many test cases do you need before a difference is real and not luck? That question comes up in [Evals 101](../06-evals-101/) and the lessons after it.
</details>

## Quick check

<details>
<summary>1. The team has a great golden set from before launch and hasn't touched it in six months. Which distinction is missing?</summary>

The feedback loop. The evaluation exists, but real customer failures aren't flowing back into it, so it's getting stale.
</details>

<details>
<summary>2. Someone proposes "hand off when confidence is below 80%". What do you ask?</summary>

Whether that confidence has been checked against real answers. If the model isn't calibrated for this task, the threshold doesn't mean what it looks like it means.
</details>

<details>
<summary>3. A new version passes every offline test. Is it ready to roll out to everyone?</summary>

It's ready to try. The offline eval is a gate. Real use, ideally compared against the old version, decides whether it actually helped.
</details>

---

**Next: [Part 5 (Wrap up)](part-5-wrap-up.md)** | [Back to the lesson](README.md)
