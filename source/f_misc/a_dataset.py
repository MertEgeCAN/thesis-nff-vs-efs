import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import to_rgba
import config
import seaborn as sns


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
        alpha = min(0.8, max(0.2, abs(delta) / 100))
        if delta > 0:
            cell.set_facecolor(to_rgba('green', alpha))
        elif delta < 0:
            cell.set_facecolor(to_rgba('red', alpha))

    plt.tight_layout()
    plt.show()


def analyze_verdict_distribution(verdict_folder, group_folder):
    records = []

    for file in os.listdir(verdict_folder):
        if file.endswith(".csv"):
            verdict_df = pd.read_csv(os.path.join(verdict_folder, file))
            group_file_path = os.path.join(group_folder, file)

            if not os.path.exists(group_file_path):
                continue

            group_df = pd.read_csv(group_file_path)

            # Count only relevant verdicts
            fail_count = (verdict_df['VERDICT'] == 'FAIL').sum()
            error_count = (verdict_df['VERDICT'] == 'ERROR').sum()
            skip_count = (verdict_df['VERDICT'] == 'SKIP').sum()

            # Total NFF from group file
            nff_total = group_df['Total_NFF'].sum() if 'Total_NFF' in group_df.columns else 0

            # Extract identifiers
            prefix, suffix = file.replace('.csv', '').split('-')

            records.append([
                prefix, suffix, fail_count, error_count, skip_count, nff_total
            ])

    return pd.DataFrame(
        records,
        columns=["NFF Count Trend", "NFF Index Trend", "FAIL", "ERROR", "SKIP", "Total NFF"]
    )


def plot_verdict_summary(df):
    df = df.copy()
    df = df.fillna(0)

    for col in ["FAIL", "ERROR", "SKIP", "Total NFF"]:
        if col not in df.columns:
            df[col] = 0

    df_sorted = df.sort_values(["FAIL", "ERROR", "SKIP"], ascending=False)
    labels = df_sorted["NFF Count Trend"] + "\n" + df_sorted["NFF Index Trend"]
    y_positions = range(len(df_sorted))

    # Reduce bar height for compact view
    bar_height = 0.22

    # Color-blind safe palette
    colors = {
        "FAIL": "#D55E00",
        "ERROR": "#CC79A7",
        "SKIP": "#F0E442",
        "Total NFF": "#56B4E9"
    }

    # Smaller vertical size per row
    fig_height = len(df_sorted) * 0.35 + 1.2
    fig, ax = plt.subplots(figsize=(10, fig_height))

    # Stacked verdict bars
    bottom = [0] * len(df_sorted)
    for verdict in ["FAIL", "ERROR", "SKIP"]:
        counts = df_sorted[verdict]
        ax.barh(y_positions, counts, height=bar_height, left=bottom, color=colors[verdict], label=verdict)
        bottom = [b + c for b, c in zip(bottom, counts)]

    # Total NFF below
    nff_y_positions = [y - bar_height - 0.04 for y in y_positions]
    ax.barh(nff_y_positions, df_sorted["Total NFF"], height=bar_height * 0.6, color=colors["Total NFF"], alpha=0.8,
            label="Total NFF")

    # Axis labels and text sizing
    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim([0, 1_000_000])
    ax.set_xlabel("Count (up to 1,000,000)", fontsize=10)
    ax.set_title("Verdict Distribution and Total NFF per Trend", fontsize=12, fontweight='bold')
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout(pad=1.0)
    plt.show()

def plot_verdict_summary_compact_vertical(df):
    df = df.copy().fillna(0)

    for col in ["FAIL", "ERROR", "SKIP", "Total NFF"]:
        if col not in df.columns:
            df[col] = 0

    df["Label"] = df["NFF Count Trend"] + "-" + df["NFF Index Trend"]
    df_sorted = df.sort_values(["FAIL", "ERROR", "SKIP"], ascending=False)
    labels = df_sorted["Label"]

    x = range(len(df_sorted))
    bar_width = 0.6

    colors = {
        "FAIL": "#D55E00",
        "ERROR": "#CC79A7",
        "SKIP": "#F0E442",
        "Total NFF": "#56B4E9"
    }

    fig, ax = plt.subplots(figsize=(max(10, len(df_sorted) * 0.45), 5))

    bottom = [0] * len(df_sorted)
    for verdict in ["FAIL", "ERROR", "SKIP"]:
        counts = df_sorted[verdict].tolist()
        ax.bar(x, counts, width=bar_width, bottom=bottom, color=colors[verdict], label=verdict)
        bottom = [b + c for b, c in zip(bottom, counts)]

    # Add Total NFF as a second bar on top, slightly offset
    ax.bar(x, df_sorted["Total NFF"], width=bar_width * 0.5, bottom=[-max(bottom) * 0.1] * len(df_sorted),
           color=colors["Total NFF"], alpha=0.9, label="Total NFF")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=10)
    ax.set_ylim([-max(bottom) * 0.2, 1_000_000])
    ax.set_ylabel("Count")
    ax.set_title("Verdict Breakdown (Compact Vertical)", fontsize=13)
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.show()


def plot_verdict_table(df):
    df = df.copy()
    df = df.fillna(0)

    # Filter and reorder columns
    columns_to_display = ["NFF Count Trend", "NFF Index Trend", "FAIL", "ERROR", "SKIP", "Total NFF"]
    df = df[columns_to_display]

    # Convert values to int for clarity
    for col in ["FAIL", "ERROR", "SKIP", "Total NFF"]:
        df[col] = df[col].astype(int)

    # Build table data
    column_labels = ["Trend", "Index", "FAIL", "ERROR", "SKIP", "NFF"]
    cell_text = df.values.tolist()

    fig, ax = plt.subplots(figsize=(12, len(df) * 0.4 + 2))
    ax.axis("off")

    # Create color map row-wise for easier visual distinction
    row_colors = ["#f9f9f9" if i % 2 == 0 else "#e6f2ff" for i in range(len(df))]

    table = ax.table(
        cellText=cell_text,
        colLabels=column_labels,
        cellLoc="center",
        loc="center",
        rowColours=row_colors
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.3)

    ax.set_title("Verdict Summary Table", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()

def plot_aggregated_trend_grouped_bars(df):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    df = df.copy().fillna(0)

    for col in ["FAIL", "ERROR", "SKIP", "Total NFF"]:
        if col not in df.columns:
            df[col] = 0

    # Custom desired order
    custom_order = [
        "decrease_exponential",
        "decrease",
        "uniform",
        "increase",
        "increase_exponential"
    ]

    # Convert NFF Index Trend to categorical with order
    df["NFF Index Trend"] = pd.Categorical(df["NFF Index Trend"], categories=custom_order, ordered=True)

    # Group and average
    df_grouped = df.groupby("NFF Index Trend")[["FAIL", "ERROR", "SKIP", "Total NFF"]].mean().reset_index()
    df_grouped = df_grouped.sort_values("NFF Index Trend")

    # Plot setup
    x_labels = df_grouped["NFF Index Trend"].tolist()
    x = np.arange(len(x_labels))
    bar_width = 0.2

    # Color-blind friendly palette
    colors = {
        "FAIL": "#D55E00",
        "ERROR": "#CC79A7",
        "SKIP": "#F0E442",
        "Total NFF": "#56B4E9"
    }

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot grouped bars side-by-side
    ax.bar(x - 1.5*bar_width, df_grouped["FAIL"], width=bar_width, color=colors["FAIL"], label="FAIL")
    ax.bar(x - 0.5*bar_width, df_grouped["ERROR"], width=bar_width, color=colors["ERROR"], label="ERROR")
    ax.bar(x + 0.5*bar_width, df_grouped["SKIP"], width=bar_width, color=colors["SKIP"], label="SKIP")
    ax.bar(x + 1.5*bar_width, df_grouped["Total NFF"], width=bar_width, color=colors["Total NFF"], label="Total NFF")

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=11)
    ax.set_ylim([0, 1_000_000])
    ax.set_ylabel("Average Count per Index")
    ax.set_title("Grouped Average Verdict Counts per NFF Index Trend", fontsize=13)
    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.show()



def summarize_release_rates_grouped_by_index(folder_path):
    import os
    import pandas as pd

    grouped = {}

    for file in os.listdir(folder_path):
        if not file.endswith('.csv'):
            continue

        try:
            _, index_trend = file.replace('.csv', '').split('-')
        except ValueError:
            continue  # Skip malformed filenames

        df = pd.read_csv(os.path.join(folder_path, file))
        rate = df['Rate'].mean()
        stable_rate = df['Stable_Rate'].mean()

        if index_trend not in grouped:
            grouped[index_trend] = {"rates": [], "stable_rates": []}

        grouped[index_trend]["rates"].append(rate)
        grouped[index_trend]["stable_rates"].append(stable_rate)

    # Aggregate per index
    records = []
    for index_trend, values in grouped.items():
        avg_rate = sum(values["rates"]) / len(values["rates"])
        avg_stable = sum(values["stable_rates"]) / len(values["stable_rates"])
        delta = avg_stable - avg_rate
        records.append([index_trend, round(avg_rate, 4), round(avg_stable, 4), round(delta, 4)])

    return pd.DataFrame(records, columns=["NFF Index Trend", "Average Rate", "Average Stable Rate", "Delta (%)"])

from matplotlib.colors import to_rgba
import matplotlib.pyplot as plt

def plot_summary_table_2(df):
    fig, ax = plt.subplots(figsize=(8, len(df) * 0.5 + 1))
    ax.axis('off')

    table_data = df.values.tolist()
    column_labels = df.columns.tolist()

    table = ax.table(cellText=table_data,
                     colLabels=column_labels,
                     loc='center',
                     cellLoc='center',
                     colLoc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.1, 1.3)

    # Conditional coloring on Delta (%)
    for i, delta in enumerate(df["Delta (%)"]):
        cell = table[(i + 1, 3)]  # column index 3 = Delta
        alpha = min(0.8, max(0.2, abs(delta) / 100))
        if delta > 0:
            cell.set_facecolor(to_rgba('green', alpha))
        elif delta < 0:
            cell.set_facecolor(to_rgba('red', alpha))

    plt.tight_layout()
    plt.show()

def plot_aggregated_trend_grouped_bars_2(df):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    df = df.copy().fillna(0)

    for col in ["FAIL", "ERROR", "SKIP", "Total NFF"]:
        if col not in df.columns:
            df[col] = 0

    # Group FIRST by original string
    df_grouped = df.groupby("NFF Index Trend")[["FAIL", "ERROR", "SKIP", "Total NFF"]].mean().reset_index()

    # Define custom order
    custom_order = [
        "decrease_exponential",
        "decrease",
        "uniform",
        "increase",
        "increase_exponential"
    ]

    # Filter only those in order list (to avoid unexpected labels like 'increase_sudden')
    df_grouped = df_grouped[df_grouped["NFF Index Trend"].isin(custom_order)]

    # Apply categorical order
    df_grouped["NFF Index Trend"] = pd.Categorical(df_grouped["NFF Index Trend"], categories=custom_order, ordered=True)
    df_grouped = df_grouped.sort_values("NFF Index Trend")

    # Plot setup
    x_labels = df_grouped["NFF Index Trend"].tolist()
    x = np.arange(len(x_labels))
    bar_width = 0.2

    colors = {
        "FAIL": "#D55E00",
        "ERROR": "#CC79A7",
        "SKIP": "#F0E442",
        "Total NFF": "#56B4E9"
    }

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(x - 1.5*bar_width, df_grouped["FAIL"], width=bar_width, color=colors["FAIL"], label="FAIL")
    ax.bar(x - 0.5*bar_width, df_grouped["ERROR"], width=bar_width, color=colors["ERROR"], label="ERROR")
    ax.bar(x + 0.5*bar_width, df_grouped["SKIP"], width=bar_width, color=colors["SKIP"], label="SKIP")
    ax.bar(x + 1.5*bar_width, df_grouped["Total NFF"], width=bar_width, color=colors["Total NFF"], label="Total NFF")

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=11)
    ax.set_ylim([0, 1_000_000])
    ax.set_ylabel("Average Count per Index")
    ax.set_title("Grouped Average Verdict Counts per NFF Index Trend", fontsize=13)
    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_aggregated_count_trend_grouped_bars_3(df):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    df = df.copy().fillna(0)

    for col in ["FAIL", "ERROR", "SKIP", "Total NFF"]:
        if col not in df.columns:
            df[col] = 0

    # Group by NFF Count Trend (not Index)
    df_grouped = df.groupby("NFF Count Trend")[["FAIL", "ERROR", "SKIP", "Total NFF"]].mean().reset_index()

    # Custom order for Count Trends
    custom_order = [
        "decrease_exponential",
        "decrease",
        "uniform",
        "increase",
        "increase_exponential"
    ]

    # Filter to include only known trends
    df_grouped = df_grouped[df_grouped["NFF Count Trend"].isin(custom_order)]

    # Sort using categorical ordering
    df_grouped["NFF Count Trend"] = pd.Categorical(df_grouped["NFF Count Trend"], categories=custom_order, ordered=True)
    df_grouped = df_grouped.sort_values("NFF Count Trend")

    # Plot setup
    x_labels = df_grouped["NFF Count Trend"].tolist()
    x = np.arange(len(x_labels))
    bar_width = 0.2

    # Color-blind safe palette
    colors = {
        "FAIL": "#D55E00",
        "ERROR": "#CC79A7",
        "SKIP": "#F0E442",
        "Total NFF": "#56B4E9"
    }

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(x - 1.5*bar_width, df_grouped["FAIL"], width=bar_width, color=colors["FAIL"], label="FAIL")
    ax.bar(x - 0.5*bar_width, df_grouped["ERROR"], width=bar_width, color=colors["ERROR"], label="ERROR")
    ax.bar(x + 0.5*bar_width, df_grouped["SKIP"], width=bar_width, color=colors["SKIP"], label="SKIP")
    ax.bar(x + 1.5*bar_width, df_grouped["Total NFF"], width=bar_width, color=colors["Total NFF"], label="Total NFF")

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=14)
    ax.set_ylim([0, 1_000_000])
    ax.set_ylabel("Average Count of Occurrence in Suite", fontsize=12)
    ax.set_title("Average NFF and  Verdict Counts per NFF Count Trend", fontsize=14)
    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.show()


# Main execution
# df_summary = summarize_release_rates("../../" + config.FOLDER_GROUP)
# plot_summary_table(df_summary)


df_summary = summarize_release_rates_grouped_by_index("../../" + config.PATH_FOLDER_GROUP)
plot_summary_table_2(df_summary)

df_verdict = analyze_verdict_distribution("../../" + config.PATH_FOLDER_RAW, "../../" + config.PATH_FOLDER_GROUP)
plot_verdict_table(df_verdict)
# plot_verdict_summary(df_verdict)
# plot_verdict_summary_compact_vertical(df_verdict)
plot_aggregated_count_trend_grouped_bars_3(df_verdict)

# plot_verdict_heatmap(df_verdict)        # 2D matrix view (new)
