import inspect
import sys
from typing import Mapping

from src.graph import Graph
from src.node import Node
from tools.algorithms import *
from models.hanoi import *


sys.setrecursionlimit(1000)

def main_hanoi():
    print('---- Hanoï ----\n')
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
    print('-- List method --')
    A_access_list = graph.list_depth_first_search(A)
    print(f'Accessibles nodes from {A} : {A_access_list}')

    D_access_list = graph.list_depth_first_search(D)
    print(f'Accessibles nodes from {D} : {D_access_list}')


    # Get reachable nodes
    print('\n-- Hash method --')
    A_access_hash = graph.hash_depth_first_search(A)
    print(f'Accessibles nodes from {A} : {A_access_hash}')

    D_access_hash = graph.hash_depth_first_search(D)
    print(f'Accessibles nodes from {D} : {D_access_hash}')


    print("\n-- Hanoi Model --")
    hanoi = ParentStoreProxy(Hanoi(3, 3))
    initial = hanoi.initial()[0]
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


    print(f"\n-- Parents --\nParents Hashmap: {parentStore.parents}")


    print('\n-- Guard & action --')
    hanoi = ParentStoreProxy(Hanoi(3, 3))
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        init = hanoi.initial()[0]
        guard = guard_def(i, j)
        action = action_def(i, j)
        g = guard(init)
        if g:
            a = action(init)
        print(f'Action {i},{j} : {"ok" if g else "not ok"} -> {init}')
    print('Chaining actions:')
    init = hanoi.initial()[0]
    for i, j in [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)]:
        guard = guard_def(i, j)
        action = action_def(i, j)
        g = guard(init)
        if g:
            a = action(init)
        print(f'Action {i},{j} : {"ok" if g else "not ok"} -> {init}')


    print("\n-- Hanoi soup --")
    soup = hanoi_soup(3, 3)
    behavior_soup = BehaviourSoupSemantics(soup)
    init = behavior_soup.initial()[0]
    print(f"initial state : {init}")
    actions_init = behavior_soup.actions(init)

    if actions_init:
        print(f"action possible from initial state :\n{inspect.getsource(action)}")
        for action in actions_init:
            exec_init = behavior_soup.execute(init, action)
            print(f"execution output : {exec_init}")


    print("\n-- STR2TR --")
    str2tr = STR2TR(behavior_soup)
    init_str = str2tr.initial()[0]
    next = str2tr.next(init_str)
    print(f"next states from {init_str} is : {next}")


    print("\n-- AcceptingProxy --")
    validation = IsAcceptingProxy(str2tr, isAccepted)
    print(f"checking acceptance of initial state : {validation.is_accepting(validation.operand.initial()[0])}")


    print("\n-- ModelChecker --")
    result = modelChecker(3, 4)
    if result[0]:
        print(f"Solution found ! --> {result[1]}")
    else:
        print(f"No solution founded :(")


    print('\n-- Get Trace --')
    soup = hanoi_soup(3, 4)
    behavior_soup = BehaviourSoupSemantics(soup)

    trace = predicateModelChecker(behavior_soup, isAccepted)
    if trace:
        print(f'Trace : {trace}')
    else:
        print('No Trace.')

def main_AliceBob():
    print('---- Alice & Bob ----\n')

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'hanoi':
        main_hanoi()
    elif (len(sys.argv) == 2 and sys.argv[1] == 'alice'):
        main_AliceBob()
    else:
        print('Usage: python main.py [hanoi/alice]')
        hanoi = input('Run hanoi ? [Y/n]')
        if hanoi not in ('n','N','No','Non','no','non'):
            main_hanoi()
        else:
            alice = input('Run alice ? [Y/n]')
            if alice not in ('n','N','No','Non','no','non'):
                main_AliceBob()
