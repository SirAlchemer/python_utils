def check_neighbours(cell_pos: list[int, int], grid: list[list[bool]]) -> list[bool | None]:
    """
    Check the neighbors (east, west, north, south) of a given cell in the grid.

    Args:
        cell_pos (list[int, int]): The [row, col] position of the cell in the grid.
        grid (list[list[bool]]): A 2D grid of boolean values.

    Returns:
        list[bool | None]: A list of booleans indicating the state of each neighbor:
                           - True: Neighbor is "alive" (True).
                           - False: Neighbor is "dead" (False).
                           - None: Neighbor is out of bounds.
    """
    neighbours = []
    rows, cols = len(grid), len(grid[0])
    for (row_offset, col_offset) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new_row, new_col = cell_pos[0] + row_offset, cell_pos[1] + col_offset
        if 0 <= new_row < rows and 0 <= new_col < cols:  # Check if within bounds
            neighbours.append(grid[new_row][new_col])
        else:
            neighbours.append(None)  # Out of bounds
    return neighbours

def get_neighbours(x, y):
    return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}
