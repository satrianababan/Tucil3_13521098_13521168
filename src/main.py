import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from Graph import *
from UCS import *
from AStar import *
from Node import *
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
        inputGraph.visualize(filename)

        startNode = int(input("Masukkan simpul asal: "))
        goalNode = int(input("Masukkan simpul tujuan: "))

        print("Pilih metode yang ingin digunakan:")
        print("1. UCS")
        print("2. A*")
        method = int(input("Masukkan pilihan metode (1 atau 2): "))
        if method == 1:
            uniformCostSearch(inputGraph, startNode, goalNode,filename)
            
        elif method == 2:
            aStar(inputGraph,listCoordinate, startNode,goalNode)

        else:
            print("Pilihan salah")
    except FileNotFoundError as e:
        print("File tidak ditemukan pada folder test")
        exit()