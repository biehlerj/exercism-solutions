def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """Determines what tree in a grid is the best to build a treehouse

    :param matrix: list[list[int]] - the grid of trees
    :return: list[dict[str, int]] - the ideal position in the grid to build a
    treehouse
    :raises: ValueError if the matrix is irregular

    v2 uses list comprehension and functional programming
    """
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    row_max = list(map(max, matrix))
    col_max = list(map(min, list(zip(*matrix))))

    return [
        {"row": r + 1, "column": c + 1}
        for r, row_m in enumerate(row_max)
        for c, col_m in enumerate(col_max)
        if row_m == col_m
    ]
