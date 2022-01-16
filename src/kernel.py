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

    def initial(self):
        return self.operand.initial()

    def next(self, c):
        return self.operand.next(c)



class ParentStoreProxy(IdentityProxy):
    def __init__(self, operand):
        super().__init__(operand)
        self.parents = {}

    def next(self, config):
        #print((self.operand))
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
        print(self.operand)
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


class oSTR:
    def __init__(self, str):
        self.operand = str

    def actions(self, conf):
        return self.operand.actions(conf)

    def execute(self, conf, actions):
        targets = []
        for a in actions(conf):
            target = self.operand.execute(conf, a)
            targets.append(target)
        return targets, self.operand



class iSTR:
    def __init__(self, str):
        self.operand = str

    def actions(self, i, conf):
        actions = self.operand.actions(conf)
        for a in actions:
            if a[0](i):
                actions.append(a)
        return actions

    def execute(self, i, conf, actions):
        targets =[]
        for a in actions(conf):
            target = self.operand.execute(conf,a)
            target.append(target)
        return targets[conf](i)







class STR2OSTR:
    def __init__(self, op):
        self.operand = op

    def initial(self):
        return self.operand.initial()

    def action(self, c):
        return self.operand.actions(c)

    def execute(self, c, source, a):
        target = self.operand.execute(c, a)
        return (source, a, target), target


class KripkeBuchiSTR(SemanticTransitionRelation):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        return list(map(lambda rc: (None, rc), self.rhs.initial()))

    def actions(self, source):
        synchronous_actions = []
        kripke_src, buchi_src = source
        if kripke_src is None:
            for k_target in self.lhs.initial():
                self.get_synchronous_actions(k_target, buchi_src, synchronous_actions)
            return synchronous_actions
        k_actions = self.lhs.actions(kripke_src)
        num_actions = len(k_actions)
        for ka in k_actions:
            ktarget = self.lhs.execute(kripke_src, ka)  # _, ktarget + uncomment STR2OSTR + add layer
            if ktarget is None:
                num_actions -= 1
            self.get_synchronous_actions(ktarget, buchi_src, synchronous_actions)

        if num_actions == 0:
            self.get_synchronous_actions(kripke_src, buchi_src, synchronous_actions)
        return synchronous_actions

    def get_synchronous_actions(self, kripke_c, buchi_c, io_synca):
        buchi_actions = self.rhs.actions(kripke_c, buchi_c)
        return io_synca.extend(map(lambda ba:(kripke_c, ba), buchi_actions))

    def execute(self, conf, action):
        ktarget, baction = action
        bsrc = conf  # _, bsrc + uncomment STR2OSTR + add layer
        return ktarget, self.rhs.execute(ktarget, baction, bsrc)


class BuchiSemantics(iSTR):
    def __init__(self, t):
        self.ini = t[0]
        self.delta = t[1]
        self.pred = t[2]

    def initial(self):
        return [self.ini]

    def actions(self, i, c):
        actions = []
        for a in self.delta[c]:
            if a[0](i):
                actions.append(a)
        return actions

    def execute(self, i, conf, a):
        return a[1]

