<sub>Lesson 11, Part 4 of 5 · about 10 min</sub>

# Escalate, refuse kindly, log, and count the cost

**In this part,** you'll make sure a handoff actually reaches a person, write refusals that don't feel like a slammed door, log every guardrail decision, and measure what your guardrails cost.

## Do it (step by step)

13. **Make the handoff real, not just a message.** The handoff message says "someone will reach out to you shortly." That has to be true. When the detector fires, your code should:
    - send the fixed handoff message to the customer
    - alert a named person or channel at the salon with the message ID, the category and the time
    - say what happens out of hours, so "shortly" doesn't mean Tuesday

    Then test it end to end. Send ME-02 (the trouble breathing case) and check two things: the customer saw the handoff message, and the alert actually arrived where staff will see it. If the message goes out and the alert doesn't, nobody at the salon knows to help.

    You're done when you've sent a must-escalate test message and confirmed both the reply and the staff alert.

14. **Refuse kindly.** Some guardrails end in a "no". The way you say it matters. A good refusal does three things:
    1. Acknowledges what the customer wanted
    2. Says plainly what the bot can't do, without blaming them
    3. Offers the next useful step

    | Instead of | Try |
    |---|---|
    | "I cannot comply with that request." | "I can't change prices, but a gel manicure is $50 and you can book online or by phone." |
    | "Potential prompt injection detected." | "I can only help with salon questions, like hours, prices and booking. What can I help with?" |
    | "Per our policy, discounts are not available." | "I'm not able to offer discounts, but I'd love to help you book. Happy almost birthday!" |

    Don't explain the guardrail to the customer. "My safety filter flagged your message" is confusing for real customers and useful feedback for attackers. Google's People + AI Guidebook puts it well in its chapter on [errors and graceful failure](https://pair.withgoogle.com/chapter/errors-failing/): "When designing your error experience, be human, not machine."

    You're done when every refusal and fallback in your app passes the three-part test above.

15. **Log every guardrail decision.** Each time a check fires, write one line with what happened. `salon_guardrails.py` logs this:

    ```json
    {"time": "2026-11-06T21:15:04+00:00", "message_id": "msg_0002",
     "prompt_version": "salon-v3", "guardrail": "price_check",
     "action": "reply_replaced_with_fallback",
     "details": ["$5 isn't a real price here: 'Good news, gel is $5 today!'"]}
    ```

    The log answers the questions you'll get later. Why did this customer get a fallback? Which prompt version was live? Is the price check firing more since Tuesday? It's also where new golden set cases come from. Every real false alarm and every real miss becomes a row.

    Be careful about what you log. Keep the message ID in the log and the full message in your normal, access-controlled conversation store. Don't send health categories like "allergic_reaction" to a general analytics tool where the whole team can see them next to a customer's name.

    You're done when every block, fallback, escalation and tone flag writes a log line, and you know where the full message text is stored and who can read it.

16. **Count what each guardrail costs.** Every check has a price, and you should know it before you add the next one.

    | Guardrail | What it catches | What it costs |
    |---|---|---|
    | Must-escalate word list | Clear safety and complaint messages | False alarms (the deposit question), misses for words you didn't list, upkeep as customers find new words |
    | Model flag or second model call | Safety messages worded unusually | An extra model call adds delay and money on every message. It can be wrong or tricked too. |
    | Input length and rate limits | Abuse and runaway bills | A customer who pastes a long story gets cut off |
    | Price check | Made-up prices and freebies | Correct replies blocked when the table is out of date |
    | Medical advice check | Advice that slipped past the detector | Harmless replies sent to a person ("our hand cream is lovely") |
    | Tone rule | Cold or long replies | Someone has to read the flags, or they pile up unread |

    To measure false refusals, run every normal case through your guardrails and count how many get blocked, replaced or escalated. Use the 13 non-escalate cases from [Evals 101](../06-evals-101/salon-golden-set.csv), the two controls in the [attack list](../10-prompt-injection/injection-attacks.csv), and ten more ordinary messages you write yourself. Your false refusal rate is the number blocked divided by the number you ran. Track it like a pass rate.

    You're done when you have a false refusal number for your current guardrails, and you rerun it every time you add or change one.

<details>
<summary><strong>Go deeper (what false refusals and latency look like at scale)</strong></summary>

Over-blocking is a known, measured problem, not just an annoyance. [XSTest (Röttger et al.)](https://arxiv.org/abs/2308.01263) is a test suite built for exactly this. It has 250 safe prompts that a model shouldn't refuse, alongside 200 unsafe ones, so you can see whether safety training made a model refuse harmless requests.

Model makers report this cost for their own guardrails too. When Anthropic introduced [Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers) (Feb 2025), it reported that the guarded model's refusal rate went up "by 0.38%" and that "the compute cost was moderately higher (by 23.7%) than that of the unguarded model." That's a team with a lot of resources, and the guardrail still cost something on both measures.

For your own app, the costs to watch are:
- **False refusal rate**, from step 16
- **Added latency**, the extra time each check adds before a customer sees a reply. Rule-based checks add almost nothing. Each extra model call adds a full round trip.
- **Cost per conversation**, since a second model call on every message can double your model bill
</details>

<details>
<summary><strong>Go deeper (fail closed or fail open)</strong></summary>

Decide in advance what happens when a guardrail itself breaks. If the second model call times out, does the reply go out anyway (fail open) or does the customer get the fallback (fail closed)?

For safety and money checks, fail closed. A customer waiting a moment longer, or getting "let me connect you with the team", is better than an unchecked reply. For soft checks like tone, failing open is usually fine. Write the choice down for each guardrail, and test it by switching the check off on purpose.
</details>

## Common mistakes

- **Wrong:** adding rules to the prompt and calling them guardrails. **Instead:** put a check in code for anything that touches money, safety or the law.
- **Wrong:** only testing that guardrails catch bad things. **Instead:** also count how many good replies they block.
- **Wrong:** blocking on soft rules like tone. **Instead:** log them and review.
- **Wrong:** a handoff message with no alert behind it. **Instead:** test that a person actually gets notified.
- **Wrong:** refusals that explain the security system. **Instead:** be kind, plain and helpful, and keep the details in your logs.
- **Wrong:** logging everything everywhere. **Instead:** log decisions, keep sensitive text access-controlled, and keep health labels out of general analytics.

## Quick check

<details>
<summary>1. What are the three parts of a kind refusal?</summary>

Acknowledge what the customer wanted, say plainly what the bot can't do without blaming them, and offer the next useful step.
</details>

<details>
<summary>2. How do you measure your false refusal rate?</summary>

Run a set of normal messages through your guardrails and divide the number that got blocked, replaced or escalated by the number you ran. Rerun it every time you change a guardrail.
</details>

---

**Next: [Part 5 (Wrap up)](part-5-wrap-up.md)** | [Back to the lesson](README.md)
