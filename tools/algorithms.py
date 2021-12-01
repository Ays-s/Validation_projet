from typing import Deque


def reachable_bfs(g):
    known = set()
    frontiere = Deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = [g.initial()]
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return known


def is_safe_bfs(g):
    known = set()
    frontiere = Deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = [g.initial()]
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


def find_accepting_bfs(g):
    known = set()
    frontiere = Deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = [g.initial()]
            at_start = True, n
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                return True, n
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False, None