import copy
class TransitionRelation:
    def initial(self):
        pass

    def next(self, node):
        pass


class AcceptingSet:
    def is_accepting(self, c):
        pass


class IdentityProxy:
    def __init__(self, opperand):
        self.opperand = opperand
    
    def __getattr__(self, __attr):
        return getattr(self.opperand, __attr)


class ParentStoreProxy(IdentityProxy):
    def __init__(self, opperand):
        super().__init__(opperand)
        self.parents = {}

    def next(self, config):
        neighs = self.opperand.next(config)
        for n in neighs:
            if n not in self.parents:
                self.parents[n] = config
        return neighs

class SemanticTransitionRelation():
    def initial(self):
        pass
    def actions(self,conf):
        pass
    def execute(self,conf,action):
        pass


class BehaviourSoupSemantics(SemanticTransitionRelation):
    def initial(self):
        return[self.soup.initial]

    def actions(self,conf):
        return list(map(lambda beh:beh.action, filter(lambda beh: beh.guard(conf),self.soup.behaviours)))

    def execute(selfself,c,a):
        target = copy.deepcopy(c)
        r = a(target)
        return target

class BehaviorSoup:
    def __init__(self, conf):
        self.inital = conf
        self.behavior = []

    def add(self, name, guard, action):
        self.behavior.append(Behavior(name, guard, action))


class Behavior:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action