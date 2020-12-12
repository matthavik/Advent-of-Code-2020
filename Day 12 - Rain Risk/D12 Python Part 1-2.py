import math
import time


def lengthdir(length, direction):
    rads = math.radians(direction)
    return(length * math.cos(rads), length * math.sin(rads))


def wrap(minimum, maximum, val):
    val = minimum + (val - minimum) % (maximum - minimum)
    return val


instructions = [(i[0], int(i[1:])) for i in open("input.txt").read().split("\n")]

# Part 1
start_time = time.time()
facing = x = y = 0

for instruction in instructions:

    code, mag = instruction

    if code == "F":
        step = lengthdir(1, facing * 90)
        while mag > 0:
            x += step[0]
            y += step[1]
            mag -= 1

    elif code == "N":
        while mag > 0:
            y -= 1
            mag -= 1

    elif code == "S":
        while mag > 0:
            y += 1
            mag -= 1

    elif code == "E":
        while mag > 0:
            x += 1
            mag -= 1

    elif code == "W":
        while mag > 0:
            x -= 1
            mag -= 1

    elif code == "R":
        facing = int(wrap(0, 4, facing + mag / 90))

    elif code == "L":
        facing = int(wrap(0, 4, facing - mag / 90))

print("[P1] Manhatten distance: {:d}            [{:3.4f}ms]".format(abs(int(x + y)), (time.time()-start_time)*1000))


# Part 2
start_time = time.time()
sfacing = sx = sy = wfacing = wx = wy = 0
wx = 10
wy = -1

for instruction in instructions:

    code, mag = instruction

    if code == "F":
        cx, cy = wx - sx, wy - sy
        sx, sy = sx + (cx * mag), sy + (cy * mag)
        wx, wy = wx + (cx * mag), wy + (cy * mag)

    elif code == "N":
        while mag > 0:
            wy -= 1
            mag -= 1

    elif code == "S":
        while mag > 0:
            wy += 1
            mag -= 1

    elif code == "E":
        while mag > 0:
            wx += 1
            mag -= 1

    elif code == "W":
        while mag > 0:
            wx -= 1
            mag -= 1

    elif code == "R":
        rotations = int(mag / 90)
        cx, cy = wx - sx, wy - sy
        while rotations > 0:
            cx, cy = cy * -1, cx
            rotations -= 1
        wx, wy = sx + cx, sy + cy

    elif code == "L":
        rotations = int(mag / 90)
        cx, cy = wx - sx, wy - sy
        while rotations > 0:
            cx, cy = cy, cx * -1
            rotations -= 1
        wx, wy = sx + cx, sy + cy

print("[P2] Manhatten distance: {:d}           [{:3.4f}ms]".format(int(abs(sx)+abs(sy)), (time.time()-start_time)*1000))
