# CodeAlpha Task 4: Automated File Organizer

An automated file organizer that sorts files in a specified directory into folders based on their file extensions. This Python script has been converted into an executable file for easy execution.

## Features

- **Automatic File Sorting**: Scans a directory and moves files into folders based on their file extensions.
- **Customizable Directory Path**: Users can specify any folder path they want to organize.
- **Error Handling**: Catches and reports errors that may occur during the file-moving process.
- **Lightweight and Fast**: Efficiently organizes files with minimal resource usage.

## Tools Used

- **Python 3.x**: Programming language used for scripting.
- **os module**: Provides functions for interacting with the operating system.
- **shutil module**: Enables file operations like copying and moving.
- **collections.defaultdict**: Facilitates the grouping of files by extension.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/automated-file-organizer.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd automated-file-organizer
    ```

3. **Install required packages**:
    (No external packages are needed as the script relies on standard Python libraries.)

## Usage

1. **Run the script**:
    ```bash
    python organizer.py
    ```
   
2. **Provide the folder path**: When prompted, enter the path of the folder you want to organize.

3. **Organize files**: The script will automatically create folders based on file extensions and move files into the corresponding folders.

## Project Structure

Automated File Organizer/
│
├── organizer.py # Main script for organizing files
└── README.md # Project documentation


## Functions

- **organizer.py**:
  - **extensions**: A `defaultdict` that groups files by their extensions.
  - **Organizing Process**:
    1. **Scan Directory**: Lists all files in the provided directory.
    2. **Group Files by Extension**: Files are grouped based on their extensions.
    3. **Create Folders**: New folders are created for each extension.
    4. **Move Files**: Files are moved to their respective extension folders.

## Contributing

Contributions are welcome! Please feel free to submit a pull request if you have any ideas or improvements.

## License

This project is licensed under the MIT License.
