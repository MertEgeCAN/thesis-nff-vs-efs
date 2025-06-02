import math

import numpy as np

import config
from source.generate.test import Test

rng = np.random.default_rng(config.RANDOM_SEED)

class Release:
    def __init__(self, release, flakiness):
        self.id = release
        self.flakiness = flakiness

        self.nff_counts = self.generate_nff_counts()
        self.tests = self.generate_tests()

    def generate_tests(self):
        tests = []
        for i in range(config.TESTS):
            test = Test(i, self.flakiness[i], self.nff_counts[i])
            tests.append(test)
        return tests

    def generate_nff_counts(self):
        if config.COUNT_TREND == 'increase':
            return sorted(rng.choice(a=config.NFF_RANGE, size=config.TESTS, p=self._weight_increase()))
        if config.COUNT_TREND == 'decrease':
            return sorted(rng.choice(a=config.NFF_RANGE, size=config.TESTS, p=self._weight_decrease()))
        if config.COUNT_TREND == 'increase_exponential':
            return sorted(rng.choice(a=config.NFF_RANGE, size=config.TESTS, p=self._weight_increase_exponential()))
        if config.COUNT_TREND == 'decrease_exponential':
            return sorted(rng.choice(a=config.NFF_RANGE, size=config.TESTS, p=self._weight_decrease_exponential()))
        if config.COUNT_TREND == 'uniform':
            return sorted(rng.choice(a=config.NFF_RANGE, size=config.TESTS, p=self._weight_uniform()))

    @staticmethod
    def _weight_increase():
        weights = [config.COUNT_INCREASE['start'] + i * config.COUNT_INCREASE['growth'] for i in range(config.NFF_RANGE)]
        return sorted([w / sum(weights) for w in weights])

    @staticmethod
    def _weight_decrease():
        weights = [config.COUNT_DECREASE['start'] + i * config.COUNT_DECREASE['growth'] for i in range(config.NFF_RANGE)]
        return sorted([w / sum(weights) for w in weights], reverse=True)

    @staticmethod
    def _weight_increase_exponential():
        weights = [math.exp(config.COUNT_INCREASE_EXPONENTIAL['lambda'] * i) for i in range(config.NFF_RANGE)]
        return sorted([w / sum(weights) for w in weights])

    @staticmethod
    def _weight_decrease_exponential():
        weights = [math.exp(config.COUNT_DECREASE_EXPONENTIAL['lambda'] * i) for i in range(config.NFF_RANGE)]
        return sorted([w / sum(weights) for w in weights], reverse=True)

    @staticmethod
    def _weight_uniform():
        weights = rng.random(size=config.NFF_RANGE)
        return sorted([w / sum(weights) for w in weights])
