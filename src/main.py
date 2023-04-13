from Node import *
from Graph import *
from UCS import *
from AStar import *
from Utility import *

if __name__ == "__main__":
    print("===================================")
    print("PROGRAM PENCARIAN LINTASAN TERDEKAT")
    print("===================================")
    print()
    filename = input("Masukkan nama file: ")
    try:
        file = open("../test/" + filename)
        listName, adjMatrix, listCoordinate = read_file(file)
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

        try:
            startNode = int(input("Masukkan simpul asal: "))
        except IndexError as e:
            print("Simpul asal tidak ada pada graf")
            exit()
        try:
            goalNode = int(input("Masukkan simpul tujuan: "))
        except IndexError as e:
            print("simpul tujuan tidak ada pada graf")
            exit()

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
    except ValueError as e:
        print("Input Graph tidak valid")
        exit()
    except IndexError as e:
            print("Input Graph Tidak Simetris")
            exit()