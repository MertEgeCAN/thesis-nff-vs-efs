import random
from datetime import datetime, timedelta

from . import config


class Run:
    def __init__(self, name, p_flaky):
        self.name = name

        self.p_flaky = p_flaky

        self.outcome = self.assign_outcome()
        self.report = self.assign_report()

        self.date = datetime.now() + timedelta(days=self.name)

    def assign_outcome(self):
        if config.RANDOM_RNG.random() < self.p_flaky:
            outcome = config.RANDOM_RNG.choice(config.OUTCOME_FLAKY, p=config.OUTCOME_FLAKY_PROBABILITY)
        else:
            outcome = config.RANDOM_RNG.choice(config.OUTCOME_CLEAN, p=config.OUTCOME_CLEAN_PROBABILITY)
        return outcome

    def assign_report(self):
        if self.outcome in config.OUTCOME_FLAKY and config.RANDOM_RNG.random() < config.REPORT_PROBABILITY:
            return True
        else:
            return False
