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
    print("Visualisasi graf dengan representasi list ketetanggaan:")
    inputGraph.displayAdjList()

    startNode = int(input("Masukkan simpul asal: "))
    goalNode = int(input("Masukkan simpul tujuan: "))

    print("Pilih metode yang ingin digunakan:")
    print("1. UCS")
    print("2. A*")
    method = int(input("Masukkan pilihan metode (1 atau 2): "))
    if method == 1:
        uniformCostSearch(inputGraph, listCoordinate, startNode, goalNode)
    elif method == 2:
        aStar(inputGraph,listCoordinate, startNode,goalNode)
    else:
        print("Pilihan salah")
