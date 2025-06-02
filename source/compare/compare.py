from pathlib import Path

import pandas as pd

import config


def calculate_flaky_rank(flaky_data):
    flaky_data = flaky_data[flaky_data['VERSIONS'] == '{v' + str(config.RELEASES - 1) + '}']
    flake_score = (flaky_data.groupby("TEST_NAME")["FLAKINESS_SCORE"].mean()).rename("Score_Flakiness")
    return flake_score / max(flake_score)


def calculate_binom_rank(binom_data):
    binom_data["Row"] = binom_data.index + 1
    binom_score = (len(binom_data) - binom_data.groupby("Test")["Row"].mean()).rename("Score_Binomial")
    return binom_score / max(binom_score)


def compare(binom_data, flaky_data):
    binom_rank = calculate_binom_rank(binom_data)
    flaky_rank = calculate_flaky_rank(flaky_data)
    print('a')



def main():
    group_list = list(Path("../../data/group").rglob("*.csv"))
    binom_list = list(Path("../../data/binom").rglob("*.csv"))
    flaky_list = list(Path("../../data/OUTPUT").rglob("BUILD*.csv"))

    for i in range(len(binom_list)):
        binom_data = pd.read_csv(binom_list[i])
        flaky_data = pd.read_csv(flaky_list[i])

        compare(binom_data, flaky_data)

if __name__ == "__main__":
    main()
    pass