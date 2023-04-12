import heapq
import math

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def neighbors(self, node):
        return self.graph_dict.get(node, {}).keys()

    def cost(self, node, next_node):
        return self.graph_dict.get(node, {}).get(next_node, math.inf)

    def heuristic(self, node, end):
        lat1, lon1 = node
        lat2, lon2 = end
        R = 6371  # jari-jari bumi dalam kilometer
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return d

def astar(graph, start, end):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: graph.heuristic(start, end)}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == end:
            path = [end]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph.cost(current, neighbor)
            if tentative_g_score < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + graph.heuristic(neighbor, end)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None
