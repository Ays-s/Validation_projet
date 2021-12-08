class TransitionRelation:
    def initial(self):
        pass

    def next(self, node):
        pass


class AcceptingSet:
    def is_accepting(self, c):
        pass


class IdentityProxy:
    def __init__(self, operand):
        self.operand = operand
    
    def __getattr__(self, __attr):
        return getattr(self.operand, __attr)


class ParentStoreProxy(IdentityProxy):
    def __init__(self, operand):
        super().__init__(operand)
        self.parents = {}

    def next(self, config):
        neighs = self.operand.next(config)
        for n in neighs:
            if n not in self.parents:
                self.parents[n] = config
        return neighs


class SemanticTransitionRelation:
    def initial(self):
        pass

    def actions(self, conf):
        pass

    def execute(self, conf, action):
        pass


class STR2TR:
    def __init__(self, ope):
        self.operand = ope

    def initial(self):
        return self.operand.initial()

    def next(self, c):
        targets = []
        for a in self.operand.actions(c):
            target = self.operand.execute(c, a)
            targets.append(target)
        return targets


class IsAcceptingProxy(IdentityProxy):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate

    def is_accepting(self, c):
        return self.predicate(c)
