import numpy as np

class Stack:

    def __init__(self):

        self.state_set = []
        self.stackingNum = 4
        self.stakingSkip = 1

    def skip_and_stack_frame(self, state):

        self.state_set.append(state)

        stacked_state = np.zeros((20, 20, self.stackingNum))

        for stack_frame in range(self.stackingNum):
            stacked_state[:,:,stack_frame] = self.state_set[-1 - (self.stakingSkip * stack_frame)]
        del self.state_set[0]

        return stacked_state

    def stacking(self, state):
        self.state_set.append(state)