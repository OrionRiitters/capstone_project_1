from Board import Board
from Player import Player
from RuleManager import RuleManager
from UI import UI

class Main:

    board = Board()
    hmnPlayer = Player('Human')
    cmpPlayer = Player('Computer')
    ruleManager = RuleManager()
    ui = UI()

    def initializeGame():
        return None


    board.fillCoordinate(55, hmnPlayer)
    UI.renderBoard(board.boardGraphic)


main = Main()

