from itertools import combinations
from math import prod


def day1_func(_numbers, _n):
    for vals in combinations(_numbers, _n):
        if sum(vals, 0) == 2020:
            return prod(vals)


with open("input.txt") as file:
    numbers = [int(line.rstrip("\n")) for line in file]

print(f"Part 1: {day1_func( numbers, 2)}")
print(f"Part 2: {day1_func( numbers, 3)}")
