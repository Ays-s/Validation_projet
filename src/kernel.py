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