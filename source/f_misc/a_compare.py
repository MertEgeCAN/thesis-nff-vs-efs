import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import config

df = pd.read_csv('../../' + config.PATH_FILE_COMPARE)

def plot_heatmap(pivot_data, title, vmin=None, vmax=None):
    plt.figure(figsize=(16, 8))
    sns.heatmap(
        pivot_data,
        annot=True,
        annot_kws={"size": 20, "weight": "bold"},
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
plot_heatmap(spearman_pivot, 'Absolute Score Difference in Spearman (NFF - EFS)', vmin=-1, vmax=1)

kendall_pivot = df.pivot(index='y', columns='x', values='difference_kendall')
plot_heatmap(kendall_pivot, 'Absolute Score Difference in Kendall (NFF - EFS)', vmin=-1, vmax=1)

hit_pivot = df.pivot(index='y', columns='x', values='difference_hit')
plot_heatmap(hit_pivot, 'Absolute Score Difference in Top-k Hit (NFF - EFS)', vmin=-1, vmax=1)

# Convert each to pivoted form
bino_spear_pivot = df.pivot(index='y', columns='x', values='nff_spearman')
efs_spear_pivot = df.pivot(index='y', columns='x', values='efs_spearman')

bino_kendall_pivot = df.pivot(index='y', columns='x', values='nff_kendall')
efs_kendall_pivot = df.pivot(index='y', columns='x', values='efs_kendall')

bino_hit_pivot = df.pivot(index='y', columns='x', values='nff_hit')
efs_hit_pivot = df.pivot(index='y', columns='x', values='efs_hit')

# Plot each heatmap
plot_heatmap(bino_spear_pivot, "NFF Spearman Score")
plot_heatmap(efs_spear_pivot, "EFS Spearman Score")

plot_heatmap(bino_kendall_pivot, "NFF Kendall Score")
plot_heatmap(efs_kendall_pivot, "EFS Kendall Score")

plot_heatmap(bino_hit_pivot, "NFF Top-k Hit")
plot_heatmap(efs_hit_pivot, "EFS Top-k Hit")

import pandas as pd

# Load dataset
df = pd.read_csv('../../' + config.PATH_FILE_COMPARE)

# Define metric groups
nff_metrics = ['nff_spearman', 'nff_kendall', 'nff_hit']
efs_metrics = ['efs_spearman', 'efs_kendall', 'efs_hit']
diff_metrics = ['difference_spearman', 'difference_kendall', 'difference_hit']

def plot_heatmap2(dataframe, title):
    if isinstance(dataframe, pd.DataFrame) and not dataframe.empty:
        plt.figure(figsize=(10, 6))
        sns.heatmap(dataframe, annot=True, cmap="Reds", vmin=-1, vmax=1)
        plt.title(f"Heatmap - {title}")
        plt.tight_layout()
        plt.show()
    else:
        print(f"[SKIP] Cannot plot heatmap for '{title}': Input is not a valid DataFrame or is empty.")

# Example heatmaps for 'x' grouping
plot_heatmap2(df.groupby('x')[nff_metrics].mean(), "Table 1: Group by X - NFF Metrics")
plot_heatmap2(df.groupby('x')[efs_metrics].mean(), "Table 2: Group by X - EFS Metrics")
plot_heatmap2(df.groupby('x')[diff_metrics].mean(), "Table 7: Group by X - Difference Metrics")

# Example heatmaps for 'y' grouping
plot_heatmap2(df.groupby('y')[nff_metrics].mean(), "Table 10: Group by Y - NFF Metrics")
plot_heatmap2(df.groupby('y')[efs_metrics].mean(), "Table 11: Group by Y - EFS Metrics")
plot_heatmap2(df.groupby('y')[diff_metrics].mean(), "Table 16: Group by Y - Difference Metrics")