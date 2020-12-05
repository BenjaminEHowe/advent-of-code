seats = []

with open("input.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        seat = {}
        seat["raw"] = line
        seat["row"] = int(seat["raw"][:7].replace("F", "0").replace("B", "1"), 2)
        seat["column"] = int(seat["raw"][-3:].replace("L", "0").replace("R", "1"), 2)
        seat["id"] = seat["row"] * 8 + seat["column"]
        seats.append(seat)

print(sorted(seats, key=lambda k: k["id"], reverse=True)[0]["id"])
