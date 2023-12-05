# input_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

with open('F:\\Projects\\AdventOfCode\\day04_Scratchcards\\data.txt', 'r') as file:
    input_data = file.read()

separete_lines = input_data.splitlines()
game_lines = [line.split(":")[1].strip() for line in separete_lines]
game_cards = [card.split("|") for card in game_lines]
cards = [[card.strip().split(" ") for card in card] for card in game_cards]
score = 0

for game in cards:
    winning_cards = len(list(set(game[0]).intersection(game[1])))
    print(winning_cards)
    if winning_cards > 0:
        score += 2**(winning_cards-1)

print(score)