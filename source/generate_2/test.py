from source.generate_2 import config
from source.generate_2.version import Version


class Test:
    def __init__(self, name):
        self.name = name

        self.p_clear = config.RANDOM_RNG.random() < config.PROBABILITY_CLEAR
        self.p_flaky = 0 if self.p_clear else config.RANDOM_RNG.uniform(config.PROBABILITY_FLAKY_LOW, config.PROBABILITY_FLAKY_HIGH)

        self.versions = self.generate_versions()

    def generate_versions(self):
        versions = []
        for i in range(config.MAX_VERSION):
            p_flaky = 0 if self.p_clear else self.calculate_p_flaky(i)
            versions.append(Version(i, p_flaky))
        return versions

    def calculate_p_flaky(self, version):
        ratio = (version + 1) / config.MAX_VERSION
        delta = config.RANDOM_RNG.uniform(config.PROBABILITY_FLAKY_DELTA_MIN, config.PROBABILITY_FLAKY_DELTA_MAX)

        p_flaky = self.p_flaky
        if config.TREND_VERSION == 'increase':
            p_flaky += delta * ratio
        if config.TREND_VERSION == 'decrease':
            p_flaky -= delta * ratio
        if config.TREND_VERSION == 'increase_exponential':
            p_flaky += delta * (ratio ** 2)
        if config.TREND_VERSION == 'decrease_exponential':
            p_flaky -= delta * (ratio ** 2)
        if config.TREND_VERSION == 'increase_sudden':
            p_flaky += delta * (version > config.MAX_VERSION / 2)
        if config.TREND_VERSION == 'decrease_sudden':
            p_flaky -= delta * (version > config.MAX_VERSION / 2)
        if p_flaky < config.PROBABILITY_FLAKY_MIN:
            p_flaky = config.PROBABILITY_FLAKY_MIN
        if p_flaky > config.PROBABILITY_FLAKY_MAX:
            p_flaky = config.PROBABILITY_FLAKY_MAX
        return p_flaky