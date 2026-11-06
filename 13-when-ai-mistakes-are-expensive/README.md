# How do you build AI for health, finance or insurance, where one mistake is too many?

You treat the dangerous cases as a separate group that has to pass every time, and you never let a good average hide a miss there. Then you build the product so the model never makes the decisions that matter on its own. Rules in code decide, a person reviews and signs off, every step is recorded, and you keep watching after launch.

![Level: Advanced](https://img.shields.io/badge/Level-Advanced-red) ![Type: Explanation and How-to](https://img.shields.io/badge/Type-Explanation%20and%20How--to-green) ![Time: 80 min](https://img.shields.io/badge/Time-80%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** In high-stakes products, a 98% average can still mean someone in danger didn't get help. So split your measures. Must-pass cases (emergencies, crises, anything that decides money or care) are hard gates checked on every run, and everything else is averaged. Build a crisis protocol that detects, stops the normal flow, hands to a person and gives the right resource. Keep hard decisions in rules, not model judgment. Write down what the AI is never allowed to do. Keep an audit trail of what was asked, what the AI said, which rule fired and who reviewed it. Get sign-off before launch, and monitor after.

> [!TIP]
> **New to this? Let me break it down.**
> At Polish & Co., most mistakes are cheap. Quote the wrong Sunday hours and someone shows up early and grabs a coffee. But the salon still has one group of messages it treats completely differently: allergic reactions, burns, infections, pregnancy questions and chargeback threats. For those, nobody improvises. There's a fixed script, a person takes over, and it has to go right every single time. Now imagine a product where most of the messages look like that group. A virtual clinic, a bank, an insurance claims line. That's what this lesson is about.

**You'll need:**
- [Evals 101](../06-evals-101/), especially the must-escalate group and pass^k
- [Guardrails](../11-guardrails/), for checks before and after the model
- [Red teaming](../12-red-teaming/), for finding what your tests missed
- No code. This lesson is about design decisions you'll make with your team.

**What you'll learn:**
- Why one miss outweighs a high average, and how to report must-pass and averaged results separately
- The four steps of a crisis protocol, and how to build them without scripting crisis counselling
- Which decisions belong to rules, which to a model and which to a person, and how to write a "never" list
- What an audit trail holds, who signs off on what, and what to monitor after launch

> [!IMPORTANT]
> This lesson teaches the design pattern for handling emergencies and crises in an AI product. It isn't clinical, legal or compliance advice. If you're building in health, finance or insurance, work with qualified experts in your field, and follow the rules where you operate. If you or someone you know is in crisis right now, call your local emergency number. In Canada and the US you can also call or text 988.

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [Why one miss outweighs a high average](part-1-one-miss.md) | Split must-pass from averaged results | 15 min |
| [ ] | [Crisis and safety protocols](part-2-crisis-protocols.md) | Design detect, stop, hand off, resource | 15 min |
| [ ] | [Hard rules, model judgment and the never list](part-3-hard-rules-never-list.md) | Decide who decides, write the never list | 15 min |
| [ ] | [Audit trails, sign-off and monitoring](part-4-audit-review-monitoring.md) | Design the record, the reviews and the alerts | 15 min |
| [ ] | [Putting it together on a telehealth intake assistant](part-5-telehealth-example.md) | Put it all together | 10 min |
| [ ] | [Wrap up](part-6-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

**Files in this lesson:**
- [`never-list-template.md`](never-list-template.md), a template for writing down what your AI is never allowed to do
- [`audit-trail-example.csv`](audit-trail-example.csv), example audit records for the salon and the made-up clinic

**Optional, Advanced:** [Extra credit](extra-credit.md), how these practices line up with NIST, health device guidance and the EU AI Act.

**[Start Part 1 →](part-1-one-miss.md)**
