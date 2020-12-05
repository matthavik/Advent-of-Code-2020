# Originally solved it quite nicely - then decided to condense it down for fun. So I apologise that it's not the most
# readable solution, but it is at least ... short? Which is important I guess? Looks clever at least.

seats = [int(seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)for seat in open("input.txt").read().split("\n")]
print(f"Highest seat id: {max(seats)}")

your_seat = [x for x in range(min(seats), max(seats)) if x not in seats and x-1 in seats and x+1 in seats].pop()
print(f"Missing seat ID (yours!): {your_seat}")
