import heapq
from LinkedNode import *

def uniformCostSearch(graph, startNode, goalNode):

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

        for i in range(len(graph)):
            if graph[expandNode.index][i] != 0 and i not in visitedNodes:
                new_path_cost = expandNode.path_cost + graph[expandNode.index][i]
                heapq.heappush(liveNodes, LinkedNode(i, expandNode, new_path_cost))

    # If there is no path from start to goal, return None
    return None