from __future__ import print_function, division

import numpy as np


class Grid:
    def __init__(self, width, height, start):
        self.width = width
        self.height = height
        self.i = start[0]
        self.j = start[1]

    def set(self, rewards, actions, obey_prob):
        self.finalState = rewards.copy()
        self.rewards = rewards
        self.actions = actions
        self.obey_prob = obey_prob

    def non_terminal_states(self):
        return self.actions.keys()

    def set_state(self, s):
        self.i = s[0]
        self.j = s[1]

    def current_state(self):
        return (self.i, self.j)

    def is_terminal(self, s):
        return s not in self.actions

    def stochastic_move(self, action):
        p = np.random.random()
        if p <= self.obey_prob:
            return action
        if action == 'U' or action == 'D':
            return np.random.choice(['L', 'R'])
        elif action == 'L' or action == 'R':
            return np.random.choice(['U', 'D'])

    def move(self, action):
        actual_action = self.stochastic_move(action)
        if actual_action in self.actions[(self.i, self.j)]:
            if actual_action == 'U':
                self.i -= 1
            elif actual_action == 'D':
                self.i += 1
            elif actual_action == 'R':
                self.j += 1
            elif actual_action == 'L':
                self.j -= 1
        return self.rewards.get((self.i, self.j), 0)

    def check_move(self, action):
        i = self.i
        j = self.j
        if action in self.actions[(self.i, self.j)]:
            if action == 'U':
                i -= 1
            elif action == 'D':
                i += 1
            elif action == 'R':
                j += 1
            elif action == 'L':
                j -= 1
        reward = self.rewards.get((i, j), 0)
        return (i, j), reward

    def get_transition_probs(self, action):
        # returns a list of (probability, reward, s') transition tuples
        probs = []
        state, reward = self.check_move(action)
        probs.append((self.obey_prob, reward, state))
        disobey_prob = 1 - self.obey_prob
        if not (disobey_prob > 0.0):
            return probs
        if action == 'U' or action == 'D':
            state, reward = self.check_move('L')
            probs.append((disobey_prob / 2, reward, state))
            state, reward = self.check_move('R')
            probs.append((disobey_prob / 2, reward, state))
        elif action == 'L' or action == 'R':
            state, reward = self.check_move('U')
            probs.append((disobey_prob / 2, reward, state))
            state, reward = self.check_move('D')
            probs.append((disobey_prob / 2, reward, state))
        return probs

    def game_over(self):
        return (self.i, self.j) not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())


def standard_grid(obey_prob=1.0, step_cost=None):
    g = Grid(6, 6, (5, 0))
    rewards = {(0, 5): 1, (1, 5): -1}
    actions = {
        (0, 0): ('D', 'R'),
        (0, 1): ('L', 'R'),
        (0, 2): ('L', 'D', 'R'),
        (0, 3): ('L', 'D', 'R'),
        (0, 4): ('L', 'D', 'R'),
        (1, 0): ('U', 'D'),
        (1, 2): ('U', 'R'),
        (1, 3): ('L', 'U', 'D', 'R'),
        (1, 4): ('L', 'U', 'D', 'R'),
        (2, 0): ('U', 'D'),
        # (2, 1): ('L', 'R', 'D'),
        # (2, 2): ('R', 'U', 'D'),
        (2, 3): ('R', 'U'),
        (2, 4): ('L', 'U', 'D', 'R'),
        (2, 5): ('L', 'U', 'D'),
        (3, 0): ('U', 'R', 'D'),
        (3, 1): ('L', 'D'),
        # (3, 2): ('D', 'R', 'L'),
        # (3, 3): ('U', 'D', 'R'),
        (3, 4): ('U', 'D', 'R'),
        (3, 5): ('L', 'U', 'D'),
        (4, 0): ('U', 'R', 'D'),
        (4, 1): ('L', 'U', 'D', 'R'),
        (4, 2): ('L', 'D', 'R'),
        (4, 3): ('L', 'D', 'R'),
        (4, 4): ('L', 'U', 'D', 'R'),
        (4, 5): ('L', 'U', 'D'),
        (5, 0): ('U', 'R'),
        (5, 1): ('L', 'U', 'R'),
        (5, 2): ('L', 'U', 'R'),
        (5, 3): ('L', 'U', 'R'),
        (5, 4): ('L', 'U', 'R'),
        (5, 5): ('U', 'L'),
    }
    g.set(rewards, actions, obey_prob)
    if step_cost is not None:
        g.rewards.update({
            (0, 0): step_cost,
            (0, 1): step_cost,
            (0, 2): step_cost,
            (0, 3): step_cost,
            (0, 4): step_cost,
            (1, 0): step_cost,
            (1, 2): step_cost,
            (1, 3): step_cost,
            (1, 4): step_cost,
            (2, 0): step_cost,
            # (2, 1): step_cost,
            # (2, 2): step_cost,
            (2, 3): step_cost,
            (2, 4): step_cost,
            (2, 5): step_cost,
            (3, 0): step_cost,
            (3, 1): step_cost,
            # (3, 2): step_cost,
            # (3, 3): step_cost,
            (3, 4): step_cost,
            (3, 5): step_cost,
            (4, 0): step_cost,
            (4, 1): step_cost,
            (4, 2): step_cost,
            (4, 3): step_cost,
            (4, 4): step_cost,
            (4, 5): step_cost,
            (5, 0): step_cost,
            (5, 1): step_cost,
            (5, 2): step_cost,
            (5, 3): step_cost,
            (5, 4): step_cost,
            (5, 5): step_cost,
        })
    return g
