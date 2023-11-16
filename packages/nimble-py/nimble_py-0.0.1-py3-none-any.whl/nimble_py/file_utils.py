# File utilities
import shutil
def rmdir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

import pathlib
def is_file_recent_enough(file_path, max_age_days):
    path = pathlib.Path(file_path)
    if not path.exists():
        return False
    last_modified_ts = fname = path.stat().st_mtime
    diff_days = (datetime.datetime.now().timestamp() - last_modified_ts) / (60*60*24)
    if diff_days < max_age_days:
        log_info(f"File: {file_path} - age_days: {diff_days} - recent enough (required {max_age_days})")
        return True
    else:
        log_info(f"File: {file_path} - age_days: {diff_days} - not recent enough (required {max_age_days})")
        return False


"""Simply reads a file's contents. Useful for reading small text files.

Args:
    filepath (str): The location of the file to read

Returns:
    str: A string containing all of the file's contents
"""
def read_file(filepath):
    with open(filepath, 'r') as reader:
        return '\n'.join(reader.readlines())

"""
Simply writes the given content to the given file. 
Useful for reading small text files. 

Args:
    filepath (str): The location of the file to write
    content (object): If the given variable is not a string, 
        it is converted to string using str(content).

Returns:
"""
def write_to_file(filepath, content, strip=True):
    if type(content) != str:
        content = str(content)
    with open(filepath, 'w') as writer:
        writer.write(content.strip())

"""
Simply append the given string to the given file. If the given variable is not a string, it is converted to string.
"""
def append_to_file(filepath, content, strip=True):
    if type(content) != str:
        content = str(content)
    with open(filepath, 'a') as appender:
        appender.write(content.strip())
                         
def read_yaml(file_path):
    import yaml
    with open(file_path, "r") as f:
        return yaml.safe_load(f)                         
