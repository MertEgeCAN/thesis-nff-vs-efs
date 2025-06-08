import pandas as pd
from scipy.stats import binom

import config


def calculate_rate():
    df_raw = pd.read_csv(config.PATH_RAW)

    df_raw['Current_NFF'] = df_raw.groupby(['Test', 'Release'])['NFF'].cumsum()
    df_raw['Current_Run'] = df_raw.groupby(['Test', 'Release']).cumcount() + 1
    df_raw['Current_Rate'] = df_raw['Current_NFF'] / df_raw['Current_Run']

    df_raw.to_csv(config.PATH_RAW, index=False)


def calculate_stable_rate():
    df_raw = pd.read_csv(config.PATH_RAW)
    df_group = df_raw[df_raw['Run'] >= (config.RUNS / 2)]

    df_raw = df_raw.groupby(['Test', 'Release']).agg(Total_NFF=('NFF', 'sum'), Total_Run=('Run', 'count')).reset_index()
    df_group = df_group.groupby(['Test', 'Release']).agg(Stable_Total_NFF=('NFF', 'sum'), Stable_Total_Run=('Run', 'count')).reset_index()

    df_group['Release_Stable_Rate'] = df_group['Stable_Total_NFF'] / df_group['Stable_Total_Run']
    df_group['Stable_Rate'] = df_group.groupby('Test')['Release_Stable_Rate'].shift(1)

    df_group['Total_NFF'] = df_raw['Total_NFF']
    df_group['Total_Run'] = df_raw['Total_Run']
    df_group['Rate'] = df_raw['Total_NFF'] / df_raw['Total_Run']

    df_group.to_csv(config.PATH_GROUP, index=False)


def calculate_confidence(e=0.05, z=1.65):
    df_group = pd.read_csv(config.PATH_GROUP)

    df_group['Confidence'] = (z ** 2) * df_group['Stable_Rate'] * (1 - df_group['Stable_Rate']) / (e ** 2)

    df_group.to_csv(config.PATH_GROUP, index=False)


def calculate_instability():
    df_raw = pd.read_csv(config.PATH_RAW)
    df_group = pd.read_csv(config.PATH_GROUP)

    df_merge = df_raw.merge(df_group, on=['Test', 'Release'], how='left')

    df_raw['Instability'] = binom.sf(
        df_raw['Current_NFF'] - 1,
        df_raw['Current_Run'],
        df_merge['Stable_Rate']
    )

    df_raw.to_csv(config.PATH_RAW, index=False)


def calculate_likelihood():
    df_raw = pd.read_csv(config.PATH_RAW)
    df_group = pd.read_csv(config.PATH_GROUP)

    df_merge = df_raw.merge(df_group, on=['Test', 'Release'], how='left')

    df_raw['Likelihood'] = binom.pmf(
        df_raw['Current_NFF'],
        df_raw['Current_Run'],
        df_merge['Stable_Rate']
    )

    df_raw.to_csv(config.PATH_RAW, index=False)


def calculate_unstable():
    df_raw = pd.read_csv(config.PATH_RAW)

    df_raw['Unstable'] = df_raw.groupby(['Test', 'Release'])['Instability'].transform(lambda s: (s < 0.05).cummax())

    df_raw.to_csv(config.PATH_RAW, index=False)
