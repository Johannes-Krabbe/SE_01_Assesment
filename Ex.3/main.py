# ex 3 is not working, the error must be Somewhere in the "doOneRound" method.
# the method "countNeighbours" returns something different when it is executed in line 26/ 27
# for example for the input 2 2 it returns 3 when it is executed in line 26/27, but when I try to execute it
# by calling it oudside of the class (line 80) it returns 2 (as it should do)


class GameOfLive:
    # constuctor expects an array of an array with 3 numbers (the three rows)
    def __init__(self, input):
        self.input = input

        if(len(self.input) == 3):
            self.heatmap = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if(len(self.input) == 4):
            self.heatmap = [[0, 0, 0, 0], [0, 0, 0, 0],
                            [0, 0, 0, 0], [0, 0, 0, 0]]

    def doOneRound(self):
        # to copy a list of lists you have to copy every list in the main list

        # programm goes through every "square"
        for i in range(len(self.heatmap)):
            for j in range(len(self.heatmap)):
                # checks if this square has min one Inhabitant
                #print(i, j)
                #print(self.countNeighbours(i, j))
                if self.countNeighbours(i, j) == 3:
                    self.heatmap[i][j] = 1

                if self.countNeighbours(i, j) >= 2 and self.input[i][j] == 1:
                    self.heatmap[i][j] = 1

    def countNeighbours(self, i, j):
        temp = 0
        if i+1 < len(self.heatmap):
            if self.input[i+1][j] != 0:
                temp = temp + 1

        if j+1 < len(self.heatmap):
            if self.input[i][j+1] != 0:
                temp = temp + 1

        if i-1 >= 0:
            if self.heatmap[i-1][j] != 0:
                temp = temp + 1

        if j-1 >= 0:
            if self.input[i][j-1] != 0:
                temp = temp + 1

        if i+1 < len(self.heatmap) and j+1 < len(self.heatmap):
            if self.input[i+1][j+1] != 0:
                temp = temp + 1

        if i+1 < len(self.heatmap) and j-1 >= 0:
            if self.input[i+1][j-1] != 0:
                temp = temp + 1

        if i-1 >= 0 and j+1 < len(self.heatmap):
            if self.input[i-1][j+1] != 0:
                temp = temp + 1

        if i-1 >= 0 and j-1 >= 0:
            if self.input[i-1][j-1] != 0:
                temp = temp + 1
        return temp

    def printOutHeatmap(self):

        # prints out the heatmap
        for i in range(len(self.heatmap)):
            print(self.heatmap[i])


# this is the example input
myInput = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]

myGame = GameOfLive(myInput)

# print(myGame.countNeighbours(2, 2))

myGame.doOneRound()
myGame.printOutHeatmap()
