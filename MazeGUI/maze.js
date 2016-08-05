var maze;
var xIndex;
var yIndex;
var svg;
var cellSize = 50;
var halfCell = cellSize / 2;
var offset = 50;
var wallkey = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
];

initializeMaze();
function initializeMaze() {
     d3.xml("mazebg.svg", function (xml) {
        divdom = document.getElementById("maze");

        var svgElement = document.getElementById("Layer_1");
        if (!svgElement) {
            divdom.appendChild(xml.documentElement);
        }
        svg = d3.select("svg"); // set the object to the appended version of the SVg for later use.

        d3.json("maze2.json", function(json) {
            maze = json.maze;
            xIndex = maze.length;
            yIndex = maze[0].length;
            console.log(maze);
            createMaze();   
            startNode();
        });  
        

    });
}

function startNode() {
    
            svg.selectAll(".nodeg").append("circle")
                .attr("class", "node")
                .attr("cx", function (d, i) { return cellSize + offset })
                .attr("cy", function (d, i) { return cellSize + offset })
                .attr("r", .25 * cellSize)
                .attr("filter", "url(#f3)")
                .style("fill", function (d, i) { return "gold" })
                .style("stroke", "grey")
                .style("stroke-width", "1");
}

function moveNode(direction) {
    
    currX = parseInt(svg.select(".node").attr("cx"));
    currY = parseInt(svg.select(".node").attr("cy"));

    newX = direction[0] * cellSize + currX;
    newY = direction[1] * cellSize + currY;

    var lineData = [{"x": currX, "y": currY}, {"x": newX, "y": newY}];
    svg.selectAll(".paths").append("path")
        .attr("d", lineFunction(lineData))
        .attr("stroke", "gold")
        .attr("stroke-width", 2)
        .attr("fill", "none")
        .attr("stroke-dasharray", cellSize)
        .attr("stroke-dashoffset", cellSize)
        .transition()
            .duration(1000)
            .ease("linear")
            .attr("stroke-dashoffset", 0)
            .attr("stroke", "grey");

    svg.select(".node")
    .transition()
        .duration(1000)
        .ease("linear")
        .attr("cx", function (d, i) { this.parentNode.insertBefore(this, this.parentNode.firstChild); return newX })
        .attr("cy", function (d, i) { return newY });
}

function createMaze() {
    for (var i = 0; i < xIndex; i++) {
        for (var j = 0; j < yIndex; j++) {
            var center = {"x": i * cellSize + cellSize + offset, "y": j * cellSize + cellSize + offset};
            var trump = wallkey[maze[j][i]];

            buildWalls(trump, center);
        }
    }
}

function buildWalls(trump, center) {
    if (trump[0]) {
        pathXsource = center.x - halfCell;
        pathXtarget = center.x + halfCell;
        pathYsource = center.y - halfCell;
        pathYtarget = center.y - halfCell;

        drawWall(pathXsource, pathXtarget, pathYsource, pathYtarget);
    } 
    if (trump[1]) {
        pathXsource = center.x + halfCell;
        pathXtarget = center.x + halfCell;
        pathYsource = center.y - halfCell;
        pathYtarget = center.y + halfCell;

        drawWall(pathXsource, pathXtarget, pathYsource, pathYtarget);
    }
    if (trump[2]) {
        pathXsource = center.x + halfCell;
        pathXtarget = center.x - halfCell;
        pathYsource = center.y + halfCell;
        pathYtarget = center.y + halfCell;

        drawWall(pathXsource, pathXtarget, pathYsource, pathYtarget);
    }
    if (trump[3]) {
        pathXsource = center.x - halfCell;
        pathXtarget = center.x - halfCell;
        pathYsource = center.y - halfCell;
        pathYtarget = center.y + halfCell;

        drawWall(pathXsource, pathXtarget, pathYsource, pathYtarget);
    }
}

var lineFunction = d3.svg.line()
                        .x(function(d) { return d.x; })
                        .y(function(d) { return d.y; });


function drawWall(x1, x2, y1, y2) {
    var lineData = [{"x": x1, "y": y1}, {"x": x2, "y": y2}];
    console.log(lineData);
    svg.append("path")
        .attr("d", lineFunction(lineData))
        .attr("stroke", "black")
        .attr("stroke-width", 3)
        .attr("fill", "none");
}