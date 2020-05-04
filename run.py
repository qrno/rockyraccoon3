import os
from rocky import FileManager, Parser, Element

fm = FileManager(__file__)

print("Looking for .rr files in", fm.get_dir('i'), '...')
input_files = fm.get_input_files()

print("Files Found:")
for file in input_files:
    print(' *', fm.base(file))

print('\nBeginning conversion')
for file in input_files:
    f = open(file, 'r')
    text = f.readlines()
    f.close()

    p = Parser(text)

    result = Parser(text).get_html()

    out_file = fm.cvt_io_file(file)
    f = open(out_file, 'w')
    f.write(result)
    f.close()
    print(' +', fm.base(out_file), 'created')
