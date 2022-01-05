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


def find_loop(g):
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
    neighbours = [start]
    for n in neighbours:
        if n not in known:
            known.add(n)
            frontiere.append(n)
    while frontiere:
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


def find_accepting_bfs(g, initial = None):
    known = set()
    frontiere = deque()
    at_start = True
    while frontiere or at_start:
        if at_start:
            if initial:
                neighbours = initial
            else:
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

def get_loop_trace(afind_loop_bfs, parentProxy, loopNode):
    result, final = afind_loop_bfs(parentProxy, loopNode)
    if result:
        trace = [final]
        tmp = parentProxy.parents[final]
        while tmp != final:
            trace.append(tmp)
            tmp = parentProxy.parents[tmp]
        trace.append(final)
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
    aParentStore2 = kernel.ParentStoreProxy(aAcceptingProxy)
    trace = get_trace(find_accepting_bfs, aParentStore)
    loopNode = find_loop(aParentStore)[1]
    loopNode = aParentStore2.next(loopNode)
    loop_trace = get_loop_trace(find_accepting_bfs, aParentStore2, loopNode)
    return trace, loop_trace