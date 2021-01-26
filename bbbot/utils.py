import os

def abs_path(file):
    return os.path.realpath(file)

def current_directory(file):
    return os.path.dirname(abs_path(file))