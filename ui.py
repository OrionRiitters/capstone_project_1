from time import sleep

class UI:

    def __init__(self):
        return None

    def renderBoard(self, board):
        print('\n')
        for column in board:
            [print(row, end='') for row in column]
            print('\n')

        s = ''

        for i in range(0,7):
            s = s + str(i).center(5)

        print(s)


    def promptUserMove(self):
        return self.promptInput(6, '\nPlease enter a number corresponding to the column in which you would like to drop a piece:\n')


    def promptBeginGame(self):
        print('\nHello! You are about to play a game of Connect Four. If you are unfamiliar with the rules of Connect Four, please google them.')
        return self.promptInput(1, '\nType \'1\' to play the first move, or \'0\' to let the computer go first:\n')


    def promptEndGame(self, player):
        self.ui.renderBoard(self.board.boardGraphic)
        if player.type == 'Human':
            print('\nYou\'ve won! Just let that sink in for a moment. You did it. Wow!')
        else:
            print('\nYou managed to lose against a program with an arbitrary, random move set!')
        return self.promptInput(1, '\nPlay again?\n1 - Yes\n0- No:\n')


    def promptInput(self, optionsRange, prompt):
        userInput = None

        while True:
            userInput = input(prompt)

            if userInput.isdigit() and int(userInput) in range(0, optionsRange+1):
                break

        return int(userInput)

    def computerMoveDialogue(self):
        print('\nThe program is thinking..')
        sleep(1.5)
        print('\nThe program is reaching for a piece..')
        sleep(.5)

    def fullColumnPrompt(self):
        print('\nWhoops! That column seems to be full.')
