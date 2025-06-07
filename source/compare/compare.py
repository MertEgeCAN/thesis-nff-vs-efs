from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, kendalltau

import config


def calculate_flaky_rank(flaky_data):
    latest_version = '{{v' + str(config.RELEASES - 1) + '}}'
    flaky_data = flaky_data[flaky_data['VERSIONS'] == latest_version].copy()
    flaky_data["Test"] = flaky_data["TEST_NAME"].str.extract(r'tc.*?(\d{1,3})(?!\d)').astype(int)
    flake_score = flaky_data[["Test", "FLAKINESS_SCORE"]]
    return flake_score[["Test", "FLAKINESS_SCORE"]].sort_values(by="FLAKINESS_SCORE", ascending=False)

def calculate_binom_rank(binom_data):
    binom_data = binom_data.reset_index(drop=True)
    binom_data["Row"] = binom_data.index
    avg_df = binom_data.groupby("Test")["Row"].mean().reset_index()
    avg_df["BINOMIAL_SCORE"] = avg_df["Row"] / avg_df["Row"].max()
    return avg_df[["Test", "BINOMIAL_SCORE"]].sort_values(by="BINOMIAL_SCORE")


def extract_ground_truth(group_data):
    latest = group_data[group_data["Release"] == group_data["Release"].max()]
    return latest[["Test", "Rate", "Stable_Rate"]].sort_values(by="Stable_Rate", ascending=False)


def compare_ranking_orders(truth, order, name=""):
    spearman = spearmanr(truth["Test"], order["Test"]).correlation
    kendall = kendalltau(truth["Test"], order["Test"]).correlation

    def top_k_hit(truth, order, k):
        truth_top = set(truth.head(k)["Test"])
        order_top = set(order.head(k)["Test"])
        return len(truth_top & order_top) / k

    hit = top_k_hit(truth, order, k=100)

    print(f"[{name}] ρ: {spearman:+.3f}, τ: {kendall:+.3f}, Top‑100 Hit: {hit:.2f}")

    return spearman, kendall, hit

def compare(group_data, binom_data, flaky_data, x, y):
    truth_order = extract_ground_truth(group_data)
    binom_order = calculate_binom_rank(binom_data)
    flaky_order = calculate_flaky_rank(flaky_data)

    binom_score_1, binom_score_2, binom_score_3 = compare_ranking_orders(truth_order, binom_order, name="Binomial")
    flaky_score_1, flaky_score_2, flaky_score_3 = compare_ranking_orders(truth_order, flaky_order, name="Flakiness")

    return (x, y, binom_score_1, flaky_score_1), (x, y, binom_score_2, flaky_score_2), (x, y, binom_score_3, flaky_score_3)

def plot_ranking_heatmaps(results, title_suffix="Score Heatmaps"):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np

    # Build axis labels
    x_labels = sorted(set(x for x, _, _, _ in results))
    y_labels = sorted(set(y for _, y, _, _ in results))

    # Initialize dataframes
    df_binom = pd.DataFrame(index=x_labels, columns=y_labels)
    df_flaky = pd.DataFrame(index=x_labels, columns=y_labels)

    for x, y, binom_score, flaky_score in results:
        df_binom.at[x, y] = binom_score
        df_flaky.at[x, y] = flaky_score

    df_binom = df_binom.astype(float)
    df_flaky = df_flaky.astype(float)

    # Create annotation DataFrames with NaNs replaced
    annot_binom = df_binom.copy().round(2).astype(str)
    annot_flaky = df_flaky.copy().round(2).astype(str)

    annot_binom = annot_binom.where(~df_binom.isna(), other="–")
    annot_flaky = annot_flaky.where(~df_flaky.isna(), other="–")

    # Plotting
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.heatmap(df_binom, annot=annot_binom, fmt='', center=0,
                cmap="icefire", vmin=-1, vmax=1, linewidths=0.5, linecolor='gray')
    plt.title(f"Binomial {title_suffix}")

    plt.subplot(1, 2, 2)
    sns.heatmap(df_flaky, annot=annot_flaky, fmt='', center=0,
                cmap="icefire", vmin=-1, vmax=1, linewidths=0.5, linecolor='gray')
    plt.title(f"Flakiness {title_suffix}")

    plt.tight_layout()
    plt.show()




def main():
    group_list = list(Path("../../data/group").rglob("*.csv"))
    binom_list = list(Path("../../data/binom").rglob("*.csv"))
    flaky_list = list(Path("../../data/OUTPUT").rglob("*.csv"))

    binom_map = {f.stem: f for f in binom_list}
    group_map = {f.stem: f for f in group_list}

    output_base = Path("../../data/OUTPUT")
    flaky_map = {}
    for f in flaky_list:
        if "BUILD_" in f.name:
            flaky_map[f.relative_to(output_base).parts[0]] = f

    common_keys = sorted(set(binom_map) & set(flaky_map) & set(group_map))

    spearman_results = []
    kendall_results = []
    hit_results = []
    for key in common_keys:
        binom_data = pd.read_csv(binom_map[key])
        flaky_data = pd.read_csv(flaky_map[key])
        group_data = pd.read_csv(group_map[key])

        x, y = key.split("-")

        print(f"\n--- {key} ---")
        spearman_result, kendall_result, hit_result = compare(group_data, binom_data, flaky_data, x, y)
        spearman_results.append(spearman_result)
        kendall_results.append(kendall_result)
        hit_results.append(hit_result)

    plot_ranking_heatmaps(spearman_results)
    plot_ranking_heatmaps(kendall_results)
    plot_ranking_heatmaps(hit_results)


if __name__ == "__main__":
    main()
