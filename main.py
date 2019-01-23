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


    board.fillCoordinate(50, hmnPlayer)
    ui.renderBoard(board.boardGraphic)
    ui.promptUserMove()

    def beginTurn(self, player):
        while True:
            column = int(self.ui.promptUserMove())
            if not self.board.checkColumnFull(column):
                self.board.fillCoordinate(self.board.findColumnTopRect(column), player)
                break


main = Main()

main.beginTurn(main.hmnPlayer)
main.ui.renderBoard(main.board.boardGraphic)
