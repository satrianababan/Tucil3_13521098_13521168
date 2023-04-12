import os
import sys
from Graph import *
from UCS import *
from AStar import *
from Node import *

if __name__ == "__main__":
    place, adjMatrix, listCoordinate = read_file(os.path.abspath(sys.argv[1]))
    listNode = []
    for i in range (len(listCoordinate)):
        newNode = Node(i,listCoordinate[i])
        listNode.append(newNode)
    inputGraph = Graph(listNode, adjMatrix)
    startNode = int(input("Masukkan simpul asal: "))
    goalNode = int(input("Masukkan simpul tujuan: "))
    print(startNode)
    print(goalNode)
    for i in range(3):
        print(listNode[1])
    print(Graph.getNode(inputGraph,9))
    uniformCostSearch(inputGraph, listCoordinate, startNode, goalNode)
    aStar(inputGraph,listCoordinate, startNode,goalNode)
