from Board import Board
from Player import Player
from RuleManager import RuleManager
from UI import UI

board = Board()
hmnPlayer = Player('Human')
cmpPlayer = Player('Computer')
ruleManager = RuleManager()
ui = UI()

def fillTestBoardOne():
        board.fillCoordinate('00', hmnPlayer)
        board.fillCoordinate('33', hmnPlayer)
        board.fillCoordinate('22', hmnPlayer)
        board.fillCoordinate('11', hmnPlayer)
        board.fillCoordinate('10', cmpPlayer)
        board.fillCoordinate('20', cmpPlayer)
        board.fillCoordinate('21', cmpPlayer)
        board.fillCoordinate('30', cmpPlayer)
        board.fillCoordinate('31', cmpPlayer)
        board.fillCoordinate('32', cmpPlayer)
        board.fillCoordinate('44', cmpPlayer)

def fillTestBoardTwo():
    for x in range(0,7):
        for y in range(0,7):
            board.fillCoordinate(str(x) + str(y), cmpPlayer)

fillTestBoardTwo()
UI.renderBoard(board.boardGraphic)
ruleManager.locatePossibleConnects(board, cmpPlayer, '66')

