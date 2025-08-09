import time

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import config


def plot_truth_test():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)
    df = df.groupby('Test')['P_Flaky_Test'].mean().sort_values().reset_index()

    fig, ax = plt.subplots(figsize=(5, 15))

    ax.barh(df['P_Flaky_Test'], width=df.index)
    ax.set_yticks(df.index, df['Test'], fontsize=8)

    ax.set_xlabel('Test')
    ax.set_ylabel('Flakiness Probability')
    ax.set_title('Average Flakiness Probability per Test')

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_TRUTH_TEST, dpi=300)
    plt.close(fig)


def plot_truth_version():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)
    df = df.groupby(['Version'])['P_Flaky_Version'].mean()

    fig, ax = plt.subplots()

    ax.plot(df.index, df.values, marker="o")
    ax.set_xticks(df.index)

    ax.set_ylim(0, 0.3)
    ax.set_xlabel('Version')
    ax.set_ylabel('Flakiness Probability')
    ax.set_title('Average Flakiness Probability per Version')

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_TRUTH_VERSION, dpi=300)
    plt.close(fig)


def plot_truth_run():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)
    df = df.groupby(['Run'])['P_Flaky_Run'].mean()

    fig, ax = plt.subplots()

    ax.scatter(df.index, df.values)

    ax.set_ylim(0, 0.2)
    ax.set_xlabel('Run')
    ax.set_ylabel('Flakiness Probability')
    ax.set_title('Average Flakiness Probability per Run')

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_TRUTH_RUN, dpi=300)
    plt.close(fig)


def plot_nff_test():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df.groupby("Test")["NFF_Rate"].mean().sort_values().reset_index()

    fig, ax = plt.subplots(figsize=(5, 15))

    ax.bar(df['NFF_Rate'], df.index)
    ax.set_xticks(df.index, df['Test'], fontsize=8)

    ax.set_xlabel("Test")
    ax.set_ylabel("NFF Rate")
    ax.set_title("Average NFF Rate per Test")

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_NFF_TEST, dpi=300)
    plt.close(fig)


def plot_nff_version():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df.groupby("Version")["NFF_Rate"].mean()

    fig, ax = plt.subplots()

    ax.plot(df.index, df.values, marker="o")
    ax.set_xticks(df.index)

    ax.set_ylim(0, 0.2)
    ax.set_xlabel("Version")
    ax.set_ylabel("NFF Rate")
    ax.set_title("Average NFF Rate per Version")

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_NFF_VERSION, dpi=300)
    plt.close(fig)


def plot_nff_run():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df.groupby("Run")["NFF_Rate"].mean()

    fig, ax = plt.subplots()

    ax.scatter(df.index, df.values)

    ax.set_ylim(0, 0.15)
    ax.set_xlabel("Run")
    ax.set_ylabel("NFF Rate")
    ax.set_title("Average NFF Rate per Run")

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_NFF_RUN, dpi=300)
    plt.close(fig)


def plot_nff_test_stable():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df.groupby("Test")["Stable_NFF_Rate"].mean().sort_values().reset_index()

    fig, ax = plt.subplots(figsize=(5, 15))

    ax.bar(df['Stable_NFF_Rate'], df.index)
    ax.set_xticks(df.index, df['Test'], rotation=90, fontsize=8)

    ax.set_xlabel("Test")
    ax.set_ylabel("Stable NFF Rate")
    ax.set_title("Average Stable NFF Rate per Test")

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_NFF_TEST_STABLE, dpi=300)
    plt.close(fig)


def plot_nff_version_stable():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df.groupby("Version")["Stable_NFF_Rate"].mean()

    fig, ax = plt.subplots()

    ax.plot(df.index, df.values, marker="o")
    ax.set_xticks(df.index)

    ax.set_ylim(0, 0.1)
    ax.set_xlabel("Version")
    ax.set_ylabel("Stable NFF Rate")
    ax.set_title("Average Stable NFF Rate per Version")

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_NFF_VERSION_STABLE, dpi=300)
    plt.close(fig)


def plot_nff_run_stable():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF_METRIC)
    df = df.groupby("Run")["Stable_NFF_Rate"].mean()

    fig, ax = plt.subplots()

    ax.scatter(df.index, df.values)

    ax.set_ylim(0, 0.15)
    ax.set_xlabel("Run")
    ax.set_ylabel("Stable NFF Rate")
    ax.set_title("Average Stable NFF Rate per Run")

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_NFF_RUN_STABLE, dpi=300)
    plt.close(fig)


def plot_efs_test():
    df = pd.read_csv(config.PATH_FILE_GENERATE_EFS)
    df['TEST_NAME'] = df['TEST_NAME'].str.replace('tc', '').astype(int)
    df['TEST_NAME'] = df['TEST_NAME'] - df['TEST_NAME'].min() + 1
    df = df.groupby(['TEST_NAME', 'VERDICT']).size().unstack(fill_value=0)
    df = df.sort_values(by='SUCCESSFUL', ascending=False)
    df = df.div(df.sum(axis=1), axis=0)

    fig, ax = plt.subplots(figsize=(15, 5))

    order = ['FAIL', 'ERROR', 'SKIP', 'SUCCESSFUL']
    color = {
        'FAIL': 'red',
        'ERROR': 'purple',
        'SKIP': 'gold',
        'SUCCESSFUL': 'green',
    }

    df = df[order]
    df.plot(
        kind='barh',
        stacked=True,
        color=[color[i] for i in order],
        ax=ax
    )

    ax.set_xlabel('Test')
    ax.set_ylabel('Verdict Ratio')
    ax.set_title('Verdict Ratio per Test')

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_EFS_TEST, dpi=300)
    plt.close(fig)


def plot_efs_test_formatted():
    df = pd.read_csv(config.PATH_FILE_GENERATE_EFS_METRIC)
    df['TEST_NAME'] = df['TEST_NAME'].str.replace('tc', '').astype(int)
    df['TEST_NAME'] = df['TEST_NAME'] - df['TEST_NAME'].min() + 1
    df = df.groupby('TEST_NAME')['FLAKINESS_SCORE'].mean().sort_values().reset_index()

    fig, ax = plt.subplots(figsize=(5, 15))

    ax.bar(df['FLAKINESS_SCORE'], df.index)
    ax.set_xticks(df.index, df['TEST_NAME'], fontsize=8)

    ax.set_xlabel('Test')
    ax.set_ylabel('Flakiness Score')
    ax.set_title('Flakiness Score per Test')

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_EFS_TEST_FORMATTED, dpi=300)
    plt.close(fig)


def plot_efs_test_scatter():
    df = pd.read_csv(config.PATH_FILE_GENERATE_EFS)
    df['TEST_NAME'] = df['TEST_NAME'].str.replace('tc', '', regex=False).astype(int)
    df['TEST_NAME'] = df['TEST_NAME'] - df['TEST_NAME'].min() + 1
    df['RUN_INDEX'] = df.groupby('TEST_NAME').cumcount() + 1
    df = df[(df['TEST_NAME'] <= 20) & (df['VERSION_ID'] == "v4")]

    fig, ax = plt.subplots(figsize=(15, 5))

    colors = {
        'FAIL': 'red',
        'ERROR': 'purple',
        'SKIP': 'gold',
        'SUCCESSFUL': 'green',
    }
    df['COLOR'] = df['VERDICT'].map(colors)

    ax.scatter(
        y=df['RUN_INDEX'],
        x=df['TEST_NAME'],
        c=df['COLOR'],
        s=40,
        edgecolors='black',
        linewidths=0.5
    )
    unique_tests = sorted(df['TEST_NAME'].unique())
    ax.set_yticks(unique_tests)
    ax.set_yticklabels(unique_tests)

    ax.set_xlabel('Run')
    ax.set_ylabel('Test')
    ax.set_title('Verdict History of First 20 Tests')

    fig.tight_layout()
    fig.savefig(config.PATH_FILE_VISUAL_EFS_TEST_SCATTER, dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    config.PATH_FILE_GENERATE_TRUTH = "../../output/0_data/0_truth/increase_sudden-decrease_exponential.csv"
    config.PATH_FILE_GENERATE_NFF_METRIC = "../../output/0_data/2_nff_metric/increase_sudden-decrease_exponential.csv"
    config.PATH_FILE_GENERATE_EFS = "../../output/0_data/3_efs/increase_sudden-decrease_exponential.csv"
    config.PATH_FILE_GENERATE_EFS_METRIC = "../../output/0_data/5_efs_metric/increase_sudden-decrease_exponential.csv"

    plot_truth_test()
    plot_truth_version()
    plot_truth_run()

    plot_nff_test()
    plot_nff_version()
    plot_nff_run()

    plot_nff_test_stable()
    plot_nff_version_stable()
    plot_nff_run_stable()

    plot_efs_test()
    plot_efs_test_formatted()
    plot_efs_test_scatter()
