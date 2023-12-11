def part1():
    letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

    def classify(hand):
        counts = [hand.count(card) for card in hand]

        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0


    def strength(hand):
        return (classify(hand), [letter_map.get(card, card) for card in hand])

    plays = []

    with open("input.txt", 'r') as file:
        for line in file:
            hand, bid = line.split()
            plays.append((hand,int(bid)))

    plays.sort(key = lambda play: strength(play[0]))

    total = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid

    return total

def part2():
    # Map J to the lowest possible value even lower than "0" which can be "."
    letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

    def score(hand):
        counts = [hand.count(card) for card in hand]

        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def replacements(hand):
        if hand == "":
            return [""]

        # Check if there are 5 J's in the hand
        if hand.count("J") == 5:
            return [hand]

        # If there is a J, replace it with the card with the highest count
        if "J" in hand:
            max_count_card = max(set(hand) - {"J"}, key=lambda card: hand.count(card))
            replaced_hand = hand.replace("J", max_count_card)
            return [replaced_hand]

        return [x + y for x in hand[0] for y in replacements(hand[1:])]
    def classify(hand):
        return max(map(score, replacements(hand)))

    def strength(hand):
        return (classify(hand), [letter_map.get(card, card) for card in hand])

    plays = []
    with open("input.txt", 'r') as file:
        for line in file:
            hand, bid = line.split()
            plays.append((hand,int(bid)))

    plays.sort(key = lambda play: strength(play[0]))

    total = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid

    return total

print(part2())
    