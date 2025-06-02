import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import config


def calculate_order_binom():
    data_raw = pd.read_csv(config.PATH_RAW)
    data_raw = data_raw[data_raw['Release'] == config.RELEASES - 1][['Test', 'Run', 'Likelihood']]

    index_run = np.array([1 for _ in range(config.TESTS)])
    index_likelihood = np.array(data_raw[data_raw['Run'] == 0]['Likelihood'])

    log = []

    for _ in range(config.TESTS * config.RUNS - config.TESTS):
        min_id = index_likelihood.argmin()
        min_row = data_raw[(data_raw["Test"] == min_id) & (data_raw["Run"] == index_run[min_id])].iloc[0]
        log.append(min_row)
        index_run[min_id] += 1
        index_likelihood[min_id] = min_row["Likelihood"] if index_run[min_id] < config.RUNS else 2

    data_log = pd.DataFrame(log, columns=['Test', 'Run', 'Likelihood'])
    data_log['Cumulative_Likelihood'] = data_log['Likelihood'].cumsum()
    data_log.to_csv(config.PATH_BINOM, index=False)


def calculate_order_normal():
    data_raw = pd.read_csv(config.PATH_RAW)
    data_raw = data_raw[(data_raw['Release'] == config.RELEASES - 1) & (data_raw['Run'] > 0)]
    data_raw = data_raw.sort_values(by='EXECUTION_TIME')
    data_raw['Cumulative_Likelihood'] = data_raw['Likelihood'].cumsum()
    data_raw.to_csv(config.PATH_NORMAL, index=False)


def plot_likelihood():
    data_binom = pd.read_csv(config.PATH_BINOM)
    data_normal = pd.read_csv(config.PATH_NORMAL)

    y = 1 - (data_binom['Cumulative_Likelihood'] / data_normal['Cumulative_Likelihood'])
    y = (y / y.max()) * 100
    x = range(len(data_binom))
    plt.plot(x, y, label='1 - Binomial / Normal', color='blue')

    plt.title(config.PATH_FILE)
    plt.xlabel('Run Number')
    plt.ylabel('Relative Difference')
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_LIKELIHOOD, dpi=300, bbox_inches='tight')
    plt.close()
