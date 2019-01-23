from board import Board
from player import Player
from rule_manager import RuleManager
from ui import UI

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
