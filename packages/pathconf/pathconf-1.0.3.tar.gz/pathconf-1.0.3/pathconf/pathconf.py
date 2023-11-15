import os
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

# Function to search for the file in given directory
def search_directories(directory, target, stop_event):
    for dirpath, dirnames, filenames in os.walk(directory):
        if stop_event.is_set():
            break
        if target in filenames:
            stop_event.set()  # Signal other threads to stop
            return os.path.join(dirpath, target)
    return None


# Function to find the file
def find_file(start_path, target):
    stop_event = threading.Event()
    directories = [os.path.join(start_path, d) for d in os.listdir(start_path) if os.path.isdir(os.path.join(start_path, d))]
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_directories, d, target, stop_event) for d in directories]
        for future in as_completed(futures):
            file_path = future.result()
            if file_path:  # If the file was found
                return file_path
    return None


def load_json_config(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}  # Return an empty dictionary if the file is empty or invalid
    

# main function called to generate the file paths config and populate it with found file paths for quicker access in future
def find_path(target_file):
    config_path = os.path.join(os.path.expanduser("~"), '.config/pathconf')
    config_filename = '.file_paths.json'
    config_file_path = os.path.join(config_path, config_filename)
    # Initialize an empty config dictionary to be populated
    config = {}
    
    # Check if the config file exists
    if os.path.isfile(config_file_path):
        # Load the config
        config = load_json_config(config_file_path)
    # Check if the file path exists in config and if the file exists
    file_path = config.get(target_file)
    if file_path and os.path.isfile(file_path):
        return file_path
    # If the file path is not in config or the file does not exist, search for it
    file_path = find_file(os.path.expanduser("~"), target_file)
    if file_path:
        # Save the new path to the config
        config[target_file] = file_path
        with open(config_file_path, 'w+') as f:
            json.dump(config, f)
        # Set the file permissions to allow read and write access for the owner and read-only access for others
        #os.chmod(config_file_path, 0o644)
        return file_path
    else:
        raise FileNotFoundError(f"{target_file} not found.")