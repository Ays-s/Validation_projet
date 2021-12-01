from src.kernel import *
import copy


class Hanoi(TransitionRelation, AcceptingSet):
    def __init__(self, nb_stacks, nb_disks):
        self.nStacks = nb_stacks
        self.nDisks = nb_disks

    def initial(self):
        return [[(self.nDisks-i) for i in range(self.nDisks)]] + [[] for _ in range(self.nStacks-1)]

    def next(self, node):
        next_states = []
        for i in range(self.nStacks):
            newNode = copy.deepcopy(node)
            if newNode[i]:
                disk = newNode[i].pop()
                for j in range(self.nStacks):
                    if i!= j and (not newNode[j] or newNode[j][-1] > disk):
                        tmp = copy.deepcopy(newNode)
                        tmp[j].append(disk)
                        next_states.append(tmp)
        return next_states

if __name__ == '__main__':
    hanoi = Hanoi(3, 3)
    initial = hanoi.initial()
    print(f'Graph initial: {initial}')
    step1 = hanoi.next(initial)
    print(f'\nStep 1 : {step1}')
    for i in range(len(step1)):
        print(f'Step2.{i} : {hanoi.next(step1[i])}')
