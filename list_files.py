import os

def get_file_metadata():
    files_info = []

    for file in os.listdir():
        if os.path.isfile(file):
            files_info.append({
                'name': file,
                'size': os.path.getsize(file)
            })

    return files_info

# Print the list
if __name__ == "__main__":
    file_list = get_file_metadata()
    print(file_list)
