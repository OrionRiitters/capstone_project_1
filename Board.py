
# This program abstracts a new data type from what would otherwise be a 2-digit integer.
# Each unit will be refered to as a 'rect' and for purposes other than mathematical
# operation will act as a tuple. Each tuple contains an x coordinate and a y coordinate
# (54: x=5, y=4). 

from math import floor

class Board:

    filledRects = []
    boardGraphic = []

    def initializeBoardGraphic():
        xAxis = []

        for i in range(0, 7):
            yAxis = [' [ ] ' for i in range(0, 7)]
            xAxis.append(yAxis)

        return xAxis

    boardGraphic = initializeBoardGraphic()


    def getRectX(self, rect):
        x = floor(rect * .1)
        return x

    def getRectY(self, rect):
        y = rect - (self.getRectX(rect) * 10)
        return y

# Takes a rect and a player, adds a rect to filledRects[], then adds a symbol
# corresponding to the player to boardGraphic[]
    def fillCoordinate(self, rect, player):
        filler = ''

        if player.type == 'Human':
            filler = ' [X] '
        else:
            filler = ' [O] '

        self.boardGraphic[self.getRectX(rect)][self.getRectY(rect)] = filler

