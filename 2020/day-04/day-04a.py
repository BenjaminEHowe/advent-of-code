passports = []

with open("input.txt") as f:
    passport = ""
    line = f.readline()
    while True:
        if line == "\n":
            fields = passport[:-1].split(" ")
            fields.sort()
            passports.append(fields)
            passport = ""
        else:
            passport += line.replace("\n", " ")
        line = f.readline()
        if not line:
            fields = passport[:-1].split(" ")
            fields.sort()
            passports.append(fields)
            break

validPassports = 0

for passport in passports:
    if passport[1][:3] == "cid":
        del passport[1]
    if len(passport) != 7:
        continue
    if passport[0][:3] != "byr":
        continue
    if passport[1][:3] != "ecl":
        continue
    if passport[2][:3] != "eyr":
        continue
    if passport[3][:3] != "hcl":
        continue
    if passport[4][:3] != "hgt":
        continue
    if passport[5][:3] != "iyr":
        continue
    if passport[6][:3] != "pid":
        continue
    validPassports += 1

print(validPassports)
