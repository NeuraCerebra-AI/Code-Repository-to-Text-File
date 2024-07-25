# Code-Repository-to-Text-File

This script recursively scans a specified folder and generates a single text file containing the contents of all non-excluded files in the repository. The contents of each file are wrapped in markers indicating the file's relative path.

## Features

- Recursively scans a specified directory
- Excludes specified folders and files
- Generates a single text file with the contents of all non-excluded files
- Each file's content is wrapped with markers indicating its relative path

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the repository folder:
   ```bash
   cd <repository_folder>
   ```

## Usage

1. Run the script:
   ```bash
   python script_name.py
   ```
2. Enter the path to the folder for the code repository when prompted.

## Configuration

The script excludes certain folders and files by default. You can modify the `EXCLUDED_FOLDERS` and `EXCLUDED_FILES` lists in the script to suit your needs.

### Default Excluded Folders

- `.git`, `.svn`, `.hg`
- `node_modules`, `dist`, `build`, `target`
- `venv`, `.venv`, `python_env`
- `.mypy_cache`, `__pycache__`
- `.idea`, `.vscode`, `.vscode-test`
- `.pytest_cache`, `.tox`
- `.coverage`, `.nyc_output`, `coverage`
- `logs`, `temp`, `tmp`, `out`
- `.gradle`, `.sconsign.dblite`
- `XMP-Toolkit-SDK`

### Default Excluded Files

- `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `pipfile.lock`
- `.DS_Store`, `Thumbs.db`, `project.pbxproj`, `UserInterfaceState.xcuserstate`
- `.class`, `.pyc`, `.pyo`

## Example Output

The script generates a text file named `repository_code.txt` in the specified folder. The contents of each file are wrapped with markers indicating the file's relative path. For example:

```
"""""""""""""""""""""""""""""
<relative/path/to/file.py>
# File contents here
</relative/path/to/file.py>
"""""""""""""""""""""""""""""
```
