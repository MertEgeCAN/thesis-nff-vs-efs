from . import config
from .run import Run


class Version:
    def __init__(self, name, p_flaky):
        self.name = name
        
        self.p_flaky = p_flaky

        self.runs = self.generate_runs()
    
    def generate_runs(self):
        runs = []
        for i in range(config.MAX_RUN):
            p_flaky = self.calculate_p_flaky(i)
            runs.append(Run(i, p_flaky))
        return runs

    def calculate_p_flaky(self, run):
        ratio = (run + 1) / config.MAX_RUN

        p_flaky = self.p_flaky
        if config.TREND_RUN == 'increase':
            p_flaky *= ratio
        if config.TREND_RUN == 'decrease':
            p_flaky *= (1 - ratio)
        if config.TREND_RUN == 'increase_exponential':
            p_flaky *= ratio ** 2
        if config.TREND_RUN == 'decrease_exponential':
            p_flaky *= (1 - ratio) ** 2
        if config.TREND_RUN == 'increase_sudden':
            p_flaky *= run > config.MAX_RUN / 2
        if config.TREND_RUN == 'decrease_sudden':
            p_flaky *= run < config.MAX_RUN / 2
        return p_flaky