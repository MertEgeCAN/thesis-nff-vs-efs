import time

from source.visualization.visualization import *


def main():
    start_total = time.time()

    start = time.time()
    plot_rate()
    end = time.time()
    print(f"plot_nff_rate finished in {end - start:.4f} seconds")

    start = time.time()
    plot_stable_rate()
    end = time.time()
    print(f"plot_stable_nff_rate finished in {end - start:.4f} seconds")

    start = time.time()
    plot_confidence()
    end = time.time()
    print(f"plot_confidence finished in {end - start:.4f} seconds")

    start = time.time()
    plot_instability()
    end = time.time()
    print(f"plot_instability finished in {end - start:.4f} seconds")

    start = time.time()
    plot_savings_1()
    end = time.time()
    print(f"plot_savings_1 finished in {end - start:.4f} seconds")

    start = time.time()
    plot_savings_2()
    end = time.time()
    print(f"plot_savings_2 finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"--- visualization --- finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass