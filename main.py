from graph import Graph
from node import Node
from algorithms import *

if __name__ == '__main__':

    # Nodes definition
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')

    # Nodes neighbors
    A.addNeighbors(B)
    A.addNeighbors(C)

    B.addNeighbors(A)
    B.addNeighbors(C)

    C.addNeighbors(B)
    C.addNeighbors(A)
    C.addNeighbors(D)

    # Graph definition
    graph = Graph([A, B, C, D, E])

    reachable_A = reachable_bfs(graph, A)
    print(f'Noeuds acceessible depuis {A} : {reachable_A}\n')

    # Get reachable nodes
    print('-- List method')
    A_access_list = graph.list_depth_first_search(A)
    print(f'Accessibles nodes from {A} : {A_access_list}')

    D_access_list = graph.list_depth_first_search(D)
    print('Accessibles nodes from {D} : {D_access_list}')

    # Get reachable nodes
    print('\n-- Hash method')
    A_access_hash = graph.hash_depth_first_search(A)
    print('Accessibles nodes from {A} : {A_access_hash}')

    D_access_hash = graph.hash_depth_first_search(D)
    print('Accessibles nodes from {D} : {D_access_hash}')
