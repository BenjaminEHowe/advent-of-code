SUM = 2020

with open("input.txt") as f:
    entries = f.read().split("\n")

entries = [int(i) for i in entries]
entries.sort()

for i, entry in enumerate(entries):
    for j, entry2 in enumerate(entries[i:]):
        if entry + entry2 == 2020:
            print("{} x {} = {}".format(entry, entry2, entry * entry2))
