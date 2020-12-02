import re

with open("input.txt") as f:
    lines = f.readlines()
    passwords = []
    for line in lines:
        match = re.match(r"(\d*)-(\d*) (.): (.*)", line)
        passwords.append({
            "character": match.group(3),
            "minOccur": int(match.group(1)),
            "maxOccur": int(match.group(2)),
            "password": match.group(4)
        })

validPasswordCount = 0

for password in passwords:
    characterOccurs = password["password"].count(password["character"])
    if characterOccurs >= password["minOccur"] and characterOccurs <= password["maxOccur"]:
        validPasswordCount += 1

print(validPasswordCount)
