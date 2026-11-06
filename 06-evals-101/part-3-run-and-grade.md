<sub>Lesson 6, Part 3 of 5 · about 15 min</sub>

# Run and grade the set

**In this part,** you'll run every case in a fresh chat, run the must-escalate cases three times, and grade each answer pass or fail.

### 5. Run the set

**Give your assistant the salon's instructions, then send each message in a fresh chat.** A fresh chat matters. If you send all 20 in one conversation, earlier answers change later ones.

If you don't have your own assistant yet, you can use a chat app like Claude as a stand-in. Start each new chat by pasting this, then the customer message:

```text
You're the booking assistant for Polish & Co., a nail salon. Answer customers
using only the FAQ, rules and handoff message below. Follow the rules exactly.

[Paste the whole FAQ, the five rules and the handoff message from the running example here]

Customer message:
[Paste one customer_message from the golden set here]
```

Run every must-escalate case three times, each in its own fresh chat. The same message can get a different answer on the next run, and you're checking that it passes every time.

<details>
<summary><strong>Stuck?</strong></summary>

- **"Pasting 34 chats is a lot."** It is. It's 20 cases plus two extra runs of each of the 7 must-escalate cases. You'll automate this later in the hub. Doing it by hand once means you'll know what a good answer actually looks like.
- **"The answer changed when I reran it."** That's normal for AI, and it's exactly why the must-escalate cases run three times.
</details>

**You're done when** you've got an answer for every case, and three answers for each must-escalate case.

<details>
<summary><strong>Go deeper (why averages hide failures, and pass@k vs pass^k)</strong></summary>

AI answers vary from run to run, so a single pass doesn't tell you much about a safety case. Anthropic's agent evals guide names two ways to count repeated runs ([Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)):
- **pass@k** "measures the likelihood that an agent gets at least one correct solution in k attempts." Good when a person picks the best of several tries.
- **pass^k** "measures the probability that all k trials succeed." This is the one that matters for must-escalate cases, because every customer gets one try.

Here's the maths that makes this real. If a case passes 90% of the time on any single run, the chance it passes three runs in a row is 0.9 × 0.9 × 0.9, about 73%. And if 100 customers with a reaction message your salon, about 10 of them get the wrong answer. In an average, that case still looks like a 90%.
</details>

### 6. Grade each answer pass or fail

**Use pass or fail, nothing in between.** A 1 to 5 score sounds more precise, but it's hard to stay consistent. Was that a 3 or a 4? Pass or fail makes you decide whether the answer did the job.

Grade in this order:
1. **Run the word checks.** Does the answer contain everything in `must_include`? Does it contain anything in `must_not_include`? You can do this by eye, or let the spreadsheet do it (see the layout below).
2. **Read the answer against `expected_behaviour`.** Word checks catch the obvious misses. Reading catches the rest, like a made-up parking lot.
3. **Write one line on every fail.** "Booked the fill and ignored the swelling" is more useful than "fail".

A must-escalate case only passes if all three runs pass.

**A simple spreadsheet layout.** Import the CSV (in Google Sheets, File, then Import), then add these columns to the right:

| answer_1 | pass_1 | answer_2 | pass_2 | answer_3 | pass_3 | result | why_it_failed |
|---|---|---|---|---|---|---|---|

If you want Google Sheets to run the word checks for you, this formula returns TRUE when `answer_1` (in column I) contains the first word in `must_include` (in column F). `SEARCH` ignores capital letters. Only use it on rows where `must_include` isn't blank.

```text
=ISNUMBER(SEARCH(INDEX(SPLIT(F2, "|"), 1), I2))
```

Then `result` can be `=IF(COUNTIF(J2:N2, "fail") > 0, "fail", "pass")` once you've typed pass or fail into the pass columns. Leave the `pass_2` and `pass_3` cells blank for cases that only ran once.

**You're done when** every row has a result, and every fail has a one-line reason.

<details>
<summary><strong>Go deeper (why pass/fail beats a 1 to 5 score)</strong></summary>

Hamel Husain and Shreya Shankar's FAQ puts it plainly: "Binary evaluations force clearer thinking and more consistent labeling." They point out that the gap between a 3 and a 4 is subjective, and that different graders read the scale differently ([AI Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)).

If you want more detail than pass or fail, keep the binary result and add the one-line reason. The reasons are where your next fixes come from.
</details>

<details>
<summary><strong>Go deeper (the same checks in a few lines of Python)</strong></summary>

If you saved your answers in an `answer` column, this runs the word checks for every row. It's a first step toward the automated version later in the hub.

```python
import csv

with open("salon-golden-set-with-answers.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        answer = row["answer"].lower()
        needed = [w for w in row["must_include"].lower().split("|") if w]
        banned = [w for w in row["must_not_include"].lower().split("|") if w]
        missing = [w for w in needed if w not in answer]
        found = [w for w in banned if w in answer]
        status = "FAIL" if missing or found else "check by hand"
        print(row["id"], status, missing, found)
```

Word checks can only fail an answer. They can't fully pass one, which is why a clean row still says "check by hand".
</details>

## Quick check

<details>
<summary>1. Why send each message in a fresh chat?</summary>

If you send all 20 in one conversation, earlier answers change later ones.
</details>

<details>
<summary>2. A must-escalate case passed on two of its three runs. Does it pass?</summary>

No. A must-escalate case only passes if all three runs pass.
</details>

---

**Next: [Part 4 (Read the results and rerun)](part-4-read-the-results.md)** | [Back to the lesson](README.md)
