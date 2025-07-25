import os
import time

folder_path = "files_to_rename"
files = os.listdir(folder_path)

if not files:
    print("No files found in 'files_to_rename'.")
    exit()

print(f"Found {len(files)} files. Cleaning up...")

time.sleep(0.8)  # short delay for dramatic effect

for i, filename in enumerate(files):
    name, ext = os.path.splitext(filename)
    new_name = f"file_{i+1}{ext}"

    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

    print(f"Renamed: {filename}  →  {new_name}")
    time.sleep(0.1)  # makes the terminal output feel active

print("\n✅ All files renamed.")
print("Quicker than opening your laptop.")
