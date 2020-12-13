import re
import time


data = [line for line in open("input.txt").read().split("\n")]

# Part 1
start_time = time.time()
earliest = int(data[0])
busses = [int(val) for val in re.findall(r"(\d+)", data[1])]

best_bus = wait_time = earliest
for bus in busses:
    btime = 0
    while btime < earliest:
        btime += bus
    if btime - earliest < wait_time:
        best_bus = bus
        wait_time = btime - earliest

print("[P1] Bus: {:d}, Wait time: {:d}, Result: {:d}            [{:3.6f}ms]".format(
    best_bus, wait_time, best_bus * wait_time, ((time.time()-start_time)*1000)/2))


# Part 2
start_time = time.time()
busses = [line for line in re.split(r"\n|,", open("input.txt").read())][1:]
# read input file, split on new lines and commas. Then only take entries past the 1st (aka cut the earliest time)

new_busses = [(0, int(busses[i]), i) for i in range(len(busses)) if busses[i] != "x"]
# create a list of tuples, each one containing
# ( start offset (0 for now - we create that in the loop below), the bus id, the required difference)

this_bus = new_busses[0]
for next_bus in new_busses:

    looped = done = False
    offset = this_bus[0]  # current start offset
    difference = next_bus[2] - this_bus[2]
    # difference between the two busses. If first bus should be leaving
    # in 9th place and other at 11th place, dif is 2

    while done == False:

        if (offset + difference) % next_bus[1] == 0:
            # if the offset (that we're calculating) + the difference divides into the
            # bus id of the next bus, we have an alignment of the busses!

            if looped == False:  # This is only the first match, we need to find two!
                looped = offset  # set our starting point/time
            else:  # This is our second match! Now we know the interval and can create our new combined bus
                done = True
                this_bus = (looped, offset - looped, this_bus[2])
                # looped is the first time they meet, aka our start time
                # offset - looped is the interval time, they'll meet each time this time passes!
                # this_bus[2] is the difference. We matched the times to the first bus, so we can pass its
                # difference over (basically we're just passing '0' up the chain, but it's clearer having the bus there)

        offset += this_bus[1]  # increase offset by the bus id

# So the answer is just the start time of the last bus (aka our combined mega bus that is actually all busses in one!)
print("[P2] Earliest Timestamp: {:d}            [{:3.6f}ms]".format(this_bus[0], (time.time()-start_time)*1000))
