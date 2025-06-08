import time

from source.compare.compare import *


def main():
    start_total = time.time()

    start = time.time()
    compare()
    end = time.time()
    print(f"compare finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"--- compare - finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
