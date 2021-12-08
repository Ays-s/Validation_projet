from models.hanoi import HConfig
from src.kernel import BehaviorSoup


def guard_def(s, t):
    return lambda c: len(c.stacks[s]) and (len(c.stacks[t]) == 0 or c.stacks[s][-1] < c.stacks[t][-1])


def action_def(s, t):
    def action(c):
        disk = c[s].pop()
        c[t].append(disk)
    return action


def hanoi_soup(nb_stacks, nb_disks):
    i_conf = HConfig(nb_stacks, nb_disks)
    soup = BehaviorSoup(i_conf)
    for i in range(nb_stacks):
        for j in range(nb_disks):
            soup.add(f'{i}-{j}', guard_def(i, j), action_def(i, j))
    return soup
