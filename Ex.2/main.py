
class GameOfLive:
    # constuctor expects an array of an array with 3 numbers (the three rows)
    def __init__(self, input):
        self.input = input

    def doOneRound(self):
        # to copy a list of lists you have to copy every list in the main list

        if(len(self.input) == 3):
            self.heatmap = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if(len(self.input) == 4):
            self.heatmap = [[0, 0, 0, 0], [0, 0, 0, 0],
                            [0, 0, 0, 0], [0, 0, 0, 0]]

        # programm goes through every "square"
        for i in range(len(self.heatmap)):
            for j in range(len(self.heatmap)):
                # checks if this square has min one Inhabitant
                if self.input[i][j] != 0:

                    # checks if the Neighbour exists and if so it adds one
                    if i+1 < len(self.heatmap):
                        self.heatmap[i+1][j] = self.heatmap[i+1][j] + 1

                    if j+1 < len(self.heatmap):
                        self.heatmap[i][j+1] = self.heatmap[i][j+1] + 1

                    if i-1 >= 0:
                        self.heatmap[i-1][j] = self.heatmap[i-1][j] + 1

                    if j-1 >= 0:
                        self.heatmap[i][j-1] = self.heatmap[i][j-1] + 1

                    if i+1 < len(self.heatmap) and j+1 < len(self.heatmap):
                        self.heatmap[i+1][j+1] = self.heatmap[i+1][j+1] + 1

                    if i+1 < len(self.heatmap) and j-1 >= 0:
                        self.heatmap[i+1][j-1] = self.heatmap[i+1][j-1] + 1

                    if i-1 >= 0 and j+1 < len(self.heatmap):
                        self.heatmap[i-1][j+1] = self.heatmap[i-1][j+1] + 1

                    if i-1 >= 0 and j-1 >= 0:
                        self.heatmap[i-1][j-1] = self.heatmap[i-1][j-1] + 1

    def printOutHeatmap(self):

        # prints out the heatmap
        for i in range(len(self.heatmap)):
            print(self.heatmap[i])


# this is the example input
myInput = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]

#myInput = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

myGame = GameOfLive(myInput)

myGame.doOneRound()
myGame.printOutHeatmap()
