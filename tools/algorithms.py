from collections import deque
from src import kernel

def reachable_bfs(g):
    known = set()
    frontiere = deque()
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

def reachable_bfsNew(g, neighbours = None):
    known = set()
    frontiere = deque()
    if not neighbours:
        neighbours = [g.initial()]
    for n in neighbours:
            if n not in known:
                known.add(n)
                frontiere.append(n)
    while frontiere:
        neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if n not in known:
                known.add(n)
                frontiere.append(n)  
    return known

def find_loops(g):
    known = set()
    frontiere = deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                if is_reachable_bfs(g,n,n):
                    return True, n
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False, None

def is_reachable_bfs(g, start, end):
    known = set()
    frontiere = deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = [start]
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if n == end:
                return True
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False


def is_safe_bfs(g):
    known = set()
    frontiere = deque()
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
    frontiere = deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else:
            neighbours = g.next(frontiere.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                return True, n
            if n not in known:
                known.add(n)
                frontiere.append(n)
    return False, None

def get_trace(afind_actepting_bfs, parentProxy):
    result, tmp = afind_actepting_bfs(parentProxy)
    if result:
        trace = []
        intial = parentProxy.initial()[0]
        while tmp != intial:
            trace.append(tmp)
            tmp = parentProxy.parents[tmp]
        trace.append(intial)
        trace.reverse()
        return trace    

def predicate_model_checker(behavior_soup, isAccepted):
    str2tr = kernel.STR2TR(behavior_soup)
    aAcceptingProxy = kernel.IsAcceptingProxy(str2tr, isAccepted)
    aParentStore = kernel.ParentStoreProxy(aAcceptingProxy)
    trace = get_trace(find_accepting_bfs, aParentStore)
    return trace

def loop_model_checker(behavior_soup, isAccepted):
    str2tr = kernel.STR2TR(behavior_soup)
    aAcceptingProxy = kernel.IsAcceptingProxy(str2tr, isAccepted)
    aParentStore = kernel.ParentStoreProxy(aAcceptingProxy)
    res = find_loops(aParentStore)
    return res