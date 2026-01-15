from mdp.envs import make_env
from mdp.policies import random_policy, always_action
from mdp.evaluation import evaluate_policy
from rewards.wrappers import RewardWrapper
from rewards.reward_families import affine_rewards

env = make_env("FrozenLake-v1")

pi1 = random_policy(env)
pi2 = always_action(0)
pi3 = always_action(1)

base_scores = {
    "pi1": evaluate_policy(env, pi1),
    "pi2": evaluate_policy(env, pi2),
    "pi3": evaluate_policy(env, pi3),
}

print("Base ordering:", base_scores)

orderable = True
for a in [-2, -1, 0.5, 1, 2]:
    for b in [-1, 0, 1]:
        wrapped = RewardWrapper(env, lambda r: affine_rewards(r, a, b))
        scores = {
            "pi1": evaluate_policy(wrapped, pi1),
            "pi2": evaluate_policy(wrapped, pi2),
            "pi3": evaluate_policy(wrapped, pi3),
        }
        if not (scores["pi1"] < scores["pi2"] < scores["pi3"]):
            orderable = False
            break

print("Strictly orderable under affine rewards:", orderable)
