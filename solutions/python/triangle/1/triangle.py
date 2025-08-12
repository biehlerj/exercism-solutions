def equilateral(sides: list[int] | list[float]) -> bool:
    """Determines if a given triangle is an equilateral triangle

    :param sides: list[int] | list[float] - The triangle to check
    :return: bool - True if a triangle is an equilateral triangle otherwise False

    Function that takes in a list of numbers that represents the length of the sides
    of a triangle and determines if the triangle is an equilateral triangle.
    """
    return len(set(sides)) == 1 and sides[0] > 0


def isosceles(sides: list[int] | list[float]) -> bool:
    """Determines if a given triangle is an isosceles triangle

    :param sides: list[int] | list[float] - The triangle to check
    :return: bool - True if a triangle is an isosceles triangle otherwise False

    Function that takes in a list of numbers that represents the length of the sides
    of a triangle and determines if the triangle is an isosceles triangle.
    """
    return (
        min(sides) > 0
        and sides[0] + sides[1] > sides[2]
        and sides[0] + sides[2] > sides[1]
        and sides[1] + sides[2] > sides[0]
        and len(set(sides)) <= 2
    )


def scalene(sides: list[int] | list[float]) -> bool:
    """Determines if a given triangle is an scalene triangle

    :param sides: list[int] | list[float] - The triangle to check
    :return: bool - True if a triangle is an scalene triangle otherwise False

    Function that takes in a list of numbers that represents the length of the sides
    of a triangle and determines if the triangle is an scalene triangle.
    """
    return (
        min(sides) > 0
        and sides[0] + sides[1] > sides[2]
        and sides[0] + sides[2] > sides[1]
        and sides[1] + sides[2] > sides[0]
        and len(set(sides)) == 3
    )
