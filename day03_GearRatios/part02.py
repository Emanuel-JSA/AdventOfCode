from functools import reduce

# input_data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

with open('data.txt', 'r') as file:
    input_data = file.read()

temp_lines = input_data.splitlines()
lines = [list(line) for line in temp_lines]

Coord = tuple[int,int]

def get_gear_pos(lines):
    gear_pos = []

    for i, line in enumerate(lines):
        for j, item in enumerate(line):
            if item == "*":
                gear_pos.append([i, j])
                
    return gear_pos

def walker_constructor(x, y, lines):
    number_to_right = ''
    number_to_left = ''
    initial_y = y

    # Construir o número à direita do ponto de partida
    i = 1
    while y + i < len(lines[x]) and lines[x][y + i].isdigit():
        number_to_right += str(lines[x][y + i])
        i += 1

    # Construir o número à esquerda do ponto de partida
    i = 1
    while y - i >= 0 and lines[x][y - i].isdigit():
        number_to_left = str(lines[x][y - i]) + number_to_left
        initial_y -= 1
        i += 1


    whole_number = int(number_to_left + lines[x][y] + number_to_right)
    return (x, initial_y), whole_number


def find_gears(lines, gear_pos):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    gear_part = []

    for i in gear_pos:
        numbers_found = {}
        for dx, dy in directions:
            x, y = i[0] + dx, i[1] + dy
            if lines[x][y].isdigit():
                coords, number = walker_constructor(x, y, lines)
                if coords not in numbers_found:  
                    numbers_found[coords] = (number)
        if numbers_found.__len__() > 1:
            temp_gear_parts = list(numbers_found.values())
            gear_part.append(reduce(lambda x, y: x*y, temp_gear_parts)) 

    return gear_part
        

gear_pos = get_gear_pos(lines)
gear_ratios = find_gears(lines, gear_pos)

print(sum(gear_ratios))
