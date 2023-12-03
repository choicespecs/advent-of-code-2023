INPUT_FILE = "input.txt"
hm = {
    "red": 12,
    "green": 13,
    "blue": 14
}

cols = ["red", "green", "blue"]

def part1():
    ids = []
    id = 1
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            possible = True
            line = line.split(':')[1]
            sets = line.split(';')
            for set in sets:
                compare = {"red" : 0, "green": 0, "blue": 0}
                set_cols = set.split(',')
                for col in set_cols:
                    single_col = col.split()
                    compare[single_col[1]] += int(single_col[0])
                for k, v in compare.items():
                    if compare[k] > hm[k]:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                ids.append(id)
            id += 1
    return sum(ids)
