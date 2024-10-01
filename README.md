# file_organizer_basic
A simple Python script that automatically organizes files in a specified directory based on file types (e.g., Documents, Images, Videos, Music, Archives, Audio, etc.)

 It can help keep your downloads folder or other directories tidy by moving files into their corresponding folders.

## Features

- Automatically creates folders based on file types (e.g., `.pdf`, `.jpg`, `.mp4`, `.mp3`, etc.)
- Moves files into the correct folder according to their extensions
- Supports the following categories:
  - Documents (`.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`)
  - Images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`)
  - Videos (`.mp4`, `.mov`, `.avi`, `.mkv`)
  - Music (`.mp3`, `.wav`, `.flac`)
  - Archives (`.zip`, `.rar`, `.tar`, `.7z`)
  - Audio (`.aac`, `.ogg`, `.m4a`)
  - Code (`.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`)
  - Programs (`.exe`, `.msi`, `.bat`, `.sh`)
  - Others (all unrecognized file types)

## Requirements

- Python 3.x
- `shutil` and `os` (standard Python libraries)
- `pathlib` (standard Python library)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/`Ludusm11/file_organizer_basic.git
    ```
   
2. **Navigate to the project directory:**
    ```bash
    cd file_organizer_basic
    ```

3. **Ensure Python is installed:**
    - Check if Python is installed by running `python --version` or `python3 --version`.
    - Install Python from [python.org](https://www.python.org/downloads/) if needed.

## Usage

1. **Edit the script:**
   - Update the `SOURCE_DIR` and `DESTINATION_DIR` variables in the script to match your directory paths.
   - Example:
     ```python
     # For macOS
     SOURCE_DIR = "/Users/YourUser/Downloads"
     DESTINATION_DIR = "/Users/YourUser/Desktop/Organized"

     # For Windows
     SOURCE_DIR = r"C:\Users\YourUser\Downloads"
     DESTINATION_DIR = r"C:\Users\markrozum\Desktop\Organized"
     ```

2. **Run the script:**
   - Open a terminal or command prompt in the project folder and run:
     ```bash
     #for mac
     python file_organizer_basic_mac.py

     #for windows
     python file_organizer_basic_windows.py
     ```

3. **The script will:**
   - Create necessary folders (Documents, Images, Videos, etc.) if they don't exist.
   - Move files from the `SOURCE_DIR` into corresponding folders in the `DESTINATION_DIR` based on their extensions.

## Example Output

Upon running the script, you’ll see output similar to the following:


![image](https://github.com/user-attachments/assets/357eb3cc-e277-4b5f-8351-671a2d2b9036)

