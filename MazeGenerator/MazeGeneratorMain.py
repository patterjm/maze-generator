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

import random
from MazeGenerator.MazeGrid import *
from MazeGenerator.NimbleMazeNavigator import *
import json


# This is kind of a patchy way to get the current cell given a specific pointer in our gridspace
# I'd like to improve it, requires more thought, I think
# @params: currCellPointer- the object containing our location in the xy grid
# @output: the cell at location (x,y) in our grid
def FetchCell(cellSpace, currPointer):
    return cellSpace.gridSpace[currPointer.x][currPointer.y]


# Checks to see if there exist any possible paths to take in recursive backtracking
# @params - currCellPointer provides x, y reference of where the navigator currently is
# @output: returns a list of any directions the navigator could possibly take
def gatherUnvisitedNeighbors(cellSpace, currPointer, m, n):
    listOfCells = []
    if currPointer.y < n - 1:
        currPointer.traveleast()
        tempCell = FetchCell(cellSpace, currPointer)
        currPointer.travelwest()
        if not tempCell.visited:
            listOfCells.append("east")

    if currPointer.y > 0:
        currPointer.travelwest()
        tempCell = FetchCell(cellSpace, currPointer)
        currPointer.traveleast()
        if not tempCell.visited:
            listOfCells.append("west")

    if currPointer.x < m - 1:
        currPointer.travelsouth()
        tempCell = FetchCell(cellSpace, currPointer)
        currPointer.travelnorth()
        if not tempCell.visited:
            listOfCells.append("south")

    if currPointer.x > 0:
        currPointer.travelnorth()
        tempCell = FetchCell(cellSpace, currPointer)
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

def createMaze(m, n, seed):
    random.seed(seed)
    cellSpace = MazeGrid(m, n)
    currCellPointer = NimbleMazeNavigator(0, 0)
    stack = []

    numUnvisitedCells = m * n - 1

    currCell = FetchCell(cellSpace, currCellPointer)
    currCell.breaker('north')
    currCell.visit()
    while numUnvisitedCells > 0:
        unvisitedNeighborList = gatherUnvisitedNeighbors(cellSpace, currCellPointer, m, n)
        if unvisitedNeighborList:
            randomChoice = random.randint(0, len(unvisitedNeighborList) - 1)
            direction = unvisitedNeighborList[randomChoice]
            currCell.breaker(direction)
            tempList = [currCell, currCellPointer.x, currCellPointer.y]
            stack.append(tempList)
            oppDirection = ""
            if direction == 'east':
                currCellPointer.traveleast()
                oppDirection = 'west'
            elif direction == 'west':
                currCellPointer.travelwest()
                oppDirection = 'east'
            elif direction == 'north':
                currCellPointer.travelnorth()
                oppDirection = 'south'
            elif direction == 'south':
                currCellPointer.travelsouth()
                oppDirection = 'north'
            else:
                print("Error in cell pointer adjustment")
            currCell = FetchCell(cellSpace, currCellPointer)
            currCell.visit()
            currCell.breaker(oppDirection)
            numUnvisitedCells -= 1
        elif stack:
            currList = stack.pop()
            currCell = currList[0]
            currCellPointer.x = currList[1]
            currCellPointer.y = currList[2]

    endX = 0
    endY = 0
    eastorsouth = random.randint(0,1)
    if eastorsouth == 0:
        endX = random.randint(0,cellSpace.rows-1)
        endY = cellSpace.cols - 1
        currCellPointer.x = endX
        currCellPointer.y = endY
        currCell = FetchCell(cellSpace, currCellPointer)
        currCell.breaker('east')
    else:
        endX = cellSpace.rows - 1
        endY = random.randint(0,cellSpace.cols-1)
        currCellPointer.x = endX
        currCellPointer.y = endY
        currCell = FetchCell(cellSpace, currCellPointer)
        currCell.breaker('south')

    print(cellSpace)
    retVal = ConvertMazeToJSONObject(cellSpace)
    return retVal

def ConvertMazeToJSONObject(mazeGrid):
    mazeObj = [[0 for x in range(mazeGrid.cols)] for y in range(mazeGrid.rows)]
    for i in range(mazeGrid.rows):
        for j in range(mazeGrid.cols):
            mazeObj[i][j] = [mazeGrid.gridSpace[i][j].north,
                             mazeGrid.gridSpace[i][j].east,
                             mazeGrid.gridSpace[i][j].south,
                             mazeGrid.gridSpace[i][j].west]
    success = True

    return json.dumps({'maze':mazeObj, 'success':success})
