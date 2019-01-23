from ui import UI
from board import Board



class Player:

    def __init__(self, type):
        self.type = type
        self.filledRects = []


#    def beginTurn(self):
#
#        while True:
#            column = self.ui.promptUserMove()
#            if not board.checkColumnFull(column):
#                board.fillCoordinate(str(findColumnTopRect(column) + 1))
#                break
