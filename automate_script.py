# Domain Specific Task:
# Automation Script:Create a script to automate a repetitive task, such as data
# file organization. Improve efficiency and reduce manual effort.

from pathlib import Path
import shutil

# Use Pathlib to handle file paths
source_dir = Path("C:/Users/91844/Downloads")
target_dirs = {
    'pdf': Path("C:/Users/91844/OneDrive/Documents/PDFs"),
    'png': Path("C:/Users/91844/OneDrive/Documents/Images"),
}

# Create target directories if they don't exist
for target_dir in target_dirs.values():
    target_dir.mkdir(parents=True, exist_ok=True)

# Organize files by their extension
def organize_files():
    # Loop through files in the source directory
    for file in source_dir.iterdir():
        if file.is_file():  # Only process files
            ext = file.suffix[1:].lower()  # Get file extension without the dot

            # Move file to the appropriate folder if extension is recognized
            if ext in target_dirs:
                dest_path = target_dirs[ext] / file.name  # Construct destination path
                shutil.move(str(file), str(dest_path))  # Move the file
                print(f"Moved: {file.name} to {target_dirs[ext]}")
            else:
                print(f"Skipped: {file.name} (Unknown file type)")

# Run the file organization
if __name__ == "__main__":
    organize_files()

