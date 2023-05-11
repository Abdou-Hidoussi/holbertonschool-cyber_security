import os
def check_file_exist(file=None, arg=None):
    """ check the existance of a file """
    if not os.path.exists(file):
        return(False)
    return True
