from rl_env.reward_normalization.normalization_strategy import NormalizationStrategy


class Normalization:

    def __init__(self):
        self.strategy: NormalizationStrategy = None

    def set_strategy(self, strategy: NormalizationStrategy):
        self.strategy = strategy

    def normalize(self, reward, max_reward, min_reward):
        return self.strategy.normalize(reward, max_reward, min_reward)
