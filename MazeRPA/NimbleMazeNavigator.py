"""
I instantiated this class as a way to easily mark where in the maze our probe existed.
I use it in practice as a pointer that can travel around the grid as it pleases
"""


class NimbleMazeNavigator:
    # Constructor inputs params of an xy plane
    # @params: x, y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Returns Row: x Col: y as string output
    def __str__(self):
        retstr = "Row: " + str(self.x)
        retstr += " Col: " + str(self.y)
        return retstr

    # The following four travel functions increment the x and y params by 1 or -1 assuming
    # the following conventions:
    #
    # A grid starts at (0,0) in the upper left and (1,1) is one to the right and one below
    # the corner grid.
    #
    # The cardinal system correlates in the following way:
    # West - left
    # East - right
    # North - up
    # South - down
    # eg travelling north from (2,1) would place you at (1,1)


    # travel east
    def traveleast(self):
        self.y += 1

    # travel west
    def travelwest(self):
        self.y -= 1

    # travel south
    def travelsouth(self):
        self.x += 1

    # travel north
    def travelnorth(self):
        self.x -= 1
