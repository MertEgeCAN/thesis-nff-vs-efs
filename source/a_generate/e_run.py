from datetime import datetime, timedelta

import config


class Run:
    def __init__(self, name, version, p_clear, p_fault, p_flaky):
        self.name = name
        self.version = version

        self.p_clear = p_clear
        self.p_fault = p_fault
        self.p_flaky = 0 if self.p_clear or self.p_fault else self.calculate_p_flaky(p_flaky)

        self.outcome, self.report = self.assign_result()

        self.date = datetime.now() + timedelta(days=(config.MAX_RUN * self.version + self.name), hours=config.RANDOM_RNG.uniform(0, 24), minutes=config.RANDOM_RNG.uniform(0, 59), seconds=config.RANDOM_RNG.uniform(0, 59))

    def calculate_p_flaky(self, p_flaky):
        ratio = self.name / config.MAX_RUN

        if config.TREND_RUN == 'increase':
            p_flaky *= ratio
        if config.TREND_RUN == 'decrease':
            p_flaky *= (1 - ratio)
        if config.TREND_RUN == 'increase_exponential':
            p_flaky *= ratio ** 2
        if config.TREND_RUN == 'decrease_exponential':
            p_flaky *= (1 - ratio) ** 2
        if config.TREND_RUN == 'increase_sudden':
            p_flaky *= self.name > config.MAX_RUN / 2
        if config.TREND_RUN == 'decrease_sudden':
            p_flaky *= self.name < config.MAX_RUN / 2

        return p_flaky

    def assign_result(self):
        outcome = config.RANDOM_RNG.choice(config.PROBABILITY_OUTCOME_CLEAN, p=config.PROBABILITY_OUTCOME_CLEAN_RATIO)
        report = False

        if self.p_fault:
            outcome = config.RANDOM_RNG.choice(config.PROBABILITY_OUTCOME_FAULT, p=config.PROBABILITY_OUTCOME_FAULT_RATIO)
            report = True
        if config.RANDOM_RNG.random() < self.p_flaky:
            outcome = config.RANDOM_RNG.choice(config.PROBABILITY_OUTCOME_FLAKY, p=config.PROBABILITY_OUTCOME_FLAKY_RATIO)
            report = config.RANDOM_RNG.random() < config.PROBABILITY_REPORT

        return outcome, report

