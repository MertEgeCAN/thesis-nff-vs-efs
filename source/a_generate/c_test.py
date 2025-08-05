import config
from source.a_generate.d_version import Version


class Test:
    def __init__(self, name):
        self.name = name

        self.rng = config.RANDOM_RNG.random()
        self.p_clear = False if self.name == 1 else self.rng < config.PROBABILITY_CLEAR
        self.p_fault = False if self.name == 1 else self.rng > config.PROBABILITY_FAULT
        self.p_delta = 0 if self.p_clear or self.p_fault else config.PROBABILITY_FLAKY_DELTA
        self.p_flaky = 0 if self.p_clear or self.p_fault else config.RANDOM_RNG.uniform(config.PROBABILITY_FLAKY_LOW, config.PROBABILITY_FLAKY_HIGH)

        self.versions = self.generate_versions()

    def generate_versions(self):
        versions = []
        for i in range(config.MAX_VERSION):
            versions.append(Version(i + 1, self.p_clear, self.p_fault, self.p_delta, self.p_flaky))
        return versions