import os
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

files_and_dirs = os.listdir(current_directory)
print(f"Files and Directories: {files_and_dirs}")
print()