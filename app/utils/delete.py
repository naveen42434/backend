import os

def delete_files(dir_name, files):
    for file_name in files:
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', dir_name, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)