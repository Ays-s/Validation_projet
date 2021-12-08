import sys

from src.graph import Graph
from src.node import Node
from tools.algorithms import *
from models.hanoi import *


sys.setrecursionlimit(1000)


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
    graph = Graph([A, B, C, D, E], A)

    reachable_A = reachable_bfs(graph)
    print(f'Noeuds acceessible depuis {A} : {reachable_A}\n')

    # Get reachable nodes
    print('-- List method')
    A_access_list = graph.list_depth_first_search(A)
    print(f'Accessibles nodes from {A} : {A_access_list}')

    D_access_list = graph.list_depth_first_search(D)
    print(f'Accessibles nodes from {D} : {D_access_list}')

    # Get reachable nodes
    print('\n-- Hash method')
    A_access_hash = graph.hash_depth_first_search(A)
    print(f'Accessibles nodes from {A} : {A_access_hash}')

    D_access_hash = graph.hash_depth_first_search(D)
    print(f'Accessibles nodes from {D} : {D_access_hash}')

    print("\n-- Hanoi Model")
    hanoi = Hanoi(3, 3)
    initial = hanoi.initial()
    print(f'Graph initial: {initial}')
    step1 = hanoi.next(initial)
    print(f'\nStep_1   : {step1}')
    for i in range(len(step1)):
        print(f'Step_2.{i} : {hanoi.next(step1[i])}')

    print('\n-- Hash --')
    for i in range(len(step1)):
        print(f'Step_{i}   : {hash(step1[i])} -- {step1[i]}')
        step2 = hanoi.next(step1[i])
        for j in range(len(step2)):
            print(f'Step_{i}.{j} : {hash(step2[j])} -- {step2[j]}')

    print('\n-- Accepting_Bfs --')
    parentStore = ParentStoreProxy(hanoi)
    res, n = find_accepting_bfs(parentStore)

    print(f"Accepted : {res} -> bfs : {n}")

