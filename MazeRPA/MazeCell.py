"""
This class is meant to be the singular "spot" in any portion of the maze.
It defines itself by 5 booleans (encoded as integers by Python, probably, not sure)
4 of which are the walls where 1 - wall exists eg MazeCell.north = 1 signifies the north wall
is in place.

The leftover boolean dictates whether a cell has been visited. Primarily used
in recursive backtracking algorithm, will be removed upon further iterations, should this be
improved, as the class should be independent of the algorithm using it
"""


class MazeCell:
    # simple 5 param constructor
    def __init__(self, north, east, south, west, visited):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.visited = visited

    # Python's way of overriding the toString method
    def __str__(self):
        retstr = "North " + str(self.north)
        retstr += " South " + str(self.south)
        retstr += " East " + str(self.east)
        retstr += " West " + str(self.west)
        retstr += " Visited " + str(self.visited)
        return retstr

    # Marks the cell as visited
    def visit(self):
        self.visited = 1

    # Destroys (sets to 0) any walls given a cardinal direction
    # @param: direction
    def breaker(self, direction):
        if direction is 'north':
            self.north = 0
        elif direction is 'south':
            self.south = 0
        elif direction is 'west':
            self.west = 0
        elif direction is 'east':
            self.east = 0
        else:
            print("Something went wrong when breaking a cell's wall!")
