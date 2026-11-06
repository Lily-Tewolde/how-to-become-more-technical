# Polish & Co. judge rubric

This rubric grades the booking assistant's replies on the two things code can't check well. Each criterion is graded on its own, as **pass** or **fail**. There's no partial credit.

The judge never grades these, because code checks them more reliably:
- whether a must-escalate case got the handoff message (the code looks for the exact handoff text)
- whether the reply contains banned words like "cream" or "ointment"
- whether every dollar amount is a real FAQ price

See [Part 1](part-1-what-a-judge-is-for.md) for why.

---

## 1. Friendly tone

**Question:** Would a customer feel welcomed and respected reading this reply?

**Pass if all of these are true:**
- It's warm and polite. It sounds like a kind person at the front desk.
- It's plain. No jargon, no stiff phrases like "per our policy" or "as previously stated".
- It doesn't blame, scold or talk down to the customer, even when the answer is no.
- When the answer is no, it says no kindly and offers something useful, like the real price or a way to reach the salon.

**Fail if any of these are true:**
- It's curt, cold or sarcastic ("Nice try.", "It's on the website.")
- It lectures the customer or tells them what they should have done
- It's so long or so full of filler that the answer gets lost

**Length isn't a reason to pass.** A long reply isn't friendlier than a short one. The salon's rule is "warm and short, two or three sentences is usually enough".

**Examples**

| Reply | Grade | Why |
|---|---|---|
| "Yes! We're open Sundays from 11am to 5pm. See you soon!" | pass | Warm, short, answers the question |
| "It's $50 and 60 minutes. It's in the FAQ, please read it before messaging." | fail | Scolds the customer |
| "Ha, nice try. No freebies." | fail | Sarcastic, and offers nothing useful |

---

## 2. Grounded in the FAQ

**Question:** Is every fact in this reply backed by the FAQ?

**Pass if all of these are true:**
- Every price, time, duration, policy and service it mentions is in the FAQ, and matches it
- When the FAQ doesn't answer the question, it says so and offers to connect the customer with the salon
- It doesn't promise anything the FAQ doesn't offer (exceptions, discounts, "we can usually...")

**Fail if any of these are true:**
- It states a fact that isn't in the FAQ, even if it sounds likely (parking, gift cards, a service not on the list)
- It gets a FAQ fact wrong (a wrong price, wrong hours, the wrong deposit rule)
- It hints at an exception or a workaround the FAQ doesn't mention

**When in doubt, fail.** A made-up fact that sounds plausible is the most dangerous kind, because customers believe it.

**Examples**

| Reply | Grade | Why |
|---|---|---|
| "I don't have info on gift cards, sorry! I can connect you with the salon and they'll let you know." | pass | Admits the FAQ doesn't say, offers to connect |
| "There's free street parking out front, and a lot behind the building!" | fail | Parking isn't in the FAQ |
| "Yes, a $20 deposit holds any appointment over $50. A full set is $75." | fail | The full set is $70 |
