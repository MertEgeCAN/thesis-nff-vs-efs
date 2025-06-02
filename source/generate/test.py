import math

import numpy as np

import config

rng = np.random.default_rng(config.RANDOM_SEED)

class Test:
    def __init__(self, test, flaky, count_nff):
        self.id = test
        self.flaky = flaky
        self.nff_count = count_nff

        self.nff_indexes = self.generate_nff_indexes()

    def generate_nff_indexes(self):
        if not self.flaky:
            return []
        if config.INDEX_TREND == 'increase':
            return rng.choice(a=config.RUNS, size=self.nff_count, replace=False, p=self._weight_increase())
        if config.INDEX_TREND == 'decrease':
            return rng.choice(a=config.RUNS, size=self.nff_count, replace=False, p=self._weight_decrease())
        if config.INDEX_TREND == 'increase_exponential':
            return rng.choice(a=config.RUNS, size=self.nff_count, replace=False, p=self._weight_increase_exponential())
        if config.INDEX_TREND == 'decrease_exponential':
            return rng.choice(a=config.RUNS, size=self.nff_count, replace=False, p=self._weight_decrease_exponential())
        if config.INDEX_TREND == 'increase_sudden':
            return rng.choice(a=config.RUNS, size=self.nff_count, replace=False, p=self._weight_increase_sudden())
        if config.INDEX_TREND == 'decrease_sudden':
            return rng.choice(a=config.RUNS, size=self.nff_count, replace=False, p=self._weight_decrease_sudden())

    @staticmethod
    def _weight_increase():
        weights = [config.INDEX_INCREASE['start'] + i * config.INDEX_INCREASE['growth'] for i in range(config.RUNS)]
        return sorted([w / sum(weights) for w in weights])

    @staticmethod
    def _weight_decrease():
        weights = [config.INDEX_DECREASE['start'] + i * config.INDEX_DECREASE['growth'] for i in range(config.RUNS)]
        return sorted([w / sum(weights) for w in weights], reverse=True)

    @staticmethod
    def _weight_increase_exponential():
        weights = [math.exp(config.INDEX_INCREASE_EXPONENTIAL['lambda'] * i) for i in range(config.RUNS)]
        return sorted([w / sum(weights) for w in weights])

    @staticmethod
    def _weight_decrease_exponential():
        weights = [math.exp(config.INDEX_DECREASE_EXPONENTIAL['lambda'] * i) for i in range(config.RUNS)]
        return sorted([w / sum(weights) for w in weights], reverse=True)

    @staticmethod
    def _weight_increase_sudden():
        weights = [config.INDEX_INCREASE_SUDDEN['low'] if i < config.INDEX_INCREASE_SUDDEN['transition'] else config.INDEX_INCREASE_SUDDEN['high'] for i in range(config.RUNS)]
        return sorted([w / sum(weights) for w in weights])

    @staticmethod
    def _weight_decrease_sudden():
        weights = [config.INDEX_DECREASE_SUDDEN['low'] if i < config.INDEX_DECREASE_SUDDEN['transition'] else config.INDEX_DECREASE_SUDDEN['high'] for i in range(config.RUNS)]
        return sorted([w / sum(weights) for w in weights], reverse=True)
