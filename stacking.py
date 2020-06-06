import numpy as np

class Stack:

    def __init__(self):

        self.state_set = []
        self.stackingNum = 4
        self.stakingSkip = 1

    def erase(self):
        self.state_set.clear()

    def skip_and_stack_frame(self, state):

        self.state_set.append(state)

        stacked_state = []

        for stack_frame in range(self.stackingNum):
            stacked_state.append(self.state_set[-1 - (self.stakingSkip * stack_frame)])
        self.state_set.pop(0)

        return stacked_state

    def stacking(self, state):
        self.state_set.append(state)