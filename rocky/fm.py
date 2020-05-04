import os
from os import listdir
from os.path import isfile, join, realpath, dirname

class FileManager:
    def __init__(self, run_file):
        self.run_file = run_file

    def get_input_dir(self, input_dirname='input'):
        current_dir = dirname(realpath(self.run_file))
        return join(current_dir, input_dirname)

    def get_files(self, filedir):
        files = [join(filedir, f) for f in listdir(filedir) if isfile(join(filedir, f))]
        return files

    def get_input_files(self):
        return self.get_files(self.get_input_dir())
