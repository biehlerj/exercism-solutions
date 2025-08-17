def annotate(garden: list[str]) -> list[str]:
    """Adds flower counts to empty squares in a completed Flower Field

    :param garden: list[str] - completed Flower Field
    :return: list[str] - filled out squares as a list
    """
    if not garden:
        return []

    row_length = len(garden[0])
    valid_chars = {"*", " "}

    for row in garden:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
        if any(c not in valid_chars for c in row):
            raise ValueError("The board is invalid with current input.")

    rows, cols = len(garden), row_length
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def count_flowers(r: int, c: int) -> int:
        """Counts the flowers in the row

        :param r: int - index of the row
        :param c: int - index of the column
        :return: int - count of the flowers
        """
        return sum(
            0 <= r + dr < rows and 0 <= c + dc < cols and garden[r + dr][c + dc] == "*"
            for dr, dc in directions
        )

    result: list[str] = []

    for i, row in enumerate(garden):
        annotated_row = ""

        for idx, cell in enumerate(row):
            if cell == "*":
                annotated_row += "*"
            else:
                count = count_flowers(i, idx)
                annotated_row += str(count) if count else " "

        result.append(annotated_row)

    return result
