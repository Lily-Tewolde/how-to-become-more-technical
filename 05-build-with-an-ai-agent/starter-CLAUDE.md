# Polish & Co. FAQ assistant

<!-- Starter CLAUDE.md from Lesson 5 of how-to-become-more-technical.
     Copy this into the root of your project and rename it to CLAUDE.md.
     Claude Code reads it at the start of every session.
     Change anything in it to match what you're building. -->

## What we're building

A tiny command-line assistant for Polish & Co., a made-up nail salon. Someone types a customer question, and it prints a short answer that comes only from `faq.md`, using the Claude API.

```
python ask.py "Are you open on Sundays?"
```

## Done looks like

- `python ask.py "question"` prints a warm answer of two or three sentences, using only `faq.md`
- `python ask.py --dry-run "question"` prints the exact prompt it would send and makes no API call
- With no `ANTHROPIC_API_KEY` set, it prints a clear one-line message and exits with an error, with no stack trace
- An empty question is rejected with a clear message
- `python -m unittest` passes, and no test calls the API

## Files

- `faq.md` holds the FAQ, the rules and the handoff message. I own this file. Never edit it.
- `ask.py` is the script.
- `test_ask.py` holds the tests.

## Rules

- The API key comes only from the `ANTHROPIC_API_KEY` environment variable. Never write a key into any file, never print it, never commit it.
- Python 3.10 or newer. Use the standard library plus the `anthropic` package only. Ask before adding anything else.
- Use the model `claude-haiku-5-5`. Ask before changing it.
- The instructions and the whole of `faq.md` go in the system prompt. The customer's question goes in the user message, inside `<customer_message>` tags.
- Never invent salon facts. If it's not in `faq.md`, the assistant says it doesn't know and offers to connect the customer with the salon.
- Keep it small. One script and one test file. No web server, database or extra files unless I ask.

## How to check your work

- Dry run: `python ask.py --dry-run "Are you open on Sundays?"`
- Tests: `python -m unittest`
- When you say something works, show me the command you ran and its output.

## How we work

- Tell me your plan before you write code. Then do one step at a time and stop after each step so I can check it.
- Commit only after I say a step looks good. One commit per step, with a short message that starts with a verb.
- Don't push, merge or open pull requests. I do that.
- Don't make live API calls. I run those myself.
- If something here is unclear or missing, stop and ask. Mark it OPEN QUESTION rather than guessing.
