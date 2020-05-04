import os
from rocky import FileManager, Parser, Element

fm = FileManager(__file__)
input_files = fm.get_input_files()

for file in input_files:
    f = open(file, 'r')
    text = f.readlines()
    f.close()

    p = Parser(text)

    result = Parser(text).get_html()
    
    f = open(fm.cvt_io_file(file), 'w')
    f.write(result)
    f.close()
