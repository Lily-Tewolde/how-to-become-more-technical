"""Guardrails for the Polish & Co. booking assistant (Lesson 11).

Four checks that run in plain code, with no AI:

1. must_escalate(message)          runs BEFORE the model
2. price_problems(reply)           runs AFTER the model
3. medical_advice_problems(reply)  runs AFTER the model
4. tone_problems(reply)            runs AFTER the model

respond() wires them together. Run the file to see them work:

    python salon_guardrails.py

Polish & Co. is a made-up salon. The prices match example/README.md.
"""

import json
import re
from datetime import datetime, timezone

PROMPT_VERSION = "salon-v3"

HANDOFF_MESSAGE = (
    "I'm so sorry, I want to make sure you get the right help. I'm passing this "
    "to our team now, and someone will reach out to you shortly. If you're having "
    "trouble breathing or this feels urgent, please call 911 or go to the nearest "
    "emergency room."
)

SAFE_FALLBACK = (
    "I want to make sure I give you the right price, so I'll let our team confirm "
    "it. You can call us or book online, and the price will show before you confirm."
)


# ---------------------------------------------------------------------------
# 1. Before the model: the must-escalate detector
# ---------------------------------------------------------------------------

# Phrases that look scary but aren't. They're removed before the patterns run.
SAFE_PHRASES = [
    "burnt orange",
    "burnt sienna",
    "this is fire",
    "was fire",
    "so fire",
]

ESCALATE_PATTERNS = {
    "allergic_reaction": [
        r"\brash\b", r"\bhives\b", r"\bitch(y|ing)?\b", r"\bswell(ing|ed|s)?\b",
        r"\bswollen\b", r"\breaction\b", r"\ballerg", r"\bbreath(e|ing)?\b",
    ],
    "burn": [r"\bburn(t|ed|s|ing)?\b", r"\bblister"],
    "infection": [r"\binfect", r"\bpus\b", r"\boozing\b", r"\bbleed(ing)?\b"],
    "pregnancy": [r"\bpregnan", r"\btrimester\b", r"\bexpecting a baby\b", r"\bbreastfeed"],
    "complaint_or_chargeback": [
        r"\bchargeback", r"\bdisput", r"\brefund", r"\bcomplain", r"\blawyer", r"\bsue\b",
    ],
}


def must_escalate(message: str) -> list[str]:
    """Return the must-escalate categories a message matches. Empty means none."""
    text = message.lower().replace("’", "'")
    for phrase in SAFE_PHRASES:
        text = text.replace(phrase, " ")
    return [
        category
        for category, patterns in ESCALATE_PATTERNS.items()
        if any(re.search(p, text) for p in patterns)
    ]


# ---------------------------------------------------------------------------
# 2. After the model: the price check
# ---------------------------------------------------------------------------

# What each service is allowed to cost, from the FAQ. Specific names come first,
# so "gel manicure" is checked before the vaguer word "gel".
SERVICE_PRICES = {
    "classic manicure": {35},
    "gel manicure": {50},
    "gel mani": {50},
    "gel removal": {15},
    "classic pedicure": {45},
    "gel pedicure": {60},
    "acrylic full set": {70},
    "full set": {70},
    "fill": {50},
    "nail art": {5 * n for n in range(1, 11)},  # from $5 a nail, up to all 10 nails
    "deposit": {20, 50},  # $20 deposit, for appointments over $50
    "kids": {20},
    "gel": {50, 60, 15},
    "manicure": {35, 50, 20},
    "pedicure": {45, 60},
    "acrylic": {70, 50},
}
ALL_FAQ_AMOUNTS = set().union(*SERVICE_PRICES.values())

# "Free" is only right for gel removal with a new set, a fix within 5 days,
# or when the bot is saying no.
FREE_IS_OK_WITH = ("removal", "fix", "can't", "cannot", "not", "isn't", "don't", "unable")


def _sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def price_problems(reply: str) -> list[str]:
    """Return a list of price problems in a reply. Empty means it passed."""
    problems = []
    for sentence in _sentences(reply):
        lowered = sentence.lower()
        amounts = {float(a) for a in re.findall(r"\$(\d+(?:\.\d{1,2})?)", sentence)}

        allowed = set()
        remaining = lowered
        for service in sorted(SERVICE_PRICES, key=len, reverse=True):
            if service in remaining:
                allowed |= SERVICE_PRICES[service]
                remaining = remaining.replace(service, " ")
        if not allowed:
            allowed = ALL_FAQ_AMOUNTS

        for amount in sorted(amounts):
            if amount not in allowed:
                problems.append(f"${amount:g} isn't a real price here: {sentence!r}")

        if "free" in lowered and not any(word in lowered for word in FREE_IS_OK_WITH):
            problems.append(f"offers something free: {sentence!r}")
    return problems


# ---------------------------------------------------------------------------
# 3. After the model: the no-medical-advice check
# ---------------------------------------------------------------------------

MEDICAL_ADVICE_WORDS = [
    "cream", "ointment", "antihistamine", "hydrocortisone", "polysporin",
    "aloe", "ice pack", "cold water", "soak it", "pop the",
    "is safe", "are safe", "perfectly safe", "should be fine",
]


def medical_advice_problems(reply: str) -> list[str]:
    lowered = reply.lower()
    return [f"sounds like medical advice: {w!r}" for w in MEDICAL_ADVICE_WORDS if w in lowered]


# ---------------------------------------------------------------------------
# 4. After the model: the tone rule (soft, logged for review, never blocked)
# ---------------------------------------------------------------------------

UNKIND_PHRASES = [
    "calm down", "as i said", "as i already said", "you should have",
    "that's not our problem", "per our policy", "obviously",
]


def tone_problems(reply: str) -> list[str]:
    problems = []
    if len(_sentences(reply)) > 4:
        problems.append("longer than 4 sentences")
    lowered = reply.lower().replace("’", "'")
    problems += [f"unkind phrase: {p!r}" for p in UNKIND_PHRASES if p in lowered]
    shouting = [w for w in re.findall(r"\b[A-Z]{4,}\b", reply) if w not in {"FAQ"}]
    if shouting:
        problems.append(f"all caps: {shouting}")
    return problems


# ---------------------------------------------------------------------------
# Wiring it together, with a log line for every decision
# ---------------------------------------------------------------------------

def log(message_id: str, guardrail: str, action: str, details: list[str]) -> None:
    """One JSON line per guardrail decision. Swap print for your real logger."""
    print(json.dumps({
        "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "message_id": message_id,
        "prompt_version": PROMPT_VERSION,
        "guardrail": guardrail,
        "action": action,
        "details": details,
    }))


def respond(message_id: str, message: str, call_model) -> str:
    # Before the model. A match means the model never sees the message.
    categories = must_escalate(message)
    if categories:
        log(message_id, "must_escalate", "handoff_sent_staff_alerted", categories)
        return HANDOFF_MESSAGE

    reply = call_model(message)

    # After the model. Hard checks block. The soft check only logs.
    medical = medical_advice_problems(reply)
    if medical:
        log(message_id, "no_medical_advice", "reply_replaced_with_handoff", medical)
        return HANDOFF_MESSAGE

    prices = price_problems(reply)
    if prices:
        log(message_id, "price_check", "reply_replaced_with_fallback", prices)
        return SAFE_FALLBACK

    tone = tone_problems(reply)
    if tone:
        log(message_id, "tone_rule", "sent_and_flagged_for_review", tone)

    return reply


# ---------------------------------------------------------------------------
# Demo: made-up messages and made-up model replies
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("1. Must-escalate detector (before the model)\n")
    messages = {
        "ME-01": "Since my gel set yesterday my fingertips are itchy and there's a rash.",
        "ME-03": "My toes got burnt in the foot bath and now there's a blister.",
        "ME-05": "I'm 5 months pregnant. Is gel polish safe for me?",
        "ME-07": "Omg love the colour!! Also the skin under one nail has been swollen since Saturday lol",
        "TW-03": "The nail art you did last time was fire, can I get the same design again?",
        "FA-01": "Can I get burnt orange tips for fall?",
        "FA-02": "If I cancel 2 days ahead, is my deposit refunded?",
        "MISS-01": "my finger looks kinda puffy and weird since my appointment",
    }
    for message_id, text in messages.items():
        hits = must_escalate(text)
        print(f"  {message_id:8} {'ESCALATE ' + str(hits) if hits else 'normal'}")
    print(
        "\n  FA-02 is a false alarm (a normal deposit question), and MISS-01 is a miss"
        "\n  ('puffy' isn't on the list). Word lists trade one for the other.\n"
    )

    print("2. Price check (after the model)\n")
    replies = [
        "A gel manicure is $50 and takes about 60 minutes.",
        "Good news, gel is $5 today!",
        "A kids' manicure is $20, and nail art is from $5 a nail.",
        "A gel manicure is $35 for you.",
        "Sure, I can book that for free!",
        "Gel removal is free when you're getting a new gel set.",
        "I can't offer a free service, but a gel mani is $50.",
    ]
    for reply in replies:
        problems = price_problems(reply)
        print(f"  {'FAIL' if problems else 'pass'}  {reply}")
        for p in problems:
            print(f"        {p}")

    print("\n3. The whole flow, with log lines\n")
    fake_model = {
        "Do you sell gift cards?": (
            "I don't have that information, but I'm happy to connect you with the salon!"
        ),
        "How much is gel?": "Good news, gel is $5 today!",
        "How long is a pedicure?": (
            "As I said, a classic pedicure is $45 and takes 50 minutes."
        ),
    }
    for i, (text, model_reply) in enumerate(fake_model.items(), start=1):
        final = respond(f"msg_{i:04}", text, lambda _m, r=model_reply: r)
        print(f"  Customer: {text}\n  Sent:     {final}\n")
    final = respond("msg_0004", messages["ME-01"], lambda _m: "Try a hydrocortisone cream!")
    print(f"  Customer: {messages['ME-01']}\n  Sent:     {final}\n")
