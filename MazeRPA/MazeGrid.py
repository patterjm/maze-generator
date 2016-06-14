"""
This class is the overarching m x n grid that houses cells

More specifically, it can be used to providing bounding figures to our
xy plane problem space
"""
from MazeCell import *


class MazeGrid:
    # constructor
    # @params: rows - number of rows to instantiate
    # cols - number of columns to instantiate
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # this is a pythonic way of creating a 2D array
        # We essentially create a list of length cols for each element in a list of length rows
        self.gridSpace = [[0 for x in range(self.cols)] for y in range(self.rows)]
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                x = MazeCell(1, 1, 1, 1, 0)
                self.gridSpace[i][j] = x

    # Will print 'Cell at space i x j str(MazeCell[i][j]) \n' for each cell in the grid
    # where i, j represented the current row and column offsets respectively
    # This is stored in ROW MAJOR order
    # eg consider a 2x3 maze, the 1st row will be:
    # MazeGrid[0][0] , MazeGrid[0][1] , MazeGrid[0][2]
    def __str__(self):
        retstr = ""
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                retstr += "Cell at space " + str(i) + " x " + str(j)
                retstr += " " + str(self.gridSpace[i][j]) + "\n"

        return retstr
