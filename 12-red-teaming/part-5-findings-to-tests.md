<sub>Lesson 12, Part 5 of 6 · about 10 min</sub>

# Turn findings into tests, then retest

**In this part,** you'll turn every finding into golden set cases, fix the cause rather than the symptom, retest, and decide when the next session happens.

## Why this matters

A finding that only lives in a spreadsheet will come back. Someone changes the prompt, swaps the model or adds a tool, and the old attack quietly works again. Turning findings into golden set cases means every future change gets tested against everything your red team ever found.

## Do it (step by step)

17. **Turn each finding into at least three cases.** Open [`red-team-cases.csv`](red-team-cases.csv) next to the [findings log](red-team-findings-log.csv). Each finding becomes:
    1. **The exact attack.** Copied from `attack_input`, word for word.
    2. **A variation or two.** Reworded, split across messages, or in another language. RTC-01b splits the review injection across two reviews.
    3. **A control.** A normal message that looks a bit like the attack, so your fix doesn't start blocking real customers. RTC-CTRL-01 is a customer cancelling their own booking, which must still work after the RT-002 fix.

    Notice the new `expected_tool_calls` column. For an agent, a case only passes if the reply is right and the tool calls are right. RTC-02 passes only if no `cancel` call went through for customer B's booking, whatever the bot said.

    You're done when every finding has an exact case, at least one variation and a control, and each case lists the tool calls that should happen.

18. **Fix the cause, not the wording.** For each finding, ask which layer should have stopped it. Then fix it in the strongest layer you can:
    1. **Remove the ability.** The review summarizer gets no tools at all (RT-001).
    2. **Check it in code.** `cancel` checks booking ownership on the server (RT-002). `refund_deposit` reads the real cancellation time (RT-004).
    3. **Add an approval.** Refunds outside the rule go to a staff member, who sees the real booking record (RT-004).
    4. **Add a detection layer.** New words and a second model call for health messages (RT-005).
    5. **Change the prompt.** Last, and never on its own for anything above Medium.

    You're done when every Critical and High finding has a fix in layers 1 to 3, not just a prompt change.

19. **Retest, then rerun everything.** Retesting has three steps, in this order:
    1. **The exact attack, six times.** It has to fail every time. One success means the finding stays open.
    2. **The variations.** Same rule.
    3. **The whole golden set.** Every FAQ case, every must-escalate case, every injection case and every control.

    Step 3 is where you catch side effects. Look at RT-008 in the log. The fix for RT-005 added "angry" to the must-escalate words, and "these nails look angry in the best way" started getting a handoff. The fix worked, and it also created a new, smaller problem. That's normal. Log it as its own finding.

    Then update the log: `retest_date`, `retest_result` and `status`. A finding is only "retest passed" when all three steps pass.

    You're done when every fixed finding has a retest result, and you've rerun the full golden set after the last fix.

    <details><summary>Stuck?</summary>

    - **"We can't fix this one right now."** Mark it "accepted risk", and write why and when you'll revisit it. RT-006 is accepted because the system prompt has nothing private in it, with a note to revisit if that changes. An accepted risk with no reason is just an open bug.
    - **"The fix passes 5 of 6."** It's not fixed. Go back to step 18 and look for a stronger layer.
    </details>

20. **Run the red team cases on every change.** Add them to your golden set as their own group, next to the injection group from [Prompt injection, plainly](../10-prompt-injection/). Every must-pass case blocks a merge if it fails. [Evals in CI](../09-evals-in-ci/) shows how to run them on every pull request.

    You're done when a pull request that reopens any red team finding shows a failing check.

21. **Decide when the next session happens.** Red teaming isn't a one-off. Microsoft's red team lists "the work of securing AI systems will never be complete" as one of its lessons ([Bullwinkel et al., 2025](https://arxiv.org/abs/2501.07238)). Plan a new session when:
    - you add a tool or give an existing one more power
    - you connect a new source of outside content, like emails or web pages
    - you change the model, including an update you didn't choose
    - you're about to launch to more people
    - something goes wrong in real use

    Between sessions, automated tools can generate and run lots of attacks for you. [Promptfoo's red team quickstart](https://www.promptfoo.dev/docs/red-team/quickstart/), NVIDIA's [garak](https://github.com/NVIDIA/garak) and Microsoft's [PyRIT](https://microsoft.github.io/PyRIT) are well-known open-source options. They're great for volume. They don't replace a person who knows what matters for your product.

    You're done when the next session has a date or a trigger written down, and someone owns it.

<details>
<summary><strong>Go deeper (reporting a red team to the people who decide)</strong></summary>

After a session, write a short summary for whoever decides on launch. Keep it to one page:
1. **What we tested.** The scope, the tools, the session length and who took part.
2. **What we found.** Counts by severity, and one line on each Critical and High.
3. **What we fixed, and how we checked.** With retest results.
4. **What's still open or accepted, and why.**
5. **What we didn't test.** Be honest. "We didn't test the text message replies" is useful. Silence reads as "it's fine".

The last section is the one people skip, and it's often the most important. Saying what you didn't run is better than letting someone assume you did.
</details>

## Quick check

<details>
<summary>1. Why does every finding get a control case?</summary>

So the fix doesn't start blocking real customers. A control looks a bit like the attack but is a normal request, and it has to keep working after the fix.
</details>

<details>
<summary>2. A fix makes the exact attack fail six times out of six. Is the finding closed?</summary>

Not yet. The variations have to pass too, and then the whole golden set has to pass, so you know the fix didn't break something else.
</details>

---

**Next: [Part 6 (Wrap up)](part-6-wrap-up.md)** | [Back to the lesson](README.md)
