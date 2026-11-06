<sub>Lesson 13, Extra credit · optional, Advanced</sub>

# Extra credit

**In this part,** you'll see how the practices in this lesson line up with the frameworks and rules regulated teams cite. It's optional. Skip it if you're done for now.

This is a map, not legal advice. Which rules apply depends on your product, your users and where you operate. Ask your legal and compliance people which ones are yours.

<details open>
<summary><strong>Go deeper (the practices, mapped to the frameworks)</strong></summary>

| Practice in this lesson | Where it shows up |
|---|---|
| Must-pass gates, tested in both directions | NIST AI RMF "Measure" function. GMLP principle 8 (testing under realistic conditions). |
| Crisis protocol with a person in the loop | GMLP principle 7 (human-AI team performance). EU AI Act Article 14 (human oversight). |
| Hard rules for decisions with a right answer | NIST AI 600-1 risks around confabulation and human-AI configuration |
| The never list, with owners and sign-off | NIST AI RMF "Govern" function |
| Audit records for every important event | EU AI Act Article 12 (record-keeping) |
| Monitoring and thresholds after launch | GMLP principle 10 (deployed models are monitored). NIST AI RMF "Manage" function. |
| Red teaming before launch | NIST AI 600-1 suggested actions include AI red teaming |

**The frameworks, briefly:**
- **[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).** A voluntary US framework organised around four functions: Govern, Map, Measure and Manage. Widely used as a shared language for AI risk, inside and outside the US.
- **[NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)** (July 2024). Applies the RMF to generative AI. It lists twelve risks, including confabulation, data privacy, information security and human-AI configuration, with suggested actions for each.
- **[Good Machine Learning Practice for Medical Device Development](https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices/good-machine-learning-practice-medical-device-development.html)** (2021). Ten guiding principles from Health Canada, the US FDA and the UK MHRA. Short and plain enough to read in one sitting. Principles 7 and 10 are the ones this lesson leans on most.
- **[EU AI Act, Article 12, Record-keeping](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12).** For high-risk AI systems: "High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system."
- **[EU AI Act, Article 14, Human oversight](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14).** High-risk systems must be designed so people can effectively oversee them while they're in use.
- **[WHO, Ethics and governance of AI for health: guidance on large multi-modal models](https://www.who.int/publications/i/item/9789240084759)** (2024). The World Health Organization's guidance for governments, developers and health providers using generative AI in health.
</details>

<details>
<summary><strong>Go deeper (common questions from a compliance review)</strong></summary>

If you're the PM on a regulated AI product, expect questions like these. Having the artifacts from this lesson ready makes the conversation much shorter.

| Question | What you'd show |
|---|---|
| What can this AI never do? | The never list, with owners and sign-off |
| How do you know it handles emergencies? | Must-pass results, five runs each, in every supported language, plus false alarm results |
| What happens if the safety check fails? | The fail closed test, with the model check switched off |
| Who reviews what the AI does? | The sign-off table and the post-launch review schedule |
| Can you show what happened in a specific conversation? | An audit record, with the full text in the access-controlled store |
| How will you know if it gets worse? | The monitoring measures, thresholds and written responses |
| What didn't you test? | Your known gaps, each with a reason |
</details>

---

[Back to the lesson](README.md) | [Part 6 (Wrap up)](part-6-wrap-up.md)
