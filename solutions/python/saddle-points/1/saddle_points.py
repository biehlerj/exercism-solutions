def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """Determines what tree in a grid is the best to build a treehouse

    :param matrix: list[list[int]] - the grid of trees
    :return: list[dict[str, int]] - the ideal position in the grid to build a
    treehouse
    :raises: ValueError if the matrix is irregular
    """
    if not matrix:
        return []

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    points: list[dict[str, int]] = []

    for i, row in enumerate(matrix):
        max_in_row = max(row)

        for j, value in enumerate(row):
            if value == max_in_row:
                col = [matrix[x][j] for x in range(len(matrix))]

                if value == min(col):
                    points.append({"row": i + 1, "column": j + 1})

    return points
