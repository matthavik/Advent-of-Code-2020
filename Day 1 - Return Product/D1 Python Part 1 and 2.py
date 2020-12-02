from itertools import combinations
from math import prod

# DAY 1

def day1_func(_numbers, _n):
    for vals in combinations(_numbers, _n):
        if sum(vals, 0) == 2020:
            return prod(vals)


with open("C:\\Python\AdventofCode\Day1\input.txt") as file:
    numbers = [int(line.rstrip("\n")) for line in file]

print(f"Part 1: {day1_func( numbers, 2)}")
print(f"Part 2: {day1_func( numbers, 3)}")
