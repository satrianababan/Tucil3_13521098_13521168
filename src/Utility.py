import networkx as nx
import matplotlib.pyplot as plt
from Node import Node
from Coordinate import Coordinate
from math import *

def read_file(filename):
    with open(filename) as f:
        nama = f.readline().strip().split()
        banyak = len(nama)
        matriks = []
        koordinat = []
        for i in range(banyak):
            line = f.readline().strip().split()
            matriks.append(line)
        for j in range(banyak):
            koor = f.readline().strip().split()
            koordinat.append(koor)
        MatrixToPoint(matriks)
        CoorToPoint(koordinat)
        return nama,matriks,koordinat
# Membaca file graf
def read_graph(filename):
    with open(filename) as f:
        nodes = f.readline().strip().split()
        n = len(nodes)
        graph = nx.Graph()
        graph.add_nodes_from(nodes)
        for i in range(n):
            line = f.readline().strip().split()
            for j in range(n):
                if line[j] != '0':
                    graph.add_edge(nodes[i], nodes[j], weight=int(line[j]))
        return graph
def addPoint(graph, point):
    if point not in graph:
        graph[point] = []
def addEdge(graph, point1, point2, weight):
    if point1 not in graph:
        graph[point1] = []
    if point2 not in graph:
        graph[point2] = []
    if point2 not in graph[point1]:
        graph[point1].append(point2)
    if point1 not in graph[point2]:
        graph[point2].append(point1)
    graph[point1][point2] = weight
    graph[point2][point1] = weight
def matrixToGraph(matrix):
    graph = {}
    for i in range(len(matrix)):
        addPoint(graph, i)
        for j in range(len(matrix[i])):
            if (matrix[i][j] != 0):
                addEdge(graph, (i, j), (i, j + 1), matrix[i][j])
                addEdge(graph, (i, j), (i + 1, j), matrix[i][j])
    return graph
def printPath(graph, NamaKota):
    for point in graph:
        for j in range (len(graph[point])):
            print(NamaKota[point], ":", NamaKota[graph[point][j][0]], "weight :", graph[point][j][1])
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()
def checkMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] != 0 and i==j):
                return False
    return True
def getIDXname(arr, name):
    for i in range(len(arr)):
        if (arr[i]==name):
            return i
        break
    return -1

def haversine(node1:Node, node2:Node, radius = 6371):
    lat1 = radians(node1.getCoordinate().getLatitude())
    lat2 = radians(node2.getCoordinate().getLatitude())
    dLat = radians(lat2 - lat1)
    dLon = radians(node2.getCoordinate().getLongitude() - node1.getCoordinate().getLongitude())
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    distance = radius * c
    return distance
def distance(graph,list):
    hasil = 0
    for i in range(len(list)-1):
        for j in range(len(graph[list[i]])):
            if(graph[list[i]][j][0]==list[i+1]):
                hasil+=graph[list[i]][j][1]
    return hasil
def visualize_graph(nama,matriks,coor):
    graph = nx.Graph()
    for i in range(len(nama)):
        graph.add_node(nama[i],pos=(coor[i][0],coor[i][1]))
    for j in range(len(nama)):
        for k in range(len(nama)):
            if(matriks[j][k]!=0):
                graph.add_edge(nama[j],nama[k],weight = int(matriks[j][k]) )
def MatrixToPoint(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            matriks[i][j] = float(matriks[i][j])
def CoorToPoint(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            matriks[i][j] = float(matriks[i][j])
def matrixToGraph(matrix):
    graph = {}
    for i in range(len(matrix)):
        addPoint(graph, i)
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                addEdge(graph, i, j, matrix[i][j])
    return graph
def drawGraphCoor(graph):
    pos=nx.get_node_attributes(graph,'pos')
    nx.draw(graph,pos,with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)