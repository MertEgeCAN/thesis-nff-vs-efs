import csv
import random
import time
from datetime import datetime, timedelta

import numpy as np

import config
from source.generate.suite import Suite

rng = np.random.default_rng(config.RANDOM_SEED)


def update_date(date):
    hour = random.randint(0, 6)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return date + timedelta(hours=hour, minutes=minute, seconds=second)


def set_verdict(test, run):
    return rng.choice(config.VERDICT_CLEAN, p=config.VERDICT_CLEAN_PROBABILITY) if run not in test.nff_indexes else rng.choice(config.VERDICT_FLAKY, p=config.VERDICT_FLAKY_PROBABILITY)


def main():
    start_total = time.time()

    with open(config.PATH_RAW, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Test',
            'Release',
            'Run',
            'Flaky',
            'NFF',
            'TEST_NAME',
            'ENVIRONMENT_ID',
            'VERSION_ID',
            'EXECUTION_TIME',
            'VERDICT'
        ])

        suite = Suite()
        datetime_suite = datetime.now()
        for release in suite.releases:
            datetime_release = datetime_suite
            for test in release.tests:
                datetime_test = datetime_release
                chunk = []
                for run in range(config.RUNS):
                    verdict = set_verdict(test, run)
                    chunk.append([
                        test.id,
                        release.id,
                        run,
                        test.flaky,
                        run in test.nff_indexes,
                        f'tc{test.id + config.TESTS * config.SUITE}',
                        0,
                        'v' + str(release.id) + '',
                        datetime_test.strftime('%Y-%m-%dT%H:%M:%SZ'),
                        verdict
                    ])
                    datetime_test = update_date(datetime_test)
                writer.writerows(chunk)
                if datetime_suite < datetime_test:
                    datetime_suite = datetime_test

    end_total = time.time()
    print(f"--- generate --- finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
