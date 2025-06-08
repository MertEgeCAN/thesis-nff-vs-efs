import os

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import to_rgba

import config


def summarize_release_rates(folder_path):
    records = []

    for file in os.listdir(folder_path):
        prefix, suffix = file.replace('.csv', '').split('-')

        df = pd.read_csv(os.path.join(folder_path, file))

        rate, stable = df['Rate'].mean(), df['Stable_Rate'].mean()
        delta = stable - rate
        records.append([prefix, suffix, round(rate, 4), round(stable, 4), round(delta, 4)])

    return pd.DataFrame(records, columns=["NFF Count Trend", "NFF Index Trend", "Average Rate", "Average Stable Rate", "Delta (%)"])


def plot_summary_table(df):
    fig, ax = plt.subplots(figsize=(10, len(df) * 0.6 + 1))
    ax.axis('off')

    # Table content and headers
    table_data = df.values.tolist()
    column_labels = df.columns.tolist()

    table = ax.table(cellText=table_data,
                     colLabels=column_labels,
                     loc='center',
                     cellLoc='center',
                     colLoc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.5)

    for i, delta in enumerate(df["Delta (%)"]):
        cell = table[(i + 1, 4)]
        alpha = min(0.8, max(0.2, abs(delta) / 100))  # alpha based on magnitude
        if delta > 0:
            cell.set_facecolor(to_rgba('green', alpha))
        elif delta < 0:
            cell.set_facecolor(to_rgba('red', alpha))

    plt.tight_layout()
    plt.show()


df_summary = summarize_release_rates("../../" + config.FOLDER_GROUP)
plot_summary_table(df_summary)
