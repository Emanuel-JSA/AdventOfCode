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
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

def calculate_hand_type(hand):
    counts = [hand.count(card) for card in set(hand)]
    counts.sort(reverse=True)

    if counts == [5]:
        return 7  # Five of a kind
    elif counts == [4, 1]:
        return 6  # Four of a kind
    elif counts == [3, 2]:
        return 5  # Full house
    elif counts == [3, 1, 1]:
        return 4  # Three of a kind
    elif counts == [2, 2, 1]:
        return 3  # Two pair
    elif counts == [2, 1, 1, 1]:
        return 2  # One pair
    else:
        return 1  # High card

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