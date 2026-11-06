# Resources

Every outside link the lessons use, in one place. They're grouped by topic, and each topic is split into three tiers:

| Tier | What's in it |
|---|---|
| **Start here** | Friendly blogs, videos and free courses. Good first reads. |
| **Go deeper** | Practitioner guides from people who build this every day. |
| **Primary** | Official docs, papers and standards. The source when you need to be exact. |

Each link also has a level, the same way the lessons do. *Beginner* needs no setup or code. *Intermediate* means some setup or reading code. *Advanced* means papers, specs or real tradeoffs.

Every link here is one I used in a lesson, and each one appears once. If a resource helps with more than one topic, it sits under the one it helps most.

## Jump to a topic

- [How software and the web work](#how-software-and-the-web-work)
- [Git, GitHub and pull requests](#git-github-and-pull-requests)
- [How LLMs and agents work](#how-llms-and-agents-work)
- [Building with a coding agent](#building-with-a-coding-agent)
- [Evals and golden sets](#evals-and-golden-sets)
- [LLM-as-judge](#llm-as-judge)
- [Evals in CI](#evals-in-ci)
- [Prompt injection](#prompt-injection)
- [Guardrails](#guardrails)
- [Red teaming](#red-teaming)
- [High-stakes AI and governance](#high-stakes-ai-and-governance)

## How software and the web work

From [Lesson 1, How software works](../01-how-software-works/).

**Start here**
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works), MDN. *Beginner.* Clients, servers and HTTP in one short page.
- [Working with JSON](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON), MDN. *Beginner.* A friendly intro to the format most requests and responses use.
- [Inspect network activity](https://developer.chrome.com/docs/devtools/network), Chrome DevTools. *Beginner.* A full tour of the Network panel, so you can watch real requests yourself.
- [SQLBolt](https://sqlbolt.com/). *Beginner.* Short, interactive SQL lessons in your browser.
- [Mess With DNS](https://messwithdns.net/), Julia Evans. *Beginner.* Play with real DNS records and see what happens.
- [CS50x](https://cs50.harvard.edu/x/), Harvard. *Beginner.* The free intro to computer science. Its later weeks cover SQL and building a web app.

**Go deeper**
- [What happens when...](https://github.com/alex/what-happens-when), a community GitHub repo. *Intermediate.* Everything that happens after you type a URL and press Enter. A classic interview question, answered in depth.
- [Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview), MDN. *Intermediate.* The request and response model in more detail.
- [Client-server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview), MDN. *Intermediate.* What the back end does with a request.
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/), MIT. *Intermediate.* The tools nobody teaches, like the terminal and git.
- [Environments](https://vercel.com/docs/deployments/environments), Vercel. *Intermediate.* How local, preview and production work on a real hosting platform.
- [The Twelve-Factor App, Dev/prod parity](https://12factor.net/dev-prod-parity). *Intermediate.* Why environments should stay alike, and the gaps that cause bugs.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), Stripe. *Advanced.* How a payments API stops a double tap from charging twice.

**Primary**
- [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) and [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status), MDN. *Intermediate.* The references behind the method and status code tables.
- [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories), GitHub Docs. *Beginner.* What a repo holds, from the people who host most of them.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) and [PostgreSQL concepts](https://www.postgresql.org/docs/current/tutorial-concepts.html), PostgreSQL docs. *Intermediate.* Tables, rows and SQL from the people who make the database.
- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), IETF (2022). *Advanced.* The actual HTTP standard.
- [RFC 8259, The JSON Data Interchange Format](https://www.rfc-editor.org/info/rfc8259/), IETF (2017). *Advanced.* The JSON standard.

## Git, GitHub and pull requests

From [Lesson 3, Your first pull request](../03-your-first-pull-request/) and [Lesson 4, Why PRs matter for a PM](../04-why-prs-matter-for-pms/).

**Start here**
- [Introduction to GitHub](https://github.com/skills/introduction-to-github), GitHub Skills. *Beginner.* A guided browser exercise where you branch, commit, open and merge a PR in under an hour.
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), GitHub Docs. *Beginner.* The official explainer for the tabs on a PR, drafts and checks.
- [first-contributions](https://github.com/firstcontributions/first-contributions), firstcontributions. *Beginner.* The classic first-PR tutorial, with links to versions that don't need the terminal.
- [How to write the perfect pull request](https://github.blog/developer-skills/github/how-to-write-the-perfect-pull-request/), Keavy McMinn, GitHub Blog. *Beginner.* The PR description as communication, which is the part PMs are already good at.
- [Conventional Comments](https://conventionalcomments.org/). *Beginner.* The label format I use for review comments, with examples of each label.

**Go deeper**
- [Code review developer guide](https://google.github.io/eng-practices/review/), Google Engineering Practices. *Intermediate.* How reviewers and authors work together at Google.
- [What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html), Google Engineering Practices. *Intermediate.* The full list a reviewer runs, from design to tests.
- [How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html), Google Engineering Practices. *Intermediate.* Courtesy, explaining why, and labelling severity.
- [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html) and [Writing good CL descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html), Google Engineering Practices. *Intermediate.* Why small changes ship faster, and how to write a description that still makes sense a year later.
- [Oh Shit, Git!?!](https://ohshitgit.com/), Katie Sylor-Miller. *Intermediate.* Plain-English fixes for when something goes wrong in the terminal.
- [GitHub Desktop docs](https://docs.github.com/en/desktop), GitHub Docs. *Beginner.* The app route, if you'd rather click than type commands.
- [GitHub CLI](https://cli.github.com/), GitHub. *Intermediate.* GitHub from the terminal, including an easy way to sign in.

**Primary**
- [Pro Git, 2nd edition](https://git-scm.com/book/en/v2), Scott Chacon and Ben Straub. *Intermediate.* The official free git book. Start with [Contributing to a Project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project) for forks and PRs.
- GitHub Docs on [creating an account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github), [editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files), [creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) and [merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request). *Beginner.* The exact buttons, in case GitHub moves them.
- [Pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) and [Reviewing proposed changes in a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request), GitHub Docs. *Beginner.* Comment, Approve and Request changes.
- [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue), GitHub Docs. *Beginner.* The closing keywords and when they work.
- [Creating a pull request template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository), GitHub Docs. *Beginner.* Where the template file can live.
- [Status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks), GitHub Docs. *Intermediate.* What checks are and what each state means.

## How LLMs and agents work

From [Lesson 2, How LLMs and agents work](../02-how-llms-and-agents-work/).

**Start here**
- [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs), 3Blue1Brown (video). *Beginner.* A short, visual intro to next-token prediction.
- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), Andrej Karpathy (video). *Beginner.* The classic one-hour explainer for general audiences.
- [Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial), Anthropic. *Beginner.* Hands-on chapters on roles, separating data from instructions, and avoiding hallucinations.
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners), Microsoft. *Beginner.* A free course of 21 lessons, each with a video.
- [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/), Simon Willison. *Beginner.* The agent loop explained plainly, including why the conversation is resent every time.

**Go deeper**
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents), Anthropic. *Intermediate.* Workflows vs agents, the common patterns, and when not to build an agent.
- [I think "agent" may finally have a widely enough agreed upon definition to be useful jargon now](https://simonwillison.net/2025/Sep/18/agents/), Simon Willison (2025). *Beginner.* A short, usable definition of an agent.
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Anthropic. *Intermediate.* Being clear and direct, giving examples, and using tags to separate parts of a prompt.
- [Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval), Anthropic. *Advanced.* How a short note on each chunk helps RAG find the right part.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), Andrej Karpathy (video). *Intermediate.* Over three hours on how models are trained, from raw text to an assistant.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), Jay Alammar. *Advanced.* The best-known visual walkthrough of what's inside a model.
- [LLM Course](https://huggingface.co/learn/llm-course), Hugging Face. *Intermediate.* Free and hands-on, for when you want to touch real models.

**Primary**
- [Glossary](https://platform.claude.com/docs/en/about-claude/glossary), [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages), [Create a Message](https://platform.claude.com/docs/en/api/messages/create), [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) and [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), Anthropic docs. *Intermediate.* The definitions and API behaviour the lesson is built on.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml), Google. *Intermediate.* Practical rules on offline tests, launches and the gap between them.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762), Vaswani et al. (2017). *Advanced.* The paper that introduced the transformer.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), Lewis et al. (2020). *Advanced.* The paper that named RAG.
- [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664), Kalai et al. (2025). *Advanced.* Why training and scoring reward a confident guess.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599), Guo et al. (2017), and [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221), Kadavath et al. (2022). *Advanced.* Why a model's confidence isn't the same as being right.

## Building with a coding agent

From [Lesson 5, Build something with an AI agent](../05-build-with-an-ai-agent/).

**Start here**
- [Claude Code 101](https://academy.claude.com/courses/claude-code-101), Claude Academy. *Beginner.* Anthropic's free self-paced intro course.
- [Terminal guide for new users](https://code.claude.com/docs/en/terminal-guide), Claude Code docs. *Beginner.* How to open a terminal and paste a command, if you've never done it.
- [Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/), MIT Missing Semester (2026). *Intermediate.* A free lecture on how coding agents work, with notes and exercises.

**Go deeper**
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices), Anthropic. *Intermediate.* Tell it what it can't see, give it a check to run, and enforce the rules that can't have exceptions.
- [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/), Simon Willison. *Intermediate.* Practical patterns from someone who builds with agents every day.
- [Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/), Simon Willison. *Intermediate.* How to keep an agent's work small and reviewable.

**Primary**
- [Claude Code overview](https://code.claude.com/docs/en/overview), [quickstart](https://code.claude.com/docs/en/quickstart), [How Claude remembers your project](https://code.claude.com/docs/en/memory) and [install troubleshooting](https://code.claude.com/docs/en/troubleshoot-install), Claude Code docs. *Beginner.* Where it runs, your first session, how `CLAUDE.md` loads, and what to do when `claude` isn't found.
- [Get started with Claude](https://platform.claude.com/docs/en/get-started) and the [Claude Console API keys page](https://platform.claude.com/settings/keys), Claude Platform. *Beginner.* Your first API call, and where you make a key.
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) and [Pricing](https://platform.claude.com/docs/en/about-claude/pricing), Claude Platform docs. *Intermediate.* Current model names and what each one costs per token.
- [AGENTS.md](https://agents.md/). *Intermediate.* The open instructions format many coding agents share.
- [Ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files) and [About secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning), GitHub Docs. *Intermediate.* How `.gitignore` works, and the safety net that can catch some leaked keys after the fact.
- [Python downloads](https://www.python.org/downloads/), python.org. *Beginner.* Where to get Python if your computer doesn't have it.

## Evals and golden sets

From [Lesson 6, Evals 101](../06-evals-101/) and [Lesson 7, Golden sets](../07-golden-sets/).

**Start here**
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/), Hamel Husain. *Beginner.* The case for evals told through a real product story.
- [Why AI evals are the hottest new skill for product builders](https://youtu.be/BsWxPI9UM4c), Lenny's Podcast with Hamel Husain and Shreya Shankar (video). *Beginner.* A friendly intro aimed at product people.
- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), Anthropic. *Beginner.* Success criteria first, then example evals, then grading by code, people or a model.

**Go deeper**
- [AI Evals: Everything You Need to Know (FAQ)](https://hamel.dev/blog/posts/evals-faq/), Hamel Husain and Shreya Shankar. *Intermediate.* The most complete free resource, and great interview prep. Used in Lessons 6, 7 and 8.
- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), Anthropic. *Intermediate.* Clear vocabulary for tasks, graders and repeated runs, including pass@k and pass^k. Used in Lessons 6, 7, 9 and 13.
- [Task-Specific LLM Evals that Do & Don't Work](https://eugeneyan.com/writing/evals/), Eugene Yan. *Intermediate.* Which checks actually work for which kinds of task.
- [Golden dataset evaluation: build and maintain LLM test sets](https://langfuse.com/resources/engineering/golden-dataset-evaluation), Langfuse. *Intermediate.* Versioning, adding production failures and comparing prompt versions. Written by a tool vendor, but the advice works with any tool.
- [A statistical approach to model evaluations](https://anthropic.com/research/statistical-approach-to-model-evals), Anthropic. *Intermediate.* A plain-language case for reading every eval score as a range.

**Primary**
- [openai/evals](https://github.com/openai/evals), OpenAI. *Advanced.* An open-source framework for running evals, plus a registry of ready-made ones.
- [Inspect](https://inspect.aisi.org.uk/), UK AI Security Institute. *Advanced.* An open-source framework used for model safety evals.
- [Who Validates the Validators?](https://arxiv.org/abs/2404.12272), Shankar et al. (2024). *Advanced.* The paper behind criteria drift, and why you can't fully define good before you grade real outputs.
- [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640), Evan Miller (2024). *Advanced.* The statistics behind reading a score as a range.

## LLM-as-judge

From [Lesson 8, LLM-as-judge](../08-llm-as-judge/).

**Start here**
- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/), Hamel Husain. *Intermediate.* The step-by-step method: an expert grades pass or fail with critiques, and the judge is built and checked against them.

**Go deeper**
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/), Eugene Yan. *Intermediate.* A practitioner's review of the research.
- [An LLM-as-Judge Won't Save The Product, Fixing Your Process Will](https://eugeneyan.com/writing/eval-process/), Eugene Yan. *Intermediate.* Why the habit of looking at data matters more than the tool.

**Primary**
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685), Zheng et al. (2023). *Advanced.* Names position, verbosity and self-enhancement bias, and measures how often strong judges agree with people.
- [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076), Panickssery, Bowman and Feng (2024). *Advanced.* The self-preference study.

## Evals in CI

From [Lesson 9, Evals in CI](../09-evals-in-ci/).

**Start here**
- [Quickstart for GitHub Actions](https://docs.github.com/en/actions/get-started/quickstart), GitHub Docs. *Beginner.* Add a workflow and watch it run in a few minutes.
- [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions), GitHub Docs. *Beginner.* Workflows, events, jobs, steps and runners in one page.
- [Hello GitHub Actions](https://github.com/skills/hello-github-actions), GitHub Skills. *Beginner.* A free, hands-on exercise that walks you through your first workflow.

**Go deeper**
- [CI/CD Integration for LLM Evaluation and Security](https://www.promptfoo.dev/docs/integrations/ci-cd/), Promptfoo. *Intermediate.* Quality gates on pass rate and posting eval results on pull requests.
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets), GitHub Docs. *Intermediate.* Creating, using and limiting secrets.
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions), GitHub Docs. *Intermediate.* What runners cost, and what's free in public repos.
- [Migration guide for Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide), Anthropic. *Intermediate.* Why "set temperature to 0" advice doesn't apply to every model.

**Primary**
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), GitHub Docs. *Intermediate.* Every key used in `evals.yml`.
- [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use), GitHub Docs. *Advanced.* Script injection, secrets in logs and risky triggers.
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [Troubleshooting required status checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks), GitHub Docs. *Intermediate.* How to make a check required, and why a skipped one can block a merge.
- [Anthropic Python SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python), Anthropic. *Intermediate.* Installing, sending messages, retries and timeouts.

## Prompt injection

From [Lesson 10, Prompt injection, plainly](../10-prompt-injection/).

**Start here**
- [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/), Simon Willison (2022). *Beginner.* The short post that named the attack.
- [Prompt injection: What's the worst that can happen?](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/), Simon Willison (2023). *Beginner.* Real examples with email assistants, search and data leaking through images.
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), Simon Willison (2025). *Beginner.* The best single mental model for anyone building agents.
- [Understanding prompt injections: a frontier security challenge](https://openai.com/index/prompt-injections/), OpenAI (2025). *Beginner.* A plain overview of how hidden instructions in web content affect agents.

**Go deeper**
- [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), Anthropic. *Intermediate.* Concrete techniques, from isolating untrusted content to layered defences. Used in Lessons 10, 11 and 13.
- [Mitigating prompt injections in browser use](https://www.anthropic.com/research/prompt-injection-defenses), Anthropic (2025). *Intermediate.* How a model maker measures and defends against injection in a browsing agent.
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/), Simon Willison (2025). *Intermediate.* The six structural patterns, explained plainly.
- [Web LLM attacks](https://portswigger.net/web-security/llm-attacks), PortSwigger Web Security Academy. *Intermediate.* A security practitioner's view, with linked labs.
- [Simon Willison's prompt injection tag](https://simonwillison.net/tags/prompt-injection/). *Intermediate.* A running record of real incidents.

**Primary**
- [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), OWASP. *Intermediate.* Definitions, attack scenarios and seven mitigations.
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/). *Intermediate.* The standard risk checklist. Prompt injection is number one.
- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173), Greshake et al. (2023). *Advanced.* The indirect prompt injection paper.
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837), Beurer-Kellner et al. (2025). *Advanced.* The paper behind the six patterns.

## Guardrails

From [Lesson 11, Guardrails](../11-guardrails/).

**Start here**
- [Safe and reliable AI via guardrails](https://www.deeplearning.ai/courses/safe-and-reliable-ai-via-guardrails), DeepLearning.AI with Shreya Rajpal. *Beginner.* A short video course with code.
- [Errors + Graceful Failure](https://pair.withgoogle.com/chapter/errors-failing/), Google People + AI Guidebook. *Beginner.* How to design what users see when the AI gets it wrong.

**Go deeper**
- [Guardrails](https://openai.github.io/openai-agents-python/guardrails/), OpenAI Agents SDK docs. *Intermediate.* Input and output guardrails, tripwires, and the parallel vs blocking tradeoff.
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), Anthropic. *Intermediate.* Letting the model say "I don't know", grounding in quotes, and citing sources.
- [NeMo Guardrails documentation](https://docs.nvidia.com/nemo-guardrails/), NVIDIA. *Advanced.* An open-source toolkit for adding programmable guardrails to an app.

**Primary**
- [LLM05:2025 Improper Output Handling](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/), OWASP. *Intermediate.* Why model output needs checking before it reaches people or other systems.
- [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), OWASP. *Intermediate.* Giving a model more tools and permissions than the job needs.
- [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674), Inan et al. (Meta, 2023). *Advanced.* A model trained to classify inputs and outputs against safety categories.
- [XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models](https://arxiv.org/abs/2308.01263), Röttger et al. *Advanced.* How to measure over-refusal.
- [Constitutional Classifiers: Defending against universal jailbreaks](https://www.anthropic.com/research/constitutional-classifiers), Anthropic (2025). *Advanced.* A large guardrail system, with its refusal and compute costs reported.

## Red teaming

From [Lesson 12, Red teaming](../12-red-teaming/).

**Start here**
- [Challenges in red teaming AI systems](https://www.anthropic.com/news/challenges-in-red-teaming-ai-systems), Anthropic (2024). *Beginner.* The kinds of red teaming a model maker does, and why there's no standard yet.
- [AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs), Microsoft. *Intermediate.* Hands-on challenges for direct and indirect injection, prompt extraction and multi-turn attacks. You run them yourself.

**Go deeper**
- [GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/), OWASP (2025). *Intermediate.* A full practitioner guide across model, implementation, infrastructure and runtime testing.
- [Lessons From Red Teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238), Bullwinkel et al., Microsoft (2025). *Intermediate.* Eight lessons from real product red teams. Used in Lessons 12 and 13.
- [OWASP Risk Rating Methodology](https://community.owasp.org/OWASP_Risk_Rating_Methodology), OWASP. *Intermediate.* The classic way to rate likelihood and impact separately, then combine them.
- [Red team quickstart](https://www.promptfoo.dev/docs/red-team/quickstart/), Promptfoo. *Advanced.* Automated red teaming you can run against your own app.
- [garak](https://github.com/NVIDIA/garak), NVIDIA. *Advanced.* An open-source scanner with a large library of attack probes.
- [PyRIT](https://microsoft.github.io/PyRIT), Microsoft. *Advanced.* An open-source framework for building your own automated red teaming, including multi-turn attacks.

**Primary**
- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). *Intermediate.* The risk list for agents that plan and use tools.
- [MITRE ATLAS](https://atlas.mitre.org/). *Advanced.* A knowledge base of attacker tactics and techniques against AI systems.
- [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST (2024). *Advanced.* Twelve generative AI risks with suggested actions, including red teaming. Used in Lessons 12 and 13.
- [AgentDojo](https://arxiv.org/abs/2406.13352), Debenedetti et al. (2024). *Advanced.* A benchmark of agent tasks with injected tool results.

## High-stakes AI and governance

From [Lesson 13, When AI mistakes are expensive](../13-when-ai-mistakes-are-expensive/).

**Start here**
- [People + AI Guidebook](https://pair.withgoogle.com/guidebook), Google PAIR. *Beginner.* Plain guidance on designing AI products people can trust, including when the AI gets it wrong.
- [WHO releases AI ethics and governance guidance for large multi-modal models](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models), World Health Organization (2024). *Beginner.* A short summary of the WHO's guidance on generative AI in health.

**Go deeper**
- [Good Machine Learning Practice for Medical Device Development: Guiding Principles](https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices/good-machine-learning-practice-medical-device-development.html), Health Canada, US FDA and UK MHRA. *Intermediate.* Ten short principles, including human and AI teams and monitoring after launch.

**Primary**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), NIST. *Intermediate.* The shared language for AI risk: Govern, Map, Measure, Manage.
- [Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models](https://www.who.int/publications/i/item/9789240084759), WHO (2024). *Advanced.* The full guidance.
- [EU AI Act, Article 12, Record-keeping](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12) and [Article 14, Human oversight](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14), European Commission AI Act Service Desk. *Advanced.* The legal text on logs and human oversight for high-risk systems.
- [Newman (1995)](https://jamanetwork.com/journals/jama/article-abstract/389714), JAMA. *Advanced.* A short letter on the rule of thumb that zero misses in N tries can still mean a real rate of about 3 in N.

**If you or someone you know needs help now:** call your local emergency number. In Canada, call or text [9-8-8](https://988.ca/about). In the US, call or text the [988 Suicide & Crisis Lifeline](https://988lifeline.org/).

---

[Back to the reference](README.md) | [Back to the hub home](../README.md)

Made by [Lily Tewolde](https://github.com/Lily-Tewolde). Find me on TikTok at [@lilytewolde](https://www.tiktok.com/@lilytewolde) and on Instagram at [@promptesss](https://www.instagram.com/promptesss).
