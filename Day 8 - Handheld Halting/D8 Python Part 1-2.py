# Can definitely make this faster with some nice recursive solution, but it's not that slow!

import time
import sys


inputs = []
with open("input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        inputs.append([line[0], int(line[1])])

# Part 1
start_time = time.time()
acc, ind, com = 0, 0, {}
while ind not in com:
    com[ind] = True
    command, param = inputs[ind]
    if command == "acc":
        acc += param
        ind += 1
    elif command == "jmp":
        ind += param
    elif command == "nop":
        ind += 1

print("[P1] Value {:4d}           [{:3.4f}ms]".format(acc, (time.time() - start_time)*1000))


# Part 2
start_time = time.time()


def acccomp(cinput):
    acc, ind, count = 0, 0, 0
    while count < len(cinput) and ind < len(cinput):
        command, param = cinput[ind]
        if command == "acc":
            acc += param
            ind += 1
        elif command == "jmp":
            ind += param
        elif command == "nop":
            ind += 1
        count += 1

    if ind >= len(cinput):
        print("[P2] Value {:4d}           [{:3.4f}ms]".format(acc, (time.time() - start_time)*1000))
        sys.exit()


for i, instruction in enumerate(inputs):
    command, param = instruction
    if command == "jmp":
        new_input = inputs.copy()
        new_input[i] = ["nop", param]
        acccomp(new_input)
    elif command == "nop":
        new_input = inputs.copy()
        new_input[i] = ["jmp", param]
        acccomp(new_input)
