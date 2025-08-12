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
    """Determines what Bob will respond to someone talking to him

    :param hey_bob: str - What is being said to Bob
    :return: str - A string depending on the kind of phrase being said to
    Bob

    Function that takes in a string and determines what Bob will respond with
    based on the contents of the string.
    """
    hey_bob = hey_bob.rstrip()

    if not hey_bob:
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_yelling:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."
