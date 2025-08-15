import math
from typing import Literal


def classify(
    number: int,
) -> Literal["perfect"] | Literal["abundant"] | Literal["deficient"]:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer

    v2 improves performance by using math.isqrt
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors_sum = 1 if number > 1 else 0

    for i in range(2, int(math.isqrt(number)) + 1):
        if number % i == 0:
            divisors_sum += i
            other = number // i

            if other != i:
                divisors_sum += other

    if divisors_sum == number:
        return "perfect"
    if divisors_sum > number:
        return "abundant"
    return "deficient"
