import os
from datetime import datetime

# === Set your folder path ===
folder_path = r""  # <-- change to your folder path

# === Output file path ===
output_file = os.path.join(folder_path, "file_list_sorted.txt")

# === Get all files and their creation time ===
files_with_ctime = []
for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):
        ctime = os.path.getctime(full_path)
        files_with_ctime.append((file, ctime))

# === Sort files by creation time ===
files_with_ctime.sort(key=lambda x: x[1])  # ascending order

# === Write to output text file ===
with open(output_file, 'w', encoding='utf-8') as f:
    for file, ctime in files_with_ctime:
        file_name, file_ext = os.path.splitext(file)
        readable_ctime = datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{file_name}\t{file_ext.lstrip('.')}\t{readable_ctime}\n")

print(f"Sorted file list saved to: {output_file}")

