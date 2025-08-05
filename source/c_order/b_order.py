import os

import pandas as pd

import config


def calculate_order_nff():
    df = pd.read_csv(config.PATH_FILE_GENERATE_NFF)
    df = df[df['Version'] == config.MAX_VERSION][['Test', 'Run', 'Instability']]

    index_run = [2 for _ in df['Test'].unique()]
    index_likelihood = df[df['Run'] == 1]['Instability'].to_list()

    order = []
    for _ in range(config.MAX_RUN * config.MAX_TEST):
        min_index = index_likelihood.index(min(index_likelihood))

        if index_run[min_index] < config.MAX_RUN:
            index_likelihood[min_index] = float(df[(df['Test'] == (min_index + 1)) & (df['Run'] == index_run[min_index])]['Instability'].iloc[0])
            index_run[min_index] += 1
            order.append(min_index + 1)
        else:
            index_likelihood[min_index] = 2

    df = pd.DataFrame(order, columns=['Order'])
    df.to_csv(config.PATH_FILE_ORDER_NFF, index=False)

def calculate_order_efs():
    def load_test_names(file_path):
        df = pd.read_csv(file_path, usecols=["TEST_NAME"])
        return set(df["TEST_NAME"].dropna())

    def find_matching_anonymous_file(named_file_path, anonymous_folder):
        target_test_names = load_test_names(named_file_path)

        for anon_filename in os.listdir(anonymous_folder):
            if not anon_filename.endswith(".csv"):
                continue
            anon_path = os.path.join(anonymous_folder, anon_filename)
            anon_test_names = load_test_names(anon_path)

            if anon_test_names == target_test_names:
                return anon_path

        return None

    def process_anonymous_file(matched_file_path):
        df = pd.read_csv(matched_file_path)

        # Filter for VERSION == 'v4'
        df_v4 = df[df["VERSIONS"] == "{v4}"]

        # Sort by FLAKINESS_SCORE descending
        df_sorted = df_v4.sort_values(by="FLAKINESS_SCORE", ascending=False).reset_index(drop=True)

        # Extract numeric part from TEST_NAME
        df_sorted["ORIGINAL_ID"] = df_sorted["TEST_NAME"].str.replace("tc", "", regex=False).astype(int)

        # Shift ORIGINAL_IDs so that the minimum becomes 1
        min_id = df_sorted["ORIGINAL_ID"].min()
        df_sorted["RENAMED_ID"] = df_sorted["ORIGINAL_ID"] - min_id + 1

        # Final output
        output_df = df_sorted[["ORIGINAL_ID", "RENAMED_ID", "FLAKINESS_SCORE"]]

        # Save to CSV
        output_path = os.path.join(os.path.dirname(matched_file_path), config.PATH_FILE_ORDER_EFS)
        output_df.to_csv(config.PATH_FILE_ORDER_EFS, index=False)

        print(f"✅ Saved mapped IDs to: {output_path}")
        print(output_df.head())

    # === Example usage ===
    named_file = config.PATH_FILE_GENERATE_EFS
    anon_folder = config.PATH_FOLDER_GENERATE_EFS_PROCESS

    matched_anon_file = find_matching_anonymous_file(named_file, anon_folder)

    if matched_anon_file:
        print(f"✔ Match found: {matched_anon_file}")
        process_anonymous_file(matched_anon_file)
    else:
        print("❌ No matching file found.")