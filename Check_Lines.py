def check_line_number(filecontent, lines):
    """ check if the number of lines in a file equal to lines"""
    line = filecontent.split("\n")
    if len(line) == lines:
        return True
    return False