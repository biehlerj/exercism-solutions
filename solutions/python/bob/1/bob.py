from typing import Literal


def response(
    hey_bob: str,
) -> Literal[
    "Sure.",
    "Whoa, chill out!",
    "Calm down, I know what I'm doing!",
    "Fine. Be that way!",
    "Whatever.",
]:
    is_question = hey_bob.rstrip().endswith("?")
    is_yelling = hey_bob.isupper()
    is_silence = hey_bob.isspace()

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yelling:
        return "Whoa, chill out!"
    if is_silence or len(hey_bob) == 0:
        return "Fine. Be that way!"
    return "Whatever."
