# Not fast, just pure brute force power!

import numpy as np
import time
import math

with open("input.txt") as file:
    data = file.read()

data = [list(line) for line in open("input.txt").read().split("\n")]
width = len(data[0])
height = len(data)
base_array = np.array(data)
dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

# Part 1
sarray = base_array.copy()


def occupied_adj(xx, yy, grid):
    if 0 <= xx < grid.shape[0] and 0 <= yy < grid.shape[1]:
        if grid[xx, yy] == "#":
            return True
    return False


def run_adj(sarray):

    while True:
        changes = False
        uarray = sarray.copy()
        for xx in range(uarray.shape[0]):
            for yy in range(uarray.shape[1]):

                occupied = 0
                for i in range(8):
                    movement = dirs[i]
                    if occupied_adj(xx + movement[0], yy + movement[1], sarray):
                        occupied += 1

                if sarray[xx, yy] == "L" and occupied == 0:
                    uarray[xx, yy] = "#"
                    changes = True
                elif sarray[xx, yy] == "#" and occupied >= 4:
                    uarray[xx, yy] = "L"
                    changes = True

        if changes == False:
            return sarray

        sarray = uarray.copy()


start_time = time.time()
val = (run_adj(sarray) == "#").sum()
print("[P1] Occupied seats: {:d}            [{:3.4f}ms]".format(val, (time.time() - start_time) * 1000))


# Part 2
sarray = base_array.copy()


def occupied_vis(xx, dx, yy, dy, grid):
    while(0 <= xx + dx < grid.shape[0] and 0 <= yy + dy < grid.shape[1]):
        xx += dx
        yy += dy
        if grid[xx, yy] == "#":
            return True
        if grid[xx, yy] == "L":
            return False
    return False


def run_vis(sarray):

    while True:
        changes = False
        uarray = sarray.copy()
        for xx in range(uarray.shape[0]):
            for yy in range(uarray.shape[1]):

                occupied = 0
                for i in range(8):
                    movement = dirs[i]
                    if occupied_vis(xx, movement[0], yy, movement[1], sarray):
                        occupied += 1

                if sarray[xx, yy] == "L" and occupied == 0:
                    uarray[xx, yy] = "#"
                    changes = True
                elif sarray[xx, yy] == "#" and occupied >= 5:
                    uarray[xx, yy] = "L"
                    changes = True

        if changes == False:
            return sarray

        sarray = uarray.copy()


start_time = time.time()
val = (run_vis(sarray) == "#").sum()
print("[P2] Occupied seats: {:d}            [{:3.4f}ms]".format(val, (time.time() - start_time) * 1000))
