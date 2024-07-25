import os

EXCLUDED_FOLDERS = [
    '.git', '.svn', '.hg', 'node_modules', 'dist', 'build', 'target', 
    'venv', '.venv', 'python_env', '.mypy_cache', '__pycache__', 
    '.idea', '.vscode', '.vscode-test', '.pytest_cache', '.tox', 
    '.coverage', '.nyc_output', 'coverage', 'logs', 'temp', 'tmp', 
    'out', '.gradle', '.sconsign.dblite', 'XMP-Toolkit-SDK'
]

EXCLUDED_FILES = [
    'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'pipfile.lock',
    '.DS_Store', 'Thumbs.db', 'project.pbxproj', 'UserInterfaceState.xcuserstate',
    '.class', '.pyc', '.pyo'
]

def get_all_files(folder_path):
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]
        # Exclude specified files
        files[:] = [f for f in files if f not in EXCLUDED_FILES]
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def generate_code_file(all_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in all_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write('"""""""""""""""""""""""""""""\n')
                    outfile.write(f"<{os.path.relpath(file_path)}>\n")
                    outfile.write(infile.read())
                    outfile.write(f"</{os.path.relpath(file_path)}>\n")
                    outfile.write('"""""""""""""""""""""""""""""\n\n')
            except IOError as e:
                print(f"Error reading file {file_path}: {e}")
    print(f"Files saved to: {os.path.abspath(output_file)}")

def main():
    folder_path = input("Enter the path to the folder for the code repository: ")
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return
    
    output_file = os.path.join(folder_path, 'repository_code.txt')
    all_files = get_all_files(folder_path)
    if not all_files:
        print("No files found in the specified folder.")
        return
    
    generate_code_file(all_files, output_file)
    print(f"All files from the repository have been saved to {output_file}.")

if __name__ == "__main__":
    main()
