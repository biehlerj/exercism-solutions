from functools import reduce
from typing import List, Optional

PAIRS = {")": "(", "]": "[", "}": "{"}
OPENING = set(PAIRS.values())
CLOSING = set(PAIRS.keys())


def is_paired(input_string: str) -> bool:
    """Checks if brackets, braces, and parentheses are balanced

    :param input_string: str - string to check
    :return: bool - True if balanced otherwise False

    v2 uses functools.reduce
    """

    def reducer(stack: Optional[List[str]], char: str) -> Optional[List[str]]:
        """Processes a single character and updates the stack of opening brackets.

        :param stack: Optional[List[str]] - The current stack of opening brackets, or None if unbalanced so far.
        :param char: str - The current character being processed.
        :return: Optional[List[str]] - The updated stack if still balanced, or None if unbalanced.
        """
        if stack is None:
            return None
        if char in OPENING:
            return stack + [char]
        elif char in CLOSING:
            if not stack or stack[-1] != PAIRS[char]:
                return None
            return stack[:-1]
        return stack

    result = reduce(reducer, input_string, [])

    return result == []
