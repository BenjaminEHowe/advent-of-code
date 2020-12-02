import re

with open("input.txt") as f:
    lines = f.readlines()
    passwords = []
    for line in lines:
        match = re.match(r"(\d*)-(\d*) (.): (.*)", line)
        passwords.append({
            "character": match.group(3),
            "positions": (int(match.group(1)), int(match.group(2))),
            "password": match.group(4)
        })

validPasswordCount = 0

for password in passwords:
    if (password["password"][password["positions"][0] - 1] == password["character"]) ^ (password["password"][password["positions"][1] - 1] == password["character"]):
        validPasswordCount += 1

print(validPasswordCount)
