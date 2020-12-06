declarations = []

with open("input.txt") as f:
    groupDeclaration = set()
    passenger = f.readline()
    while True:
        if passenger == "\n":
            declarations.append(groupDeclaration)
            groupDeclaration = set()
        else:
            for declaration in passenger.replace("\n", ""):
                groupDeclaration.add(declaration)
        passenger = f.readline()
        if not passenger:
            declarations.append(groupDeclaration)
            break

print(sum(len(d) for d in declarations))
