from flask import Flask
from MazeGenerator import MazeGeneratorMain
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Maze API landing page! This is currently a WIP to get an interface for a Maze Solver."

@app.route("/CreateMaze", methods=['POST'])
def CreateMaze():
    retStr = MazeGeneratorMain.createMaze(2,3,10)
    return "JSON: " + retStr


if __name__ == "__main__":
    app.run()