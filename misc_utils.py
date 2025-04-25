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

def validate_coordinates(x, y, grid):
    """
    Validates if the coordinate (x, y) is within the bounds of a 2D grid.

    Args:
        x (int): Row index (0-based).
        y (int): Column index (0-based).
        grid (list of lists): The 2D grid represented as a list of lists.

    Returns:
        bool: True if the coordinates are valid, False otherwise.
    """
    # Check if x is within the row bounds
    if x < 0 or x >= len(grid):
        return False
    
    # Check if y is within the column bounds for the given row
    if y < 0 or y >= len(grid[x]):
        return False
    
    return True

def get_neighbours(x, y):
    return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}

def get_neighbours_exclude_corners_and_middle(x, y):
    # Generate all neighbors excluding corners and middle
    return {
        (x + i, y + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i == 0 or j == 0) and not (i == 0 and j == 0)
    }

def get_corners(x, y):
    # Include only the diagonal corner neighbors
    return {
        (x - 1, y - 1),  # Top-left corner
        (x - 1, y + 1),  # Top-right corner
        (x + 1, y - 1),  # Bottom-left corner
        (x + 1, y + 1)   # Bottom-right corner
    }

# Example usage
print(get_corners(2, 3))

def get_surounding(x, y):
    # Generate all neighbors and exclude the middle point
    return {
        (x + i, y + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if not (i == 0 and j == 0)  # Exclude the middle point
    }

# Example usage
print(get_all_but_middle(2, 3))
