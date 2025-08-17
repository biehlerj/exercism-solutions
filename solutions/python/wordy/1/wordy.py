import re


def answer(question: str) -> int:
    """Orchestrates parsing and evaluation of a math word problem.

    :param question: The math question as a string.
    :return: The integer result of evaluating the question.
    :raises ValueError: For unknown operations or syntax errors.
    """
    tokens = parse_question(question)
    return evaluate_tokens(tokens)


def parse_question(question: str) -> list[str]:
    """Parses the question string into a list of tokens (numbers and operators).

    :param question: The math question as a string.
    :return: List of tokens (numbers as strings and operator symbols).
    :raises ValueError: For unknown operations or syntax errors.
    """
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")  # changed from "unknown operation"
    q = question[8:-1].strip()
    if not q:
        raise ValueError("syntax error")

    # Replace multi-word operators first
    q = q.replace("multiplied by", "*")
    q = q.replace("divided by", "/")
    # Replace single-word operators
    q = q.replace("plus", "+")
    q = q.replace("minus", "-")

    # Split into tokens (numbers and operators)
    tokens = re.findall(r"-?\d+|[+\-*/]", q)

    # If there are any stray words, check if it's a syntax error (extra numbers) or unknown operation (extra words)
    leftovers = re.sub(r"-?\d+|[+\-*/]", "", q).strip()
    if leftovers:
        # If leftovers are only digits and whitespace, it's a syntax error (e.g., "1 2 plus")
        if re.fullmatch(r"[\d\s-]+", leftovers):
            raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")

    if not tokens:
        raise ValueError("syntax error")

    # Validate tokens: must alternate number, operator, number, ...
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")
    for i, t in enumerate(tokens):
        if i % 2 == 0:
            if not re.fullmatch(r"-?\d+", t):
                raise ValueError("syntax error")
        else:
            if t not in "+-*/":
                raise ValueError("syntax error")  # changed from "unknown operation"

    return tokens


def evaluate_tokens(tokens: list[str]) -> int:
    """Evaluates a list of tokens representing a left-to-right math expression.

    :param tokens: List of tokens (numbers as strings and operator symbols).
    :return: The integer result of evaluating the tokens.
    :raises ValueError: For syntax errors.
    """
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        try:
            num = int(tokens[i + 1])
        except Exception:
            raise ValueError("syntax error")
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        elif op == "*":
            result *= num
        elif op == "/":
            result //= num
        else:
            raise ValueError("unknown operation")
        i += 2
    return result
