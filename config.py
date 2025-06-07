MAIN_GENERATE = False
MAIN_METRIC = False
MAIN_VISUAL = False
MAIN_ORDER = True

SUITE = 0
RELEASES = 5
TESTS = 500
RUNS = 400

FLAKINESS = 0.8
NFF_RANGE = int(RUNS / 2)
RANDOM_SEED = 42

PATH_FILE = None
PATH_RAW = None
PATH_GROUP = None
PATH_BINOM = None
PATH_NORMAL = None
PATH_RATE = None
PATH_STABLE = None
PATH_CONFIDENCE = None
PATH_INSTABILITY = None
PATH_SAVINGS_1 = None
PATH_SAVINGS_2 = None
PATH_LIKELIHOOD = None

FOLDER_RAW = 'data/raw/'
FOLDER_GROUP = 'data/group/'
FOLDER_BINOM = 'data/binom/'
FOLDER_NORMAL = 'data/normal/'
FOLDER_RATE = 'plot/rate/'
FOLDER_STABLE = 'plot/stable/'
FOLDER_CONFIDENCE = 'plot/confidence/'
FOLDER_INSTABILITY = 'plot/instability/'
FOLDER_SAVINGS_1 = 'plot/savings_1/'
FOLDER_SAVINGS_2 = 'plot/savings_2/'
FOLDER_LIKELIHOOD = 'plot/likelihood/'

VERDICT_CLEAN = ['SUCCESSFUL', 'SKIP', 'FAIL', 'ERROR']
VERDICT_CLEAN_PROBABILITY = [0.7, 0.1, 0.1, 0.1]
VERDICT_FLAKY = ['SKIP', 'FAIL', 'ERROR']
VERDICT_FLAKY_PROBABILITY = [0.25, 0.25, 0.5]

COUNT_TREND = None
COUNT_TRENDS = ['uniform', 'increase', 'decrease', 'increase_exponential', 'decrease_exponential']
COUNT_INCREASE = {
    "start": 1,
    "growth": 5
}
COUNT_DECREASE = {
    "start": 1,
    "growth": 5
}
COUNT_INCREASE_EXPONENTIAL = {
    'lambda': 0.05
}
COUNT_DECREASE_EXPONENTIAL = {
    'lambda': 0.05
}

INDEX_TREND = None
INDEX_TRENDS = ['uniform', 'increase', 'decrease', 'increase_exponential', 'decrease_exponential', 'increase_sudden', 'decrease_sudden']
INDEX_INCREASE = {
    "start": 1,
    "growth": 5
}
INDEX_DECREASE = {
    "start": 1,
    "growth": 5
}
INDEX_INCREASE_EXPONENTIAL = {
    "lambda": 0.05
}
INDEX_DECREASE_EXPONENTIAL = {
    "lambda": 0.05
}
INDEX_INCREASE_SUDDEN = {
    "transition": int(RUNS * 0.75),
    "low": 1,
    "high": 5
}
INDEX_DECREASE_SUDDEN = {
    "transition": int(RUNS * 0.75),
    "low": 1,
    "high": 5
}

