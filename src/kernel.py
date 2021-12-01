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
    
    def __getattribute__(self, __name: str):
        return getattr(self.opperand, __name)

class ParentStoreProxy(IdentityProxy):
    def __init__(self, opperand):
        super.__init__(opperand)
        self.parents =  {}

    def next(self, config):
        neighs = self.opperand.next(config)
        for n in neighs:
            if n not in self.parents:
                self.parents[n] = config
        return neighs