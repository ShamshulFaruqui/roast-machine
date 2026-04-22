BLOCKED_TERMS = [
    "kill yourself",
    "suicide",
    "self harm",
    "self-harm",
    "you are worthless",
    "i hate myself",
]

INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "you are now",
    "forget everything",
    "new personality",
    "disregard your",
    "pretend you are",
    "act as if",
]

def check_input(user_input: str) -> dict:
    text = user_input.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in text:
            return {
                "safe": False,
                "reason": "prompt_injection",
                "message": "Nice try — detected a prompt injection attempt. I'm logging this. 👀"
            }
    for term in BLOCKED_TERMS:
        if term in text:
            return {
                "safe": False,
                "reason": "harmful_content",
                "message": "That crosses the line — roasts should be funny, not harmful. Try something else."
            }
    return {"safe": True, "reason": None, "message": None}

def check_roast_output(roast: str) -> dict:
    text = roast.lower()
    for term in BLOCKED_TERMS:
        if term in text:
            return {
                "safe": False,
                "message": "The AI tried to go too far — output blocked by guardrail."
            }
    return {"safe": True, "message": roast}