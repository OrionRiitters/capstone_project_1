from Board import Board
from Player import Player
from RuleManager import RuleManager
from UI import UI

class Main:

    board = Board()
    hmnPlayer = Player()
    cmpPlayer = Player()
    ruleManager = RuleManager()
    ui = UI()

    def initializeGame():
        return None

    def beginGame(self, board):
        UI.renderBoard(board.makeBoardGraphic())


main = Main()
main.beginGame(main.board)
