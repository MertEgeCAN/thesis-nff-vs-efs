import os

import pandas as pd

import config


def calculate_order_nff():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df[df['Version'] == config.MAX_VERSION][['Test', 'Run', 'Instability', 'Likelihood']]

    index_run = [2 for _ in df['Test'].unique()]
    index_instability = df[df['Run'] == 1]['Instability'].to_list()
    index_likelihood = df[df['Run'] == 1]['Likelihood'].to_list()

    order = []

    for i in range(config.MAX_TEST):
        order.append(i + 1)

    for _ in range(config.MAX_RUN * config.MAX_TEST):
        min_index = index_likelihood.index(min(index_likelihood))

        if index_run[min_index] > config.MAX_RUN:
            index_likelihood[min_index] = 42
        elif index_instability[min_index] < 0.05:
            index_likelihood[min_index] = 42
        elif index_likelihood[min_index] == 42:
            index_likelihood[min_index] = 42
        else:
            index_instability[min_index] = float(df[(df['Test'] == (min_index + 1)) & (df['Run'] == index_run[min_index])]['Instability'].iloc[0])
            index_likelihood[min_index] = float(df[(df['Test'] == (min_index + 1)) & (df['Run'] == index_run[min_index])]['Likelihood'].iloc[0])
            index_run[min_index] += 1
            order.append(min_index + 1)

    df = pd.DataFrame(order, columns=['Order'])
    df.to_csv(config.PATH_FILE_ORDER_NFF, index=False)
