from src.soup import BehaviorSoup

# TODO : adpater ce code pour alice et bob

class HConfig(list):
    def __init__(self, nb_stacks, nb_disks):
        list.__init__(self, [[(nb_disks - i) for i in range(nb_disks)]] + [[] for _ in range(nb_stacks - 1)])

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


def guard_def(s, t):
    return lambda c: len(c[s]) and (len(c[t]) == 0 or c[s][-1] < c[t][-1])


def action_def(s, t):
    def action(c):
        disk = c[s].pop()
        c[t].append(disk)

    return action


def hanoi_soup(nb_stacks, nb_disks):
    i_conf = HConfig(nb_stacks, nb_disks)
    soup = BehaviorSoup(i_conf)
    for i in range(nb_stacks):
        for j in range(nb_stacks):
            soup.add(f'{i}-{j}', guard_def(i, j), action_def(i, j))
    return soup


def isAccepted(c):
    nDisks = max(max(c))

    if len(c[-1]) != nDisks:
        return False
    for k in range(nDisks):
        if c[-1][k] != nDisks - k:
            return False
    return True
