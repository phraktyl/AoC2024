class Day02:
    def __init__(self, levels):
        self.levels = levels
        self.toleranceFlag = False

    def setTolerance(self):
        self.toleranceFlag = True

    def getPart1(self):
        safeCount = 0

        for level in self.levels:
            if self.testLevel(level) == True:
                safeCount += 1

        return safeCount

    def testLevel(self, levels, last = None):
        safeFlag = True

        if levels[1] > levels[0]:
            increasingFlag = True
        else:
            increasingFlag = False

        index = 1

        while index < len(levels):
            lev = levels[index] - levels[index - 1]

            if (lev > 0) != increasingFlag:
                safeFlag = False
            
            elif abs(lev) > 3:
                safeFlag = False

            elif abs(lev) == 0:
                safeFlag = False

            if  safeFlag == False:
                break

            index += 1

        # Test cases with missing elements
        if safeFlag != True and last != True and len(levels) > 2 and self.toleranceFlag == True:
            for i in range(0, len(levels)):
                trimmedLevels = levels[:]
                del trimmedLevels[i]

                safeFlag = self.testLevel(trimmedLevels, True)

                if safeFlag == True: break

        return safeFlag

    def getPart2(self):
        safeCount = 0

        for level in self.levels:
            if self.testLevel(level) == True:
                safeCount += 1

        return safeCount

