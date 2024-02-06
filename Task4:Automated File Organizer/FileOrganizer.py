#CodeAlpha Task 4:Automated File Organizer
#This python script is converted to exe file for easy execution.
import os
import shutil
from collections import defaultdict


path = input("Enter Path of Folder to Organize:").strip()


files = os.listdir(path)


extensions = defaultdict(list)


for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    extensions[extension].append(file)


for extension, files in extensions.items():
    target_dir = os.path.join(path, extension)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for file in files:
        source_file = os.path.join(path, file)
        target_file = os.path.join(target_dir, file)
        try:
            shutil.move(source_file, target_file)
        except Exception as e:
            print(f"Error moving {file}: {e}")

print("Organization successful.")
