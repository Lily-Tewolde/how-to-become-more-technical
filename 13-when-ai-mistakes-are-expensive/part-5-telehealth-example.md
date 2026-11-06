<sub>Lesson 13, Part 5 of 6 · about 10 min</sub>

# Putting it together on a telehealth intake assistant

**In this part,** you'll put the whole lesson together on one made-up product, so you can see how the pieces fit.

The product, the clinic and every detail below are made up for this lesson. It isn't based on any real company, and it isn't a design to copy for real patients without clinical, legal and privacy experts.

## The product

A made-up virtual clinic offers video visits with clinicians. Before each visit, an AI intake assistant chats with the patient. It:
- asks what's going on, in the patient's own words
- asks about current medications and allergies
- writes a short summary for the clinician to read before the visit

It doesn't diagnose, prescribe, book follow-ups or decide who can be seen. A clinician reads every summary before the visit.

## 1. Sort must-pass from averaged

| Must-pass, every case, five runs each | Averaged, with a bar |
|---|---|
| Emergency signs get the emergency tier, every time | Questions are clear (90% bar) |
| Crisis mentions get the crisis pattern from Part 2, every time | Tone is warm and plain (90% bar) |
| No diagnosis, and no comment on any dose | Summaries are under 150 words (95% bar) |
| Medication names are copied exactly as typed, with unclear ones marked | Fewer than six questions on average |
| Every summary line cites the message it came from | |
| Normal messages with alarming idioms don't escalate | |

The results table leads with the six gates. One failed run on any of them, and the version doesn't ship.

## 2. The crisis protocol

Three tiers, defined with the clinical lead:
1. **Emergency.** Signs of a medical emergency, or someone saying they or someone else is in danger.
2. **Urgent.** Worrying, needs a clinician today. For example, symptoms clearly getting worse.
3. **Normal.** The usual intake.

For emergency and crisis messages, the four steps:
1. **Detect.** A phrase list on the raw message, plus a separate model call. Either one escalates. If the model call fails, the phrase list still runs and the message goes to a person.
2. **Stop.** No more intake questions. The model doesn't write the reply.
3. **Hand off.** The on-call clinician gets an alert with the patient's own words, the tier, which layer flagged it and the time. Target pickup times are set per tier, with an out-of-hours plan.
4. **Resource.** A fixed message, written and signed off by the clinical lead, that says a clinician is being told, gives the local emergency number, and gives the crisis line for the patient's location, such as 988 in Canada and the US.

## 3. Who decides what

| Decision | Owner |
|---|---|
| Is this patient in an area the clinic serves, and old enough? | Rules in code, from extracted fields |
| Which tier is this message? | Detection layers, then a person for anything flagged |
| What's in the summary? | The model, with every line citing a message ID |
| What's wrong, and what's the treatment? | The clinician. Never the AI. |

## 4. The never list

1. Never diagnose, or say what a symptom is likely to be
2. Never suggest, change or comment on a medication or dose
3. Never tell a patient they're eligible, or that they'll be seen
4. Never correct a medication name to the closest match
5. Never add anything to the summary the patient didn't say

Each line points to must-pass test cases, and each is enforced somewhere other than the prompt.

## 5. The audit record

For a crisis escalation, the record shows:
- the event and message IDs, and the time
- that the phrase list and the model check both flagged it, or which one did
- that the model was skipped and the fixed resource message (version 3) was shown
- that the on-call clinician picked it up, when, and what they did
- the model and prompt versions live at the time

Full message text sits in the access-controlled patient record, not in the audit log or any analytics tool. There's a row like this in [`audit-trail-example.csv`](audit-trail-example.csv).

## 6. Sign-off and monitoring

Before launch:
- The clinical lead signs off the tiers, the resource message and the never list
- Privacy signs off the audit record and retention
- Product and engineering sign off the must-pass results, with all five runs shown

After launch:
- Every escalation is reviewed within a set time
- A weekly random sample of non-escalated conversations is read by a clinician, looking for misses
- Any confirmed missed emergency pauses the AI intake, and everyone goes to a human-led intake until it's fixed and retested
- Every miss and false alarm becomes a new must-pass case
- The whole set reruns on every prompt, model or flow change

## Quick check

<details>
<summary>1. A patient writes "is this a migraine or something worse?". What does the assistant do?</summary>

It doesn't answer the question, because diagnosis is on the never list. It records the patient's words in the summary for the clinician, and if the message also shows emergency signs, the crisis protocol takes over.
</details>

<details>
<summary>2. A clinician-led weekly review finds one emergency the detector missed. What happens?</summary>

It's an incident. The AI intake pauses and patients go to a human-led intake. The team investigates, adds the message (and variations) to the must-pass set, fixes the detector, reruns everything, and only resumes when every gate passes.
</details>

---

**Next: [Part 6 (Wrap up)](part-6-wrap-up.md)** | [Back to the lesson](README.md)
