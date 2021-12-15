from src.soup import BehaviorSoup

# TODO : adpater ce code pour alice et bob

class ABConfig(list):
    def __init__(self):
        list.__init__(self, [-1, -1])

    def __hash__(self):
        return self[0] + 10*self[1]


def alice_guard_def(b):
    def guard(c):
        if c[b] == 1:
            return False
        elif b == 1 and c[0] == 0:
            return False
        elif b == 0 and c[1] == 0:
            return False
    return guard
    

def alice_action_def(b):
    def action(c):
        c[b] += 1
    return action


def alice_soup():
    i_conf = ABConfig()
    soup = BehaviorSoup(i_conf)
    for i in range(2):
            soup.add(f'{i}', alice_guard_def(i), alice_action_def(i))
    return soup


def alice_isAccepted(c):
    return c == [1, 1]
