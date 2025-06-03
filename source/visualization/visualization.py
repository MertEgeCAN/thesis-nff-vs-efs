import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import config


def plot_rate():
    df_group = pd.read_csv(config.PATH_GROUP)

    for release in df_group['Release'].unique()[1:]:
        release_group = df_group[df_group['Release'] == release]

        x = np.sort(release_group['Rate'])
        y = np.arange(len(x)) / len(x) * 100
        plt.plot(x, y, label=f'Release {release}')

    plt.title(config.PATH_FILE)
    plt.xlim(0, 0.5)
    plt.ylim(0, 100)
    plt.xlabel('Flake Rate')
    plt.ylabel('Percentage of Tests')
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_RATE, dpi=300, bbox_inches='tight')
    plt.close()


def plot_stable_rate():
    df_group = pd.read_csv(config.PATH_GROUP)

    for release in df_group['Release'].unique()[1:]:
        release_group = df_group[df_group['Release'] == release]

        x = np.sort(release_group['Release_Stable_Rate'])
        y = np.arange(len(x)) / len(x) * 100
        plt.plot(x, y, label=f'Release {release}')

    plt.title(config.PATH_FILE)
    plt.xlim(0, 0.5)
    plt.ylim(0, 100)
    plt.xlabel('Stable Rate')
    plt.ylabel('Percentage of Tests')
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_STABLE, dpi=300, bbox_inches='tight')
    plt.close()


def plot_confidence():
    df_group = pd.read_csv(config.PATH_GROUP)

    for release in df_group['Release'].unique()[1:]:
        release_group = df_group[df_group['Release'] == release]

        y = [len(release_group[release_group['Confidence'] < i]) / config.TESTS * 100 for i in range(config.RUNS)]
        x = np.linspace(0, config.RUNS, len(y))
        plt.plot(x, y, label=f"Release {release}")

    plt.title(config.PATH_FILE)
    plt.xlim(0, config.RUNS)
    plt.ylim(0, 100)
    plt.xlabel("Run")
    plt.ylabel("Percentage of Tests with Confidence >= 95%")
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_CONFIDENCE, dpi=300, bbox_inches='tight')
    plt.close()


def plot_instability():
    df_raw = pd.read_csv(config.PATH_RAW)

    for release in df_raw['Release'].unique()[1:]:
        release_raw = df_raw[df_raw['Release'] == release]

        y = [len(release_raw[(release_raw['Run'] == i) & (release_raw['Unstable'] == True)]) / config.TESTS * 100 for i in range(config.RUNS)]
        x = np.linspace(0, config.RUNS, len(y))
        plt.plot(x, y, label=f"Release {release}")

    plt.title(config.PATH_FILE)
    plt.xlim(0, config.RUNS)
    plt.ylim(0, 100)
    plt.xlabel("Run")
    plt.ylabel("Sum of Significant Cumulative Instability Changes")
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_INSTABILITY, dpi=300, bbox_inches='tight')
    plt.close()


def plot_savings_1():
    df_raw = pd.read_csv(config.PATH_RAW)

    for release in df_raw['Release'].unique()[1:]:
        release_raw = df_raw[df_raw['Release'] == release]

        y = [len(release_raw[(release_raw['Run'] == i) & (release_raw['Current_NFF'] > 0)]) / config.TESTS * 100 for i in range(config.RUNS)]
        x = np.linspace(0, config.RUNS, len(y))
        plt.plot(x, y, label=f"Release {release}")

    plt.title(config.PATH_FILE)
    plt.xlim(0, config.RUNS)
    plt.ylim(0, 100)
    plt.xlabel("Run")
    plt.ylabel("Cumulative Percentage of Failed Tests")
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_SAVINGS_1, dpi=300, bbox_inches='tight')
    plt.close()


def plot_savings_2():
    df_raw = pd.read_csv(config.PATH_RAW)

    for release in df_raw['Release'].unique()[1:]:
        release_raw = df_raw[df_raw['Release'] == release]

        y = [len(release_raw[(release_raw['Run'] == i) & (release_raw['Current_NFF'] > 0) & (release_raw['Unstable']  == False)]) / config.TESTS * 100 for i in range(config.RUNS)]
        x = np.linspace(0, config.RUNS, len(y))
        plt.plot(x, y, label=f"Release {release}")

    plt.title(config.PATH_FILE)
    plt.xlim(0, config.RUNS)
    plt.ylim(0, 100)
    plt.xlabel("Run")
    plt.ylabel("Cumulative Percentage of Savings")
    plt.legend()
    plt.grid(True)
    plt.savefig(config.PATH_SAVINGS_2, dpi=300, bbox_inches='tight')
    plt.close()
