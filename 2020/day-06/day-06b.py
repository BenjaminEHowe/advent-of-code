declarations = []

with open("input.txt") as f:
    groupDeclarations = []
    passenger = f.readline()
    while True:
        if passenger == "\n":
            declarations.append(set(groupDeclarations[0]).intersection(*groupDeclarations[1:]))
            groupDeclarations = []
        else:
            passengerDeclaration = set()
            for declaration in passenger.replace("\n", ""):
                passengerDeclaration.add(declaration)
            groupDeclarations.append(passengerDeclaration)
        passenger = f.readline()
        if not passenger:
            declarations.append(set(groupDeclarations[0]).intersection(*groupDeclarations[1:]))
            break

print(sum(len(d) for d in declarations))
