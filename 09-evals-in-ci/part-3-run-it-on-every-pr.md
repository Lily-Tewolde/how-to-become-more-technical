<sub>Lesson 9, Part 3 of 5 · about 15 min</sub>

# Run it on every pull request

**In this part,** you'll store your API key as a GitHub secret, add the workflow file, open a pull request and read the result, then make the check required so a red result blocks the merge.

## Do it (step by step)

### 6. Store your API key as a secret

**Your API key goes in GitHub's secret store, never in a file.** A secret is encrypted, and GitHub hides it in logs. Anyone who can read your repo can read your files, so a key in a file is a key you've given away.

These are the steps from GitHub's guide, [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets):
1. Go to the main page of your repo and click **Settings**.
2. In the "Security" section of the sidebar, select **Secrets and variables**, then click **Actions**.
3. On the **Secrets** tab, click **New repository secret**.
4. In **Name**, type `ANTHROPIC_API_KEY`.
5. In **Secret**, paste your key.
6. Click **Add secret**.

A few habits worth having:
- **Make a key just for CI.** If it ever leaks, you can delete that one key without breaking anything else.
- **Set a low spending limit** if your API account lets you. A loop gone wrong should cost you a few dollars, not a few hundred.
- **Never print the key** in a script or a log, even to "check it's there".

**You're done when** `ANTHROPIC_API_KEY` shows in your repo's list of Actions secrets.

<details>
<summary><strong>Stuck?</strong></summary>

- **"I don't see Settings."** You need admin access to the repo. If it's someone else's, ask them to add the secret.
- **"Someone forked my repo and their PR fails with 'No ANTHROPIC_API_KEY'."** That's GitHub protecting you. Its docs say: "With the exception of `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository." Otherwise anyone could open a PR that prints your key. Review the change, and if it's safe, recreate it on a branch in your own repo to run the evals.
</details>

### 7. Add the workflow file

**Create `.github/workflows/evals.yml` on your branch and paste in [`evals.yml`](evals.yml).** Here's what it says, in plain words:

| Part of the file | What it means |
|---|---|
| `on: pull_request` | Run this whenever a pull request is opened or updated |
| `workflow_dispatch` with a `set` choice | Also let me start it by hand from the Actions tab, and pick the full set or the smoke set |
| `permissions: contents: read` | The job can read the code and nothing else. It can't push, comment or change settings. |
| `concurrency` with `cancel-in-progress: true` | If you push again while a run is going, cancel the old run. You only care about the latest code, and this saves money. |
| `runs-on: ubuntu-latest` | Use a fresh Linux runner |
| `timeout-minutes: 15` | Give up after 15 minutes. GitHub's default is 360, which is a long time to pay for a stuck run. |
| `actions/checkout@v7` | Get the code from the pull request |
| `actions/setup-python@v7` | Install Python 3.13 |
| `pip install -r evals/requirements.txt` | Install the Anthropic SDK |
| `env:` on the last step | Hand the secret and the chosen set to the script as environment variables |
| `run: python evals/run_evals.py` | Run the golden set. If the script exits with 1, this step fails, and so does the check. |

Two small details. The `@v7` on each action is its major version, which was current when I checked in November 2026. And the chosen set reaches the script through an environment variable, not pasted straight into the command. GitHub's [secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) recommends that pattern, so a value can't change the command that runs.

**You're done when** your branch has `.github/workflows/evals.yml` and the five files in `evals/`.

### 8. Open a pull request and read the result

**Open a pull request from your branch.** Within a few seconds, a box near the bottom of the pull request shows the check running. When it's done, you'll see a green tick or a red cross next to it.

To read the result:
1. Click **Details** next to the check. This opens the run's log.
2. Open the **Run the golden set** step to see everything the script printed. That's one line per case as it ran, then the report.
3. Go to the run's **Summary** page to see the report as a table. It's the same report, written to the summary by the script.

When a check fails, read which one failed and why before you change anything. The report tells you:
- which must-pass cases failed, by ID
- what the bot actually said on every failed case
- the score, the baseline, and whether it dropped
- which must-pass cases a person still has to read

**Then try the red version.** Push a commit to the same branch that deletes the bleeding line from rule 3 in `bot-prompt.txt`, like step 5. The check should go red with the must-escalate failures listed. Undo the commit, and it goes green again.

**You're done when** you've seen the check go green, then red, then green again on the same pull request.

<details>
<summary><strong>Stuck?</strong></summary>

- **"No check shows up."** Make sure the file is at exactly `.github/workflows/evals.yml`, with the dot, and that the YAML indentation uses spaces, not tabs. Check the **Actions** tab for an error about the file.
- **"The check is yellow forever."** It's queued or running. Each must-pass case runs three times, so a full run takes a few minutes.
- **"It failed, but I didn't change the prompt."** Open the report and read the failed answers. It could be a real failure that comes and goes. Part 4 covers what to do with those.
</details>

### 9. Make the check required

**A red cross only blocks the merge if you tell GitHub it's required.** Without that, someone can merge anyway. To make it required, add a branch protection rule for your main branch with **Require status checks to pass before merging** turned on, and pick the `golden-set` check. GitHub explains the options in [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

Two things to know:
- **Plan.** GitHub says "protected branches are available in public repositories with GitHub Free and GitHub Free for organizations". Private repos need a paid plan for this. The same goes for [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), GitHub's newer way to set the same rule.
- **Practising in a private repo on GitHub Free?** You won't be able to turn this on. You've got two options:
  - Make your practice repo public, if nothing in it is private. Your API key stays safe either way, because it's stored as a GitHub secret, not in your code.
  - Skip this step. The red cross still shows on every pull request. It just won't stop anyone merging.
- **Don't let a required check get skipped.** You can tell a workflow to run only when certain files change. But GitHub warns that when a required workflow is skipped that way, its checks "stay in a 'Pending' state and block merging", and its advice is to "avoid requiring workflows that can be skipped" ([Troubleshooting required status checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)). That's why `evals.yml` runs on every pull request.

**You're done when** a pull request with a red `golden-set` check can't be merged. If you skipped this step on a private repo, you're done when you've seen the red cross on the pull request.

## Quick check

<details>
<summary>1. Why can't a pull request from a fork see your API key?</summary>

GitHub doesn't pass secrets to workflows triggered from a fork. Otherwise anyone could open a pull request that prints your key.
</details>

<details>
<summary>2. The check went red. What's the first thing you do?</summary>

Read which cases failed and what the bot actually said, in the run's report. Don't change anything until you know why it failed.
</details>

<details>
<summary>3. Why doesn't <code>evals.yml</code> only run when the prompt changes?</summary>

Because a required check that gets skipped stays pending and blocks the merge. It's simpler to run it on every pull request.
</details>

---

**Next: [Part 4 (Cost, flaky results and smoke sets)](part-4-cost-flakiness-smoke-sets.md)** | [Back to the lesson](README.md)
