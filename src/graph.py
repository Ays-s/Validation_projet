from src.kernel import AcceptingSet, TransitionRelation


class Graph(TransitionRelation):
    def __init__(self, nodes):
        self.nodes = nodes

    def get_nodes(self):
        return self.nodes
    
    def next(self, node):
        return self.get_outgoing_edges(node)

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


class NFA(Graph, AcceptingSet):
    def __init__(self, nodes, acc):
        super.__init__(nodes)
        self.accepting = acc
    
    def is_accepting(self, c):
        return c in self.accepting
