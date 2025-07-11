import pandas as pd
from scipy.stats import binom

import config


def calculate_nff_rate():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)

    df['NFF'] = (df['Outcome'].isin(config.PROBABILITY_OUTCOME_FLAKY)) & (df['Report'] == False)
    df['NFF_Cumulative'] = df.groupby(['Test', 'Version'])['NFF'].cumsum()
    df['NFF_Rate'] = df['NFF_Cumulative'] / df['Run']

    df.to_csv(config.PATH_FILE_GENERATE_NFF, index=False)


def calculate_stable_nff_rate():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)

    df['Stable_NFF'] = (df['NFF']) & (df['Run'] > config.MAX_RUN / 2)
    df['Stable_NFF_Cumulative'] = df.groupby(['Test', 'Version'])['Stable_NFF'].cumsum()
    df['Stable_NFF_Rate'] = df['Stable_NFF_Cumulative'] / (df['Run'] - config.MAX_RUN / 2)

    df_merge = df.groupby(['Test', 'Version'])['Stable_NFF_Rate'].last().groupby('Test').shift()

    df = df.merge(df_merge.rename('Stable_Rate'), on=['Test', 'Version'], how='left')

    df.to_csv(config.PATH_FILE_GENERATE_NFF, index=False)


def calculate_confidence(e=0.05, z=1.65):
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)

    df['Confidence'] = (z ** 2) * df['Stable_Rate'] * (1 - df['Stable_Rate']) / (e ** 2)

    df.to_csv(config.PATH_FILE_GENERATE_NFF, index=False)


def calculate_instability():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)

    df['Instability'] = binom.sf(
        df['NFF_Cumulative'] - 1,
        df['Run'],
        df['Stable_Rate']
    )

    df.to_csv(config.PATH_FILE_GENERATE_NFF, index=False)


def calculate_likelihood():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)

    df['Likelihood'] = binom.pmf(
        df['NFF_Cumulative'],
        df['Run'],
        df['Stable_Rate']
    )

    df.to_csv(config.PATH_FILE_GENERATE_NFF, index=False)


def calculate_unstable(e=0.05):
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)

    df_merge = df.groupby(['Test', 'Version'])['Instability'].min().lt(e)

    df = df.merge(df_merge.rename('Unstable'), on=['Test', 'Version'], how='left')

    df.to_csv(config.PATH_FILE_GENERATE_NFF, index=False)
