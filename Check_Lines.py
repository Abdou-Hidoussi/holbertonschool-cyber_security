def check_line_number(filename, lines):
    """ check if the number of lines in a file equal to lines"""
    with open(filename, "r") as fp:
        line =  fp.readlines()
    if len(line) == lines:
        return True
    return False