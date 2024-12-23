class Day01:
    def __init__(self, locationsA, locationsB):
        self.locationsA = sorted([int(num) for num in locationsA])
        self.locationsB = sorted([int(num) for num in locationsB])

        self.distance = 0
        self.similarity = 0

    def getPart1(self):
        for locA, locB in zip(self.locationsA, self.locationsB):
            self.distance += self.getDistance(locA, locB)

        return self.distance

    def getDistance(self, locA, locB):
        return abs(locA - locB)

    def getPart2(self):
        for loc in self.locationsA:
            self.similarity += loc * self.locationsB.count(loc)

        return self.similarity
