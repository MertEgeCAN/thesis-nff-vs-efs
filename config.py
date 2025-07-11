import numpy as np

RANDOM_SEED = 42
RANDOM_RNG = np.random.default_rng(RANDOM_SEED)

MAIN_GENERATE = True
MAIN_METRIC = True
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

PROBABILITY_CLEAR = 0.25
PROBABILITY_FAULT = 0.75
PROBABILITY_FLAKY_LOW = 0.2
PROBABILITY_FLAKY_HIGH = 0.3
PROBABILITY_FLAKY_DELTA = 0.2
PROBABILITY_OUTCOME_CLEAN = ['SUCCESSFUL', 'SKIP']
PROBABILITY_OUTCOME_CLEAN_RATIO = [0.75, 0.25]
PROBABILITY_OUTCOME_FAULT = ['FAIL', 'SKIP']
PROBABILITY_OUTCOME_FAULT_RATIO = [0.75, 0.25]
PROBABILITY_OUTCOME_FLAKY = ['SUCCESSFUL', 'SKIP', 'FAIL', 'ERROR']
PROBABILITY_OUTCOME_FLAKY_RATIO = [0.25, 0.25, 0.25, 0.25]
PROBABILITY_REPORT = 0.25

HEADER_TRUTH = [
    'Test',
    'Version',
    'Run',
    'P_Clear',
    'P_Fault',
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
    'Date',
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
    # 'efs_spearman',
    # 'efs_kendall',
    # 'efs_hit',
    # 'difference_spearman',
    # 'difference_kendall',
    # 'difference_hit'
]

PATH_FILE_GENERATE_TRUTH = None
PATH_FILE_GENERATE_NFF = None
PATH_FILE_GENERATE_EFS = None
PATH_FILE_ORDER_NORMAL = None
PATH_FILE_ORDER_NFF = None
PATH_FILE_ORDER_EFS = None
PATH_FILE_COMPARE = 'output/2_compare/compare.csv'
PATH_FILE_VISUAL_PRE_TEST = None
PATH_FILE_VISUAL_PRE_VERSION = None
PATH_FILE_VISUAL_PRE_RUN = None
PATH_FILE_VISUAL_POST_RATE = None
PATH_FILE_VISUAL_POST_STABLE = None
PATH_FILE_VISUAL_POST_CONFIDENCE = None
PATH_FILE_VISUAL_POST_INSTABILITY = None
PATH_FILE_VISUAL_POST_SAVINGS_1 = None
PATH_FILE_VISUAL_POST_SAVINGS_2 = None
PATH_FILE_VISUAL_POST_LIKELIHOOD = None

PATH_FOLDER_GENERATE_TRUTH = 'output/0_data/0_truth/'
PATH_FOLDER_GENERATE_NFF = 'output/0_data/1_nff/'
PATH_FOLDER_GENERATE_EFS = 'output/0_data/2_efs/'
PATH_FOLDER_ORDER_NORMAL = 'output/1_order/0_normal/'
PATH_FOLDER_ORDER_NFF = 'output/1_order/1_nff/'
PATH_FOLDER_ORDER_EFS = 'output/1_order/2_efs/'
PATH_FOLDER_COMPARE = 'output/2_compare/'
PATH_FOLDER_VISUAL_PRE_TEST = 'output/3_plot/1_pre/0_test/'
PATH_FOLDER_VISUAL_PRE_VERSION = 'output/3_plot/1_pre/1_version/'
PATH_FOLDER_VISUAL_PRE_RUN = 'output/3_plot/1_pre/2_run/'
PATH_FOLDER_VISUAL_POST_RATE = 'output/3_plot/2_post/rate/'
PATH_FOLDER_VISUAL_POST_STABLE = 'output/3_plot/2_post/stable/'
PATH_FOLDER_VISUAL_POST_CONFIDENCE = 'output/3_plot/2_post/confidence/'
PATH_FOLDER_VISUAL_POST_INSTABILITY = 'output/3_plot/2_post/instability/'
PATH_FOLDER_VISUAL_POST_SAVINGS_1 = 'output/3_plot/2_post/savings_1/'
PATH_FOLDER_VISUAL_POST_SAVINGS_2 = 'output/3_plot/2_post/savings_2/'
PATH_FOLDER_VISUAL_POST_LIKELIHOOD = 'output/3_plot/2_post/likelihood/'