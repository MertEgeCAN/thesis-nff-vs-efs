import pandas as pd
import matplotlib.pyplot as plt


def plot_flakiness_per_version(df: pd.DataFrame, value_col='P_Flaky_Version'):
    """
    Plot bar graphs of `value_col` per Test, for each Version, with tests sorted by the value.

    Args:
        df: DataFrame with at least ['Test', 'Version', value_col] columns.
        value_col: Name of the column with flakiness scores to plot.
    """
    grouped = df.groupby(['Test', 'Version'])[value_col].mean().reset_index()
    versions = sorted(grouped['Version'].unique())

    for version in versions:
        subset = grouped[grouped['Version'] == version].sort_values(by=value_col)
        plt.figure(figsize=(10, 4))
        plt.bar(subset['Test'].astype(str), subset[value_col])
        plt.title(f"{value_col} per Test (Version {version})")
        plt.xlabel("Test")
        plt.ylim(0, 0.5)
        plt.ylabel(value_col)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def plot_flakiness_per_test(df: pd.DataFrame, value_col='P_Flaky_Test'):
    """
    Plot a single bar graph of `value_col` per Test, sorted ascending.

    Args:
        df: DataFrame with at least ['Test', value_col] columns.
        value_col: Name of the column with flakiness scores to plot.
    """
    grouped = df.groupby('Test')[value_col].mean().reset_index()
    subset = grouped.sort_values(by=value_col)

    plt.figure(figsize=(10, 4))
    plt.bar(subset['Test'].astype(str), subset[value_col])
    plt.title(f"{value_col} per Test")
    plt.xlabel("Test")
    plt.ylim(0, 0.5)
    plt.ylabel(value_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_cumulative_report_true(df: pd.DataFrame, test_name: str):
    """
    Plot cumulative count of True values in 'Report' column per version for a given test.

    Args:
        df: DataFrame with columns ['Test', 'Version', 'Run', 'Report'].
        test_name: Name of the test to visualize.
    """
    test_df = df[df['Test'] == test_name]
    versions = sorted(test_df['Version'].unique())

    for version in versions:
        subset = test_df[test_df['Version'] == version].sort_values(by='Run').copy()

        # Ensure Report is boolean (or convert if it's 'True'/'False' strings)
        subset['Report'] = subset['Report'].astype(bool)
        subset['Cumulative True Count'] = subset['Report'].cumsum()

        plt.plot(subset['Run'], subset['Cumulative True Count'], label=f'Version {version}', marker='o')

    plt.title(f"Cumulative 'True' Reports for Test: {test_name}")
    plt.xlabel("Run")
    plt.ylabel("Cumulative True Report Count")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_report_per_run(df: pd.DataFrame, test_name: str):
    """
    Plot which runs have Report=True and which don't, for each version of a selected test.

    Args:
        df: DataFrame with ['Test', 'Version', 'Run', 'Report'] columns.
        test_name: Name of the test to visualize.
    """
    import matplotlib.pyplot as plt

    test_df = df[df['Test'] == test_name].copy()
    test_df['Report'] = test_df['Report'].astype(bool)
    versions = sorted(test_df['Version'].unique())

    plt.figure(figsize=(10, 5))

    for version in versions:
        subset = test_df[test_df['Version'] == version].sort_values(by='Run')
        color = ['green' if r else 'red' for r in subset['Report']]

        plt.scatter(subset['Run'], [version] * len(subset), c=color, label=f"Version {version}", alpha=0.7,
                    edgecolors='k')

    plt.xlabel("Run")
    plt.ylabel("Version")
    plt.title(f"'Report' Status per Run for Test: {test_name}")
    plt.yticks(versions)
    plt.grid(True, axis='x')
    plt.tight_layout()
    plt.show()


df = pd.read_csv("data/raw/test.csv")
# plot_flakiness_per_test(df)
# plot_flakiness_per_version(df, value_col='P_Flaky_Version')
# plot_cumulative_report_true(df,31)
plot_report_per_run(df, 69)