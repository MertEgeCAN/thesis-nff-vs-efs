from source.e_visual.b_visual import *


def main():
    print(f"    ---- visual started")
    start_total = time.time()

    start = time.time()
    plot_truth_test()
    end = time.time()
    print(f"        -------- plot_test finished in {end - start:.4f} seconds")

    start = time.time()
    plot_truth_version()
    end = time.time()
    print(f"        -------- plot_version finished in {end - start:.4f} seconds")

    start = time.time()
    plot_truth_run()
    end = time.time()
    print(f"        -------- plot_run finished in {end - start:.4f} seconds")

    start = time.time()
    plot_nff_test()
    end = time.time()
    print(f"        -------- plot_nff_test finished in {end - start:.4f} seconds")

    start = time.time()
    plot_nff_version()
    end = time.time()
    print(f"        -------- plot_nff_version finished in {end - start:.4f} seconds")

    start = time.time()
    plot_nff_run()
    end = time.time()
    print(f"        -------- plot_nff_run finished in {end - start:.4f} seconds")

    start = time.time()
    plot_nff_test_stable()
    end = time.time()
    print(f"        -------- plot_nff_test_stable finished in {end - start:.4f} seconds")

    start = time.time()
    plot_nff_version_stable()
    end = time.time()
    print(f"        -------- plot_nff_version_stable finished in {end - start:.4f} seconds")

    start = time.time()
    plot_nff_run_stable()
    end = time.time()
    print(f"        -------- plot_nff_run_stable finished in {end - start:.4f} seconds")

    start = time.time()
    plot_efs_test()
    end = time.time()
    print(f"        -------- plot_efs_test finished in {end - start:.4f} seconds")

    start = time.time()
    plot_efs_test_formatted()
    end = time.time()
    print(f"        -------- plot_efs_test_formatted finished in {end - start:.4f} seconds")

    start = time.time()
    plot_efs_test_scatter()
    end = time.time()
    print(f"        -------- plot_efs_test_scatter finished in {end - start:.4f} seconds")

    end_total = time.time()
    print(f"    ---- visual finished in {end_total - start_total:.4f} seconds")


if __name__ == '__main__':
    main()
    pass
