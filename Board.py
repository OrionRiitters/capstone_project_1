from dataclasses import dataclass

# This program abstracts a new data type from what would otherwise be a 2-digit integer.
# Each unit will be refered to as a 'rect' and for purposes other than mathematical
# operation will act as a tuple. Each tuple contains a y coordinate and an x coordinate,
# respectively. (e.g. 54: y=5, x=4). Methods will be provided to obtain coordinates.

@dataclass
class Board:

    filledRects = [] # An array of 

    def makeBoardGraphic(self):
        xAxis = []

        for i in range(0, 7):
            yAxis = [' [ ] ' for i in range(0, 7)]
            xAxis.append(yAxis)

        return xAxis
