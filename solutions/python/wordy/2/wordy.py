from functools import reduce
from operator import add, floordiv, mul, sub

OPERATORS = {"plus": add, "minus": sub, "multiplied": mul, "divided": floordiv}


def answer(question):
    """Provides the answer to a math question

    :param question: str - a math question
    :return: int - answer to the math question

    v2 uses functools.reduce()
    """
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")

    question = list(
        filter(lambda x: x not in ("What", "is", "by"), question.strip("?").split())
    )
    operations = question[1::2]
    digits = [
        int(element) if (element.isdigit() or element[1:].isdigit()) else None
        for element in question[::2]
    ]

    if len(digits) - 1 != len(operations) or None in digits:
        raise ValueError("syntax error")

    result = reduce(lambda x, y: OPERATORS[operations.pop(0)](x, y), digits)

    return result
