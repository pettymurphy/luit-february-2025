import os

def get_file_metadata(path='.'):
    """
    Scans the given directory (recursively) and returns a list of dictionaries,
    each containing the name, full path, and size of each file.
    
    Parameters:
    - path (str): Optional. Path to scan. Defaults to current working directory.
    
    Returns:
    - List[Dict]: Each dict includes file 'name', 'path', and 'size' in bytes.
    """
    files_info = []

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            files_info.append({
                'name': file,
                'path': full_path,
                'size': os.path.getsize(full_path)
            })

    return files_info

# Example usage
if __name__ == "__main__":
    metadata = get_file_metadata()  # or get_file_metadata("C:/some/folder")
    print(metadata)
