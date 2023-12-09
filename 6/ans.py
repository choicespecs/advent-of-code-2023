
def part1():
    time,distance = open('input.txt').read().split("\n")

    time = time.split(':')[1]
    distance = distance.split(':')[1]

    time = list(map(int, time.split()))
    distance = list(map(int, distance.split()))

    n = len(time)

    ans = 1
    for i in range(n):
        num_ways = 0
        time_compare = time[i]
        distance_compare = distance[i]
        for i in range(1, time_compare - 1):
            rem = time_compare - i
            if rem * i > distance_compare:
                num_ways += 1
        ans *= num_ways
    return ans

def part2():
    time,distance = open('input.txt').read().split("\n")
    time = time.split(':')[1]
    time = time.split()
    distance = distance.split(':')[1]
    distance = distance.split()
    final_time = ""
    final_distance = ""
    for t in time:
        final_time += t
    for d in distance:
        final_distance += d
    final_time = int(final_time)
    final_distance = int(final_distance)
    ways = 0
    for i in range(1, final_time - 1):
        rem = final_time - i
        if rem * i > final_distance:
            ways += 1
    return ways