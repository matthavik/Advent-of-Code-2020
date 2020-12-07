# Not fast, or pretty, but took less lines than I thought it would take without using
# some fancy algorithm to solve it

import re

# Read file and strip new lines, split into parts [bag col, [inside cols]]
# pass inside cols through regex to extract colour only
bag_data = []
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n.").split("bags contain")
        line = [line[0].strip(" "), line[1].split(",")]
        for i, subline in enumerate(line[1]):
            if "no other bags" not in subline:
                line[1][i] = re.match(r"\s+\d{1,2} (\D+) bags?$", subline).groups()[0]
        bag_data.append(line)

possible_bags = ["shiny gold"]
while True:
    new_bags = False
    for bag in bag_data:
        for bag_name in possible_bags:
            if bag_name in bag[1] and bag[0] not in possible_bags:
                possible_bags.append(bag[0])
                new_bags = True
    if new_bags == False:
        break

print(f"[P1] Total bags: {len(possible_bags) - 1}")


# Read file and strip new lines, split into parts [bag col, [inside cols]]
# pass inside cols through regex to extract number and colour
bag_data = []
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n.").split("bags contain")
        line = [line[0].strip(" "), line[1].split(",")]
        for i, subline in enumerate(line[1]):
            if "no other bags" not in subline:
                matches = re.match(r"\s+(\d{1,2}) (\D+) bags?$", subline).groups()
                line[1][i] = [int(matches[0]), matches[1]]
        bag_data.append(line)

total_bags, bag_queue = 0, []
next_bags = ["shiny gold"]  # starting bag
while len(next_bags) != 0:
    for next_bag in next_bags:
        this_bag = [bag for bag in bag_data if bag[0] == next_bag][0]
        for subbag in this_bag[1]:
            if "no other bags" not in subbag:
                for i in range(subbag[0]):
                    bag_queue.append(subbag[1])
                    total_bags += 1

    next_bags = bag_queue.copy()
    bag_queue.clear()

print(f"[P2] Total bags: {total_bags}")
