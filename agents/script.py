import os
import shutil

TARGET_DIR = r'c:\Users\bilal\Desktop\agno-Test\agents\agent__lis'
for filename in os.listdir(TARGET_DIR):
    file_path = os.path.join(TARGET_DIR, filename)
    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)
        folder_path = os.path.join(TARGET_DIR, name)
        # Skip if a file (not a folder) with the same name exists
        if os.path.isfile(folder_path):
            print(f"Skipping {filename}: {folder_path} is a file, not a folder.")
            continue
        os.makedirs(folder_path, exist_ok=True)
        new_file_path = os.path.join(folder_path, filename)
        shutil.move(file_path, new_file_path)
        print(f"Moved {filename} to {folder_path}")