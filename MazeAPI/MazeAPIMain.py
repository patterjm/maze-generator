from flask import Flask, request
from MazeGenerator import MazeGeneratorMain
from MazeAPI import MazeAPIUtil
import json
from flask_socketio import SocketIO
app = Flask(__name__)

socketio = SocketIO(app)
@app.route("/")
def hello():
    return "Welcome to the Maze API landing page! This is currently a WIP to get an interface for a Maze Solver."

@socketio.on('connect')
def ws_conn():
    return True

@app.route("/CreateMaze", methods=['POST'])
def CreateMaze():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']),int(requestObject['cols']),
                                          int(requestObject['seed']))
    socketio.emit('maze', retStr)
    return retStr

@app.route("/CheckAll", methods=['POST'])
def CheckAll():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']),int(requestObject['cols']),
                                          int(requestObject['seed']))
    tempObj = json.loads(retStr)
    checkArr = MazeAPIUtil.CheckAll(tempObj['maze'], int(requestObject['x']), int(requestObject['y']))
    return checkArr

@app.route("/CheckWest", methods=['POST'])
def CheckWest():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    tempObj = json.loads(retStr)
    checkVal = MazeAPIUtil.CheckWest(tempObj['maze'], int(requestObject['x']), int(requestObject['y']))
    return json.dumps({"success":checkVal})

@app.route("/CheckEast", methods=['POST'])
def CheckEast():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    checkVal = MazeAPIUtil.CheckEast(json.loads(retStr)['maze'], int(requestObject['x']), int(requestObject['y']))
    return json.dumps({"success": checkVal})

@app.route("/CheckNorth", methods=['POST'])
def CheckNorth():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    checkVal = MazeAPIUtil.CheckNorth(json.loads(retStr)['maze'], int(requestObject['x']), int(requestObject['y']))
    return json.dumps({"success": checkVal})

@app.route("/CheckSouth", methods=['POST'])
def CheckSouth():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    checkVal = MazeAPIUtil.CheckSouth(json.loads(retStr)['maze'], int(requestObject['x']), int(requestObject['y']))
    return json.dumps({"success": checkVal})

@app.route("/MoveWest", methods=['POST'])
def MoveWest():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    moveVal = MazeAPIUtil.MoveWest(int(requestObject['x']), int(requestObject['y']))
    socketio.emit('direction', {'direction': [-1, 0]})
    return json.dumps(moveVal)

@app.route("/MoveEast", methods=['POST'])
def MoveEast():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    moveVal = MazeAPIUtil.MoveEast(int(requestObject['x']), int(requestObject['y']))
    socketio.emit('direction', {'direction': [1, 0]})
    return json.dumps(moveVal)

@app.route("/MoveNorth", methods=['POST'])
def MoveNorth():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    moveVal = MazeAPIUtil.MoveNorth(int(requestObject['x']), int(requestObject['y']))
    socketio.emit('direction', {'direction': [0, -1]})
    return json.dumps(moveVal)

@app.route("/MoveSouth", methods=['POST'])
def MoveSouth():
    requestObject = request.get_json()
    retStr = MazeGeneratorMain.createMaze(int(requestObject['rows']), int(requestObject['cols']),
                                          int(requestObject['seed']))
    moveVal = MazeAPIUtil.MoveSouth(int(requestObject['x']), int(requestObject['y']))
    socketio.emit('direction', {'direction': [0, 1]})
    return json.dumps(moveVal)

@app.route("/CheckExit", methods=['POST'])
def CheckExit():
    requestObject = request.get_json()
    retStr = MazeAPIUtil.CheckExit(int(requestObject['rows']), int(requestObject['cols']),
                                   int(requestObject['x']), int(requestObject['y']))
    socketio.emit('complete', {'complete': True})
    return json.dumps({"success": retStr})


if __name__ == "__main__":
    socketio.run(app)