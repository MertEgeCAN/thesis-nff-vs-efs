import csv
from pathlib import Path

import pandas as pd
from scipy.stats import spearmanr, kendalltau

import config


def calculate_rank_truth():
    df = pd.read_csv(config.PATH_FILE_GENERATE_TRUTH)

    df = df[df['Version'] == config.MAX_VERSION]
    df = df.groupby('Test')["P_Flaky_Version"].mean().sort_values(ascending=False).reset_index()

    return df


def calculate_rank_nff():
    df = pd.read_csv(config.PATH_FILE_ORDER_NFF)

    df["Row"] = df.index

    df = df.groupby("Order")["Row"].mean().reset_index()
    df = df.sort_values('Row')

    return df


def calculate_rank_efs():
    data_efs = pd.read_csv(next(Path(config.PATH_EFS).rglob("*.csv")))

    data_efs = data_efs[data_efs['VERSIONS'] == '{{v' + str(config.RELEASES - 1) + '}}'].copy()
    data_efs["Test"] = data_efs["TEST_NAME"].str.extract(r'tc.*?(\d{1,3})(?!\d)').astype(int)

    score_efs = data_efs[["Test", "FLAKINESS_SCORE"]]
    score_efs = score_efs[["Test", "FLAKINESS_SCORE"]].sort_values(by="FLAKINESS_SCORE", ascending=False)

    return score_efs


def calculate_score(truth, order):
    def top_k_hit(truth, order):
        k = int(config.MAX_TEST / 10)
        truth_top = set(truth.head(k)["Test"])
        order_top = set(order.head(k)["Order"])
        return len(truth_top & order_top) / k

    spearman = spearmanr(truth["Test"], order["Order"]).correlation
    kendall = kendalltau(truth["Test"], order["Order"]).correlation
    hit = top_k_hit(truth, order)

    return spearman, kendall, hit


def calculate_compare():
    rank_truth = calculate_rank_truth()
    rank_nff = calculate_rank_nff()
    # rank_efs = calculate_rank_efs()

    nff_spearman, nff_kendall, nff_hit = calculate_score(rank_truth, rank_nff)
    # efs_spearman, efs_kendall, efs_hit = calculate_score(rank_truth, rank_efs)

    x, y = config.SUITE_NAME.split('-')
    # difference_spearman = nff_spearman - efs_spearman
    # difference_kendall = nff_kendall - efs_kendall
    # difference_hit = nff_hit - efs_hit

    data_row = {
        'x': x,
        'y': y,
        'nff_spearman': nff_spearman,
        'nff_kendall': nff_kendall,
        'nff_hit': nff_hit,
        # 'efs_spearman': efs_spearman,
        # 'efs_kendall': efs_kendall,
        # 'efs_hit': efs_hit,
        # 'difference_spearman': difference_spearman,
        # 'difference_kendall': difference_kendall,
        # 'difference_hit': difference_hit
    }

    with open(config.PATH_FILE_COMPARE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=config.HEADER_COMPARE)
        writer.writerow(data_row)
