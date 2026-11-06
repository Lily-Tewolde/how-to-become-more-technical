<sub>Lesson 13, Part 4 of 6 · about 15 min</sub>

# Audit trails, sign-off and monitoring

**In this part,** you'll design the record you keep for every important moment, decide who reviews and signs off on what, and plan what you'll watch after launch.

## Why this matters

When something goes wrong in a high-stakes product, someone will ask what happened. A customer, a regulator, a lawyer or your own team. "The model said it" isn't an answer. You need to be able to show what was asked, what the AI said, which rule fired, what happened next, and who looked at it.

This isn't only about blame. The same record is how you find problems early, how you prove a fix worked, and where your next golden set cases come from.

## Do it (step by step)

15. **Design the audit record.** For every moment that matters (an escalation, a blocked reply, a rule decision, a human review), write one record. Look at [`audit-trail-example.csv`](audit-trail-example.csv) for examples from the salon and the made-up clinic. Each record holds:

    | Field | Answers the question |
    |---|---|
    | `event_id`, `time` | Which event, and when? |
    | `conversation_id`, `message_id` | Which conversation and message? (The full text lives in a separate, access-controlled store.) |
    | `asked` | What was asked, as a short reference or a safe excerpt |
    | `ai_output` | What the AI said or proposed |
    | `shown_to_user` | What the person actually saw, which may differ if a guardrail replaced it |
    | `rule_fired` | Which rule, guardrail or detector layer fired |
    | `action` | What the system did: handed off, blocked, approved, sent |
    | `model_version`, `prompt_version` | What was live at the time |
    | `reviewed_by`, `review_time`, `review_decision` | Who looked at it, when, and what they decided |

    Keep `ai_output` and `shown_to_user` as separate fields. If a guardrail replaced a reply, you want to see both what the model tried to say and what the person actually got.

    You're done when every escalation, block and rule decision in your flow writes a record with all of these fields.

16. **Decide what not to put in the record.** An audit trail full of sensitive details is its own risk. A few rules:
    - Store the full conversation once, with access controls and a retention period, and point to it by ID
    - Only the people who need it can read it, and reads are logged too
    - Keep sensitive labels like "crisis" or "hardship" out of general analytics and product dashboards
    - Write down how long records are kept, and why

    This one is easy to miss, because analytics events get added quickly and by lots of people. An event called `crisis_flag_shown` with a user ID attached is health data sitting in a tool the whole company can open. Check every event name and property in your analytics setup, not just the database.

    You're done when you know where every sensitive field is stored, who can read it, and how long it's kept.

17. **Agree who signs off on what, before launch.** Sign-off means a named person has read the thing and agreed it's ready. Write the list down:

    | What | Who signs off |
    |---|---|
    | The crisis tiers and resource message | Clinical or crisis lead |
    | The never list | Product, plus whoever owns the risk (clinical, legal or compliance) |
    | The must-pass eval results | Product and engineering, together |
    | The audit record design and retention | Privacy or compliance |
    | Go or no-go for launch | Product, with all of the above |

    The PM usually drafts most of these. The point of sign-off is that the people who answer for each kind of mistake have actually looked.

    You're done when every item has a named person, and you know what they need to see before they'll say yes.

18. **Plan human review after launch.** Automated checks catch structure. People catch behaviour. On a health-related build, I did three kinds of review on the same product: automated tests, a code review and a hand pass where I used it like a real person would. Each found different things. The automated tests caught structure, the code review caught logic and safety, and the hand pass caught behaviour. The worst finding came from the hand pass. A button rendered perfectly and worked before a required safety checkbox was ticked.

    After launch, plan regular review:
    - **Every escalation**, to check it was right and handled in time
    - **A random sample of conversations that didn't escalate**, to find misses
    - **Every time a person overrode the AI**, to learn why
    - **A regular hand pass** of the full flow, especially after changes

    You're done when each kind of review has an owner and a schedule.

19. **Decide what you'll monitor, and the numbers that trigger action.** Pick a few measures and set the thresholds before launch, so nobody has to decide under pressure:
    - **Escalation rate.** A sudden drop can mean the detector broke. A sudden rise can mean false alarms.
    - **Misses found in review.** Any confirmed must-pass miss is an incident.
    - **Time to human pickup**, for each tier
    - **Override rate**, how often reviewers disagree with the AI
    - **Refusal and fallback rate**, so you notice when the product starts failing ordinary users
    - **Version changes**, including model updates you didn't choose

    For each one, write the number that triggers a response, and what the response is. For example: "Any confirmed missed emergency: pause the AI flow, route everyone to people, investigate." It's much easier to act on a number everyone agreed before launch than to argue about one after.

    Every confirmed miss and false alarm becomes a new case in your must-pass set, and you rerun everything.

    You're done when every measure has an owner, a threshold and a written response.

<details>
<summary><strong>Go deeper (what the standards say about monitoring)</strong></summary>

Health device regulators have said this plainly. The [Good Machine Learning Practice guiding principles](https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices/good-machine-learning-practice-medical-device-development.html), published by Health Canada with the US FDA and the UK MHRA, list ten principles. Two map straight onto this part:
- Principle 7: focus on how the human and the AI perform together, not just the model alone
- Principle 10: deployed models are monitored, and risks from retraining are managed

Anthropic's guide to [mitigating jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) also has a section on continuous monitoring: regularly analyse outputs for signs that an attack got through, and refine your defences. The [Extra credit](extra-credit.md) page covers what the EU AI Act says about logs and human oversight.
</details>

## Quick check

<details>
<summary>1. Why keep <code>ai_output</code> and <code>shown_to_user</code> as separate fields?</summary>

Because a guardrail may have replaced the reply. You need to see both what the model tried to say and what the person actually got.
</details>

<details>
<summary>2. Name three kinds of human review to plan after launch.</summary>

Any three of: every escalation, a random sample of conversations that didn't escalate, every override, and a regular hand pass of the full flow.
</details>

<details>
<summary>3. Why set monitoring thresholds before launch?</summary>

So the decision is already made when something goes wrong. Nobody has to debate under pressure whether a number is bad enough to act on.
</details>

---

**Next: [Part 5 (Putting it together on a telehealth intake assistant)](part-5-telehealth-example.md)** | [Back to the lesson](README.md)
