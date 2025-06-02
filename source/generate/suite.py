import random

import config
from source.generate.release import Release


class Suite:
    def __init__(self):
        self.flakiness = self.generate_flakiness()
        self.releases = self.generate_releases()

    def generate_releases(self):
        releases = []
        for i in range(config.RELEASES):
            release = Release(i, self.flakiness)
            releases.append(release)
        return releases

    @staticmethod
    def generate_flakiness():
        return [random.random() < config.FLAKINESS for _ in range(config.TESTS)]
