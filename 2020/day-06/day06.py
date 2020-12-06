class Day06:

    def __init__(self, fileName):
        self.declarations = [[]]

        with open(fileName) as f:
            for passenger in f.readlines():
                if passenger == "\n":
                    self.declarations.append([])
                else:
                    self.declarations[-1].append(passenger.strip())


    def getPartOne(self):
        totalDeclarations = 0
        for group in self.declarations:
            groupDeclaration = set()
            for passenger in group:
                for declaration in passenger:
                    groupDeclaration.add(declaration)
            totalDeclarations += len(groupDeclaration)
        return totalDeclarations
    
    
    def getPartTwo(self):
        totalDeclarations = 0
        for group in self.declarations:
            groupDeclarations = []
            for passenger in group:
                passengerDeclaration = set()
                for declaration in passenger:
                    passengerDeclaration.add(declaration)
                groupDeclarations.append(passengerDeclaration)
            totalDeclarations += len(set(groupDeclarations[0]).intersection(*groupDeclarations[1:]))
        return totalDeclarations
