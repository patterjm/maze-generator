""" Maze Generation & Machine Learning Independent Project
Created by: Jake Patterson
Project Start Date: 6/1/2016
Project End Date: LOL Let's work on it first

I was very interested in how RPA and code automation works, so I started with this
from scratch project that would create and solve various mazes, tracking the
average optimization time of some algorithms I plan to play around with.

UPDATE: 6/13/2016
From here on out, I will be working on fine tuning the (now completed) maze generator
and creating an API around the following code. The end goal is to have a graphic and some
form of RESTful API so that others can pull from the maze
"""

from random import randint
from MazeGrid import *
from NimbleMazeNavigator import *


# This is kind of a patchy way to get the current cell given a specific pointer in our gridspace
# I'd like to improve it, requires more thought, I think
# @params: currCellPointer- the object containing our location in the xy grid
# @output: the cell at location (x,y) in our grid
def FetchCell(currPointer):
    return cellSpace.gridSpace[currPointer.x][currPointer.y]


# Checks to see if there exist any possible paths to take in recursive backtracking
# @params - currCellPointer provides x, y reference of where the navigator currently is
# @output: returns a list of any directions the navigator could possibly take
def gatherUnvisitedNeighbors(currPointer):
    listOfCells = []
    if currPointer.y < n - 1:
        currPointer.traveleast()
        tempCell = FetchCell(currPointer)
        currPointer.travelwest()
        if not tempCell.visited:
            listOfCells.append("east")

    if currPointer.y > 0:
        currPointer.travelwest()
        tempCell = FetchCell(currPointer)
        currPointer.traveleast()
        if not tempCell.visited:
            listOfCells.append("west")

    if currPointer.x < m - 1:
        currPointer.travelsouth()
        tempCell = FetchCell(currPointer)
        currPointer.travelnorth()
        if not tempCell.visited:
            listOfCells.append("south")

    if currPointer.x > 0:
        currPointer.travelnorth()
        tempCell = FetchCell(currPointer)
        currPointer.travelsouth()
        if not tempCell.visited:
            listOfCells.append("north")

    return listOfCells


# found on S/O used to assign value None to variables that were given non-integer
# values
# Source:
# http://stackoverflow.com/questions/2262333/is-there-a-built-in-or-more-pythonic-way-to-try-to-parse-a-string-to-an-integer
def try_parse_int(s, base=10, val=None):
    try:
        return int(s, base)
    except ValueError:
        return val


validInput = False
m = 0
n = 0
# Crafty while loop to force correct integer parameters for m, n
while validInput is False:
    m = try_parse_int(input("Please input the number of rows you'd like in the matrix"))
    n = try_parse_int(input("Please input the number of columns you'd like in the matrix"))

    if m is None and n is not None:
        print("Your row input was not given as a proper integer value")
    elif n is None and m is not None:
        print("Your column input was not given as a proper integer value")
    elif n is None and m is None:
        print("neither input received a proper integer value")
    else:
        print("You gave me the following matrix", m, "x", n)
        print("Now constructing maze")
        validInput = True

cellSpace = MazeGrid(m, n)

print("Maze constructed")

print("Creating initial pointer at 0,0")
currCellPointer = NimbleMazeNavigator(0, 0)
stack = []

numUnvisitedCells = m * n - 1

currCell = FetchCell(currCellPointer)
currCell.visit()
print("Initial pointer and cell established, entering RBA loop")
while numUnvisitedCells > 0:
    unvisitedNeighborList = gatherUnvisitedNeighbors(currCellPointer)
    if unvisitedNeighborList:
        randomChoice = randint(0, len(unvisitedNeighborList) - 1)
        direction = unvisitedNeighborList[randomChoice]
        currCell.breaker(direction)
        # print("Traveled:", direction, "Cell result:", currCell)
        tempList = [currCell, currCellPointer.x, currCellPointer.y]
        stack.append(tempList)
        oppDirection = ""
        if direction is 'east':
            currCellPointer.traveleast()
            oppDirection = 'west'
        elif direction is 'west':
            currCellPointer.travelwest()
            oppDirection = 'east'
        elif direction is 'north':
            currCellPointer.travelnorth()
            oppDirection = 'south'
        elif direction is 'south':
            currCellPointer.travelsouth()
            oppDirection = 'north'
        else:
            print("Error in cell pointer adjustment")
        currCell = FetchCell(currCellPointer)
        currCell.visit()
        # print("Opp Direction: ", oppDirection)
        currCell.breaker(oppDirection)
        numUnvisitedCells -= 1
    elif stack:
        currList = stack.pop()
        currCell = currList[0]
        currCellPointer.x = currList[1]
        currCellPointer.y = currList[2]

print(cellSpace)
