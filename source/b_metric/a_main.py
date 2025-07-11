import time

from source.b_metric.b_metric import *


def main():
    print(f"    ---- metric started")
    start_total = time.time()

    start = time.time()
    calculate_nff_rate()
    end = time.time()
    print(f"        -------- calculate_nff_rate finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_stable_nff_rate()
    end = time.time()
    print(f"        -------- calculate_stable_nff_rate finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_confidence()
    end = time.time()
    print(f"        -------- calculate_confidence finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_instability()
    end = time.time()
    print(f"        -------- calculate_instability finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_likelihood()
    end = time.time()
    print(f"        -------- calculate_likelihood finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_unstable()
    end = time.time()
    print(f"        -------- calculate_unstable finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"    ---- metric finished in {end_total - start_total:.4f} seconds")

if __name__ == '__main__':
    main()
    pass
