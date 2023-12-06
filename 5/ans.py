INPUT_FILE = "input.txt"

def part1():
    ## Assigns first value to seeds and remaining values to blocks
    seeds, *blocks = open(INPUT_FILE).read().split("\n\n")

    seeds = list(map(int,seeds.split(":")[1].split()))


    for block in blocks:
        ranges = []
        ## Splits line based on \n
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for x in seeds:
            for a, b, c in ranges:
                if b <= x < b + c:
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new
    return min(seeds)

def part2():
    inputs, *blocks = open(INPUT_FILE).read().split("\n\n")

    inputs = list(map(int,inputs.split(":")[1].split()))

    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        ## Splits line based on \n
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while seeds:
            s, e = seeds.pop()
            for a,b,c in ranges:
                os = max(s,b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))
        seeds = new
    return min(seeds)
