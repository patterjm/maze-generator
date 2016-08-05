from MazeGenerator import *
import json
def CheckExit(rows, cols, x, y):
    return x >= rows | y >= cols

def CheckAll(maze, x, y):
    westBool = CheckWest(maze, x, y)
    eastBool = CheckEast(maze, x, y)
    northBool = CheckNorth(maze,x,y)
    southBool = CheckSouth(maze, x, y)
    return json.dumps({"North":northBool, "East":eastBool, "South":southBool, "West":westBool})


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