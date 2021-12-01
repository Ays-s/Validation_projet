class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def addNeighbors(self, node):
        if node.name not in self.neighbors.keys():
            self.neighbors[node.name] = node
            return True
        return False
