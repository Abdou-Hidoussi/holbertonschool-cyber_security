import os
def check_file_exist(file=None, arg=None):
    if not os.path.exists(file):
        return(False)
    return True
