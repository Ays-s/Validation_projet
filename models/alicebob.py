from src.soup import BehaviorSoup

# TODO : adpater ce code pour alice et bob

class ABConfig(list):
    def __init__(self):
        list.__init__(self, [-1, -1])

    def __hash__(self):
        return self[0] + 10*self[1]


def alice_guard_def(b):
    def guard(c):
        if b == 1 and c[0] == 0:
            return False
        elif b == 0 and c[1] == 0:
            return False
        return True
    return guard
    

def alice_action_def(b):
    def action(c):
        if c[b] == 1:
            c[b] -=1
        else:
            c[b] += 1
    return action


def alice_soup():
    i_conf = ABConfig()
    soup = BehaviorSoup(i_conf)
    for i in range(2):
        for j in range(3):
            soup.add(f'{i}-{j}', alice_guard_def(i), alice_action_def(i))
    return soup


def alice_is_accepted(c):
    return c[0] == 1 and c[1] == 1
