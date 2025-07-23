"""
File Sorter by Keyword
=======================

This script organizes files into subfolders based on specific keywords in their filenames.

Use Case:
---------
Useful for sorting microscopy or imaging data into folders such as:
- 'zstack' for files containing '_zstack'
- 'timeseries' for files containing '_timeseries'
- 'snap' (default) for all other files

How It Works:
-------------
1. You specify a `base_folder` containing unsorted files.
2. The script creates target folders if they don't exist.
3. It moves files to the appropriate folder based on matching keywords.

Usage:
------
1. Modify the `base_folder` path.
2. Run the script:

    python sort_files_by_keyword.py

Requirements:
-------------
- Python 3.x
- Standard libraries: os, shutil

"""

import os
import shutil

# === Set your base folder here ===
base_folder = r"Path\To\Your\Data\Folder"  # ← Change this to your input folder

# === Define classification rules ===
rules = {
    "_zstack": "zstack",
    "_timeseries": "timeseries",
}

# === Create target folders if they don't exist ===
target_folders = set(rules.values())
target_folders.add("snap")  # Default category
for folder in target_folders:
    os.makedirs(os.path.join(base_folder, folder), exist_ok=True)

# === Sort and move files ===
for file in os.listdir(base_folder):
    file_path = os.path.join(base_folder, file)
    if os.path.isfile(file_path):
        moved = False
        for keyword, folder_name in rules.items():
            if keyword in file:
                shutil.move(file_path, os.path.join(base_folder, folder_name, file))
                print(f"Moved '{file}' → {folder_name}/")
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(base_folder, "snap", file))
            print(f"Moved '{file}' → snap/")

print("✅ All files have been sorted.")
