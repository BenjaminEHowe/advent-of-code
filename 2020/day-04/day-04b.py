passports = []

def parseFields(passport):
    parsedPassport = {}
    fields = passport[:-1].split(" ")
    for field in fields:
        pair = field.split(":", 1)
        parsedPassport[pair[0]] = pair[1]
    return parsedPassport


def validatePassportFields(passport):
    return bool(validatePassportFieldBirthYear(passport["byr"])
        and validatePassportFieldIssueYear(passport["iyr"])
        and validatePassportFieldExpirationYear(passport["eyr"])
        and validatePassportFieldHight(passport["hgt"])
        and validatePassportFieldHairColour(passport["hcl"])
        and validatePassportFieldEyeColour(passport["ecl"])
        and validatePassportFieldPassportId(passport["pid"]))


def validatePassportFieldBirthYear(birthYear):
    birthYear = int(birthYear)
    if birthYear < 1920 or birthYear > 2002:
        print("Invalid birth year: {}".format(passport["byr"]))
        return False
    return True


def validatePassportFieldIssueYear(issueYear):
    issueYear = int(issueYear)
    if issueYear < 2010 or issueYear > 2020:
        print("Invalid issue year: {}".format(passport["iyr"]))
        return False
    return True


def validatePassportFieldExpirationYear(expirationYear):
    expirationYear = int(expirationYear)
    if expirationYear < 2020 or expirationYear > 2030:
        print("Invalid expiration year: {}".format(passport["eyr"]))
        return False
    return True


def validatePassportFieldHight(hight):
    if len(hight) < 4:
        print("Invalid height: {}".format(hight))
        return False
    hightUnit = hight[-2:]
    hightQuantity = int(hight[:-2])
    if hightUnit == "cm":
        if hightQuantity < 150 or hightQuantity > 193:
            print("Invalid height: {}".format(hight))
            return False
    elif hightUnit == "in":
        if hightQuantity < 59 or hightQuantity > 76:
            print("Invalid height: {}".format(hight))
            return False
    else:
        return False
    return True


def validatePassportFieldHairColour(hairColour):
    if len(hairColour) != 7:
        print("Invalid hair colour: {}".format(hairColour))
        return False
    if hairColour[0] != "#":
        print("Invalid hair colour: {}".format(hairColour))
        return False
    for character in hairColour[1:]:
        if character not in ("0123456789abcdef"):
            print("Invalid hair colour: {}".format(hairColour))
            return False
    return True


def validatePassportFieldEyeColour(eyeColour):
    if eyeColour not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        print("Invalid eye colour: {}".format(eyeColour))
        return False
    return True


def validatePassportFieldPassportId(passportId):
    try:
        int(passportId)
    except ValueError:
        return False
    if len(passportId) > 9:
        print("Invalid passport ID: {}".format(passportId))
        return False
    return True


with open("input.txt") as f:
    passport = ""
    line = f.readline()
    while True:
        if line == "\n":
            passports.append(parseFields(passport))
            passport = ""
        else:
            passport += line.replace("\n", " ")
        line = f.readline()
        if not line:
            passports.append(parseFields(passport))
            break

requiredFields = ("byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid")
validPassports = 0

for passport in passports:
    invalidPassport = False
    for field in requiredFields:
        if field not in passport:
            invalidPassport = True
            break
    if invalidPassport:
        continue
    if validatePassportFields(passport):
        validPassports += 1

print(validPassports)
