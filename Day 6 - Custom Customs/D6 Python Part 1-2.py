

# Part 1
total = sum([len(set("".join(group.split("\n")))) for group in open("input.txt").read().split("\n\n")])
print(f"[P1] Sum of counts: {total}")


# Part 2
total = sum([len(set.intersection(*[set(sub) for sub in group.split("\n")])) for group in open("input.txt").read().split("\n\n")])
print(f"[P2] Sum of counts: {total}")
