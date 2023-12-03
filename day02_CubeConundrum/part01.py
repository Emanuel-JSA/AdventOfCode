# input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """

with open('data.txt', 'r') as file:
    input_data = file.read()

test_data = {'red': 12, 'green': 13, 'blue': 14}

input_lines = input_data.splitlines()
filtered_lines = []

for line in input_lines:
    game_string = line.split(':')[1].strip()
    color_used = {}

    parts = game_string.split(';')

    for part in parts:
        words = part.split(',')
        
        for word in words:
            number, color = word.strip().split()
            number = int(number)
            
            if color not in color_used:
                color_used[color] = []
            color_used[color].append(number)
    filtered_lines.append(color_used)

def test_if_game_is_valid(game):
    for color in game:
        for color_count in game[color]:
            if color_count > test_data[color]:
                return False
    return True

game_id = 1
game_id_sum = 0
for game in filtered_lines:
    if test_if_game_is_valid(game):
        game_id_sum += game_id
    game_id += 1

print(game_id_sum)
