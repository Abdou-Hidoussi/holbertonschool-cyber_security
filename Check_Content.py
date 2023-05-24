import re
import difflib
import json

def check_file_content(filecontent, regx):
    """ check if the regex argumant is in the file """
    pattern = re.compile(regx, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    match = re.search(pattern, filecontent)
    if match:
        return True
    else:
        return False
