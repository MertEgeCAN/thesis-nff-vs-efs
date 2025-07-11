import time

import pandas as pd
from matplotlib import pyplot as plt

import config


def plot_test():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)

    df_test = df.groupby('Test')['P_Flaky_Test'].mean()

    plt.bar(df_test.index, sorted(df_test))

    plt.xlabel('Test')
    plt.ylabel('Flakiness')
    plt.title('Flakiness per Test')

    plt.savefig(config.PATH_FILE_VISUAL_PRE_TEST, dpi=300)
    plt.close()


def plot_version():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)

    df_version = df[df['Test'] == 1].groupby(['Version'])['P_Flaky_Version'].mean()

    plt.bar(df_version.index, df_version)

    plt.xlabel('Version')
    plt.ylabel('Flakiness')
    plt.title('Flakiness per Version')

    plt.savefig(config.PATH_FILE_VISUAL_PRE_VERSION, dpi=300)
    plt.close()


def plot_run():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)

    df_run = df[(df['Test'] == 1) & (df['Version'] == 1)].groupby(['Run'])['P_Flaky_Run'].mean()

    plt.bar(df_run.index, df_run)

    plt.xlabel('Run')
    plt.ylabel('Flakiness')
    plt.title('Flakiness per Run')

    plt.savefig(config.PATH_FILE_VISUAL_PRE_RUN, dpi=300)
    plt.close()


def pre_plot():
    start = time.time()
    plot_test()
    end = time.time()
    print(f"        -------- plot_test finished in {end - start:.4f} seconds")

    start = time.time()
    plot_version()
    end = time.time()
    print(f"        -------- plot_version finished in {end - start:.4f} seconds")

    start = time.time()
    plot_run()
    end = time.time()
    print(f"        -------- plot_run finished in {end - start:.4f} seconds")
