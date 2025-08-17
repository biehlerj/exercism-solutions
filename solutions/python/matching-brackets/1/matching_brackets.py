PAIRS = {")": "(", "]": "[", "}": "{"}
OPENING = set(PAIRS.values())
CLOSING = set(PAIRS.keys())


def is_paired(input_string: str) -> bool:
    """Checks if brackets, braces, and parentheses are balanced

    :param input_string: str - string to check
    :return: bool - True if balanced otherwise False
    """

    stack: list[str] = []

    for char in input_string:
        if char in OPENING:
            stack.append(char)
        elif char in CLOSING:
            if not stack or stack[-1] != PAIRS[char]:
                return False
            stack.pop()

    return not stack
