# Maybe more condensed than it needs to be... but it was fun! Tried two different methods

# Part 1
def mountain_line():
    count = -3
    for line in open("input.txt"):
        count = (count + 3) % (len(line) - 1)
        yield line[count]


mountain_gen = mountain_line()
trees = sum(char == "#" for char in mountain_gen)
print(f"P1 Trees: {trees}")


# Part 2
with open("input copy.txt") as file:
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


# Part 2 method 2

# trees = 0
# for x, y in zip((x % width for x in range(0, len(mountain), 3)), range(0, height, 1)):
#     trees = trees + 1 if mountain[x + width * y] == "#" else trees

# print(f"P1 Trees: {trees}")
# class mountain_line:

#     x = 0
#     y = 0
#     xc = 1
#     yc = 1
#     with open("input.txt") as file:
#         lines = file.readlines()
#     w = len(lines[0])

#     def __init__(self, xc="1", xy="1"):
#         self.xc = xc
#         self.yc = xy

#     def data(self):
#         print(f"X: {self.x} Y: {self.y} XC: {self.xc} YC: {self.yc}")

#     def __iter__(self):
#         char = self.lines[self.y][self.x + self.y * self.w]
#         self.x = (self.x + self.xc) % self.w
#         self.y += self.yc
#         yield char


# gen1 = mountain_line(3, 1)
# for val in range(10):
#     print(next(gen1))

# def mountain_line(_x, _y):
#     x, y, xc, yc = _x, _y, 0, 0
#     with open("input.txt") as file:
#         lines = file.readlines()

#     for line in lines if:  # open("input.txt"):
#         count = (count + x) % (len(line) - 1)
#         yield line[count]


# mountain_gen = mountain_line(3, 1)
# trees = sum(char == "#" for char in mountain_gen)
# print(f"Trees: {trees}")


# def mountain_line():
#     count = -3
#     for line in open("input.txt"):
#         count = (count + 3) % (len(line) - 1)
#         yield line[count]

# mountain_gen = mountain_line()
# trees = sum(char == "#" for char in mountain_gen)
# print(f"Trees: {trees}")


#
# for i in range(10):
#    print(next(mountain_gen))


# mountain = []
# with open("input.txt") as file:
#     for line in file:
#         mountain.append(line)

#     mountain = file.read()
# height = mountain.count("\n") + 1
# mountain = mountain.replace("\n", "")
# width = int(len(mountain) / height)


# width = 11
# gen_test = (x % width for x in range(0, 100, 3))
# count = 10
# while(count > 0):
#     print(next(gen_test))
#     count -= 1
