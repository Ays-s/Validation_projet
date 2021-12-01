from typing import Deque


def reachable_bfs(g, node):
    known = set()
    frontiere = Deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = [node]
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return known


def is_safe_bfs(g, node):
    known = set()
    frontiere = Deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = [node]
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                return False
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return True
