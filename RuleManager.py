class RuleManager:

    def locatePossibleConnects(self, board, player, rect):
        connectFourEdges = []
        rectX = board.getRectX(rect)
        rectY = board.getRectY(rect)

        for x in range(rectX-30, rectX+31, 30):
            for y in range(rectY-3, rectY+4, 3):
                if x>=0 and y>=0 and x+y in [int(rect) for rect in player.filledRects]:
                    connectFourEdges.append(x+y)

        print(player.filledRects)
