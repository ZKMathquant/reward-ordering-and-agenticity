from mdp.envs import make_env
from mdp.policies import always_action
from mdp.evaluation import evaluate_policy

def test_non_triviality():
    env = make_env("FrozenLake-v1")
    pi0 = always_action(0)
    pi1 = always_action(1)
    assert evaluate_policy(env, pi0) != evaluate_policy(env, pi1)

