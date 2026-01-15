import numpy as np
from scipy.stats import spearmanr
from mdp.envs import make_env
from mdp.evaluation import evaluate_policy
from mdp.policies import random_policy, always_action
from rewards.wrappers import RewardWrapper
from rewards.reward_families import affine_rewards

def agenticity_variance(env, policy, reward_transforms):
    """Lower variance = more robust = higher agenticity"""
    scores = []
    for transform in reward_transforms:
        wrapped = RewardWrapper(env, transform)
        scores.append(evaluate_policy(wrapped, policy, episodes=100))
    return np.std(scores)

def agenticity_rank_stability(env, policies, reward_transforms):
    """How often does policy ranking stay consistent across reward changes"""
    rankings = []
    for transform in reward_transforms:
        wrapped = RewardWrapper(env, transform)
        scores = {name: evaluate_policy(wrapped, pi, episodes=100) 
                  for name, pi in policies.items()}
        rankings.append([scores[name] for name in policies.keys()])
    
    correlations = []
    base_rank = rankings[0]
    for rank in rankings[1:]:
        corr, _ = spearmanr(base_rank, rank)
        correlations.append(corr)
    
    return np.mean(correlations)

if __name__ == "__main__":
    env = make_env("Taxi-v3")
    
    policies = {
        "random": random_policy(env),
        "always_0": always_action(0),
        "always_1": always_action(1),
    }
    
    transforms = [
        lambda r: affine_rewards(r, a, b) 
        for a in [0.5, 1.0, 2.0] 
        for b in [-1, 0, 1]
    ]
    
    print("=== Agenticity: Variance-based ===")
    for name, pi in policies.items():
        score = agenticity_variance(env, pi, transforms)
        print(f"{name:12s}: {score:.4f}")
    
    print("\n=== Agenticity: Rank stability ===")
    stability = agenticity_rank_stability(env, policies, transforms)
    print(f"Mean rank correlation: {stability:.4f}")

