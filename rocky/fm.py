import os
from os import listdir
from os.path import isfile, join, realpath, dirname, basename, splitext

class FileManager:
    def __init__(self, run_file, input_dirname='input', output_dirname='output', input_extension='rr'):
        self.run_file = run_file                        # runfile should be __file__
        self.input_dirname = input_dirname
        self.output_dirname = output_dirname
        self.input_extension = input_extension

    def get_dir(self, io):
        if io == 'i':
            dir = self.input_dirname
        elif io == 'o':
            dir = self.output_dirname
        current_dir = dirname(realpath(self.run_file))
        return join(current_dir, dir)

    def get_files(self, filedir):
        files = [join(filedir, f) for f in listdir(filedir) if isfile(join(filedir, f))]
        return files

    def get_input_files(self):
        all_files = self.get_files(self.get_dir('i'))
        files_ext =  [f for f in all_files if f.endswith('.'+self.input_extension)]
        return files_ext

    def cvt_io_file(self, file):
        out_dir = self.get_dir('o')
        filename = basename(file)
        filename_without_ext = splitext(filename)[0]
        filename_html = filename_without_ext + '.html'
        out_file = join(out_dir, filename_html)
        return out_file

    def base(self, file):
        return basename(file)
