def is_armstrong_number(number: int) -> bool:
    """Calculates if a given number is an Armstrong Number

    :param number: int - the number to check
    :return: bool - True if the number is an Armstrong number, otherwise False

    Function that takes in an integer and checks if it is an Armstrong number
    """
    digits = str(abs(number))
    num_of_digits = len(digits)
    sum_of_pow = sum(int(digit) ** num_of_digits for digit in digits)

    return sum_of_pow == number
