import re


p1_valid = 0
p2_valid = 0
password_match = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

with open("input.txt") as file:
    for string in file:
        num1, num2, letter, password = password_match.match(string).groups()

        # Part 1
        if int(num1) <= password.count(letter) <= int(num2):
            p1_valid += 1

        # Part 2
        if (password[int(num1) - 1] == letter) != (password[int(num2) - 1] == letter):
            p2_valid += 1

print(f"Part 1: {p1_valid} valid passwords!")
print(f"Part 2: {p2_valid} valid passwords!")
