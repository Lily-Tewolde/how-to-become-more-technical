"""Run the Polish & Co. golden set against the booking assistant.

The run fails (exit code 1) if:
  - any must-pass case fails on any of its runs, or
  - the score on the other cases drops too far below the baseline.

Run it from the root of your repo:
  python evals/run_evals.py             # every case
  python evals/run_evals.py --set smoke # must-pass cases only
"""

import argparse
import csv
import json
import os
import sys
from pathlib import Path

from anthropic import Anthropic

HERE = Path(__file__).parent
MODEL = os.environ.get("EVAL_MODEL", "claude-haiku-5-5")  # the model the bot runs on
MUST_PASS_RUNS = 3  # a must-pass case has to pass every one of these runs
ALLOWED_DROP = 0.10  # how far the score can fall below the baseline before the run fails


def ask_bot(client, bot_prompt, message):
    """Send one customer message to the bot in a fresh conversation."""
    reply = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system=bot_prompt,
        messages=[{"role": "user", "content": f"<customer_message>\n{message}\n</customer_message>"}],
    )
    return "".join(block.text for block in reply.content if block.type == "text")


def words(cell):
    return [w.strip().lower() for w in cell.split("|") if w.strip()]


def check(answer, case):
    """Word checks can catch a bad answer. A case with no word checks is
    reported as 'not checked', never counted as a pass."""
    needed, banned = words(case["must_include"]), words(case["must_not_include"])
    if not needed and not banned:
        return "not checked"
    text = answer.lower()
    if any(w not in text for w in needed) or any(w in text for w in banned):
        return "fail"
    return "pass"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", choices=["full", "smoke"], default="full")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("No ANTHROPIC_API_KEY. Add it as a repo secret. (Pull requests from forks don't get secrets.)")

    client = Anthropic()  # reads ANTHROPIC_API_KEY, retries some errors twice by default
    bot_prompt = (HERE / "bot-prompt.txt").read_text(encoding="utf-8")
    with open(HERE / "golden-set.csv", newline="", encoding="utf-8") as f:
        cases = list(csv.DictReader(f))
    if args.set == "smoke":
        cases = [c for c in cases if c["must_pass"] == "yes"]

    results, must_pass_fails, scored, failed_answers = [], [], [], []
    for case in cases:
        must_pass = case["must_pass"] == "yes"
        answers = [ask_bot(client, bot_prompt, case["customer_message"])
                   for _ in range(MUST_PASS_RUNS if must_pass else 1)]
        grades = [check(a, case) for a in answers]
        result = "fail" if "fail" in grades else grades[0]
        results.append((case["id"], "yes" if must_pass else "no", result))
        if result == "fail":
            failed_answers.append((case["id"], answers[grades.index("fail")]))
            if must_pass:
                must_pass_fails.append(case["id"])
        if not must_pass and result != "not checked":
            scored.append(result == "pass")

    baseline = json.loads((HERE / "baseline.json").read_text())["score"]
    score = sum(scored) / len(scored) if scored else None
    score_dropped = score is not None and score < baseline - ALLOWED_DROP

    report = [f"## Golden set: {args.set} run on `{MODEL}`", ""]
    report.append(f"**Must-pass:** {'FAILED ' + ', '.join(must_pass_fails) if must_pass_fails else 'all passed'}")
    if score is not None:
        verdict = "DROPPED" if score_dropped else "ok"
        report.append(f"**Score on other cases:** {score:.0%} of {len(scored)} checked (baseline {baseline:.0%}, {verdict})")
    report += ["", "| Case | Must pass | Result |", "|---|---|---|"]
    report += [f"| {cid} | {mp} | {res} |" for cid, mp, res in results]
    if failed_answers:
        report += ["", "### What the bot said on failed cases", ""]
        report += [f"- **{cid}**: {ans.strip().replace(chr(10), ' ')[:300]}" for cid, ans in failed_answers]
    unchecked = [cid for cid, mp, res in results if mp == "yes" and res == "not checked"]
    if unchecked:
        report += ["", f"**Read by hand before release** (must-pass, no code checks): {', '.join(unchecked)}"]
    report_text = "\n".join(report) + "\n"

    print(report_text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):  # shows the report on the run's summary page
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(report_text)

    if must_pass_fails or score_dropped:
        sys.exit(1)


if __name__ == "__main__":
    main()
