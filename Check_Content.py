import re
import difflib

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

def check_file_content_compare(filename, filecompare):
    """ check if two file content are Idedntical """
    with open(filename, "rb") as file_a, open(filecompare, "rb") as file_b: 
        if file_a.read() == file_b.read(): 
            return True
        else: 
            xor_result = int.from_bytes(file_a.read()) ^ int.from_bytes(file_b.read())
            if xor_result == 0: 
                return True
            else: 
                return False