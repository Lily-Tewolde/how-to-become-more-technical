<sub>Lesson 13, Part 3 of 6 · about 15 min</sub>

# Hard rules, model judgment and the never list

**In this part,** you'll decide which decisions belong to rules in code, which to the model and which to a person, then write down what the AI is never allowed to do.

## Why this matters

Models are very good with language. They can read a messy message, pull out what matters, and write a clear summary. They're not a safe place to make decisions that have a right answer written in a policy, like who's eligible, what something costs, or what a dose is. Those decisions need to be the same every time, explainable afterwards, and easy to change when the policy changes. Rules in code do all three. A model does none of them reliably.

In a salon, the price check from [Guardrails](../11-guardrails/part-3-checks-after.md) protects $15. In an insurance product, the same pattern protects whether someone's claim gets paid.

## Do it (step by step)

11. **List every decision your product makes, and give each one an owner.** There are three possible owners:

    | Owner | Good for | Examples |
    |---|---|---|
    | **Rules in code** | Anything with a right answer in a policy | Who's eligible, prices and premiums, coverage limits, deadlines, which tier a crisis flag goes to |
    | **The model** | Language work, with checks after | Turning a messy answer into structured fields, writing a summary, phrasing a question, sorting free text into categories |
    | **A person** | Judgment, exceptions, anything that can't be undone | Diagnosis and treatment, approving an exception, a claim denial, anything a rule can't cover |

    A useful test: if a customer asked "why did this happen?", could you point to the rule? If the honest answer is "the model decided", that decision is in the wrong column.

    You're done when every decision has one owner, and nothing with a right answer in a policy is owned by the model.

12. **Let rules decide, and let the model only feed them.** The model can turn "I'm 17 and live in Manitoba" into `age: 17, province: MB`. A rule then decides whether that person can use the service. The model never says "you're eligible". If the model can't pull out a clear value, the rule treats it as unknown and asks again or sends it to a person. It never guesses.

    Business rules work as a hard filter, never as a hint to the model. "Prefer not to book people under 18" in a prompt is a hint. `if age < 18: route_to_person()` is a rule.

    You're done when every rule-owned decision is made by code from structured fields, and "unknown" has its own path.

13. **Never silently correct something that could mean two things.** Some inputs look like typos but might not be. A medication name typed with one letter wrong could be a different medication. A policy number with a swapped digit could be someone else's policy. The model will happily "fix" these to the closest match, and it'll sound sure.

    The rule: keep exactly what the person typed, mark it unclear, and ask them or flag it for a person. Store the person's own words separately from any cleaned-up version, so a reviewer can always see what was actually said.

    You're done when you have test cases for look-alike inputs, and every one of them keeps the original text and gets marked unclear.

14. **Write the never list.** This is a short, plain list of things your AI must never do, whatever the user says and whatever the prompt says. Use [`never-list-template.md`](never-list-template.md). Every line needs four things:
    1. **The rule**, in one sentence anyone can understand
    2. **Why**, in plain words
    3. **Where it's enforced**, which should be more than just the prompt
    4. **The test cases** that prove it holds

    A few examples, from the salon and from a made-up health product:

    | Never | Enforced in | Tests |
    |---|---|---|
    | Give medical advice (salon) | Must-escalate detector before the model, medical advice check after | ME-01 to ME-05 |
    | Quote a price that isn't in the price list (salon) | Price check in code | Price check cases, INJ-02 |
    | Diagnose, or say what a symptom "probably" is (health) | Prompt, output check for diagnostic phrases, clinician review | Diagnosis bait cases |
    | Change, suggest or comment on a dose (health) | Output check, medication fields copied exactly from the patient | Dose change cases |
    | Tell someone they're eligible or covered (health, insurance) | Rules in code decide, the model can't produce that wording | Eligibility cases |

    If a line has no tests, nothing tells you when it stops holding. So every line points to cases in your golden set, and they're all must-pass.

    You're done when your never list has at least five lines, each with an enforcement point and at least one must-pass test case.

    <details><summary>Stuck?</summary>

    - **"My never list keeps growing."** Keep it short. If a line is really a style preference, it belongs in the prompt and your averaged evals. The never list is for things that could hurt someone or break a law.
    - **"Who decides what goes on it?"** The PM drafts it. The people who own the risk sign it off: clinical, legal, compliance, or whoever answers for that kind of mistake in your company. Part 4 covers sign-off.
    </details>

<details>
<summary><strong>Go deeper (keep the record of what was said separate from what the system decided)</strong></summary>

In high-stakes products you'll often have three versions of the same information:
1. **What the person said**, word for word
2. **What the model extracted**, as structured fields
3. **What the system decided**, from the rules

Keep all three, and label them clearly. A clinician reading an intake summary should be able to see that "patient wrote 'my chest feels tight when I climb stairs'" is a quote, and "symptom: chest tightness, on exertion" is the model's extraction. If those get blended, a reviewer can't tell where a mistake came in.

The same idea makes summaries checkable. If every line of a summary has to cite the message it came from, a test can check that the cited message exists and says something close. A summary line with no source is either removed or flagged.
</details>

## Quick check

<details>
<summary>1. The model reads "I'm 17" and replies "You're eligible for our service." What's wrong?</summary>

The model made an eligibility decision. It should only extract `age: 17`, and a rule in code should decide eligibility.
</details>

<details>
<summary>2. A patient types a medication name with a typo that could be one of two medicines. What should the assistant do?</summary>

Keep exactly what they typed, mark it unclear, and ask them or flag it for a person. Never silently correct it to the closest match.
</details>

<details>
<summary>3. What four things does every line on the never list need?</summary>

The rule, why it matters, where it's enforced, and the test cases that prove it holds.
</details>

---

**Next: [Part 4 (Audit trails, sign-off and monitoring)](part-4-audit-review-monitoring.md)** | [Back to the lesson](README.md)
