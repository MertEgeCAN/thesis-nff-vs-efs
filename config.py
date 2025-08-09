import numpy as np

RANDOM_SEED = 42
RANDOM_RNG = np.random.default_rng(RANDOM_SEED)

MAIN_GENERATE = False
MAIN_METRIC = False
MAIN_ORDER = False
MAIN_COMPARE = True
MAIN_VISUAL = True

MAX_TEST = 100
MAX_VERSION = 4
MAX_RUN = 250

SUITE = 0
SUITE_NAME = None

TREND_VERSION = None
TRENDS_VERSION = ['uniform', 'increase', 'decrease', 'increase_exponential', 'decrease_exponential', 'increase_sudden', 'decrease_sudden']
TREND_RUN = None
TRENDS_RUN = ['uniform', 'increase', 'decrease', 'increase_exponential', 'decrease_exponential', 'increase_sudden', 'decrease_sudden']

PROBABILITY_CLEAR = 0.2
PROBABILITY_FAULT = 0.8
PROBABILITY_FLAKY_LOW = 0.1
PROBABILITY_FLAKY_HIGH = 0.4
PROBABILITY_FLAKY_DELTA = 0.1
PROBABILITY_OUTCOME_CLEAR = ['SUCCESSFUL', 'SKIP']
PROBABILITY_OUTCOME_CLEAR_RATIO = [1.0, 0.0]
PROBABILITY_OUTCOME_FAULT = ['FAIL', 'SKIP']
PROBABILITY_OUTCOME_FAULT_RATIO = [1.0, 0.0]
PROBABILITY_OUTCOME_FLAKY = ['SUCCESSFUL', 'SKIP', 'FAIL', 'ERROR']
PROBABILITY_OUTCOME_FLAKY_RATIO = [0.0, 0.1, 0.8, 0.1]
PROBABILITY_REPORT = 0.2

HEADER_TRUTH = [
    'Test',
    'Version',
    'Run',
    'P_Clear',
    'P_Fault',
    'P_Delta',
    'P_Flaky_Test',
    'P_Flaky_Version',
    'P_Flaky_Run',
    'Outcome',
    'Report'
]
HEADER_NFF = [
    'Test',
    'Version',
    'Run',
    'Outcome',
    'Report'
]
HEADER_EFS = [
    'TEST_NAME',
    'VERSION_ID',
    'EXECUTION_TIME',
    'VERDICT',
    'ENVIRONMENT_ID'
]
HEADER_COMPARE = [
    'x',
    'y',
    'nff_spearman',
    'nff_kendall',
    'nff_hit',
    'efs_spearman',
    'efs_kendall',
    'efs_hit',
    'difference_spearman',
    'difference_kendall',
    'difference_hit'
]

PATH_FOLDER_GENERATE_TRUTH = 'output/0_data/0_truth/'
PATH_FOLDER_GENERATE_NFF = 'output/0_data/1_nff/'
PATH_FOLDER_GENERATE_NFF_METRIC = 'output/0_data/2_nff_metric/'
PATH_FOLDER_GENERATE_EFS = 'output/0_data/3_efs/'
PATH_FOLDER_GENERATE_EFS_FORMATTED = 'output/0_data/5_efs_metric/'
PATH_FOLDER_ORDER_NFF = 'output/1_order/0_nff/'
PATH_FOLDER_COMPARE = 'output/2_compare/'
PATH_FOLDER_VISUAL_TRUTH_TEST = 'output/3_plot/0_truth/0_test/'
PATH_FOLDER_VISUAL_TRUTH_VERSION = 'output/3_plot/0_truth/1_version/'
PATH_FOLDER_VISUAL_TRUTH_RUN = 'output/3_plot/0_truth/2_run/'
PATH_FOLDER_VISUAL_NFF_TEST = 'output/3_plot/1_nff/0_test/'
PATH_FOLDER_VISUAL_NFF_VERSION = 'output/3_plot/1_nff/1_version/'
PATH_FOLDER_VISUAL_NFF_RUN = 'output/3_plot/1_nff/2_run/'
PATH_FOLDER_VISUAL_NFF_TEST_STABLE = 'output/3_plot/2_nff_stable/0_test/'
PATH_FOLDER_VISUAL_NFF_VERSION_STABLE = 'output/3_plot/2_nff_stable/1_version/'
PATH_FOLDER_VISUAL_NFF_RUN_STABLE = 'output/3_plot/2_nff_stable/2_run/'
PATH_FOLDER_VISUAL_EFS_TEST = 'output/3_plot/3_efs/0_test/'
PATH_FOLDER_VISUAL_EFS_TEST_FORMATTED = 'output/3_plot/3_efs/1_test_formatted/'
PATH_FOLDER_VISUAL_EFS_TEST_SCATTER = 'output/3_plot/3_efs/2_test_scatter/'

PATH_FILE_GENERATE_TRUTH = None
PATH_FILE_GENERATE_NFF = None
PATH_FILE_GENERATE_NFF_METRIC = None
PATH_FILE_GENERATE_EFS = None
PATH_FILE_GENERATE_EFS_METRIC = None
PATH_FILE_ORDER_NFF = None
PATH_FILE_COMPARE = PATH_FOLDER_COMPARE+ 'compare.csv'
PATH_FILE_VISUAL_TRUTH_TEST = None
PATH_FILE_VISUAL_TRUTH_VERSION = None
PATH_FILE_VISUAL_TRUTH_RUN = None
PATH_FILE_VISUAL_NFF_TEST = None
PATH_FILE_VISUAL_NFF_VERSION = None
PATH_FILE_VISUAL_NFF_RUN = None
PATH_FILE_VISUAL_NFF_TEST_STABLE = None
PATH_FILE_VISUAL_NFF_VERSION_STABLE = None
PATH_FILE_VISUAL_NFF_RUN_STABLE = None
PATH_FILE_VISUAL_EFS_TEST = None
PATH_FILE_VISUAL_EFS_TEST_FORMATTED = None
PATH_FILE_VISUAL_EFS_TEST_SCATTER = None