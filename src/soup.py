from src.kernel import *


class BehaviorSoup:
    def __init__(self, conf):
        self.inital = conf
        self.behavior = []

    def add(self, name, guard, action):
        self.behavior.append(Behavior(name, guard, action))


class Behavior:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action
