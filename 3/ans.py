INPUT_FILE="input.txt"

with open(INPUT_FILE, 'r') as file:
    data = file.read()
    lines = data.strip().split("\n")

x = len(lines)
y = len(lines[0])

def part1():
    def is_symbol(i, j):
        if i < 0 or i >= x:
            return False
        if j < 0 or j >= y:
            return False

        return lines[i][j] != '.' and not lines[i][j].isdigit()

    ans = 0
    for i, line in enumerate(lines):
        j = 0
        while j < y:
            start = j
            num = ""
            while j < y and line[j].isdigit():
                num += line[j]
                j += 1
            if num == "":
                j += 1
                continue
            num = int(num)

            if is_symbol(i, start - 1) or is_symbol(i, j):
                ans += num
                continue

            for k in range(start - 1, j + 1):
                if is_symbol(i - 1, k) or is_symbol(i + 1, k):
                    ans += num
                    break
    return ans

def part2():
    gears = [[[] for _ in range(y)] for _ in range(x)]

    def is_symbol(i, j, num):
        if i < 0 or i >= x:
            return False
        if j < 0 or j >= y:
            return False

        if lines[i][j] == "*":
            gears[i][j].append(num)
        return lines[i][j] != "." and not lines[i][j].isdigit()

    ans = 0
    for i, line in enumerate(lines):
        j = 0

        while j < y:
            start = j
            num = ""
            while j < y and line[j].isdigit():
                num += line[j]
                j += 1

            if num == "":
                j += 1
                continue

            num = int(num)

            is_symbol(i, start-1, num) or is_symbol(i, j, num)

            for k in range(start - 1, j + 1):
                is_symbol(i - 1, k, num) or is_symbol(i + 1, k, num)

    for i in range(x):
        for j in range(y):
            nums = gears[i][j]
            if lines[i][j] == "*" and len(nums) == 2:
                ans += nums[0] * nums[1]

    return ans

print(part2())