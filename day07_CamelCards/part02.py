# input_data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

with open('data.txt', 'r') as file:
    input_data = file.read()

hands = input_data.split('\n')
hands = [hand.split(' ') for hand in hands]

card_values = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

def calculate_hand_type(hand):
    uniques = list(set(hand))
    num_unique_cards = len(uniques)

    if 'J' in hand and num_unique_cards != 1:
        most_common_card = max(hand.replace("J",""), key=lambda card: hand.count(card))
        hand = hand.replace("J",most_common_card)
        uniques = list(set(hand))
        num_unique_cards -= 1

    if num_unique_cards == 1:
        return 7
    if num_unique_cards == 2:
        countUnique = hand.count(uniques[0])
        if countUnique == 1 or countUnique == 4:
            return 6
        return 5
    if num_unique_cards == 3:
        structure = sorted([hand.count(uniques[i]) for i in range(3)])
        if structure == [1,1,3]:
            return 4
        return 3
    if num_unique_cards == 4:
        return 2
    return 1

def calculate_hand_strength(hand):
    hand = hand[0]
    total = 0
    for i, card in enumerate(hand[::-1]):
        # add the value of the card to the total, multiplied by 16 to the power of its position
        total += card_values[card] * (22**i)
    total += calculate_hand_type(hand) * (22**5)
    return total

ranked_hands = sorted(hands, key=lambda hand: calculate_hand_strength(hand))

total_winnings = 0

for i, hand in enumerate(ranked_hands):
    total_winnings += int(hand[1]) * (i + 1)

print(total_winnings)