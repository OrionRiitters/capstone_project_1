from dataclasses import dataclass

@dataclass
class Board:


    def makeBoard(self):
        xAxis = []
        
        for i in range(0, 7):
            yAxis = [' [ ] ' for i in range(0, 7)]
            xAxis.append(yAxis)

        for column in xAxis:
            for row in column:
                print(row, end='')
            print('\n')
