import csv
import time

import config
from source.a_generate.b_suite import Suite


def main():
    print(f"    ---- generate started")
    start_total = time.time()

    with open(config.PATH_FILE_GENERATE_TRUTH, mode='w', newline='') as file_truth, open(config.PATH_FILE_GENERATE_NFF, mode='w', newline='') as file_nff, open(config.PATH_FILE_GENERATE_EFS, mode='w', newline='') as file_efs:
        writer_truth = csv.writer(file_truth)
        writer_nff = csv.writer(file_nff)
        writer_efs = csv.writer(file_efs)

        writer_truth.writerow(config.HEADER_TRUTH)
        writer_nff.writerow(config.HEADER_NFF)
        writer_efs.writerow(config.HEADER_EFS)

        suite = Suite()

        for test in suite.tests:
            chunk_truth = []
            chunk_nff = []
            chunk_efs = []

            for version in test.versions:
                for run in version.runs:
                    chunk_truth.append([
                        test.name,
                        version.name,
                        run.name,
                        test.p_clear,
                        test.p_fault,
                        test.p_delta,
                        test.p_flaky,
                        version.p_flaky,
                        run.p_flaky,
                        run.outcome,
                        run.report
                    ])
                    chunk_nff.append([
                        test.name,
                        version.name,
                        run.name,
                        run.outcome,
                        run.report
                    ])
                    chunk_efs.append([
                        f'tc{test.name + config.MAX_TEST * config.SUITE}',
                        f'v{version.name}',
                        run.date,
                        run.outcome,
                        0
                    ])

            writer_truth.writerows(chunk_truth)
            writer_nff.writerows(chunk_nff)
            writer_efs.writerows(chunk_efs)

    end_total = time.time()
    print(f"    ---- generate finished in {end_total - start_total:.4f} seconds")

if __name__ == '__main__':
    main()
    pass
