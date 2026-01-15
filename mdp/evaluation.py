import numpy as np

def evaluate_policy(env, policy, episodes=1000):
    returns = []
    for _ in range(episodes):
        obs, _ = env.reset()
        done = False
        total = 0
        while not done:
            action = policy(obs)
            obs, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            total += reward
        returns.append(total)
    return np.mean(returns)

