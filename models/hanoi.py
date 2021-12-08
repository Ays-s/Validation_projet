from src.kernel import *
import copy


class HConfig(list):
    def __hash__(self):
        h = 0
        m = max(self)[0]
        for stack in self:
            h += sum(stack) * m
            m *= 2
        return h

    def __eq__(self, config):
        if len(self) != len(config):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(config[i]):
                return False
            for j in range(len(self[i])):
                if config[i][j] != self[i][j]:
                    return False
        return True


class Hanoi(TransitionRelation, AcceptingSet):
    def __init__(self, nb_stacks, nb_disks):
        self.nStacks = nb_stacks
        self.nDisks = nb_disks

    def initial(self):
        return HConfig([[(self.nDisks-i) for i in range(self.nDisks)]] + [[] for _ in range(self.nStacks-1)])

    def next(self, node):
        next_states = []
        for i in range(self.nStacks):
            newNode = copy.deepcopy(node)
            if newNode[i]:
                disk = newNode[i].pop()
                for j in range(self.nStacks):
                    if i != j and (not newNode[j] or newNode[j][-1] > disk):
                        tmp = copy.deepcopy(newNode)
                        tmp[j].append(disk)
                        next_states.append(tmp)
        return next_states

    def is_accepting(self, c):
        k = 0
        if not c[-1]:
            return False
        for disk in c[-1]:
            if disk != self.nDisks - k:
                return False
            k += 1
        return True
