import re

def check_file_content(filename, regx):
    """ check if the regex argumant is in the file """
    with open(filename, 'r') as file:
        contents = file.read()
    pattern = r'{}'.format(regx)
    match = re.search(pattern, contents)
    if match:
        return True
    else:
        return False
