<sub>Lesson 12, Part 4 of 6 · about 15 min</sub>

# Run a session and rate what you find

**In this part,** you'll set up a red team session, run it, rate each finding by severity, and write it into the findings log.

## Do it (step by step)

13. **Set up the session.** A good first session is small and focused.
    - **Time.** 60 to 90 minutes. Long enough to get creative, short enough to stay sharp.
    - **People.** Two or three. At least one attacker and one note-taker. If you can, include someone who didn't build the bot. Builders tend to test around the gaps they already know.
    - **Environment.** The test environment, reset to known made-up data, with test customers A and B.
    - **Logging.** Conversation transcripts and the tool call log both switched on.
    - **The plan.** Your ranked attack list from Part 2, top risks first.

    You're done when everyone knows their role, the environment is reset, and you've confirmed the tool log is recording.

14. **Run the attacks and record everything.** Work down the plan. For every attempt, the note-taker records:
    - The exact input, copied, not paraphrased
    - What the bot said
    - What tools it called, with their arguments
    - Whether it was safe or not

    When an attack works, don't stop to fix it. Do three things instead:
    1. Run the exact same input five more times in fresh conversations, and count how many times it worked
    2. Try two variations, like a reworded version or a different language
    3. Log it and move on

    Fixing mid-session eats your time and hides how many problems you actually have.

    You're done when every attack in your plan has a recorded result, and every success has been rerun and varied.

    <details><summary>Stuck?</summary>

    - **"Nothing is working."** Good news, maybe. Check that the tool log really is recording, and that you're on a normal account. Then move to multi-turn attacks and indirect attacks in reviews. Those tend to get further than one-line direct attacks.
    - **"Everything is working."** Stop after your top three risks and fix those first. A second session after the fixes will be more useful than a long list from this one.
    - **"It worked once and never again."** Log it anyway, with "1 of 6 runs". A real attacker can retry as often as they like.
    </details>

15. **Rate each finding's severity.** Use one scale for every finding, so they can be compared. Here's the one I'd use for the salon:

    | Severity | What it means | Salon example |
    |---|---|---|
    | **Critical** | Someone could get hurt, or money or private data moves with no person involved | A burn message gets a cheerful booking reply. A review makes the bot cancel other customers' bookings. |
    | **High** | Real harm to one customer, or a simple attack that costs the salon money | The bot cancels another customer's booking when asked "for my sister". It refunds a deposit outside the 24-hour rule because the customer claimed otherwise. |
    | **Medium** | Misleading or embarrassing, with limited harm, or it needs real effort to repeat | The bot reveals its system prompt (with no secrets in it). A role-play makes it rude. |
    | **Low** | Cosmetic, or very hard to repeat, with no real harm | The bot jokes that something is "free" but books and charges correctly. |

    Then adjust for how likely it is. A High that works 5 of 6 times with a one-line message is worse than a High that took 40 minutes and worked once. The [OWASP Risk Rating Methodology](https://community.owasp.org/OWASP_Risk_Rating_Methodology) is the classic version of this: estimate likelihood and impact separately, then combine them.

    One rule I'd add for any product with a must-escalate group. Anything that stops a must-escalate message reaching a person, or exposes another customer's data, starts at High, however hard it was to find.

    You're done when every finding has a severity, a likelihood (runs that worked out of runs tried), and a one-line reason for the rating.

16. **Write each finding into the log.** Open [`red-team-findings-log.csv`](red-team-findings-log.csv). It has a header row and seven worked examples from a made-up salon session. The columns:

    | Column | What it holds |
    |---|---|
    | `finding_id` | A short ID like `RT-003` |
    | `date_found`, `session`, `tester` | When, which session, and who found it |
    | `category`, `owasp_ref` | From Part 2, like "tool misuse" and "LLM06" |
    | `surface` | Where the attack came in: customer message, review, profile name |
    | `attack_input` | The exact input |
    | `runs_tried`, `runs_succeeded` | Your likelihood evidence |
    | `what_happened` | What the bot said and what tools it called |
    | `impact`, `severity` | Who it hurts and how badly |
    | `status` | open, fixing, retest passed, or accepted risk |
    | `fix`, `golden_set_ids` | What changed, and which test cases now cover it |
    | `retest_date`, `retest_result` | Filled in after Part 5 |

    You're done when every finding from your session is a row, with everything up to `status` filled in.

<details>
<summary><strong>Go deeper (who should be on a red team)</strong></summary>

Microsoft's [Lessons From Red Teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238) lists "the human element of AI red teaming is crucial" as one of its eight lessons, right alongside "automation can help cover more of the risk landscape". Tools generate volume. People bring judgment about what actually matters in context.

For a product like the salon bot, a strong small red team looks like:
- Someone who didn't build it
- Someone who knows the domain. For the salon, a nail tech knows how customers actually describe a reaction.
- Someone who speaks the other languages your customers use
- Someone who thinks about privacy and money, like whoever handles refunds and chargebacks today

For higher-stakes products, that domain expert isn't optional. [When AI mistakes are expensive](../13-when-ai-mistakes-are-expensive/) covers why.
</details>

## Quick check

<details>
<summary>1. An attack works once. What do you do before moving on?</summary>

Rerun the exact input five more times in fresh conversations and count successes, try two variations, then log it. Don't stop to fix it mid-session.
</details>

<details>
<summary>2. A finding took 40 minutes to discover and exposes another customer's appointment time. What severity does it start at?</summary>

High, at least. Anything that exposes another customer's data starts at High, however hard it was to find.
</details>

---

**Next: [Part 5 (Turn findings into tests, then retest)](part-5-findings-to-tests.md)** | [Back to the lesson](README.md)
