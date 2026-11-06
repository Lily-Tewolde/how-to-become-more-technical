<sub>Lesson 7, Part 4 of 5 · about 10 min</sub>

# How many cases is enough

**In this part,** you'll see how big a golden set should be, why a score on a small set is a rough reading, and why must-pass cases never get averaged in.

## Do it (step by step)

### 12. Start small, and grow on purpose

**20 to 50 is a real starting size.** Anthropic's agent evals guide says "20-50 simple tasks drawn from real failures is a great start" ([Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)). Hamel Husain and Shreya Shankar's [AI Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) adds that "a purpose-built eval set often grows to 100 or more examples."

So 40 is a fine size for Polish & Co. today. You know you need more when:
- a cell in your coverage grid from Part 1 is still empty
- new real messages keep finding failures your set didn't catch
- you want to tell two good prompts apart, not just catch a broken one (step 13 explains why that takes more cases)

You know you have enough for now when new cases stop finding new problems.

**You're done when** you can say why your set is the size it is, in one sentence.

### 13. Read every score as a range

**A score on a small set is a rough reading.** Say 18 of 20 cases pass. That's 90%. But if you wrote 20 different, equally fair cases, you might get 16 or 20. The 90% is one draw.

Here's how wide that wobble is. I worked these out with a standard formula called the Wilson interval. Each range is where the "true" pass rate probably sits (95% confidence):

| Cases passed | Score | The real rate is probably between |
|---|---|---|
| 18 of 20 | 90% | about 70% and 97% |
| 36 of 40 | 90% | about 77% and 96% |
| 90 of 100 | 90% | about 83% and 95% |
| 180 of 200 | 90% | about 85% and 93% |

Same 90%, very different certainty. Two things follow.

**Small changes on small sets are noise.** If your prompt goes from 17 of 20 to 19 of 20, that feels like progress. It might be. But the ranges overlap so much that it might also be luck. Read the cases that flipped instead of celebrating the number. Did they flip for a reason you can explain?

**A small set is a smoke alarm.** It tells you when something is badly broken. It can't tell you a change made answers 5% better. For that, you need hundreds of cases, or real usage after launch.

Anthropic's research team makes the same point for model benchmarks in [A statistical approach to model evaluations](https://anthropic.com/research/statistical-approach-to-model-evals). They "encourage researchers to report the SEM", the standard error, next to every eval score, so readers can see how much it might wobble.

<details>
<summary><strong>Go deeper (the Wilson interval in a few lines of Python)</strong></summary>

You don't need to memorise this. It's here so you can check your own numbers.

```python
import math

def wilson(passed, total, z=1.96):
    """95% range for a pass rate. Works better than the simple formula on small sets."""
    p = passed / total
    centre = (p + z * z / (2 * total)) / (1 + z * z / total)
    spread = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / (1 + z * z / total)
    return centre - spread, centre + spread

print(wilson(18, 20))  # about (0.70, 0.97)
```

Why not just use plus or minus a standard error? On small sets and scores near 100%, the simple formula gives ranges that run past 100% or shrink to nothing when every case passes. The Wilson interval stays sensible. The [paper behind Anthropic's post](https://arxiv.org/abs/2411.00640) covers the standard error approach and when to use it for larger evals.
</details>

### 14. Never average the must-pass cases

**Must-pass cases are gates, not part of the score.** In Evals 101 you saw why. A 95% average can hide the one missed allergic reaction. Here's the statistics version of the same point.

Say all 12 must-escalate cases pass. That feels like proof the bot is safe. It isn't. With 12 cases and zero misses, a real miss rate as high as about 22% still can't be ruled out. With 7 cases it's about 35%. Zero fails on a small set means "nothing is obviously broken". It doesn't mean "this never fails".

So for must-pass cases:
1. **Any single fail stops the release.** No averaging, no trading a safety miss against better FAQ answers.
2. **Run each one several times.** The pass^k idea from [Evals 101, Part 3](../06-evals-101/part-3-run-and-grade.md). Three runs of 12 cases gives you 36 tries, not 12.
3. **Keep adding must-pass cases.** Different wording, different people writing, the important bit in a different spot. More cases is the only way to shrink that "can't rule out" number.
4. **Watch real conversations after launch.** The golden set is a gate before launch. It's not a guarantee after.

One honest caveat. Running the same message three times checks that the bot is consistent. It doesn't cover new customers or new wording. That's what more cases are for.

**You're done when** your must-pass cases are reported on their own line, as "all passed" or "these failed", and never folded into a percentage.

<details>
<summary><strong>Go deeper (the rule of three)</strong></summary>

There's a handy shortcut for "zero fails in n tries". The most the real failure rate could plausibly be (at 95% confidence) is roughly 3 divided by n. Twenty clean runs means the real rate could still be up to about 15%. To claim a miss rate under 1%, you'd need around 300 clean runs in a row. The numbers in step 14 use the exact version of this calculation, which gives slightly smaller values on tiny sets.

That's why teams with high-stakes AI features don't rely on pre-launch evals alone. [Lesson 13: When AI mistakes are expensive](../13-when-ai-mistakes-are-expensive/) goes further.
</details>

## Quick check

<details>
<summary>1. Your prompt went from 17 of 20 to 19 of 20. Is it better?</summary>

Maybe, but the difference is small enough to be luck on 20 cases. Read the cases that flipped and check you can explain why.
</details>

<details>
<summary>2. All 12 must-escalate cases passed. Is the bot safe?</summary>

You can't say that from 12 cases. A real miss rate of about 22% still can't be ruled out. It means nothing is obviously broken, so keep adding cases and keep watching after launch.
</details>

<details>
<summary>3. Why report must-pass cases on their own line?</summary>

Because they're gates. One fail stops the release, so folding them into an average would hide exactly the miss that matters.
</details>

---

**Next: [Part 5 (Wrap up)](part-5-wrap-up.md)** | [Back to the lesson](README.md)
