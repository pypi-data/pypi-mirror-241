import os

def generate_folders(folders, logging=True, message=None):
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        if logging:
            folder_name = os.path.basename(folder)
            msg = message if message else f"{folder_name} has been generated ~"
            print(msg)

def generate_files(files, logging=True, message=None):
    for file in files:
        with open(file, 'w') as f:
            pass
        if logging:
            file_name = os.path.basename(file)
            msg = message if message else f"{file_name} has been generated ~"
            print(msg)

def generate_file_contents(file_contents, logging=True, message=None):
    for file_path, contents in file_contents.items():
        with open(file_path, 'w') as f:
            f.writelines(contents)
        if logging:
            file_name = os.path.basename(file_path)
            msg = message if message else f"{file_name}'s contents have been generated ~"
            print(msg)

def generate_template(folders=None, files=None, file_contents=None, logging=True, message=None):
    if isinstance(logging, bool):
        logging_options = [logging] * 3
    elif isinstance(logging, list):
        logging_options = logging + [True] * (3 - len(logging))
    else:
        raise ValueError("Logging argument must be a boolean or a list of booleans.")

    if folders:
        generate_folders(folders, logging=logging_options[0], message=message)
    if files:
        generate_files(files, logging=logging_options[1], message=message)
    if file_contents:
        generate_file_contents(file_contents, logging=logging_options[2], message=message)
