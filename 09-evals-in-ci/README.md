# How do you run your evals automatically on every pull request?

You add a small workflow file to your repo that tells GitHub Actions to run your eval script whenever someone opens or updates a pull request. If a must-pass case fails or the score drops, the script exits with an error, the check on the pull request goes red, and the change can't merge until someone fixes it.

![Level: Intermediate](https://img.shields.io/badge/Level-Intermediate-yellow) ![Type: How-to](https://img.shields.io/badge/Type-How--to-green) ![Time: 60 min](https://img.shields.io/badge/Time-60%20min-orange) ![Last checked: 2026-11](https://img.shields.io/badge/Last%20checked-2026--11-lightgrey)

> **TL;DR** Put your golden set, your bot's prompt and a short Python script in an `evals/` folder. Add a workflow file at `.github/workflows/evals.yml` and store your API key as a GitHub secret. Now every pull request runs the golden set and shows a green tick or a red cross. Must-pass cases run several times and any single fail blocks the merge. AI answers vary between runs, so you budget for that instead of hitting re-run until it goes green.

> [!TIP]
> **New to this? Let me break it down.** Picture the salon manager doing all the practice calls herself every time anyone touches the training binder. She'd forget, or skip it when she's busy, and that's exactly when something slips through. Now picture a rule taped to the binder: "Nobody files a change until the practice calls are done, and if anyone gets the allergic reaction call wrong, the change doesn't go in." And someone who runs those calls automatically, every single time. That's CI. The practice calls are your golden set. The rule is the required check on your pull request.

**You'll need:**
- [Lesson 3: Your first pull request](../03-your-first-pull-request/), so you know branches and PRs
- [Lesson 7: Golden sets](../07-golden-sets/), for the 40-case [`salon-golden-set-v2.csv`](../07-golden-sets/salon-golden-set-v2.csv)
- A GitHub repo of your own, and an Anthropic API key from the [Claude Console](https://platform.claude.com/docs/en/get-started)
- Optional: Python 3.10 or later on your computer, if you want to run the script yourself before CI does

**What you'll learn:**
- What CI is, in plain words, and the GitHub Actions vocabulary you'll see
- How a short eval script turns pass or fail into an exit code that CI understands
- How to store an API key safely as a secret, and read the results on a pull request
- How to handle cost and flaky results, and when to run a smoke set instead of the full set

## The parts

| | Part | What you'll do | Time |
|---|---|---|---|
| [ ] | [What CI is](part-1-what-ci-is.md) | Learn the words, set up the folder | 10 min |
| [ ] | [The eval script](part-2-the-eval-script.md) | Read it, run it, break it on purpose | 15 min |
| [ ] | [Run it on every pull request](part-3-run-it-on-every-pr.md) | Add the secret and the workflow, read results | 15 min |
| [ ] | [Cost, flaky results and smoke sets](part-4-cost-flakiness-smoke-sets.md) | Keep it cheap and trustworthy | 10 min |
| [ ] | [Wrap up](part-5-wrap-up.md) | Checklist, challenge, interview questions | 10 min |

The files you'll copy into your repo:

| File in this lesson | Where it goes in your repo | What it is |
|---|---|---|
| [`evals.yml`](evals.yml) | `.github/workflows/evals.yml` | The workflow GitHub runs |
| [`run_evals.py`](run_evals.py) | `evals/run_evals.py` | The eval script |
| [`bot-prompt.txt`](bot-prompt.txt) | `evals/bot-prompt.txt` | The booking assistant's instructions |
| [`baseline.json`](baseline.json) | `evals/baseline.json` | The score to compare against |
| [`requirements.txt`](requirements.txt) | `evals/requirements.txt` | The Python package the script needs |
| [`salon-golden-set-v2.csv`](../07-golden-sets/salon-golden-set-v2.csv) from Lesson 7 | `evals/golden-set.csv` | The golden set |

**[Start Part 1 →](part-1-what-ci-is.md)**
