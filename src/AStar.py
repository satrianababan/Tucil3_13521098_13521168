import heapq
from Node import *
from LinkedNode import *
from Graph import *
from Utility import *
from Node import *

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
            return ShowPath(graph, path, startNode, goalNode)
        
        visitedNodes.add(expandNode.index)

        for i in range(len(graph.getAdjMatrix())):
            if graph.getAdjMatrix()[expandNode.index][i] != 0 and i not in visitedNodes:
                radius = 6371
                lat1 = radians(coordinate[i][0])
                lat2 = radians(coordinate[goalNode][0])
                dLat = radians(lat2 - lat1)
                dLon = radians(coordinate[goalNode][1] - coordinate[i][1])
                a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
                c = 2*asin(sqrt(a))
                distance = radius * c
                new_path_cost = expandNode.path_cost + graph.getAdjMatrix()[expandNode.index][i] + distance
                heapq.heappush(liveNodes, LinkedNode(i, expandNode, new_path_cost))
    return displayPathNotFound()

def displayPath(graph,startNode,goalNode,path):
    print(f"Lintasan terpendek dari simpul {startNode} ke {goalNode} adalah ",end='')
    i = 0
    while(i < len(path)):
        print(path[i],end='')
        i = i + 1
        if (i < len(path)):
            print(" --> ", end='')
    print(f" dengan panjang lintasan sebesar {sum(graph.getAdjMatrix()[path[i-1]][path[i]] for i in range(1, len(path)))}")

def displayPathNotFound():
    print("Tidak ada lintasan dari simpul asal ke simpul tujuan")
    
def ShowPath(graph:Graph,path, startNode, goalNode):
    print(f"Lintasan terpendek dari simpul {startNode} ke {goalNode} adalah ",end='')
    i = 0
    while(i < len(path)):
        print(path[i],end='')
        i = i + 1
        if (i < len(path)):
            print(" --> ", end='')
    print(f" dengan panjang lintasan sebesar {sum(graph.getAdjMatrix()[path[i-1]][path[i]] for i in range(1, len(path)))}")
    graph.drawGraphColor(path)
    plt.show()