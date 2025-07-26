import time

from source.c_order.b_order import *


def main():
    print(f"    ---- order started")
    start_total = time.time()

    start = time.time()
    calculate_order_nff()
    end = time.time()
    print(f"        -------- calculate_order_nff finished in {end - start:.4f} seconds")

    # start = time.time()
    # calculate_order_efs()
    # end = time.time()
    # print(f"        -------- calculate_order_efs finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"        ---- order finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
