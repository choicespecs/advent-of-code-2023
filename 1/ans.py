INPUT_FILE = "input.txt"

def part1():
    sum = 0
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            stk = []
            for char in line:
                if char.isdigit():
                    stk.append(char)
            if len(stk) > 1:
                first = stk[0]
                second = stk[-1]
                sum += int(first + second)
            elif len(stk) == 1:
                first = stk[0]
                second = stk[0]
                sum += int(first + second)
    return sum

def part2():
    hm = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    sum = 0
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            stk = []
            for i, char in enumerate(line):
                if char.isdigit():
                    stk.append(char)
                else:
                    if i < len(line) - 2 and line[i:i+3] in hm:
                        stk.append(hm[line[i:i+3]])
                    if i < len(line) - 3 and line[i:i+4] in hm:
                        stk.append(hm[line[i:i+4]])
                    if i < len(line) - 4 and line[i:i+5] in hm:
                        stk.append(hm[line[i:i+5]])
            if len(stk) > 1:
                first = stk[0]
                last = stk[-1]
                sum += int(first + last)
            elif len(stk) == 1:
                first = stk[0]
                last = stk[0]
                sum += int(first + last)
    return sum
