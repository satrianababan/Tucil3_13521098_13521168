import os
import sys
from Graph import *
from UCS import *
from AStar import *
from Node import *
from Utility import *

if __name__ == "__main__":
    filename = input("Masukkan nama file: ")
    file = open("test/" + filename)
    place, adjMatrix, listCoordinate = read_file(file)
    
    listNode = []
    for i in range (len(listCoordinate)):
        newNode = Node(i,listCoordinate[i])
        listNode.append(newNode)
    inputGraph = Graph(listNode, adjMatrix)
    startNode = int(input("Masukkan simpul asal: "))
    goalNode = int(input("Masukkan simpul tujuan: "))
    print(Graph.getNode(inputGraph,9))
    method = input("Pilih metode: ")
    if method == "UCS":
        uniformCostSearch(inputGraph, listCoordinate, startNode, goalNode)
    elif method == "Astar":
        aStar(inputGraph,listCoordinate, startNode,goalNode)
