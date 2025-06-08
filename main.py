import csv
import os
import time

import config
from source.algorithm import main as am
from source.metric import main as mm
from source.generate import main as tm
from source.visualization import main as vm
from source.compare import main as cm


def run():
    if config.MAIN_GENERATE:
        tm.main()
    if config.MAIN_METRIC:
        mm.main()
    if config.MAIN_VISUAL:
        vm.main()
    if config.MAIN_ORDER:
        am.main()
    if config.MAIN_COMPARE:
        cm.main()


if __name__ == '__main__':
    folder_names = [
        config.FOLDER_RAW,
        config.FOLDER_GROUP,
        config.FOLDER_BINOM,
        config.FOLDER_NORMAL,
        config.FOLDER_EFS,
        config.FOLDER_RATE,
        config.FOLDER_STABLE,
        config.FOLDER_CONFIDENCE,
        config.FOLDER_INSTABILITY,
        config.FOLDER_SAVINGS_1,
        config.FOLDER_SAVINGS_2,
        config.FOLDER_LIKELIHOOD,
    ]
    for name in folder_names:
        os.makedirs(name, exist_ok=True)

    with open(config.PATH_COMPARE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(config.COMPARE_HEADER)

    start = time.time()
    for i, count_trend in enumerate(config.COUNT_TRENDS):
        for j, index_trend in enumerate(config.INDEX_TRENDS):
            config.SUITE = i * len(config.INDEX_TRENDS) + j
            config.COUNT_TREND = count_trend
            config.INDEX_TREND = index_trend

            config.FILE = f'{count_trend}-{index_trend}'

            config.PATH_RAW = config.FOLDER_RAW + config.FILE + '.csv'
            config.PATH_GROUP = config.FOLDER_GROUP + config.FILE + '.csv'
            config.PATH_BINOM = config.FOLDER_BINOM + config.FILE + '.csv'
            config.PATH_NORMAL = config.FOLDER_NORMAL + config.FILE + '.csv'
            config.PATH_EFS = config.FOLDER_EFS + config.FILE  + '/0/LAMBDA_0.1/PERIOD_24/UA_WEIGHTED_SCORE_1/MULTI_TRANSITION_RATE/VerdictPair[ALL]'

            config.PATH_RATE = config.FOLDER_RATE + config.FILE + '.png'
            config.PATH_STABLE = config.FOLDER_STABLE + config.FILE + '.png'
            config.PATH_CONFIDENCE = config.FOLDER_CONFIDENCE + config.FILE + '.png'
            config.PATH_INSTABILITY = config.FOLDER_INSTABILITY + config.FILE + '.png'
            config.PATH_SAVINGS_1 = config.FOLDER_SAVINGS_1 + config.FILE + '.png'
            config.PATH_SAVINGS_2 = config.FOLDER_SAVINGS_2 + config.FILE + '.png'
            config.PATH_LIKELIHOOD = config.FOLDER_LIKELIHOOD + config.FILE + '.png'

            print('====================     ' + config.FILE + '     ====================')
            run_start = time.time()
            run()
            run_end = time.time()
            print(f"run finished in {run_end - run_start:.4f} seconds")

    end = time.time()
    print(f"total finished in {end - start:.4f} seconds")
