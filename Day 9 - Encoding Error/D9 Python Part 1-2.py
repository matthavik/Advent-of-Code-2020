import itertools
import time

number_input = [int(number.strip()) for number in open("input.txt").readlines()]


def unloved_number(numbers):
    for i, number in enumerate(numbers[:-1]):
        if i >= 25:
            combinations = itertools.combinations(numbers[:i], 2)
            result = [sum(pair) for pair in combinations if sum(pair) == number]
            if len(result) == 0:
                return number


start_time = time.time()
print("[P1] I ain't got a pair! {:8d}         [{:3.4f}ms]".format(unloved_number(number_input), (time.time() - start_time)*1000))


# Part 2
def gimme_nums(numbers, target, low=0, high=1):
    test = numbers[low] + numbers[high]
    while test != target:
        if test < target:
            high += 1
            test += numbers[high]
        else:
            test -= numbers[low]
            low += 1
    return min(numbers[low:high + 1]) + max(numbers[low:high + 1])


required_number = 41682220
start_time = time.time()
print("[P2] I found the number! {:8d}         [{:3.4f}ms]".format(gimme_nums(number_input, required_number), (time.time() - start_time)*1000))
