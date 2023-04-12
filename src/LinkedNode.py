class LinkedNode:
    def __init__(self, index, parent=None, path_cost=0):
        self.index = index
        self.parent = parent
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost