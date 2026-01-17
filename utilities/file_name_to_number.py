import os
import re

directory = '/home/josh/Documents/code/project-euler/python'

for filename in os.listdir(directory):
    if filename.endswith("_None.py"):
        match = re.match(r"(\d+)_None\.py", filename)
        if match:
            number = int(match.group(1))
            new_filename = f"{number:03d}.py"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")