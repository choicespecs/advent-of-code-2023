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

        # Find the card with the highest count, excluding J
        max_count_card = None
        max_count = 0
        for card in set(hand) - {"J"}:
            count = hand.count(card)
            if count > max_count:
                max_count = count
                max_count_card = card

        # If there is a J, replace it with the card with the highest count
        if "J" in hand and max_count_card is not None:
            return [hand.replace("J", max_count_card)]

        # No replacements needed
        return [hand]
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
    