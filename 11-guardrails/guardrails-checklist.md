# Guardrails checklist

A one-page checklist for any AI feature. Copy it into your own repo and tick it off. It goes with [Lesson 11, Guardrails](README.md).

## 1. Sort your rules

- [ ] Every rule the AI follows is written down in one place
- [ ] Each rule is marked: prompt only, check before the model, check after the model, or more than one
- [ ] Every rule that touches money, safety, privacy or the law has at least one check in code
- [ ] Each check has one action: block and replace, escalate, or log only

## 2. Before the model

- [ ] Must-escalate messages are caught by code, and the model is skipped
- [ ] The handoff message is fixed text, written and approved by a person
- [ ] A second layer (a model flag or a separate classifier) can also escalate
- [ ] Either layer can escalate, and neither can cancel the other
- [ ] Messages have a length limit
- [ ] Each user has a rate limit
- [ ] No input filter blocks normal phrases like "ignore my last message"

## 3. After the model

- [ ] Prices, amounts and anything else with one right answer are checked against the source of truth, not a copy
- [ ] Replies are checked for advice the product must never give (medical, legal, financial)
- [ ] Soft rules like tone are logged for review, not blocked
- [ ] The output has a strict format, and anything outside it gets the safe fallback with no retry loop
- [ ] Output is shown as plain text, or only links to approved domains are rendered

## 4. When a check fires

- [ ] Every handoff alerts a real person, and that alert has been tested end to end
- [ ] Out-of-hours handoffs say honestly when someone will reply
- [ ] Every refusal acknowledges the request, says plainly what the AI can't do, and offers a next step
- [ ] No refusal explains the guardrail to the user
- [ ] Any action that costs money or can't be undone needs a person to approve it

## 5. Logging

- [ ] Every block, fallback, escalation and flag writes a log line
- [ ] Each line has the time, a message ID, the prompt or model version, the guardrail and the action
- [ ] Full message text is stored separately with access controls
- [ ] Sensitive labels (health, money trouble) don't go into general analytics tools

## 6. Costs and testing

- [ ] Each guardrail is tested in both directions: it catches what it should, and it doesn't block normal messages
- [ ] You have a false refusal rate, measured on normal messages
- [ ] You know roughly how much delay and cost each guardrail adds
- [ ] Each guardrail has a written choice for when it breaks: fail closed (safety, money) or fail open (style)
- [ ] You've switched each guardrail off once and watched its tests go red
- [ ] Guardrail tests run on every pull request
- [ ] Real misses and false alarms from the logs become new golden set cases
