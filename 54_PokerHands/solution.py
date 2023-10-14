card_values = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}


def log(msg):
    # print(msg)
    return


def royal_flush(cards):
    suite = cards[0][-1]
    for i, card in enumerate(cards):
        if card[-1] != suite:
            return 0
        if (card_value(card) != 9+i):
            return 0
    log(f"royal flush {14**14}")
    return 14**14


def straight_flush(cards):
    suite = cards[0][-1]
    for i, card in enumerate(cards):
        if card[-1] != suite:
            return 0
        if (card_value(card) != card_value(cards[0])+i):
            return 0
    log(f"straight flush {card_value(cards[0])*14**13}")
    return card_value(cards[0])*14**13


def four_of_a_kind(cards):
    card_counts = {}
    value = 0
    for card in cards:
        card_strength = card_value(card)
        if card_strength in card_counts:
            card_counts[card_strength] += 1
        else:
            card_counts[card_strength] = 1

    if 4 in card_counts.values():
        for card_strength, card_frequency in card_counts.items():
            if card_frequency == 4:
                value += card_strength*14**12
            else:
                value += card_strength
    if value != 0:
        log(f"4 of a kind {value}")
    return value


def full_house(cards):
    value = 0
    card_counts = {}
    for card in cards:
        if card_value(card) in card_counts:
            card_counts[card_value(card)] += 1
        else:
            card_counts[card_value(card)] = 1
    card_frequency = card_counts.values()
    if 2 in card_frequency and 3 in card_frequency:
        for card_strength, card_count in card_counts.items():
            if card_count == 3:
                value += card_strength*14**11
            else:
                value += card_strength
    if value != 0:
        log(f"full house {value}")
    return value


def flush(cards):
    card_counts = {}
    suite = cards[0][-1]
    value = 14**10
    sorted_cards_values = []
    for card in cards:
        if card[-1] != suite:
            return 0
        if card_value(card) in card_counts:
            card_counts[card_value(card)] += 1
        else:
            card_counts[card_value(card)] = 1
        sorted_cards_values.append(card_value(card))
    sorted_cards_values.sort()
    for i, strength in enumerate(sorted_cards_values):
        value += strength*14**i

    if value != 0:
        log(f"flush {value}")
    return value


def straight(cards):
    for i, card in enumerate(cards):
        if card_value(card) != card_value(cards[0])+i:
            return 0

    log(f"straight {card_value(cards[0])*14**9}")
    return card_value(cards[0])*14**9


def three_of_a_kind(cards):
    value = 0
    card_counts = {}
    single_cards_strength = []
    for card in cards:
        if card_value(card) in card_counts:
            card_counts[card_value(card)] += 1
        else:
            card_counts[card_value(card)] = 1

    if 3 in card_counts.values():
        for strength, count in card_counts.items():
            if count == 3:
                value += strength*14**8
            else:
                single_cards_strength.append(strength)

    single_cards_strength.sort()
    for i, strength in enumerate(single_cards_strength):
        value += strength*14**i

    if value != 0:
        log(f"three_of_a_kind {value}")
    return value


def two_pairs(cards):
    value = 0
    card_counts = {}
    pairs = []
    single_card_strength = 0
    for card in cards:
        if card_value(card) in card_counts:
            card_counts[card_value(card)] += 1
        else:
            card_counts[card_value(card)] = 1

    for strength, count in card_counts.items():
        if count == 2:
            pairs.append(strength)
        else:
            single_card_strength += strength

    if (len(pairs) == 2):
        pairs.sort()
        value += pairs[0]*14**6+pairs[1]*14**7+single_card_strength

    if value != 0:
        log(f"two_pairs {value}")
    return value


def one_pair(cards):
    value = 0
    card_counts = {}
    single_cards_strength = []
    pairs = []
    for card in cards:
        if card_value(card) in card_counts:
            card_counts[card_value(card)] += 1
        else:
            card_counts[card_value(card)] = 1

    for strength, count in card_counts.items():
        if count == 2:
            pairs.append(strength)
        if count == 1:
            single_cards_strength.append(strength)

    if (len(pairs) == 1 and len(single_cards_strength) == 3):
        value += pairs[0]*14**5
        single_cards_strength.sort()
        for i, strength in enumerate(single_cards_strength):
            value += strength*14**i

    if value != 0:
        log(f"one_pair {value}")
    return value


def high_card(cards):
    value = 0
    card_counts = {}
    for card in cards:
        if card_value(card) in card_counts:
            card_counts[card_value(card)] += 1
        else:
            card_counts[card_value(card)] = 1

    if len(card_counts.keys()) == 5:
        values = list(card_counts.keys())
        values.sort()
        for i, v in enumerate(values):
            value += v*14**i

    if value != 0:
        log(f"high_card {value}")
    return value


def highest_card(cards):
    max_value = 0
    for card in cards:
        if max_value < card_value(card):
            max_value = card_value(card)
    return max_value


def hand_value(cards: list[str]):
    cards.sort(key=card_value)
    value = 0
    rank_functions = [royal_flush, straight_flush, four_of_a_kind,
                      full_house, flush, straight, three_of_a_kind,
                      two_pairs, one_pair, high_card]
    for rank_function in rank_functions:
        value = rank_function(cards)
        if value != 0:
            return value


def card_value(card):
    return card_values[card[0:-1]]


player1_wins = 0
player2_wins = 0
f = open("poker.txt", "r",)
for line in f:
    line = line.strip("\n").split(" ")
    player1_hand = line[:5]
    player2_hand = line[5:10]
    # print(player1_hand, " # ", player2_hand)
    if hand_value(player1_hand) > hand_value(player2_hand):
        player1_wins += 1
        # print("player1 won")
    else:
        player2_wins += 1
        # print("player2 won")
f.close()

print(f"Player1 won {player1_wins} times. Player2: {player2_wins}")


# tests
# print(hand_value(['TD', 'JD', 'QD', 'KD', 'AD']))  # royal_flush
# print(hand_value(['TD', 'JD', 'TD', 'KD', 'AD']))  # flush
# print(hand_value(['TD', 'JH', 'QS', 'KD', 'AD']))  # straight
# print(hand_value(['6D', '6H', '6S', '2C', 'JD']))  # 3
# print(hand_value(['5D', '6H', '7S', '8C', '9D']))  # straight
# print(hand_value(['6H', '7H', '8H', '9H', 'TH']))  # straight flush
# print(hand_value(['8D', '8H', '8S', '8C', 'KD']))  # 4
# print(hand_value(['9D', '9H', '9S', '3C', '3D']))  # full
# print(hand_value(['4D', '4H', '7S', '7C', 'QS']))  # 2 pairs
# print(hand_value(['2H', '2D', '8S', '9C', 'KS']))  # 1 pair
# print(hand_value(['AD', 'KH', '7S', 'TC', 'QD']))  # high
