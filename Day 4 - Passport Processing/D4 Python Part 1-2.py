

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


#

#

#

# # Part 2
# with open("input.txt") as file:
#     passports = file.read().split("\n\n")

# passports = [re.split("\n| ", passport) for passport in passports]

# valid = 0
# for passport in passports:

#     kv = dict(kv.split(":") for kv in passport)  # Split into key/value pairs
#     checks = 0  # Total passed validation checks

#     if "byr" in kv:
#         byr = kv["byr"]
#         if len(byr) == 4 and 1920 <= int(byr) <= 2002:
#             checks += 1
#             valid_births += 1

#     if "iyr" in kv:
#         iyr = kv["iyr"]
#         if len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
#             checks += 1
#             valid_years += 1

#     if "eyr" in kv:
#         eyr = kv["eyr"]
#         if len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
#             checks += 1
#             valid_eyears += 1

#     if "hgt" in kv:
#         hgt = kv["hgt"]
#         if hgt[-2:] == "cm":
#             hgt = int(hgt[:-2])
#             if 150 <= hgt <= 193:
#                 checks += 1
#                 valid_heights += 1
#         elif hgt[-2:] == "in":
#             hgt = int(hgt[:-2])
#             if 59 <= hgt <= 76:
#                 checks += 1
#                 valid_heights += 1

#     if "hcl" in kv:
#         hcl = kv["hcl"]
#         if hcl[0] == "#":
#             hcl = hcl[1:]
#             if sum(map(hcl.count, "abcdef")) + sum(map(hcl.count, "0123456789")) == 6:
#                 checks += 1
#                 valid_haircols += 1

#     if "ecl" in kv:
#         ecl = kv["ecl"]
#         if ecl in "ambblubrngrygrnhzloth":
#             checks += 1
#             valid_eyecol += 1

#     if "pid" in kv:
#         pid = kv["pid"]
#         if pid.isnumeric() and len(pid) == 9:
#             checks += 1
#             valid_pids += 1

#     if checks >= 7:
#         valid += 1

# print(valid)


# valid = 0
# births = 0
# for passport in passports:
#     checks = 0
#     passport = dict(kv.split(":") for kv in passport)
#     if "byr" in passport:
#         #checks = checks + 1 if (len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002) else checks
#         if (len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002):
#             checks += 1
#             births += 1
#     if "iyr" in passport:
#         checks = checks + 1 if (len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020) else checks
#     if "eyr" in passport:
#         checks = checks + 1 if (len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030) else checks
#     if "hgt" in passport:
#         height = re.split("(cm)|(in)", passport["hgt"])
#         if "cm" in height:
#             checks = checks + 1 if (150 <= int(height[0]) <= 193) else checks
#         if "in" in height:
#             checks = checks + 1 if (59 <= int(height[0]) <= 76) else checks
#     if "hcl" in passport:
#         if passport["hcl"][0] == "#":
#             passport["hcl"] = passport["hcl"].lstrip("#")
#             checks = checks + 1 if sum(map(passport["hcl"].count, "abcdef")) + \
#                 sum(map(passport["hcl"].count, "0123456789")) == 6 else checks
#     if "ecl" in passport:
#         checks = checks + 1 if sum(map(passport["ecl"].count, ("amb", "blu", "gry", "grn", "hzl", "oth"))) == 1 else checks
#     if "pid" in passport:
#         checks = checks + 1 if passport["pid"].isnumeric() and len(passport["pid"]) == 9 else checks

#     if checks >= 7:
#         valid += 1

# print(f"P2 Valid Passports: {valid}")
# print(f"Valid births {births}")


# if passport["byr"] > 0:
# print(passport["ere"])

# passport = dict(kv.split(":", 1) for kv in passport)
# print(passport)

# passports = [dict(kv.split(":") for kv in passports)]

# print(f"KV Pairs:\n{passports}\n")

# kvpairs = dict(passport.split(":") for passport in passports)
# print(kvpairs)

# for passport in passports:
#     passport = re.split("-|\n| ", passport)
#     for kvpair in passport:
#         kvpair = dict(st.split(":", 1) for st in kvpair)

# print(passport)
