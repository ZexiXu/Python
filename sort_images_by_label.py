"""
Image Sorter by Label
=====================

This script organizes microscopy image files into subfolders based on keyword labels 
(e.g., "AAA", "BBB", etc.) found in the filenames.

Typical Use Case:
- Confocal microscopy outputs with filenames indicating experimental condition
- Automatically groups images by condition into labeled subdirectories

Instructions:
-------------
1. Set `base_folder` to your working directory (containing the image files).
2. Define your list of `categories` (labels to search for).
3. Run the script with Python 3.

Example:
--------
A file named "C3-AAA_tile.png" will be moved to the subfolder "AAA/".

Author: ZX
Date: 2025-07-22
Location: Martinsried
"""

import os
import shutil

# === Define your folder ===
base_folder = r"E:\Path\To\Your\ImageFolder"

# === Sort categories by length DESCENDING to avoid substring match issues ===
categories = sorted(["AAA", "BBB", "CCC", "DDD"], key=len, reverse=True)

# === Loop through files and assign to correct subfolder ===
for filename in os.listdir(base_folder):
    filepath = os.path.join(base_folder, filename)
    
    if os.path.isfile(filepath):
        matched = False
        for category in categories:
            if category in filename:
                target_folder = os.path.join(base_folder, category)
                os.makedirs(target_folder, exist_ok=True)
                
                target_path = os.path.join(target_folder, filename)
                shutil.move(filepath, target_path)
                
                print(f"✅ Moved: {filename} → {category}/")
                matched = True
                break

        if not matched:
            print(f"⚠️ Skipped: {filename} (no matching category)")
