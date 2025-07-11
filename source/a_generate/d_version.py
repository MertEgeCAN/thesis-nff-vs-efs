import config
from source.a_generate.e_run import Run


class Version:
    def __init__(self, name, p_clear, p_fault, p_delta, p_flaky):
        self.name = name

        self.p_clear = p_clear
        self.p_fault = p_fault
        self.p_delta = p_delta
        self.p_flaky = 0 if self.p_clear or self.p_fault else self.calculate_p_flaky(p_flaky)

        self.runs = self.generate_runs()
    
    def generate_runs(self):
        runs = []
        for i in range(config.MAX_RUN):
            runs.append(Run(i + 1, self.name, self.p_clear, self.p_fault, self.p_flaky))
        return runs

    def calculate_p_flaky(self, p_flaky):
        ratio = self.name / config.MAX_VERSION

        if config.TREND_VERSION == 'increase':
            p_flaky += self.p_delta * ratio
        if config.TREND_VERSION == 'decrease':
            p_flaky -= self.p_delta * ratio
        if config.TREND_VERSION == 'increase_exponential':
            p_flaky += self.p_delta * ratio ** 2
        if config.TREND_VERSION == 'decrease_exponential':
            p_flaky -= self.p_delta * ratio ** 2
        if config.TREND_VERSION == 'increase_sudden':
            p_flaky += self.p_delta if self.name > config.MAX_VERSION / 2 else -self.p_delta
        if config.TREND_VERSION == 'decrease_sudden':
            p_flaky += self.p_delta if self.name < config.MAX_VERSION / 2 else -self.p_delta

        return p_flaky