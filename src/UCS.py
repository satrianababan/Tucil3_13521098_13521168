import heapq
from LinkedNode import *
from Graph import *

def uniformCostSearch(graph, listCoordinate, startNode, goalNode):

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
            return displayPath(graph,startNode,goalNode,path, listCoordinate)

        visitedNodes.add(expandNode.index)

        for i in range(len(graph.getAdjMatrix())):
            if graph.getAdjMatrix()[expandNode.index][i] != 0 and i not in visitedNodes:
                new_path_cost = expandNode.path_cost + graph.getAdjMatrix()[expandNode.index][i]
                heapq.heappush(liveNodes, LinkedNode(i, expandNode, new_path_cost))
    return displayPathNotFound()

def displayPath(graph,startNode,goalNode,path,listCoordinate):
    print(f"Lintasan terpendek dari {listCoordinate[startNode]} ke {listCoordinate[goalNode]} adalah {path} dengan biaya sebesar {sum(graph.getAdjMatrix()[path[i-1]][path[i]] for i in range(1, len(path)))}.")

def displayPathNotFound():
    print("Tidak ada lintasan dari simpul asal ke simpul tujuan")