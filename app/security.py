import re


def input_clean_data(text):

    # Remove suspicious prompt injection phrases
    blocked_patterns = [
        "ignore previous instructions",
        "system prompt",
        "act as",
        "bypass",
        "override security"
    ]

    text = text.lower()

    for pattern in blocked_patterns:
        text = text.replace(pattern, "")

    return text


def no_sensitive_data(text):

    # Mask emails
    text = re.sub(
        r'\\S+@\\S+',
        '[EMAIL_MASKED]',
        text
    )

    # Mask phone numbers
    text = re.sub(
        r'\\b\\d{10}\\b',
        '[PHONE_MASKED]',
        text
    )

    return text