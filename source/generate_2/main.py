import csv
import time

from source.generate_2 import config
from source.generate_2.suite import Suite


def main():
    start_total = time.time()

    with open(config.PATH_NFF, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Test',
            'Version',
            'Run',
            'P_Clear',
            'P_Flaky_Test',
            'P_Flaky_Version',
            'P_Flaky_Run',
            'Outcome',
            'Report',
            'TEST_NAME',
            'ENVIRONMENT_ID',
            'VERSION_ID',
            'EXECUTION_TIME',
            'VERDICT'
        ])

        suite = Suite()
        for test in suite.tests:
            chunk = []
            for version in test.versions:
                for run in version.runs:
                    chunk.append([
                        test.name,
                        version.name,
                        run.name,
                        test.p_clear,
                        test.p_flaky,
                        version.p_flaky,
                        run.p_flaky,
                        run.outcome,
                        run.report,
                        f'tc{test.name}',
                        0,
                        f'v{version.name}',
                        run.date,
                        run.outcome
                    ])
            writer.writerows(chunk)

    end_total = time.time()
    print(f"--- generate --- finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
