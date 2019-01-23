from math import pow

class RuleManager:



    def locatePossibleConnects(self, board, player, rect):
        connectFour = False
        connectFourEdges = []
        rectX = board.getRectX(rect)
        rectY = board.getRectY(rect)
        for x in range(rectX-30, rectX+31, 30):
            for y in range(rectY-3, rectY+4, 3):

                if x in range(0,70,10) and y in range(0,7) and x+y in [int(rect) for rect in player.filledRects]:
                    connectFourEdges.append(x+y)
                else: connectFourEdges.append(-1)
        connectFourEdges.remove(int(rect))
        print(connectFourEdges)


        for i in range(1, 9):
            accum = 0
           # print(i)
            #print(self.polynomialEq(i))
            for j in range(connectFourEdges[i-1], int(rect), self.polynomialEq(i)):
                if j in [int(rect) for rect in player.filledRects]:
                    accum += 1
                    if accum == 3:
                        connectFour = True
                else:
                    break

        return connectFour

    def polynomialEq(self, x):
        y = round((-19/504) * pow(x, 7) + (19/16) * pow(x, 6) - (2201/144) * pow(x, 5) + (1655/16) * pow(x, 4) - (56669/144) * pow(x, 3) + (6639/8) * pow(x, 2) - (12371/14) * x + 369)

        return y


