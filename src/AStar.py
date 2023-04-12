import heapq
from Node import *
from LinkedNode import *
from Graph import *
from Utility import *
from Node import *
import copy

def aStar(graph:Graph, coordinate,startNode:int, goalNode:int):

    liveNodes = []
    heapq.heappush(liveNodes, LinkedNode(startNode))

    visitedNodes = set()

    while liveNodes:
        expandNode = heapq.heappop(liveNodes)

        if expandNode.index == goalNode:
            path = []
            while expandNode:
                path.append(expandNode.index)
                expandNode = expandNode.parent
            path.reverse()
            return path
        
        visitedNodes.add(expandNode.index)

        for i in range(len(graph.getAdjMatrix())):
            if graph.getAdjMatrix()[expandNode.index][i] != 0 and i not in visitedNodes:
                node1 = Node(graph.getNode(i),coordinate[i])
                node2 = Node(graph.getNode(goalNode),coordinate[goalNode])
                radius = 6371
                lat1 = radians(node1.getCoordinate().getLatitude())
                lat2 = radians(node2.getCoordinate().getLatitude())
                dLat = radians(lat2 - lat1)
                dLon = radians(node2.getCoordinate().getLongitude() - node1.getCoordinate().getLongitude())
                a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
                c = 2*asin(sqrt(a))
                distance = radius * c
                new_path_cost = expandNode.path_cost + graph.getAdjMatrix()[expandNode.index][i] + distance
                heapq.heappush(liveNodes, LinkedNode(i, expandNode, new_path_cost))
    return displayPathNotFound()

def displayPath(graph,startNode,goalNode,path,listCoordinate):
    print(f"Lintasan terpendek dari {listCoordinate[startNode]} ke {listCoordinate[goalNode]} adalah {path} dengan biaya sebesar {sum(graph[path[i-1]][path[i]] for i in range(1, len(path)))}.")

def displayPathNotFound():
    print("Tidak ada lintasan dari simpul asal ke simpul tujuan")