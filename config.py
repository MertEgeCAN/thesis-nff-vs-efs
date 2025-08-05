import numpy as np

RANDOM_SEED = 42
RANDOM_RNG = np.random.default_rng(RANDOM_SEED)

MAIN_GENERATE = False
MAIN_METRIC = False
MAIN_ORDER = True
MAIN_COMPARE = True
MAIN_VISUAL = False

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
PROBABILITY_OUTCOME_CLEAR_RATIO = [0.9, 0.1]
PROBABILITY_OUTCOME_FAULT = ['FAIL', 'SKIP']
PROBABILITY_OUTCOME_FAULT_RATIO = [0.9, 0.1]
PROBABILITY_OUTCOME_FLAKY = ['SUCCESSFUL', 'SKIP', 'FAIL', 'ERROR']
PROBABILITY_OUTCOME_FLAKY_RATIO = [0.1, 0.1, 0.4, 0.4]
PROBABILITY_REPORT = 0.1

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

PATH_FILE_GENERATE_TRUTH = None
PATH_FILE_GENERATE_NFF = None
PATH_FILE_GENERATE_EFS = None
PATH_FILE_ORDER_NFF = None
PATH_FILE_ORDER_EFS = None
PATH_FILE_COMPARE = 'output/2_compare/compare.csv'
PATH_FILE_VISUAL_PRE_TEST = None
PATH_FILE_VISUAL_PRE_VERSION = None
PATH_FILE_VISUAL_PRE_RUN = None

PATH_FOLDER_GENERATE_TRUTH = 'output/0_data/0_truth/'
PATH_FOLDER_GENERATE_NFF = 'output/0_data/1_nff/'
PATH_FOLDER_GENERATE_EFS = 'output/0_data/2_efs/'
PATH_FOLDER_GENERATE_EFS_PROCESS = 'output/0_data/3_efs_process/'
PATH_FOLDER_ORDER_NFF = 'output/1_order/1_nff/'
PATH_FOLDER_ORDER_EFS = 'output/1_order/2_efs/'
PATH_FOLDER_COMPARE = 'output/2_compare/'
PATH_FOLDER_VISUAL_PRE_TEST = 'output/3_plot/1_pre/0_test/'
PATH_FOLDER_VISUAL_PRE_VERSION = 'output/3_plot/1_pre/1_version/'
PATH_FOLDER_VISUAL_PRE_RUN = 'output/3_plot/1_pre/2_run/'