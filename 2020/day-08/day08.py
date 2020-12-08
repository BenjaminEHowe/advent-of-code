class Day08:

    def __init__(self, fileName):
        with open(fileName) as f:
            self.instructions = []
            self.accumulator = 0
            self.programCounter = 0
            self.visitedLines = []
            for line in f.readlines():
                self.instructions.append(line.strip().split(" "))
    

    def getPartOne(self):
        while self.programCounter not in self.visitedLines:
            self.visitedLines.append(self.programCounter)
            command = self.instructions[self.programCounter][0]
            value = int(self.instructions[self.programCounter][1])
            if command == "acc":
                self.accumulator += value
            elif command == "jmp":
                self.programCounter += value
                continue
            elif command == "noop":
                pass
            self.programCounter += 1
        return self.accumulator
    
    
    def getPartTwo(self):
        for i, instruction in enumerate(self.instructions):
            if instruction[0] == "acc":
                continue
            elif instruction[0] == "nop":
                self.instructions[i][0] = "jmp"
            elif instruction[0] == "jmp":
                self.instructions[i][0] = "nop"
            self.accumulator = 0
            self.programCounter = 0
            self.visitedLines = []
            try:
                self.getPartOne()
            except IndexError:
                return self.accumulator
            if instruction[0] == "nop":
                self.instructions[i][0] = "jmp"
            elif instruction[0] == "jmp":
                self.instructions[i][0] = "nop"
