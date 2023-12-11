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

input_data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

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

loop_positions = seen

def is_valid_position(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def flood_fill(x, y, grid, seen):
    if not is_valid_position(x, y, grid) or (x, y) in seen:
        return
    seen.add((x, y))
    flood_fill(x + 1, y, grid, seen)
    flood_fill(x - 1, y, grid, seen)
    flood_fill(x, y + 1, grid, seen)
    flood_fill(x, y - 1, grid, seen)

def is_unseen(x, y, seen):
    return (x, y) not in seen

def count_inside_loop_tiles(grid, loop_positions):
    flood_seen = set()
    flood_fill(0, 0, grid, flood_seen)
    return sum(1 for y in range(len(grid)) for x in range(len(grid[y])) 
               if is_valid_position(x, y, grid) and is_unseen(x, y, flood_seen) and (x, y) not in loop_positions)

inside_loop_count = count_inside_loop_tiles(grid, loop_positions)
print(inside_loop_count)