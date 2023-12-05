INPUT_FILE = "input.txt"

def part1():
    totals = 0
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            line = line.split(':')[1]
            nums = line.split('|')

            winners = nums[0].strip()
            winners = winners.split()
            winners = set(winners)

            compare = nums[1].strip()
            compare = compare.split()

            winner_count = 0
            for val in compare:
                if val in winners:
                    winner_count += 1

            if winner_count > 0:
                totals += pow(2, (winner_count - 1))

    return totals

def part2():
    cards = 0
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            cards += 1
    scratchcards = [1 for i in range(cards)]
    with open(INPUT_FILE, 'r') as file:
        for i, line in enumerate(file):
            line = line.split(':')[1]
            nums = line.split('|')

            winners = nums[0].strip()
            winners = winners.split()
            winners = set(winners)

            compare = nums[1].strip()
            compare = compare.split()
            winner_count = 0
            for val in compare:
                if val in winners:
                    winner_count += 1
            for j in range(winner_count):
                scratchcards[i + (j + 1)] += scratchcards[i]
    return sum(scratchcards)