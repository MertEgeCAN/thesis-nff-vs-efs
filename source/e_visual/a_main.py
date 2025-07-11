from source.e_visual.b_pre_visual import *
from source.e_visual.c_post_visual import *


def main():
    print(f"    ---- visual started")
    start_total = time.time()

    pre_plot()
    # post_plot()

    end_total = time.time()
    print(f"    ---- visual finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
