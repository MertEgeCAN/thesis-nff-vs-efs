import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import config

df = pd.read_csv('../../' + config.PATH_FILE_COMPARE)

def plot_heatmap(pivot_data, title, vmin=-1, vmax=1):
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
    plt.xlabel('Version Trend', fontsize=16, fontweight='bold')
    plt.ylabel('Run Trend', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=16)  # axis tick labels
    plt.xticks(fontsize=16, rotation=90)  # axis tick labels
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig("../../output/3_plot/4_compare/" + title + ".png", dpi=300)
    plt.close()

spearman_pivot = df.pivot(index='run', columns='version', values='difference_spearman')
plot_heatmap(spearman_pivot, 'Absolute Score Difference in Spearman (NFF - EFS)', vmin=-1, vmax=1)

kendall_pivot = df.pivot(index='run', columns='version', values='difference_kendall')
plot_heatmap(kendall_pivot, 'Absolute Score Difference in Kendall (NFF - EFS)', vmin=-1, vmax=1)

hit_pivot = df.pivot(index='run', columns='version', values='difference_hit')
plot_heatmap(hit_pivot, 'Absolute Score Difference in Top-k Hit (NFF - EFS)', vmin=-1, vmax=1)

# Convert each to pivoted form
bino_spear_pivot = df.pivot(index='run', columns='version', values='nff_spearman')
efs_spear_pivot = df.pivot(index='run', columns='version', values='efs_spearman')

bino_kendall_pivot = df.pivot(index='run', columns='version', values='nff_kendall')
efs_kendall_pivot = df.pivot(index='run', columns='version', values='efs_kendall')

bino_hit_pivot = df.pivot(index='run', columns='version', values='nff_hit')
efs_hit_pivot = df.pivot(index='run', columns='version', values='efs_hit')

# Plot each heatmap
plot_heatmap(bino_spear_pivot, "NFF Spearman Scores")
plot_heatmap(efs_spear_pivot, "EFS Spearman Scores")

plot_heatmap(bino_kendall_pivot, "NFF Kendall Scores")
plot_heatmap(efs_kendall_pivot, "EFS Kendall Scores")

plot_heatmap(bino_hit_pivot, "NFF Top-k Hit Scores")
plot_heatmap(efs_hit_pivot, "EFS Top-k HitScores")

import pandas as pd

# Load dataset
df = pd.read_csv('../../' + config.PATH_FILE_COMPARE)

# Define metric groups
nff_metrics = ['nff_spearman', 'nff_kendall', 'nff_hit']
efs_metrics = ['efs_spearman', 'efs_kendall', 'efs_hit']
diff_metrics = ['difference_spearman', 'difference_kendall', 'difference_hit']

def plot_heatmap2(dataframe, title, trend):
    if isinstance(dataframe, pd.DataFrame) and not dataframe.empty:
        plt.figure(figsize=(10, 6))
        sns.heatmap(dataframe, annot=True, cmap="PuOr", vmin=-1, vmax=1)
        plt.title(f"{title}")
        plt.ylabel(trend, rotation=90)
        plt.tight_layout()
        plt.savefig("../../output/3_plot/4_compare/" + title + ".png", dpi=300)
        plt.close()
    else:
        print(f"[SKIP] Cannot plot heatmap for '{title}': Input is not a valid DataFrame or is empty.")

# Example heatmaps for 'x' grouping
plot_heatmap2(df.groupby('version')[nff_metrics].mean(), "Version Trends - Average NFF Scores", "Version Trend")
plot_heatmap2(df.groupby('version')[efs_metrics].mean(), "Version Trends - Average EFS Scores", "Version Trend")
plot_heatmap2(df.groupby('version')[diff_metrics].mean(),"Version Trends - Average Difference Scores", "Version Trend")

# Example heatmaps for 'y' grouping
plot_heatmap2(df.groupby('run')[nff_metrics].mean(), "Run Trends - Average NFF Scores", "Run Trends")
plot_heatmap2(df.groupby('run')[efs_metrics].mean(), "Run Trends - Average EFS Scores", "Run Trends")
plot_heatmap2(df.groupby('run')[diff_metrics].mean(),"Run Trends - Average Difference Scores", "Run Trends")