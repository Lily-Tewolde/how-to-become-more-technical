<sub>Lesson 6, Part 5 of 5 · about 10 min</sub>

# Wrap up

**In this part,** you'll check your work against the list, try the challenge and practise the questions you'd get in an interview.

## What I learned doing this

On a build where an AI assistant had to hand certain messages to a person, I wrote the evals before the prompt. The test harness was in place before any prompt was merged. That order is the reason I trusted the results. If I'd written the prompt first, I'd have written tests it already passed.

A few other things I'd tell myself at the start:
- **Run safety cases more than once.** A safety case that passes 4 of 5 runs isn't 100%.
- **Test both directions.** It has to catch what it must catch, and it can't panic at messages that only sound scary.
- **Check the checker.** I once had a test that couldn't fail. It passed every time because it wasn't really checking anything. Now a perfect score makes me check the grader before I celebrate.
- **Say what you didn't run.** If a case wasn't scored, I write that it wasn't scored. I don't count it as a pass.

## You're done when

- [ ] You have 20 test cases across four groups, in a CSV or a sheet
- [ ] Every case has an expected behaviour someone else could grade
- [ ] All must-escalate cases are marked `must_pass: yes`
- [ ] You've run every case, and each must-escalate case three times in fresh chats
- [ ] Every answer is graded pass or fail, with a reason on each fail
- [ ] You can say whether this version ships, using the per-group results
- [ ] You've changed one thing and rerun the whole set

## Challenge

Add five cases of your own to the golden set, then rerun all 25:
1. Someone booking for a friend who's pregnant
2. A message in another language your salon might hear
3. A false alarm with a scary word that isn't a problem
4. A customer who asks for a discount in a sneaky way
5. A must-escalate message where the important part is in the last few words

Did any of them fail? Which group did the fail land in?

## Check yourself (interview style)

<details>
<summary><strong>1. What's the difference between an eval and a vibe check?</strong></summary>

A vibe check is trying a few messages and eyeballing the answers. It changes every time and usually skips the hard cases. An eval is a fixed set of cases with written expected behaviour, run the same way every time, so you can compare versions and point to exactly what broke.
</details>

<details>
<summary><strong>2. Your eval scores 95%. Do you ship?</strong></summary>

It depends on where the 5% is. I'd look at per-category results first. If the miss is in a safety or must-escalate group, it doesn't ship, because those have a 100% bar and one miss means a real person didn't get help. If the miss is a slightly clunky FAQ answer and every hard gate passed, it can ship, and I'd log the fail as a case to fix.
</details>

<details>
<summary><strong>3. Why run the safety cases more than once?</strong></summary>

AI answers vary between runs, even with the same message. One pass only shows it can get it right. Running it several times shows whether it gets it right every time, which is what matters when each customer only gets one answer. That's pass^k, where all k runs have to pass.
</details>

<details>
<summary><strong>4. Why write the evals before the prompt?</strong></summary>

So you decide what good looks like first. If you write the prompt first, you tend to write tests it already passes. Writing evals first also gives you a way to judge every future change to the prompt, the model or the FAQ.
</details>

<details>
<summary><strong>5. What would a 20-case eval fail to catch?</strong></summary>

A lot. It won't show small improvements, like answers getting 5% better. It won't cover customers or wording you didn't think of. It goes stale when the product changes. That's why it's a gate before launch, and why you also watch real usage after launch and keep adding real failures to the set.
</details>

## Further reading

**Start here**
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/), Hamel Husain. The case for evals told through a real product story. Very readable.
- [Why AI evals are the hottest new skill for product builders](https://youtu.be/BsWxPI9UM4c), Lenny's Podcast with Hamel Husain and Shreya Shankar (video). A friendly intro aimed at product people. The written post on Lenny's site is paid. The video is free on YouTube.
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), Anthropic. Success criteria first, then example evals, then grading methods from exact match to model grading.

**Go deeper**
- [AI Evals: Everything You Need to Know (FAQ)](https://hamel.dev/blog/posts/evals-faq/), Hamel Husain and Shreya Shankar. The most complete free resource. Great for interview prep too.
- [Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents), Anthropic. Clear vocabulary for tasks, graders and repeated runs, including pass@k and pass^k.
- [Task-Specific LLM Evals that Do & Don't Work](https://eugeneyan.com/writing/evals/), Eugene Yan. Which checks actually work for which kinds of task.

**Primary sources**
- [openai/evals](https://github.com/openai/evals), OpenAI. An open-source framework for running evals, plus a registry of ready-made ones.
- [Inspect](https://inspect.aisi.org.uk/), UK AI Security Institute. An open-source framework used for model safety evals.
- [Who Validates the Validators?](https://arxiv.org/abs/2404.12272), Shankar et al. (2024). The paper behind "criteria drift": you find out what good looks like partly by grading, which is why your set keeps growing.

## Next lesson

**Next: [Lesson 7, Build a golden set](../07-golden-sets/).** You'll grow these 20 cases into a proper golden set, find who's missing, and keep it fresh as the salon changes.

After that:
- [Lesson 8, LLM-as-judge](../08-llm-as-judge/) uses a second AI to grade things word checks can't, like whether the tone is warm, and shows you how to check that grader against your own judgment.
- [Lesson 13, When AI mistakes are expensive](../13-when-ai-mistakes-are-expensive/) is the advanced version of the must-escalate idea, for products where one miss is costly.

[Back to the lesson](README.md) | ← [Lesson 5, Build something with an AI agent](../05-build-with-an-ai-agent/) | **Next: [Lesson 7, Build a golden set](../07-golden-sets/) →**

---

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
