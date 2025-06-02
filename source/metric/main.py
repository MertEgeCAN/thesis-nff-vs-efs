import time

from source.metric.metric import *


def main():
    start = time.time()
    calculate_rate()
    end = time.time()
    print(f"calculate_rate finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_stable_rate()
    end = time.time()
    print(f"calculate_stable_rate finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_confidence()
    end = time.time()
    print(f"calculate_confidence finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_instability()
    end = time.time()
    print(f"calculate_instability finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_likelihood()
    end = time.time()
    print(f"calculate_likelihood finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_unstable()
    end = time.time()
    print(f"calculate_unstable finished in {end - start:.4f} seconds")

if __name__ == '__main__':
    # main()
    pass
