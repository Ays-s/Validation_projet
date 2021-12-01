"""
Graph class : 
    - attributes : 
        - nodes : nodes composing the graph
    
    - Objectives : 
        - represents a Graph composed of Nodes (type Node)
    
    - types specifications : 
        - nodes is a list of Nodes type

Invoke class :
    - create an instance by giving a list of already created Nodes instances
    - call list/hash_depth_first_search to do a depth first search on the graph from a given starting node
"""


class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        values = node.neighbors.values()
        return [value for value in values]

    def list_depth_first_search(self, start_node):
        accessible_nodes = [start_node]

        for node in accessible_nodes:
            neighbors = self.get_outgoing_edges(node)

            for neighbor in neighbors:
                if neighbor not in accessible_nodes:
                    accessible_nodes.append(neighbor)
        return accessible_nodes

    def hash_depth_first_search(self, start_node):
        accessible_nodes = {0: start_node}
        neighbors = self.get_outgoing_edges(start_node)
        i = 0

        while neighbors:
            for neighbor in neighbors:
                if neighbor not in accessible_nodes.values():
                    accessible_nodes[len(accessible_nodes)] = neighbor
            i += 1
            neighbors = self.get_outgoing_edges(accessible_nodes[i])
        return accessible_nodes
