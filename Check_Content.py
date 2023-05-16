import re

def check_file_content(filename, regx):
    """ check if the regex argumant is in the file """
    with open(filename, 'r') as file:
        contents = file.read()
    pattern = re.compile(regx, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    match = re.search(pattern, contents)
    if match:
        return True
    else:
        return False
