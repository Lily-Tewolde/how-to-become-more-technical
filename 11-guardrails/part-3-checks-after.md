<sub>Lesson 11, Part 3 of 5 · about 15 min</sub>

# Checks after the model

**In this part,** you'll check every reply before a customer sees it. Prices must match the price list, there's no medical advice, and the tone rule flags anything cold or long.

## Why check after the model

The checks before the model only see what the customer wrote. The model can still invent a price, slip in a tip about aloe, or answer like a tired receptionist. A check after the model reads the actual reply, which is the thing your customer will see.

## Do it (step by step)

9. **Check every price against the price list, sentence by sentence.** In [Prompt injection, plainly](../10-prompt-injection/part-4-rules-approvals-retests.md) you saw a simple check that every dollar amount is a real FAQ price. It had a gap. Nail art really is "from $5", so "gel is $5 today" slipped through.

   The fix is to check each amount against the service it sits next to. In [`salon_guardrails.py`](salon_guardrails.py), each service has the amounts it's allowed to show:

   ```python
   SERVICE_PRICES = {
       "gel manicure": {50},
       "gel removal": {15},
       "gel pedicure": {60},
       "nail art": {5 * n for n in range(1, 11)},  # from $5 a nail, up to 10 nails
       "deposit": {20, 50},                         # $20, for appointments over $50
       "gel": {50, 60, 15},                         # the vaguer word, checked last
       # ...and the rest of the FAQ
   }
   ```

   The check splits the reply into sentences, finds the services in each one, and fails any amount that isn't allowed for them. It also fails "free" unless it's about gel removal, the 5 day fix, or the bot saying no. Here's what it did with a few made-up replies:

   | Reply | Result |
   |---|---|
   | "A gel manicure is $50 and takes about 60 minutes." | Pass |
   | "Good news, gel is $5 today!" | **Fail.** $5 isn't a gel price. |
   | "A gel manicure is $35 for you." | **Fail.** $35 is a classic manicure. |
   | "Sure, I can book that for free!" | **Fail.** Offers something free. |
   | "Gel removal is free when you're getting a new gel set." | Pass |
   | "I can't offer a free service, but a gel mani is $50." | Pass |

   When the price check fails, the reply is replaced with a safe fallback that doesn't quote a price at all. Notice that writing this check meant making product decisions. Is "$50 for ten nails of art" a real price? The FAQ says "from $5 a nail", so I said yes, up to ten nails. Somebody has to make that call, and it's usually the PM.

   You're done when every price in the FAQ is in your table, and the six replies above get the results shown.

   <details><summary>Stuck?</summary>

   - **"A correct reply failed."** Good, you found a gap in the table, not in the bot. Add the missing amount or service name, then rerun everything.
   - **"Our prices change every month."** Then the check should read the same price list your website uses, not a copy in the code. One source of truth means the guardrail updates when the price does.
   </details>

10. **Block anything that sounds like medical advice.** The must-escalate detector should catch health messages before the model, but this is your backup in case one gets through. Check the reply for words a salon bot should never say, like "cream", "ointment", "antihistamine", "ice pack" or "is safe". If one shows up, replace the whole reply with the handoff message and alert staff.

    This check is deliberately crude. It'll occasionally flag something harmless, like "our hand cream is lovely". That's fine for a backup on a safety rule. You'd rather a person look at it.

    You're done when a reply containing "try a hydrocortisone cream" gets replaced with the handoff message.

11. **Add a soft tone rule.** Rule 5 says warm and short. Code can't tell you if something is warm, but it can spot a few things that definitely aren't:
    - More than four sentences
    - Phrases like "as I said", "calm down", "you should have" or "per our policy"
    - Words in ALL CAPS

    When this check fires, the reply still goes out, and it's logged for review. Judging warmth properly needs a person or a second model, which is what [LLM-as-judge](../08-llm-as-judge/) is for.

    You're done when "As I said, a classic pedicure is $45 and takes 50 minutes." goes out to the customer and also appears in your log as a tone flag.

12. **Ask for a strict output format.** This one's optional, and it makes every other check easier. Instead of free text, ask the model to return a small structure:

    ```json
    {
      "reply": "A gel manicure is $50 and takes about 60 minutes.",
      "needs_handoff": false,
      "services_mentioned": ["gel manicure"]
    }
    ```

    Your code checks the structure before anything else. If it's missing a field or isn't valid, the customer gets the safe fallback, and you don't retry. Retrying a broken answer in a loop is how you get slow replies and surprise bills. The `needs_handoff` field is the second escalation layer from step 7.

    You're done when a broken or missing structure leads to the fallback, not an error page.

<details>
<summary><strong>Go deeper (what this price check still misses)</strong></summary>

Be honest about gaps, in the code and in your docs.
- **No service named.** "Everything is $5 today!" names no service, so the check only asks whether $5 is any FAQ price. It is (nail art), so it passes.
- **Prices in words.** "Fifty dollars" has no `$`, so it's never checked.
- **Wrong maths.** "Two gel manicures are $90" fails, which is good, but "$100" for two would also fail even though it's right.

You can close some of these with more code. You can catch others in your golden set. The rest is what the semantic reading in [Evals 101](../06-evals-101/part-3-run-and-grade.md) and [LLM-as-judge](../08-llm-as-judge/) is for. A guardrail lowers the odds. It doesn't make the bot perfect.
</details>

<details>
<summary><strong>Go deeper (show output as plain text)</strong></summary>

One of the strongest after-the-model guardrails isn't a check at all. It's how you display the reply. If your app shows the model's output as plain text, an injected link, image or script can't run or load. That closes the data exfiltration trick from [Prompt injection, plainly](../10-prompt-injection/part-4-rules-approvals-retests.md). If you need links, only render ones that point to domains you approve.
</details>

## Quick check

<details>
<summary>1. Why check prices sentence by sentence instead of across the whole reply?</summary>

So each amount gets checked against the service it sits next to. Across the whole reply, "$5" would pass because nail art is from $5, even if the sentence says gel is $5.
</details>

<details>
<summary>2. The medical advice check flags "our hand cream is lovely". Is that a problem?</summary>

Not really. It's a backup for a safety rule, so a false alarm that sends a reply to a person is an acceptable cost. Track how often it happens (Part 4).
</details>

<details>
<summary>3. The model returns a reply with a missing field. What should happen?</summary>

The customer gets the safe fallback, and the app doesn't retry in a loop.
</details>

---

**Next: [Part 4 (Escalate, refuse kindly, log, and count the cost)](part-4-escalate-refuse-log.md)** | [Back to the lesson](README.md)
