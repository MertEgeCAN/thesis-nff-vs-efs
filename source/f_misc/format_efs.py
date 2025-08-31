import os
import shutil

def clean(root_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for folder_path, folder_names, file_names in os.walk(root_folder):
        if "UA_UNWEIGHTED_SCORE" in folder_path:
            relative_path = os.path.relpath(folder_path, root_folder)

            split = relative_path.split(os.sep)

            if len(split) >= 1 and split[0].startswith("0_"):
                new_folder_name = split[0][2:]
                for filename in file_names:
                    if filename.endswith(".csv"):
                        src_file = os.path.join(folder_path, filename)
                        dst_file = os.path.join(output_folder, f"{new_folder_name}.csv")
                        print(f"Copying {src_file} -> {dst_file}")
                        shutil.copyfile(src_file, dst_file)

if __name__ == "__main__":
    # Change path to raw EFS data

    root_folder = "../../0_data/4_efs_raw"
    output_folder = "../../0_data/5_efs_metric"
    clean(root_folder, output_folder)
