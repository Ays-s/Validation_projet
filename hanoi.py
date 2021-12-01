from src.kernel import *
import copy


class Hanoi(TransitionRelation, AcceptingSet):
    def __init__(self, nb_stacks, nb_disks):
        self.nStacks = nb_stacks
        self.nDisks = nb_disks

    def initial(self):
        return [[(self.nDisks-i) for i in range(self.nDisks)]] + [[]] * (self.nStacks-1)

    def next(self, node):
        next_states = []
        newNode = copy.deepcopy(node)

        for i in range(self.nStacks):
            if newNode[i]:
                disk = newNode[i].pop()
                reset = False
                for j in range(self.nStacks):
                    if i != j:
                        if newNode[j]:
                            if newNode[j][-1] < disk:
                                newNode[j].append(disk)
                                next_states.append(newNode)
                                reset = True
                        else:
                            newNode[j].append(disk)
                            next_states.append(newNode)
                            reset = True
                        if reset:
                            newNode = copy.deepcopy(node)
                            reset = False
        return next_states

a = Hanoi(3, 3)
b = a.initial()
print(b)
print(a.next(b))