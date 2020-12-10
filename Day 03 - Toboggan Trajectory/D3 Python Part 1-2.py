# Maybe more condensed than it needs to be... but it was fun! Tried two different methods

# Part 1 - using a generator!
def mountain_line():
    count = -3
    for line in open("input.txt"):
        count = (count + 3) % (len(line) - 1)
        yield line[count]


mountain_gen = mountain_line()
trees = sum(char == "#" for char in mountain_gen)
print(f"P1 Trees: {trees}")


# Part 2 - using ... generator comprehension and for loops!
with open("input.txt") as file:
    mountain = file.read()
height = mountain.count("\n") + 1
mountain = mountain.replace("\n", "")
width = int(len(mountain) / height)


trees, trees_multiple, attempts = 0, 1, [1, 1, 3, 1, 5, 1, 7, 1, 1, 2]
for i in range(0, len(attempts), 2):
    for x, y in zip((x % width for x in range(0, len(mountain), attempts[i])), range(0, height, attempts[i + 1])):
        trees = trees + 1 if mountain[x + width * y] == "#" else trees
    trees_multiple, trees = trees_multiple * trees, 0

print(f"P2 Trees: {trees_multiple}")
