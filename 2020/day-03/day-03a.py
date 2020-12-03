with open("input.txt") as f:
    slope = f.readlines()

trees = 0
hight = len(slope)
width = len(slope[0]) - 1
xPos = 0

for row in slope[1:]:
    xPos = (xPos + 3) % width
    if row[xPos] == "#":
        trees += 1

print(trees)
