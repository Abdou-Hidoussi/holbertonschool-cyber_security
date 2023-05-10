import subprocess
def check_betty(file=None, arg=None):
    betty = subprocess.run(["betty", file])
    if betty.returncode != 0:
        return (False)
    return True
