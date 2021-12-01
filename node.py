"""
Node class : 
    - attributes : 
        - name : node name 
        - neighbors : neighbors in the graph
    
    - Objectives : 
        - represents a Node in a Graph

Invoke class :
    - import Node class
    - create an instance by giving a name (str) and a key (16 byte array) use to decrypt messages
    - call addNeighbors to add a Node as a neighbor of another one

"""


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
