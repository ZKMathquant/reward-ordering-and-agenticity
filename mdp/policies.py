import numpy as np

def random_policy(env):
    return lambda obs: env.action_space.sample()

def always_action(a):
    return lambda obs: a

def greedy_from_q(Q):
    return lambda obs: int(np.argmax(Q[obs]))

