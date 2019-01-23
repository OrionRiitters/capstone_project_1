from board import Board
from player import Player
from rule_manager import RuleManager
from ui import UI
from random import randint

class Main:

    board = Board()
    hmnPlayer = Player('Human')
    cmpPlayer = Player('Computer')
    ruleManager = RuleManager()
    ui = UI()

    def initializeGame(self):

        initInput = self.ui.promptBeginGame()

        if initInput == 1:
            self.ui.renderBoard(self.board.boardGraphic)
            self.beginHmnTurn(self.hmnPlayer)
            self.ui.renderBoard(self.board.boardGraphic)

        while True:
            self.beginCmpTurn(self.cmpPlayer)
            self.ui.computerMoveDialogue()
            self.ui.renderBoard(self.board.boardGraphic)
            self.beginHmnTurn(self.hmnPlayer)
            self.ui.renderBoard(self.board.boardGraphic)
    


    def beginHmnTurn(self, player):
        currentRect = -1

        while True:
            column = int(self.ui.promptUserMove())
            if not self.board.checkColumnFull(column):
                currentRect = self.board.findColumnTopRect(column)
                self.board.fillCoordinate(currentRect, player)

                break
        if self.ruleManager.locatePossibleConnects(self.board, player, currentRect):
            self.ui.promptEndGame(player)

    def beginCmpTurn(self, player):
        currentRect = -1

        while True:
            column = randint(0,0)
            if not self.board.checkColumnFull(column):
                currentRect = self.board.findColumnTopRect(column)
                self.board.fillCoordinate(currentRect, player)

                break
            else:
                self.ui.fullColumnPrompt()
        if self.ruleManager.locatePossibleConnects(self.board, player, currentRect):
            self.ui.promptEndGame(player)

main = Main()
main.initializeGame()

#main.board.fillCoordinate('00', main.cmpPlayer)
#main.board.fillCoordinate('01', main.cmpPlayer)
#main.board.fillCoordinate('02', main.cmpPlayer)
#main.board.fillCoordinate('13', main.cmpPlayer)
#main.ui.renderBoard(main.board.boardGraphic)
#main.beginTurn(main.cmpPlayer)
#main.ui.renderBoard(main.board.boardGraphic)
