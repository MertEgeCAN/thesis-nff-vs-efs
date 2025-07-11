import time

from source.d_compare.b_compare import *


def main():
    print(f"    ---- compare started")
    start_total = time.time()

    start = time.time()
    calculate_compare()
    end = time.time()
    print(f"        -------- calculate_compare finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"    ---- compare finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
