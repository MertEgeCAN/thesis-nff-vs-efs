import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import config

df = pd.read_csv('../../' + config.PATH_COMPARE)

def plot_heatmap(pivot_data, title, vmin=None, vmax=None):
    plt.figure(figsize=(16, 8))
    sns.heatmap(
        pivot_data,
        annot=True,
        annot_kws={"size": 20, "weight": "bold"},  # larger, bolder cell text
        cmap='PuOr',
        vmin=vmin,
        vmax=vmax
    )
    plt.title(title, fontsize=16, fontweight='bold')  # larger, bold title
    plt.xlabel('NFF Count Trend', fontsize=16, fontweight='bold')
    plt.ylabel('NFF Index Trend', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=16)  # axis tick labels
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.show()


spearman_pivot = df.pivot(index='y', columns='x', values='difference_spearman')
plot_heatmap(spearman_pivot, 'Absolute Score Difference in Spearman (NFF - EFS)', vmin=-2, vmax=2)

kendall_pivot = df.pivot(index='y', columns='x', values='difference_kendall')
plot_heatmap(kendall_pivot, 'Absolute Score Difference in Kendall (NFF - EFS)', vmin=-2, vmax=2)

hit_pivot = df.pivot(index='y', columns='x', values='difference_hit')
plot_heatmap(hit_pivot, 'Absolute Score Difference in Top-k Hit (NFF - EFS)', vmin=-1, vmax=1)

# Convert each to pivoted form
bino_spear_pivot = df.pivot(index='y', columns='x', values='binomial_spearman')
efs_spear_pivot = df.pivot(index='y', columns='x', values='efs_spearman')

bino_kendall_pivot = df.pivot(index='y', columns='x', values='binomial_kendall')
efs_kendall_pivot = df.pivot(index='y', columns='x', values='efs_kendall')

bino_hit_pivot = df.pivot(index='y', columns='x', values='binomial_hit')
efs_hit_pivot = df.pivot(index='y', columns='x', values='efs_hit')

# Plot each heatmap
plot_heatmap(bino_spear_pivot, "NFF Spearman Score")
plot_heatmap(efs_spear_pivot, "EFS Spearman Score")

plot_heatmap(bino_kendall_pivot, "NFF Kendall Score")
plot_heatmap(efs_kendall_pivot, "EFS Kendall Score")

plot_heatmap(bino_hit_pivot, "NFF Top-k Hit")
plot_heatmap(efs_hit_pivot, "EFS Top-k Hit")