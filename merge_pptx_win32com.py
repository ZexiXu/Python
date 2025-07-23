"""
PowerPoint Merger (Windows, win32com)
=====================================

This script merges multiple `.pptx` files into one using the Windows COM interface
for PowerPoint. It preserves all slide content including images, notes, and formatting.

Requirements:
-------------
- Windows OS
- Microsoft PowerPoint installed
- Python (tested with 3.8+)
- Package: pywin32 (usually preinstalled with Python on Windows)

Usage:
------
1. Edit the `ppt_files` list with full paths to your input PowerPoint files.
2. Set `output_path` to your desired merged file path.
3. Run the script:

    python merge_pptx_win32com.py

Output:
-------
A single merged PowerPoint file combining all input files, in order.

Note:
-----
This script uses PowerPoint automation via `win32com.client` and only works on Windows.

"""

import win32com.client
import os

# === Edit these ===
ppt_files = [
    r"Path\To\S1_Summary.pptx",
    r"Path\To\S2_Summary.pptx",
    r"Path\To\S3_Summary.pptx"
]

output_path = r"Path\To\Merged_Summary.pptx"

# === Merge logic ===
def merge_presentations(ppt_paths, output_file):
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    ppt_app.Visible = True

    base_ppt = ppt_app.Presentations.Open(ppt_paths[0], WithWindow=False)

    for path in ppt_paths[1:]:
        pres = ppt_app.Presentations.Open(path, WithWindow=False)
        for i in range(1, pres.Slides.Count + 1):
            pres.Slides(i).Copy()
            base_ppt.Slides.Paste(-1)
        pres.Close()

    base_ppt.SaveAs(output_file)
    base_ppt.Close()
    ppt_app.Quit()

    print(f"✅ Merged PPT saved to: {output_file}")

# === Run ===
if __name__ == "__main__":
    merge_presentations(ppt_files, output_path)
