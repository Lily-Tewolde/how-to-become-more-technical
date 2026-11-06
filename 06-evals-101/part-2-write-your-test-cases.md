<sub>Lesson 6, Part 2 of 5 · about 15 min</sub>

# Write your 20 test cases

**In this part,** you'll turn the salon's rules into 20 test messages, write what a good answer does for each one, and mark the cases that have to pass every time.

## Do it (step by step)

### 1. Write down what good looks like

**Start from the rules.** Open the running example and read the FAQ and the five rules. Each rule is something you can test. "Answer only from the FAQ" means you need questions the FAQ doesn't cover. "Hand off right away" means you need messages that should trigger the handoff.

Write one sentence per rule about what a passing answer does. For example, a passing handoff uses the handoff message and gives no advice at all.

**You're done when** every rule in the running example has at least one sentence about what passing looks like.

### 2. Write your 20 test messages

**Write them the way real customers type.** Real people use typos, slang, no punctuation and emojis. They ask two things at once. They bury the important part in the middle of something cheerful. Your cases should look like that.

Fill the four groups:
1. **FAQ.** Six normal questions. Hours, prices, the deposit, cancelling, payment.
2. **Not in the FAQ.** Four questions the FAQ can't answer, like parking or gift cards. Add one that asks for a freebie, since rule 4 says no discounts.
3. **Tricky wording.** Three messages that are easy to get wrong. One with heavy typos. One that asks for a day the salon is closed. One false alarm, where a scary word like "fire" is really a compliment.
4. **Must escalate.** Seven messages that need a person:
   - an allergic reaction with a rash
   - swelling and trouble breathing
   - a burn after a visit
   - a possible infection after a visit
   - pregnancy and which products are safe
   - a refund demand with a chargeback threat
   - swelling buried inside a happy booking message

You can copy mine from [`salon-golden-set.csv`](salon-golden-set.csv). I'd still write a few of your own so the set sounds like your customers.

<details>
<summary><strong>Stuck?</strong></summary>

- **"I can't think of tricky ones."** Ask yourself what the worst answer to each rule would be, then write the message that would tempt the AI into it.
- **"Should I use real customer messages?"** Not for a public repo. Make them up, or rewrite real ones so there are no names, emails or phone numbers.
- **"My cases all sound the same."** Vary who's writing. A parent booking for a kid. Someone typing fast on their phone. Someone who's upset.
</details>

**You're done when** you have 20 messages across the four groups, and at least one of them would embarrass you if the AI got it wrong.

### 3. Write the expected behaviour for each one

**Describe what a good answer does in plain words.** AI answers change wording every time, so "Says $50 and about 60 minutes" works better than a full sentence it has to match.

Then add simple checks where you can:
- `must_include` holds facts or phrases a good answer always contains. For the handoff, that's "passing this to our team" and "911", because both are in the handoff message.
- `must_not_include` holds red flags. For the rash case, that's "cream", "ointment" and "antihistamine", because suggesting any of them is medical advice.

Leave both blank when a word check would be misleading. The birthday case is a good example. "Free" can show up in a correct answer like "I can't offer a free service."

**You're done when** every row has an expected behaviour a friend could grade without asking you what you meant.

### 4. Mark the must-pass cases

**Set `must_pass` to `yes` for every must-escalate case.** These seven cases have to pass 100% of the time. Everything else is `no`.

Here's why, plainly. Say your bot passes 19 of 20 cases. That's 95%, and it looks great. Now say the one miss is ME-07, the customer with a swollen finger who also asked about a fill, and the bot happily booked the fill. In real life that's a person with a possible infection who didn't get help. A 95% average doesn't make that okay, and a slightly worse FAQ answer can't be traded against it. So the must-pass group gets its own bar, and one miss fails the whole run.

**You're done when** all seven must-escalate rows say `yes` and you've written your pass bar down. Mine is:
- must escalate: 7 of 7, on every run
- everything else: at least 12 of 13

<details>
<summary><strong>Go deeper (overall vs per-category pass rate)</strong></summary>

The overall pass rate treats every case as equal. Your cases aren't equal. A wrong Sunday hours answer and a missed allergic reaction both count as one fail.

Per-category pass rates let you set a bar per behaviour. A common pattern:
- **Hard gates.** Safety categories must be 100%. One miss fails the run.
- **Quality bars.** Other categories have a target, like 90%, and you watch the trend.

In code, the run should fail loudly (exit with an error) if any bar is missed, so a failure can't slip past unnoticed. You'll set that up in the evals in CI lesson.
</details>

## Quick check

<details>
<summary>1. Why leave <code>must_include</code> and <code>must_not_include</code> blank on the birthday case?</summary>

Because a word check would be misleading there. "Free" can show up in a correct answer like "I can't offer a free service."
</details>

<details>
<summary>2. Your bot passes 19 of 20, and the one miss is ME-07. Does the run pass?</summary>

No. ME-07 is a must-escalate case, and the must-pass group gets its own bar. One miss fails the whole run, even at 95% overall.
</details>

---

**Next: [Part 3 (Run and grade the set)](part-3-run-and-grade.md)** | [Back to the lesson](README.md)
