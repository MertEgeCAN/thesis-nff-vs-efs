import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import config

df = pd.read_csv('../../' + config.PATH_COMPARE)

def plot_heatmap(pivot_data, title, vmin=None, vmax=None):
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_data, annot=True, cmap='cividis', vmin=vmin, vmax=vmax)
    plt.title(title)
    plt.xlabel('NFF Count Trend')
    plt.ylabel('NFF Index Trend')
    plt.tight_layout()
    plt.show()

spearman_pivot = df.pivot(index='y', columns='x', values='difference_spearman')
plot_heatmap(spearman_pivot, 'Relative Difference in Spearman', vmin=-2, vmax=2)

kendall_pivot = df.pivot(index='y', columns='x', values='difference_kendall')
plot_heatmap(kendall_pivot, 'Relative Difference in Kendall', vmin=-2, vmax=2)

hit_pivot = df.pivot(index='y', columns='x', values='difference_hit')
plot_heatmap(hit_pivot, 'Relative Difference in Top-k Hit', vmin=-1, vmax=1)
