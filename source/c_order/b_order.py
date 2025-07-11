import pandas as pd

import config


def calculate_order_normal():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)
    df = df[(df['Version'] == config.MAX_VERSION)][['Test', 'Date']].sort_values('Date')
    df = df.rename(columns={'Test': 'Order'})['Order']
    df.to_csv(config.PATH_FILE_ORDER_NORMAL, index=False)


def calculate_order_nff():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)
    df = df[df['Version'] == config.MAX_VERSION][['Test', 'Run', 'Likelihood']]

    index_run = [2 for _ in df['Test'].unique()]
    index_likelihood = df[df['Run'] == 1]['Likelihood'].to_list()

    order = []
    for _ in range(config.MAX_RUN * config.MAX_TEST):
        min_index = index_likelihood.index(min(index_likelihood))

        if index_run[min_index] < config.MAX_RUN:
            index_likelihood[min_index] = float(df[(df['Test'] == (min_index + 1)) & (df['Run'] == index_run[min_index])]['Likelihood'].iloc[0])
            index_run[min_index] += 1
            order.append(min_index + 1)
        else:
            index_likelihood[min_index] = 2

    df = pd.DataFrame(order, columns=['Order'])
    df.to_csv(config.PATH_FILE_ORDER_NFF, index=False)
