class RewardWrapper:
    def __init__(self, env, transform):
        self.env = env
        self.transform = transform

    def reset(self):
        return self.env.reset()

    def step(self, action):
        obs, reward, term, trunc, info = self.env.step(action)
        return obs, self.transform(reward), term, trunc, info

