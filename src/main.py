from Node import *
from Graph import *
from UCS import *
from AStar import *
from Utility import *

if __name__ == "__main__":
    print("PROGRAM PENCARIAN LINTASAN TERDEKAT")
    print()
    filename = input("Masukkan nama file: ")
    try:
        file = open("../test/" + filename)
        place, adjMatrix, listCoordinate = read_file(file)
        listNode = []
        for i in range (len(listCoordinate)):
            newNode = Node(i,listCoordinate[i])
            listNode.append(newNode)
        inputGraph = Graph(listNode, adjMatrix)
        print("Visualisasi graf dengan representasi list ketetanggaan:")
        inputGraph.displayAdjList()
        graphOutputName = filename.split(".")[0] + ".png"
        UCSOutputName = filename.split(".")[0] + "PathUCS.png"
        aStarOutputName = filename.split(".")[0] + "PathAstar.png"
        inputGraph.drawGraph(graphOutputName)

        startNode = int(input("Masukkan simpul asal: "))
        goalNode = int(input("Masukkan simpul tujuan: "))

        print("Pilih metode yang ingin digunakan:")
        print("1. UCS")
        print("2. A*")
        method = int(input("Masukkan pilihan metode (1 atau 2): "))
        if method == 1:
            uniformCostSearch(inputGraph, startNode, goalNode, UCSOutputName)
            
        elif method == 2:
            aStar(inputGraph,listCoordinate, startNode,goalNode, aStarOutputName)
        else:
            print("Pilihan salah")
    except FileNotFoundError as e:
        print("File tidak ditemukan pada folder test")
        exit()