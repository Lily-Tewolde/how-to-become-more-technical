# Never list template

What our AI is never allowed to do, whatever a user says and whatever the prompt says. It goes with [Lesson 13, When AI mistakes are expensive](README.md).

Copy this file into your project and fill it in. Keep it short. Style preferences belong in the prompt and your averaged evals. This list is for things that could hurt someone, cost someone money they're owed, treat someone unfairly or break a law.

**Product:** _name_
**Version:** _1_
**Last reviewed:** _YYYY-MM-DD_
**Signed off by:** _name and role, for each kind of risk (for example clinical lead, compliance, product)_

## The list

| # | Never | Why | Enforced in (not just the prompt) | Must-pass test cases | Owner |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## Worked examples

These come from the lesson's two made-up products. Delete them once you've written your own.

| # | Never | Why | Enforced in | Must-pass test cases | Owner |
|---|---|---|---|---|---|
| S1 | Give medical advice (salon) | A customer could be hurt, and the salon isn't qualified | Must-escalate detector before the model. Medical advice check after it. | ME-01 to ME-05, RTC-05 | Salon owner |
| S2 | Quote a price that isn't in the price list (salon) | Customers are misled and the salon loses money | Price check in code, reading the live price list | Price check cases, INJ-02, INJ-09 | Salon owner |
| S3 | Act on another customer's booking (salon) | Privacy, and real harm to the other customer | Server-side ownership check on every booking tool | RTC-02, RTC-02b, RTC-03 | Engineering lead |
| H1 | Diagnose, or say what a symptom is likely to be (health) | Only a clinician can, and a wrong guess can delay care | Output check for diagnostic phrases. Clinician reads every summary. | Diagnosis bait cases | Clinical lead |
| H2 | Suggest, change or comment on a dose (health) | Direct risk of harm | Output check. Medication fields copied exactly as typed. | Dose cases, look-alike medication name cases | Clinical lead |
| H3 | Tell someone they're eligible or covered (health, insurance) | Eligibility is a policy decision, and a wrong yes is a broken promise | Rules in code decide from structured fields. The model can't produce that wording. | Eligibility cases | Product, compliance |
| H4 | Write the reply to a crisis message (health) | Crisis wording must be expert-approved and consistent | Detection layers skip the model and show the fixed resource message | Crisis cases, five runs each | Clinical lead |

## Checks before you sign this off

- [ ] Every line is one plain sentence a new team member would understand
- [ ] Every line has a "why"
- [ ] Every line is enforced somewhere other than the prompt
- [ ] Every line points to at least one must-pass test case, and those cases are in the golden set
- [ ] Every line has an owner
- [ ] The people who answer for each kind of risk have signed off
- [ ] The list is reviewed again whenever the product, the model or the rules change
