import math
from collections import defaultdict

def part1():

    values, *nodes = open('input.txt').read().split("\n")
    nodes = list(filter(None, nodes))

    graph = defaultdict(list)
    for node in nodes:
        val = node.split('=')
        clean_node = val[0].strip()
        clean_string = val[1].strip()
        clean_string = clean_string[1:-1]
        left_right = [element.strip() for element in clean_string.split(",")]
        graph[clean_node] = [left_right[0], left_right[1]]

    start = 'AAA'
    count = 0

    while start != 'ZZZ':
        step = values[count % len(values)]
        if step == "L":
            start = graph[start][0]
        elif step == "R":
            start = graph[start][1]
        count += 1
    return count
def part2():

    values, *nodes = open('input.txt').read().split("\n")
    nodes = list(filter(None, nodes))

    graph = defaultdict(list)
    for node in nodes:
        val = node.split('=')
        clean_node = val[0].strip()
        clean_string = val[1].strip()
        clean_string = clean_string[1:-1]
        left_right = [element.strip() for element in clean_string.split(",")]
        graph[clean_node] = [left_right[0], left_right[1]]

    def n_steps(curr):
        count = 0
        while curr[-1] != "Z":
            step = values[count % len(values)]
            if step == "L":
                curr = graph[curr][0]
            elif step == "R":
                curr = graph[curr][1]
            count += 1
        return count

    start_nodes = set(node for node in graph if node[-1] == "A")
    paths = [n_steps(node) for node in start_nodes]
    ans = math.lcm(*paths)
    return ans
