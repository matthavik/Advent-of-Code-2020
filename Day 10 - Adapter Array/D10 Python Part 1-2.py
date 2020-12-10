import time


# Part 1
joltages = [int(joltage) for joltage in open("input.txt").read().split("\n")]
start_time = time.time()
joltages.sort()
joltages.insert(0, 0)
joltages.append(max(joltages) + 3)
joltage_differences = [0, 0]

for i, joltage in enumerate(joltages):
    if joltage - joltages[i - 1] == 1:
        joltage_differences[0] += 1
    elif joltage - joltages[i - 1] == 3:
        joltage_differences[1] += 1

print("[P1] Required number: {:d}                             [{:3.8f}ms]".format((joltage_differences[0] * joltage_differences[1]), time.time()-start_time))


# Part 2
start_time = time.time()
joltages = sorted([int(joltage) for joltage in open("input.txt").read().split("\n")])
joltages.insert(0, 0)

joltage_map = {jolt: 0 for jolt in joltages}
joltage_map[0] = 1
total = 0

for joltage in joltages:
    for dif in [1, 2, 3]:
        if joltage + dif in joltages:
            joltage_map[joltage + dif] += joltage_map[joltage]
            total = joltage_map[joltage + dif]

print("[P2] Total distinct combinations: {:d}       [{:3.8f}ms]".format(total, (time.time()-start_time)*1000))
''
