from MazeGenerator import *

def CheckExit(rows, cols, x, y):
    return x >= rows | y >= cols

def CheckWest(maze, x, y):
    numToTest = maze[x][y]
    if x >= len(maze) or y >= len(maze[x]) or numToTest & 0x01 == 1:
        return False
    else:
        return True

def CheckEast(maze, x, y):
    numToTest = maze[x][y]
    if x >= len(maze) or y >= len(maze[x]) or numToTest >> 2 & 0x01 == 1:
        return False
    else:
        return True

def CheckNorth(maze, x, y):
    numToTest = maze[x][y]
    if x >= len(maze) or y >= len(maze[x]) or numToTest >> 3 & 0x01 == 1:
        return False
    else:
        return True

def CheckSouth(maze, x, y):
    numToTest = maze[x][y]
    if x >= len(maze) or y >= len(maze[x]) or numToTest >> 1 & 0x01 == 1:
        return False
    else:
        return True

def MoveWest(x, y):
    jsonObj = {"x":x, "y": y-1}
    return jsonObj

def MoveEast(x, y):
    jsonObj = {"x":x, "y": y+1}
    return jsonObj

def MoveNorth(x, y):
    jsonObj = {"x":x+1, "y": y}
    return jsonObj

def MoveSouth(x, y):
    jsonObj = {"x": x-1, "y": y}
    return jsonObj