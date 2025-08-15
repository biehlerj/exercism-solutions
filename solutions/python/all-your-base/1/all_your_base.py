from itertools import dropwhile


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not digits:
        return [0]
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    digits = list(dropwhile(lambda x: x == 0, digits))

    if not digits:
        return [0]

    num = 0

    for d in digits:
        num = num * input_base + d

    result = []

    while num > 0:
        result.append(num % output_base)
        num //= output_base

    return result[::-1] if result else [0]
