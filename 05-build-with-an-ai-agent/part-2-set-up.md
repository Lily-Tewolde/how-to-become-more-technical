<sub>Lesson 5, Part 2 of 5 · about 15 min</sub>

# Set up your project

**In this part,** you'll make a new repo, add your spec and the FAQ on a branch, install Claude Code, and set up your API key so it never touches a file.

## Do it (step by step)

### 4. Make a new repo on GitHub

**Start with an empty repo that already ignores the files you never want committed.** On GitHub, click **+** at the top right, then **New repository**.
- Name it `polish-faq-assistant`.
- Public or private is up to you.
- Turn on the option to add a README.
- In the .gitignore options, choose the **Python** template.

Click **Create repository**.

The Python `.gitignore` tells git to skip files like your virtual environment folder (`.venv`) and `.env`. It's your safety net if a secret ever ends up in a file in this folder.

You're done when your new repo shows `README.md` and `.gitignore`.

### 5. Copy it to your computer and make a branch

**Work on a branch from the very first change.** Open a terminal and run these, using your own username:

```bash
git clone https://github.com/YOUR-USERNAME/polish-faq-assistant.git
cd polish-faq-assistant
git switch -c build/faq-assistant
```

The branch name starts with `build/` because this is new work. Everything you and the agent do from here lands on this branch, and `main` stays clean until your PR merges.

You're done when `git status` says `On branch build/faq-assistant`.

<details>
<summary>Stuck?</summary>

- **`git clone` asks for a password and then fails.** GitHub doesn't accept your account password for git. Lesson 3's [terminal route](../03-your-first-pull-request/extra-credit.md) covers the options. The quickest is the [GitHub CLI](https://cli.github.com/) and `gh auth login`.
- **`git switch` isn't recognised.** Your git is older. Use `git checkout -b build/faq-assistant` instead.
</details>

### 6. Add your spec, the FAQ and the Claude API library

**Put the two files the agent needs in the project, then install the one library it's allowed to use.**
1. Create `CLAUDE.md` in the project folder and paste in your version from Part 1.
2. Create `faq.md` and paste in three sections of the [running example](../example/README.md): **The FAQ the assistant answers from**, **Rules the assistant follows**, and the handoff message under them.
3. Make a virtual environment and install the Claude API's Python library:

   ```bash
   # macOS or Linux
   python3 -m venv .venv
   source .venv/bin/activate
   pip install anthropic
   ```

   ```powershell
   # Windows PowerShell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install anthropic
   ```

   A virtual environment keeps this project's libraries separate from everything else on your computer. Your prompt usually shows `(.venv)` while it's on.

4. Commit the two files:

   ```bash
   git add CLAUDE.md faq.md
   git commit -m "Add the spec and the salon FAQ"
   ```

You're done when `git log --oneline` shows your commit, and `git status` doesn't list `.venv` (the `.gitignore` is hiding it, which is what you want).

<details>
<summary>Stuck?</summary>

- **`python3` isn't found.** On Windows, use `python`. If neither works, install Python 3.10 or newer from [python.org](https://www.python.org/downloads/).
- **PowerShell won't run `Activate.ps1`.** Windows blocks scripts by default. Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.
- **`git status` lists `.venv/`.** The `.gitignore` didn't make it. Check it's in the project folder and has a `.venv` line.
</details>

### 7. Install Claude Code and start it in your project

**Install it once, then start it from inside the project folder.** These are the install commands from the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart):

```bash
# macOS, Linux or WSL
curl -fsSL https://claude.ai/install.sh | bash
```

```powershell
# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

Open a new terminal window, then check it worked:

```bash
claude --version
```

Now go to your project, turn on the virtual environment, and start Claude Code:

```bash
cd polish-faq-assistant
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
claude
```

The first time, it asks you to log in through your browser. Then ask it:

```text
What does this project do, and what are you not allowed to do here?
```

You're done when its answer matches your `CLAUDE.md`, including that it won't edit `faq.md` or make live API calls. That's how you know it read the file.

<details>
<summary>Stuck?</summary>

- **`claude` isn't found after installing.** Open a brand new terminal window. If it's still not found, the install folder isn't on your PATH yet. The [troubleshooting page](https://code.claude.com/docs/en/troubleshoot-install) has the fix.
- **You'd rather not use the terminal.** Claude Code also runs in a desktop app, in VS Code and on the web. The [overview](https://code.claude.com/docs/en/overview) lists them all. The steps in this lesson are the same, you just type into a different window.
- **Its answer doesn't mention your rules.** Check that `CLAUDE.md` is in the folder you started `claude` from, and the name is exactly `CLAUDE.md`.
</details>

### 8. Get your API key and keep it out of every file

**The key goes in a second terminal's environment, never in your code.** The assistant you're building calls the Claude API, and the API needs a key.
1. Create a key in the [Claude Console](https://platform.claude.com/settings/keys). Copy it somewhere safe for a minute. You won't see it again.
2. Open a **second** terminal window. This is where you'll run the assistant yourself. Leave Claude Code running in the first one.
3. In the second terminal, go to the project, turn on the virtual environment, and set the key:

   ```bash
   # macOS or Linux
   cd polish-faq-assistant
   source .venv/bin/activate
   export ANTHROPIC_API_KEY="paste-your-key-here"
   ```

   ```powershell
   # Windows PowerShell
   cd polish-faq-assistant
   .venv\Scripts\Activate.ps1
   $env:ANTHROPIC_API_KEY = "paste-your-key-here"
   ```

The key now lives only in that terminal window. When you close it, it's gone, and you set it again next time.

Here's why I keep two terminals:
- **The agent never sees the key.** Claude Code is in the first terminal, where the key isn't set. It can't print it, paste it into a file or commit it.
- **You stay the one who checks the live answers.** That's step 11, and it's worth doing yourself.
- **Claude Code keeps using your Claude login.** If it starts in a terminal where `ANTHROPIC_API_KEY` is set, it asks whether to use that key instead, which bills Claude Code's own work to your API credit.

To check without printing the key on screen, run this in each terminal:

```bash
python -c "import os; print('key is set' if os.environ.get('ANTHROPIC_API_KEY') else 'no key here')"
```

You're done when the second terminal says `key is set` and the Claude Code terminal says `no key here`. In the Claude Code window, type `!` before the command so it runs as a plain shell command instead of a message to Claude.

> [!WARNING]
> Never paste your key into a chat, a file in this project, a commit or a PR. If it ever gets committed, deleting the file isn't enough, because git keeps the history. Delete the key in the Claude Console and make a new one.

<details>
<summary><strong>Go deeper (environment variables and .env files)</strong></summary>

An environment variable is a named value your terminal hands to any program it starts. `ANTHROPIC_API_KEY` is the name the Claude SDKs look for, so `anthropic.Anthropic()` finds it without your code ever mentioning the key ([Claude Platform docs, Get started](https://platform.claude.com/docs/en/get-started)).

Real projects often keep keys in a `.env` file so you don't retype them. That's fine if two things are true:
- `.env` is in `.gitignore` before the file exists. The Python template already does this.
- The agent is blocked from reading it. A line in `CLAUDE.md` isn't enough for that. Use a permission rule, shown in [Extra credit](extra-credit.md).

Remember that `.gitignore` only works on files git isn't already tracking. If a secret file was committed once, you have to untrack it and rotate the secret ([GitHub Docs, Ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files)). On public repos, GitHub's [secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) runs for free and can catch some keys after the fact, but don't plan on it.
</details>

## Quick check

<details>
<summary>1. Why does Claude Code run in a terminal where the API key isn't set?</summary>

So the agent never sees the key and can't print it, write it into a file or commit it. It also means Claude Code keeps using your Claude login instead of billing its work to your API credit.
</details>

<details>
<summary>2. Your key got committed and you deleted the file in the next commit. Are you safe?</summary>

No. Git keeps every earlier version, so the key is still in the history. Delete the key in the Claude Console and make a new one.
</details>

---

**Next: [Part 3 (Build it in small steps)](part-3-build-in-small-steps.md)** | [Back to the lesson](README.md)
