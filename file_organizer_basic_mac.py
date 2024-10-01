import os
import shutil
from pathlib import Path

# Update paths for macOS
SOURCE_DIR = r"/Users/YourUser/Downloads"  # replace to your path to the folder you want to organize
DESTINATION_DIR = r"/Users/YourUser/Desktop/Organized"  # replace to your path where organized files will go

# Dictionary mapping file types to folder names - You can add new ones
FILE_TYPE_FOLDERS = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Archives': ['.zip', '.tar', '.rar', '.7z'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Programs': ['.exe', '.msi', '.bat', '.sh'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp']
}

# Function to create folders based on file types if they don't exist
def create_folders():
    for folder in FILE_TYPE_FOLDERS:
        folder_path = os.path.join(DESTINATION_DIR, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

# Function to move files to the appropriate folder based on file type
def move_files():
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        file_extension = Path(filename).suffix.lower()

        # Check the file type and move to the corresponding folder
        moved = False
        for folder, extensions in FILE_TYPE_FOLDERS.items():
            if file_extension in extensions:
                dest_folder = os.path.join(DESTINATION_DIR, folder)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                print(f"Moved {filename} to {dest_folder}")
                break
        
        # If file type doesn't match, move to an 'Others' folder
        if not moved:
            others_folder = os.path.join(DESTINATION_DIR, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved {filename} to {others_folder}")

# Main function to organize files
if __name__ == "__main__":
    # Create folders based on file types
    create_folders()

    # Move files from the source directory to the appropriate folder
    move_files()

    print("File organization complete!")
