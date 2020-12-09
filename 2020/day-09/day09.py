class Day09:

    def __init__(self, fileName, preambleLength):
        self.preambleLength = preambleLength
        with open(fileName) as f:
            self.numbers = list(map(int, f.readlines()))
    

    def getPartOne(self):
        for i, number in enumerate(self.numbers):
            if i < self.preambleLength:
                continue
            previousNumbers = self.numbers[i-self.preambleLength:i]
            numberSumOfPreviousNumbers = False
            for previousNumber in previousNumbers:
                if number - previousNumber in previousNumbers:
                    numberSumOfPreviousNumbers = True
                    break
            if not numberSumOfPreviousNumbers:
                return number
    
    
    def getPartTwo(self):
        invalidNumber = self.getPartOne()
        for i, number in enumerate(self.numbers):
            candidateNumbers = []
            for number in self.numbers[i:]:
                candidateNumbers.append(number)
                if sum(candidateNumbers) == invalidNumber:
                    candidateNumbers.sort()
                    return candidateNumbers[0] + candidateNumbers[-1]
                elif sum(candidateNumbers) > invalidNumber:
                    break
