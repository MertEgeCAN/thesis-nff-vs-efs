import heapq

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import config


def calculate_order_binom():
    data_raw = pd.read_csv(config.PATH_RAW)
    data_raw = data_raw[data_raw['Release'] == config.RELEASES - 1][['Test', 'Run', 'Likelihood']]

    likelihood_matrix = np.full((config.TESTS, config.RUNS), np.inf)
    for _, row in data_raw.iterrows():
        t, r, l = int(row['Test']), int(row['Run']), row['Likelihood']
        likelihood_matrix[t, r] = l

    index_run = np.full(config.TESTS, 1, dtype=int)

    heap = [(likelihood_matrix[i, 1], i) for i in range(config.TESTS)]
    heapq.heapify(heap)

    log = []
    total_iterations = config.TESTS * (config.RUNS - 1)

    for _ in range(total_iterations):
        value, test_id = heapq.heappop(heap)
        run_id = index_run[test_id]

        log.append((test_id, run_id, value))

        index_run[test_id] += 1
        if index_run[test_id] < config.RUNS:
            next_likelihood = likelihood_matrix[test_id, index_run[test_id]]
        else:
            next_likelihood = np.inf

        heapq.heappush(heap, (next_likelihood, test_id))

    df_log = pd.DataFrame(log, columns=['Test', 'Run', 'Likelihood'])
    df_log['Cumulative_Likelihood'] = df_log['Likelihood'].cumsum()
    df_log.to_csv(config.PATH_BINOM, index=False)


def calculate_order_normal():
    data_raw = pd.read_csv(config.PATH_RAW)
    data_raw = data_raw[(data_raw['Release'] == config.RELEASES - 1) & (data_raw['Run'] > 9)]
    data_raw = data_raw.sort_values(by='EXECUTION_TIME')
    data_raw['Cumulative_Likelihood'] = data_raw['Likelihood'].cumsum()
    data_raw.to_csv(config.PATH_NORMAL, index=False)


def plot_likelihood():
    data_binom = pd.read_csv(config.PATH_BINOM)
    data_normal = pd.read_csv(config.PATH_NORMAL)

    y = 1 - (data_binom['Cumulative_Likelihood'] / data_normal['Cumulative_Likelihood'])
    y = (y / y.max()) * 100
    x = np.arange(len(y)) / len(y) * 100
    plt.plot(x, y, label='1 - Binomial / Normal')

    plt.title(config.FILE)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.xlabel('Percentage of Runs')
    plt.ylabel('Relative Difference between Binomial Ordering and Normal Ordering')
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_LIKELIHOOD, dpi=300, bbox_inches='tight')
    plt.close()

# def calculate_order_binom():
#     data_raw = pd.read_csv(config.PATH_RAW)
#     data_raw = data_raw[data_raw['Release'] == config.RELEASES - 1][['Test', 'Run', 'Likelihood']]
#
#     index_run = np.array([10 for _ in range(config.TESTS)])
#     index_likelihood = np.array(data_raw[data_raw['Run'] == 0]['Likelihood'])
#
#     log = []
#
#     for _ in range(config.TESTS * config.RUNS - config.TESTS * 1):
#         min_id = index_likelihood.argmin()
#         min_row = data_raw[(data_raw["Test"] == min_id) & (data_raw["Run"] == index_run[min_id])].iloc[0]
#         log.append(min_row)
#         index_run[min_id] += 1
#         index_likelihood[min_id] = min_row["Likelihood"] if index_run[min_id] < config.RUNS else 2
#
#     data_log = pd.DataFrame(log, columns=['Test', 'Run', 'Likelihood'])
#     data_log['Cumulative_Likelihood'] = data_log['Likelihood'].cumsum()
#     data_log.to_csv(config.PATH_BINOM, index=False)
