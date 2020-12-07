# TODO: try re-implementing today's challenge using AnyTree (https://anytree.readthedocs.io/en/latest/)

import re

class Day07:

    def __init__(self, fileName):
        with open(fileName) as f:
            self.bagRules = f.readlines()
    

    def __numberOfBagsIn(self, colour, dict):
        bags = dict[colour]
        if bags == "no other bags":
            return 0
        else:
            numberOfBags = 0
            for bag in bags.split(", "):
                bagMatch = re.match(r"(\d*) (.*?) bag", bag)
                bagQuantity = int(bagMatch.group(1))
                bagColour = bagMatch.group(2)
                numberOfBags += bagQuantity + (bagQuantity * self.__numberOfBagsIn(bagColour, dict))
            return numberOfBags


    def getPartOne(self):
        outerBagColours = set()
        previousOuterBagColoursLength = -1
        while previousOuterBagColoursLength != len(outerBagColours):
            previousOuterBagColoursLength = len(outerBagColours)
            for rule in self.bagRules:
                rule = re.match(r"(.*?) bags contain ((?:(?:\d* .*? bags?(?:, )?)*)|no other bags)\.", rule).groups()
                if rule[0] in outerBagColours or rule[1] == "no other bags":
                    continue
                for bag in rule[1].split(", "):
                    bagName = re.match(r"\d* (.*?) bag", bag).group(1)
                    if bagName == "shiny gold" or bagName in outerBagColours:
                        outerBagColours.add(rule[0])
                        continue
        return len(outerBagColours)
    
    
    def getPartTwo(self):
        bagRulesDict = {}
        for rule in self.bagRules:
            rule = re.match(r"(.*?) bags contain ((?:(?:\d* .*? bags?(?:, )?)*)|no other bags)\.", rule).groups()
            bagRulesDict[rule[0]] = rule[1]
        return self.__numberOfBagsIn("shiny gold", bagRulesDict)
