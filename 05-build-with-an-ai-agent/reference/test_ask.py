"""Tests for ask.py. None of these call the Claude API.

Run them with:  python -m unittest
"""

import io
import os
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

import ask


class PromptTests(unittest.TestCase):
    def test_system_prompt_contains_the_whole_faq(self):
        faq = ask.FAQ_PATH.read_text(encoding="utf-8").strip()
        self.assertIn(faq, ask.build_system_prompt(faq))

    def test_system_prompt_contains_the_handoff_message(self):
        faq = ask.FAQ_PATH.read_text(encoding="utf-8")
        self.assertIn("passing this to our team", ask.build_system_prompt(faq))

    def test_question_is_wrapped_in_customer_message_tags(self):
        message = ask.build_user_message("Are you open on Sundays?")
        self.assertTrue(message.startswith("<customer_message>"))
        self.assertTrue(message.endswith("</customer_message>"))


class CommandTests(unittest.TestCase):
    def test_dry_run_prints_the_prompt_and_makes_no_api_call(self):
        out = io.StringIO()
        with mock.patch.object(ask, "ask_claude") as fake_call, redirect_stdout(out):
            code = ask.main(["--dry-run", "Are you open on Sundays?"])
        self.assertEqual(code, 0)
        fake_call.assert_not_called()
        self.assertIn("Are you open on Sundays?", out.getvalue())

    def test_missing_key_gives_a_clear_error_and_no_api_call(self):
        err = io.StringIO()
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch.object(ask, "ask_claude") as fake_call, redirect_stderr(err):
            code = ask.main(["Are you open on Sundays?"])
        self.assertEqual(code, 1)
        fake_call.assert_not_called()
        self.assertIn("ANTHROPIC_API_KEY", err.getvalue())

    def test_empty_question_is_rejected(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(ask.main(["   "]), 2)


if __name__ == "__main__":
    unittest.main()
