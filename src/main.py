import os
import sys
from Parser import *
from Graph import *
from Path import *

if __name__ == "__main__":
    parser = Parser(os.path.abspath(sys.argv[1]))
    # try:
    adjMatrix = parser.parseFile()
    print(adjMatrix)
    c0 = Coordinate(0, 0)
    c1 = Coordinate(1, 2)
    c2 = Coordinate(2, 1)
    c3 = Coordinate(4, 2)
    c4 = Coordinate(4, 0)
    n0 = Node(0, c0)
    n1 = Node(1, c1)
    n2 = Node(2, c2)
    n3 = Node(3, c3)
    n4 = Node(4, c4)
    listNodes = [n0, n1, n2, n3, n4]
    for node in listNodes:
        print(node)
    inputGraph = Graph(listNodes, adjMatrix)
    start = Node(0,c0)
    goal = Node(4,c4)
    pathFinder = Path(inputGraph, start, goal)
    pathFinder.uniformCostSearch()
    pathFinder.aStar()
    # except Exception as e:
    #     print(e)
    #     exit()

# python main.py ../test/matrix.txt
