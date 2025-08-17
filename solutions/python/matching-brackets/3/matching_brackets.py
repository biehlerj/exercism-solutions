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

        v2 of reducer uses structural pattern matching
        """
        if stack is None:
            return None

        match char:
            case c if c in OPENING:
                return stack + [c]
            case c if c in CLOSING:
                match stack:
                    case [*rest, top] if top == PAIRS[c]:
                        return rest
                    case _:
                        return None
            case _:
                return stack

    result = reduce(reducer, input_string, [])

    return result == []
