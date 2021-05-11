
class GameOfLive:
    # constuctor expects an array of an array with 3 numbers (the three rows)
    def __init__(self, input):
        self.input = input

    def doOneRound(self):
        # to copy a list of lists you have to copy every list in the main list
        self.heatmap = [self.input[0].copy(), self.input[1].copy(),
                        self.input[2].copy()]

        # programm goes through every "square"
        for i in range(3):
            for j in range(3):

                # checks if this square has min one Inhabitant
                if self.input[i][j] != 0:

                    # checks if the Neighbour exists and if so it adds one
                    if i+1 < 3:
                        self.heatmap[i+1][j] = self.heatmap[i+1][j] + 1

                    if j+1 < 3:
                        self.heatmap[i][j+1] = self.heatmap[i][j+1] + 1

                    if i-1 >= 0:
                        self.heatmap[i-1][j] = self.heatmap[i-1][j] + 1

                    if j-1 >= 0:
                        self.heatmap[i][j-1] = self.heatmap[i][j-1] + 1

    def printOutHeatmap(self):

        # prints out the heatmap
        print(self.heatmap[0])
        print(self.heatmap[1])
        print(self.heatmap[2])


# this is the example input
myInput = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


myGame = GameOfLive(myInput)

myGame.doOneRound()
myGame.printOutHeatmap()
