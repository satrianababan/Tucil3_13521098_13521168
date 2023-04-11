from math import *

def haversine(dot1, dot2):
    # jari2 bumi dalam km
    r = 6371
    dtr = pi/180
    lat = (dot2["x"]-dot1["x"])*dtr
    lon = (dot2["y"]-dot1["y"])*dtr
    akar = sin(lat/2)**2 + cos(dot2["x"]*dtr) * cos(dot1["x"]*dtr) * sin(lon/2)**2
    return 2*r*asin(sqrt(akar))

def dheuristics(parsed, goal_node):
    for i in range(len(parsed[1])):
        if parsed[1][i] == goal_node:
            end = i
    dgoal = []
    # Buat dictionary key = node, value = jarak lurus node ke simpul tujuan
    h={}
    for i in range(len(parsed[1])):
        dgoal.append(haversine(parsed[2][end],parsed[2][i]))
        h[parsed[1][i]] = dgoal[i]
    return h

def sortB (list, dictB):
    # Mengurutkan list simpul sesuai dengan Bobot value terminimum
    dicttemp = {}
    for node in list:
        if dictB.get(node, "Not Available") != "Not Available":
          dicttemp[node] = dictB[node]
    dicttemp = dict(sorted(dicttemp.items(), key=lambda item: item[1]))
    sorted_list = []
    for i in dicttemp.keys():
      sorted_list.append(i)
    return sorted_list

# A* search
def astar_search(parsed, heuristics, start_node, goal_node): 
    
    # Inisialisasi open node dan closed node
    open_node = []
    closed_node = []

    # Bikin dictionary prev, key = node dan value = parent node
    prev = {}
    for i in parsed[1]:
      prev[i] = None

    # Bikin dictionary B value, D value
    dictB= {}
    dictB[start_node] = heuristics[start_node]

    dictD = {}
    dictD[start_node] = 0

    # Append simpul awal ke list open node
    open_node.append(start_node)
    
    # Looping open node hingga open node kosong
    while len(open_node) > 0:
        # Ambil simpul yang memiliki B value terkecil
        open_node = sortB(open_node, dictB)
        current_node = open_node.pop(0)
        closed_node.append(current_node)

        # Jika sudah mencapai simpul tujuan
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = prev[current_node]
            path.append(start_node)
            return path[::-1]

        # looping simpul tetangga dari current node
        neighbors = parsed[0][current_node]  

        for neighbor in neighbors.keys():    
            # Kasus simpul sudah diperiksa
            if(neighbor in closed_node):
                continue
            prev[neighbor] = current_node

            # Update nilai D value dan B value jika B value baru lebih minimum
            if(dictD[current_node] + neighbors[neighbor] + heuristics[neighbor] < dictB.get(neighbor, 99999999)):
              dictD[neighbor] = dictD[current_node] + neighbors[neighbor] 
              dictB[neighbor] = dictD[neighbor] + heuristics[neighbor]
              open_node.append(neighbor)
    # Return None jika tidak ada jalur
    return None