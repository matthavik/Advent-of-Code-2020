

import re


# Part 1
with open("input.txt") as file:
    passports = file.read().split("\n\n")

total_valid = 0
for passport in passports:
    if sum(map(passport.count, ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))) >= 7:
        total_valid += 1

print(f"P1 Valid Passports: {total_valid}")


# Part 2
with open("input.txt") as file:
    passports = file.read().split("\n\n")

passports = [re.split("\n| ", passport) for passport in passports]

valid = 0
for passport in passports:

    kv = dict(kv.split(":") for kv in passport)  # Split into key/value pairs
    vc = 0  # Total passed validation checks

    vc = vc + 1 if "byr" in kv and len(kv["byr"]) == 4 and 1920 <= int(kv["byr"]) <= 2002 else vc
    vc = vc + 1 if "iyr" in kv and len(kv["iyr"]) == 4 and 2010 <= int(kv["iyr"]) <= 2020 else vc
    vc = vc + 1 if "eyr" in kv and len(kv["eyr"]) == 4 and 2020 <= int(kv["eyr"]) <= 2030 else vc

    if "hgt" in kv:
        vc = vc + 1 if kv["hgt"][-2:] == "cm" and 150 <= int(kv["hgt"][:-2]) <= 193 else vc
        vc = vc + 1 if kv["hgt"][-2:] == "in" and 59 <= int(kv["hgt"][:-2]) <= 76 else vc

    vc = vc + 1 if "hcl" in kv and kv["hcl"][0] == "#" and sum(map(kv["hcl"][1:].count, "abcdef")) + \
        sum(map(kv["hcl"][1:].count, "0123456789")) == 6 else vc

    vc = vc + 1 if "ecl" in kv and kv["ecl"] in "ambblubrngrygrnhzloth" else vc
    vc = vc + 1 if "pid" in kv and kv["pid"].isnumeric() and len(kv["pid"]) == 9 else vc

    valid = valid + 1 if vc >= 7 else valid

print(f"P2 Valid Passports: {valid}")
