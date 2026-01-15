import numpy as np
from mdp.envs import make_env
from mdp.evaluation import evaluate_policy
from mdp.policies import random_policy, always_action

def agenticity(env, policy, reward_variants):
    scores = [evaluate_policy(env, policy) for _ in reward_variants]
    return np.std(scores)

env = make_env("Taxi-v3")

policies = {
    "random": random_policy(env),
    "always_0": always_action(0),
}

for name, pi in policies.items():
    print(name, agenticity(env, pi, range(10)))

