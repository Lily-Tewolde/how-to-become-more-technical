<sub>Lesson 13, Part 1 of 6 · about 15 min</sub>

# Why one miss outweighs a high average

**In this part,** you'll see how a great average hides the failures that matter, then split your results into must-pass gates and averaged quality scores.

**Quick check before you start.** If you can answer these, skip ahead to the "Go deeper" sections.
1. A safety case passes 99% of the time on a single run. What's the chance it passes five runs in a row?
2. You ran 50 crisis cases and none failed. Does that mean your miss rate is zero?

## Why this matters

Back in [Evals 101](../06-evals-101/part-2-write-your-test-cases.md), the salon bot scored 95% and still didn't ship, because the one miss was a customer with a swollen finger. That rule was a small part of a salon bot. In health, finance and insurance, it's most of the product.

Here's a made-up example to show the scale. A virtual clinic's intake assistant has 2,000 conversations a week. Say 1% of them, 20 a week, mention an emergency or a crisis. The detector catches 95% of those. That sounds good. It also means about one person a week, roughly 50 a year, gets a normal intake reply when they needed a person right away. If the other 1,980 conversations were all handled perfectly, the overall accuracy would be 99.95%.

An average treats every case as equal. These cases aren't equal. A slightly awkward question and a missed emergency both count as one fail, and only one of them can hurt someone.

## Do it (step by step)

1. **Split your eval into must-pass and averaged groups.** Go through every behaviour your product has and ask one question. If this goes wrong once, could someone be hurt, lose money they're owed, or be treated unfairly? If yes, it's must-pass. If no, it's averaged.

   | Must-pass (hard gates) | Averaged (quality bars) |
   |---|---|
   | Emergencies and crises get handed to a person | Questions are clear and easy to answer |
   | The AI never diagnoses, prescribes or decides coverage | Tone is warm and plain |
   | Medication names are kept exactly as typed | Summaries are concise |
   | Every summary line traces back to something the person said | Fewer follow-up questions needed |

   You're done when every behaviour is in one column, and nothing in the left column touches an average.

2. **Report the two groups separately, every time.** Your results table should never have a single "overall" number at the top. Lead with the gates, then the averages.

   | Group | Cases | Bar | Result | Gate |
   |---|---|---|---|---|
   | Emergency and crisis handoff | 40 | Every case, every run | 39 of 40 | **Fail** |
   | Never diagnoses or prescribes | 25 | Every case, every run | 25 of 25 | Pass |
   | Question clarity | 60 | 90% | 93% | n/a |
   | Tone | 60 | 90% | 88% | n/a (watch) |

   One failed gate fails the run, no matter how good the averages are. That decision should be written down before you run anything, so nobody argues it away after a disappointing result.

   You're done when your results template leads with the gates and has no blended overall score.

3. **Run must-pass cases several times, and count all of them.** AI outputs vary from run to run. When I built a flow that had to catch crisis messages, I ran every crisis case five times, and all five had to pass. A crisis case that passes four of five runs isn't 100%.

   The maths makes this real. If a case passes 99% of the time on one run, the chance it passes five runs in a row is 0.99 to the power of 5, about 95%. At 95% per run, five in a row drops to about 77%. That's pass^k from [Evals 101](../06-evals-101/part-3-run-and-grade.md): every run has to pass, because every real person only gets one.

   You're done when every must-pass case runs at least five times, and a single failed run fails the case.

4. **Test both directions, in every language you support.** A crisis detector that flags everything would pass step 3. So measure two numbers for every must-pass group:
   - **Miss rate.** Real crises it didn't catch.
   - **False alarm rate.** Normal messages it escalated. "I'm dying to get this appointment" isn't a crisis.

   Both need test cases in every language your users write in. A detector tuned in English can miss a crisis in French and panic at an idiom in Spanish.

   You're done when every must-pass group has both kinds of cases, in every supported language.

5. **Check your grader before you trust it on safety cases.** If a model grades your outputs, grade a sample yourself first, without looking at what the grader said. Plant some outputs you know are wrong, so a grader that passes everything can't look perfect. If you and the grader disagree on any safety case, fix the grader before you trust any of its results. [LLM-as-judge](../08-llm-as-judge/) covers how.

   You're done when you've blind-graded a sample that includes planted failures, and the grader agrees with you on every safety case.

<details>
<summary><strong>Go deeper (zero misses doesn't mean a zero miss rate)</strong></summary>

Say you ran 50 crisis cases and caught all of them. It's tempting to write "100% detection". But 50 cases can't prove that. A long-standing rule of thumb in medical statistics says that if you see zero events in N tries, the true rate could still be as high as about 3 in N, at 95% confidence. A short JAMA letter by [Newman (1995)](https://jamanetwork.com/journals/jama/article-abstract/389714) summarizes it, crediting Hanley and Lippman-Hand.

So zero misses in 50 cases is consistent with a real miss rate of up to about 6%. Zero in 300 gets you to about 1%. That's why I write "caught 50 of 50 test cases" instead of "catches every crisis". It's honest about what the test can show, and it's a reason to keep growing the must-pass set from real conversations after launch.
</details>

<details>
<summary><strong>Go deeper (confidence isn't correctness)</strong></summary>

A common design is "hand off to a person when the model's confidence is below X". That only works if the confidence number means something. What a model says about how sure it is isn't the same as being right, and modern models are often overconfident. [Guo et al. (2017), On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) is the classic paper on this gap, called calibration.

Before you use a confidence threshold for anything must-pass, check it against real labelled cases. And for emergencies, don't rely on a threshold at all. Any sign of an emergency should escalate, however unsure the model is.
</details>

## Quick check

<details>
<summary>1. Your eval is 99% overall, and one emergency case failed one of its five runs. Does it ship?</summary>

No. The emergency group is a hard gate, and one failed run fails the case. The overall number doesn't matter.
</details>

<details>
<summary>2. Why measure the false alarm rate on a crisis detector, if missing a crisis is worse?</summary>

Because a detector that flags everything would look perfect on misses. Too many false alarms also wear out the people responding, and they start to ignore alerts. You need both numbers to know the detector actually works.
</details>

---

**Next: [Part 2 (Crisis and safety protocols)](part-2-crisis-protocols.md)** | [Back to the lesson](README.md)
