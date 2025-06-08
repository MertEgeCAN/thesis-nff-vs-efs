import csv
from pathlib import Path

import pandas as pd
from scipy.stats import spearmanr, kendalltau

import config


def calculate_rank_efs():
    data_efs = pd.read_csv(next(Path(config.PATH_EFS).rglob("*.csv")))

    data_efs = data_efs[data_efs['VERSIONS'] == '{{v' + str(config.RELEASES - 1) + '}}'].copy()
    data_efs["Test"] = data_efs["TEST_NAME"].str.extract(r'tc.*?(\d{1,3})(?!\d)').astype(int)

    score_efs = data_efs[["Test", "FLAKINESS_SCORE"]]
    score_efs = score_efs[["Test", "FLAKINESS_SCORE"]].sort_values(by="FLAKINESS_SCORE", ascending=False)

    return score_efs


def calculate_rank_binomial():
    data_binomial = pd.read_csv(config.PATH_BINOM)

    data_binomial = data_binomial.reset_index(drop=True)
    data_binomial["Row"] = data_binomial.index

    score_binomial = data_binomial.groupby("Test")["Row"].mean().reset_index()
    score_binomial["BINOMIAL_SCORE"] = score_binomial["Row"] / score_binomial["Row"].max()
    score_binomial = score_binomial[["Test", "BINOMIAL_SCORE"]].sort_values(by="BINOMIAL_SCORE")

    return score_binomial


def calculate_rank_truth():
    group_data = pd.read_csv(config.PATH_GROUP)

    truth = group_data[group_data["Release"] == group_data["Release"].max()]
    truth = truth[["Test", "Rate", "Stable_Rate"]].sort_values(by="Rate", ascending=False)

    return truth


def calculate_score(truth, order):
    def top_k_hit(truth, order, k=100):
        truth_top = set(truth.head(k)["Test"])
        order_top = set(order.head(k)["Test"])
        return len(truth_top & order_top) / k

    spearman = spearmanr(truth["Test"], order["Test"]).correlation
    kendall = kendalltau(truth["Test"], order["Test"]).correlation
    hit = top_k_hit(truth, order)

    return spearman, kendall, hit


def compare():
    rank_truth = calculate_rank_truth()
    rank_binomial = calculate_rank_binomial()
    rank_efs = calculate_rank_efs()

    binomial_spearman, binomial_kendall, binomial_hit = calculate_score(rank_truth, rank_binomial)
    efs_spearman, efs_kendall, efs_hit = calculate_score(rank_truth, rank_efs)

    x, y = config.FILE.split('-')
    difference_spearman = binomial_spearman - efs_spearman
    difference_kendall = binomial_kendall - efs_kendall
    difference_hit = binomial_hit - efs_hit

    data_row = {
        'x': x,
        'y': y,
        'binomial_spearman': binomial_spearman,
        'binomial_kendall': binomial_kendall,
        'binomial_hit': binomial_hit,
        'efs_spearman': efs_spearman,
        'efs_kendall': efs_kendall,
        'efs_hit': efs_hit,
        'difference_spearman': difference_spearman,
        'difference_kendall': difference_kendall,
        'difference_hit': difference_hit
    }

    with open(config.PATH_COMPARE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=config.COMPARE_HEADER)
        writer.writerow(data_row)
