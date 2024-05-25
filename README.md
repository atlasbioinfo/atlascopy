# atlascopy

This Python script is designed to copy files from a source folder to a destination folder while handling file comparisons and user prompts for file replacement.

## Features

- Copies files from a source folder to a destination folder
- Compares files by size and MD5 hash to identify differences
- Prompts the user for confirmation when a file with the same name but different content exists in the destination folder
- Displays progress using tqdm progress bar
- Supports command-line arguments for specifying source and destination folders

## Requirements

- Python 3.x
- tqdm library

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies by running the following command:

```
pip install tqdm
```

## Usage

To use the script, run the following command in the terminal:

```
python copy_folder.py source_folder destination_folder
```

Replace `source_folder` with the path to the source folder and `destination_folder` with the path to the destination folder.

## How It Works

1. The script takes two command-line arguments: the source folder path and the destination folder path.
2. It iterates through all the files in the source folder and its subfolders using `os.walk()`.
3. For each file, it checks if the file already exists in the destination folder.
   - If the file doesn't exist, it copies the file to the destination folder.
   - If the file exists and has the same content (compared by size and MD5 hash), it skips the file.
   - If the file exists but has different content, it prompts the user to confirm whether to replace the file or keep the existing one.
4. The script displays a progress bar using tqdm to indicate the copying progress.
5. After copying all the files, it prints a completion message.

## License

This script is released under the [Apache License V2.0](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
