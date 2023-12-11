pipe_directions = {
    "|": [(0, -1), (0, 1)],  # north, south
    "-": [(-1, 0), (1, 0)],  # west, east
    "L": [(0, -1), (1, 0)],  # north, east
    "J": [(0, -1), (-1, 0)],  # north, west
    "7": [(0, 1), (-1, 0)],  # south, west
    "F": [(0, 1), (1, 0)],  # south, east
}

with open('data.txt', 'r') as file:
    input_data = file.read()

# input_data = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ"""

grid = [list(row) for row in input_data.split("\n")]

start = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'S'][0]

def get_connections(x, y, grid):
    c = grid[y][x]
    if c in pipe_directions:
        return [(x + dx, y + dy) for dx, dy in pipe_directions[c]]
    return []

positions = [start]
seen = set()

while positions:
    next_positions = set()
    for x, y in positions:
        if (x, y) not in seen:
            seen.add((x, y))
            for nx, ny in get_connections(x, y, grid):
                if (nx, ny) not in seen and 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    next_positions.add((nx, ny))
    positions = next_positions

print(int(len(seen)/2))