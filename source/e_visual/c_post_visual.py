import time

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import config


def plot_run():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)

    df_run = df[(df['Test'] == 1) & (df['Version'] == 1)].groupby(['Run'])['P_Flaky_Run'].mean()

    plt.bar(df_run.index, df_run)

    plt.xlabel('Run')
    plt.ylabel('Flakiness')
    plt.title('Flakiness per Run')

    plt.savefig(config.PATH_FILE_VISUAL_PRE_RUN, dpi=300)
    plt.close()

def post_plot():
    start = time.time()
    plot_run()
    end = time.time()
    print(f"plot_run finished in {end - start:.4f} seconds")