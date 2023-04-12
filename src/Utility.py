import networkx as nx
import matplotlib.pyplot as plt
    
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