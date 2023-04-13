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
        inputLines, adjMatrix, listCoordinate = read_file(file)
        listName = inputLines[1]
        print(listName)
        listNode = []
        for i in range (len(listCoordinate)):
            newNode = Node(i,listCoordinate[i])
            listNode.append(newNode)
        inputGraph = Graph(listNode, adjMatrix)
        print("Visualisasi graf dengan representasi list ketetanggaan:")
        inputGraph.displayAdjList()
        graphInputName = filename.split(".")[0] + ".png"
        graphUCSName = filename.split(".")[0] + "PathUCS.png"
        graphAStarName = filename.split(".")[0] + "PathAStar.png"
        inputGraph.drawInputGraph(graphInputName)

        startNode = int(input("Masukkan simpul asal: "))
        goalNode = int(input("Masukkan simpul tujuan: "))

        print("Pilih metode yang ingin digunakan:")
        print("1. UCS")
        print("2. A*")
        method = int(input("Masukkan pilihan metode (1 atau 2): "))
        if method == 1:
            uniformCostSearch(inputGraph, startNode, goalNode, graphUCSName)
        elif method == 2:
            aStar(inputGraph,listCoordinate, startNode,goalNode, graphAStarName)
        else:
            print("Pilihan salah")
    except FileNotFoundError as e:
        print("File tidak ditemukan pada folder test")
        exit()