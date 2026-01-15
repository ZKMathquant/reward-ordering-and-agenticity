import numpy as np

def affine_rewards(base_reward, alpha, beta):
    return alpha * base_reward + beta

def clipped_rewards(base_reward, low=-1, high=1):
    return np.clip(base_reward, low, high)

