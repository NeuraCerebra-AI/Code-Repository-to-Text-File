import os

EXCLUDED_FOLDERS = ['.git', 'out', '.vscode', 'python_env', 'node_modules', '__pycache__']
EXCLUDED_FILES = ['package-lock.json', 'json.hpp', '.DS_Store', 'project.pbxproj', 'UserInterfaceState.xcuserstate']

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
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                outfile.write('"""""""""""""""""""""""""""""\n')
                outfile.write(f"{os.path.relpath(file_path)}:\n")
                outfile.write('"""""""""""""""""""""""""""""\n')
                outfile.write(infile.read())
                outfile.write('\n\n')
    print(f"Files saved to: {os.path.abspath(output_file)}")  # Add this print statement

def main():
    folder_path = input("Enter the path to the folder for the code repository: ")
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return
    
    output_file = os.path.join(folder_path, 'repository_code.txt')  # Update output file path
    all_files = get_all_files(folder_path)
    if not all_files:
        print("No files found in the specified folder.")
        return
    
    generate_code_file(all_files, output_file)
    print(f"All files from the repository have been saved to {output_file}.")

if __name__ == "__main__":
    main()
