import math

with open("input.txt") as f:
    slope = f.readlines()

transformations = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

trees = []
hight = len(slope)
width = len(slope[0]) - 1

for transformation in transformations:
    currentPosition = [0, 0]
    treesThisTime = 0
    while True:
        currentPosition[0] += transformation[0]
        currentPosition[1] = (currentPosition[1] + transformation[1]) % width

        if currentPosition[0] >= hight:
            trees.append(treesThisTime)
            break

        if slope[currentPosition[0]][currentPosition[1]] == "#":
            treesThisTime += 1

print(math.prod(trees))
