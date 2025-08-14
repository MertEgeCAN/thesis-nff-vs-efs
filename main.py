import csv
import os
import time

import config
from source.a_generate import a_main as gm
from source.b_metric import a_main as mm
from source.c_order import a_main as am
from source.d_compare import a_main as cm
from source.e_visual import a_main as vm


def execute():
    if config.MAIN_GENERATE:
        gm.main()
    if config.MAIN_METRIC:
        mm.main()
    if config.MAIN_ORDER:
        am.main()
    if config.MAIN_COMPARE:
        cm.main()
    if config.MAIN_VISUAL:
        vm.main()


if __name__ == '__main__':
    folder_names = [
        config.PATH_FOLDER_GENERATE_TRUTH,
        config.PATH_FOLDER_GENERATE_NFF,
        config.PATH_FOLDER_GENERATE_NFF_METRIC,
        config.PATH_FOLDER_GENERATE_EFS,
        config.PATH_FOLDER_GENERATE_EFS_FORMATTED,
        config.PATH_FOLDER_ORDER_NFF,
        config.PATH_FOLDER_COMPARE,
        config.PATH_FOLDER_VISUAL_TRUTH_TEST,
        config.PATH_FOLDER_VISUAL_TRUTH_VERSION,
        config.PATH_FOLDER_VISUAL_TRUTH_RUN,
        config.PATH_FOLDER_VISUAL_NFF_TEST,
        config.PATH_FOLDER_VISUAL_NFF_VERSION,
        config.PATH_FOLDER_VISUAL_NFF_RUN,
        config.PATH_FOLDER_VISUAL_NFF_TEST_SCATTER,
        config.PATH_FOLDER_VISUAL_NFF_TEST_STABLE,
        config.PATH_FOLDER_VISUAL_NFF_VERSION_STABLE,
        config.PATH_FOLDER_VISUAL_NFF_RUN_STABLE,
        config.PATH_FOLDER_VISUAL_EFS_TEST,
        config.PATH_FOLDER_VISUAL_EFS_TEST_FORMATTED,
        config.PATH_FOLDER_VISUAL_EFS_TEST_SCATTER,
    ]
    for name in folder_names:
        os.makedirs(name, exist_ok=True)
    with open(config.PATH_FILE_COMPARE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(config.HEADER_COMPARE)

    start = time.time()
    for i, trend_version in enumerate(config.TRENDS_VERSION):
        for j, trend_run in enumerate(config.TRENDS_RUN):
            config.SUITE = i * len(config.TRENDS_RUN) + j
            config.SUITE_NAME = f'{trend_version}-{trend_run}'

            config.TREND_VERSION = trend_version
            config.TREND_RUN = trend_run

            config.PATH_FILE_GENERATE_TRUTH = config.PATH_FOLDER_GENERATE_TRUTH + config.SUITE_NAME + '.csv'
            config.PATH_FILE_GENERATE_NFF = config.PATH_FOLDER_GENERATE_NFF + config.SUITE_NAME + '.csv'
            config.PATH_FILE_GENERATE_NFF_METRIC = config.PATH_FOLDER_GENERATE_NFF_METRIC + config.SUITE_NAME + '.csv'
            config.PATH_FILE_GENERATE_EFS = config.PATH_FOLDER_GENERATE_EFS + config.SUITE_NAME + '.csv'
            config.PATH_FILE_GENERATE_EFS_METRIC = config.PATH_FOLDER_GENERATE_EFS_FORMATTED + config.SUITE_NAME + '.csv'
            config.PATH_FILE_ORDER_NFF = config.PATH_FOLDER_ORDER_NFF + config.SUITE_NAME + '.csv'
            config.PATH_FILE_VISUAL_TRUTH_TEST = config.PATH_FOLDER_VISUAL_TRUTH_TEST + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_TRUTH_VERSION = config.PATH_FOLDER_VISUAL_TRUTH_VERSION + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_TRUTH_RUN = config.PATH_FOLDER_VISUAL_TRUTH_RUN + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_TEST = config.PATH_FOLDER_VISUAL_NFF_TEST + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_VERSION = config.PATH_FOLDER_VISUAL_NFF_VERSION + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_RUN = config.PATH_FOLDER_VISUAL_NFF_RUN + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_TEST_SCATTER = config.PATH_FOLDER_VISUAL_NFF_TEST_SCATTER + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_TEST_STABLE = config.PATH_FOLDER_VISUAL_NFF_TEST_STABLE + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_VERSION_STABLE = config.PATH_FOLDER_VISUAL_NFF_VERSION_STABLE + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_NFF_RUN_STABLE = config.PATH_FOLDER_VISUAL_NFF_RUN_STABLE + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_EFS_TEST = config.PATH_FOLDER_VISUAL_EFS_TEST + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_EFS_TEST_FORMATTED = config.PATH_FOLDER_VISUAL_EFS_TEST_FORMATTED + config.SUITE_NAME + '.png'
            config.PATH_FILE_VISUAL_EFS_TEST_SCATTER = config.PATH_FOLDER_VISUAL_EFS_TEST_SCATTER + config.SUITE_NAME + '.png'

            print('====================     ' + config.SUITE_NAME + '     ====================')
            print(f"-- execute started")
            execute_start = time.time()
            execute()
            execute_end = time.time()
            print(f"-- execute finished in {execute_end - execute_start:.4f} seconds")

    end = time.time()
    print(f"total finished in {end - start:.4f} seconds")
