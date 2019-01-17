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

    def __init__(self):
        print("See ya!")

    def initializeGame():
        return None

    def beginGame(self, board):
        board.makeBoard()
        print(board)


main = Main()
main.beginGame(main.board)
