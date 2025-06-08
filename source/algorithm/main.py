import time

from source.algorithm.algorithm import *


def main():
    start_total = time.time()

    start = time.time()
    calculate_order_binom()
    end = time.time()
    print(f"calculate_order_binom finished in {end - start:.4f} seconds")

    start = time.time()
    calculate_order_normal()
    end = time.time()
    print(f"calculate_order_normal finished in {end - start:.4f} seconds")

    start = time.time()
    plot_likelihood()
    end = time.time()
    print(f"plot_likelihood finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"--- algorithm --- finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
