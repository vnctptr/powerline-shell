#! /usr/bin/env python
import importlib
from .colortrans import rgb2short, RGB2SHORT_DICT

def short2rgb (shortstring):
    return str((list(RGB2SHORT_DICT.keys())[list(RGB2SHORT_DICT.values()).index(int(shortstring))]))

# TODO cleanup, use module
# def module_to_scss(filename_python):

#     mod = importlib.import_module(module_prefix + module_or_file)
#     file_python = open('./config/themes/soft-blue.py', 'r')
#     file_scss = open("./config/themes/soft-blue.scss", "a")

#     for line in file_python.readlines():
#         line = line.split(' ')
#         if (line[0] == '\n'):
#             new_line = ''
#         elif(line[2].strip() == "-1"):
#             new_line = line[0] + ": " + line[2].strip() + ";"
#         elif line[2].strip() == 'True' or line[2].strip() == 'False':
#             new_line = line[0] + ": " + line[2].strip() + ";" 
#         else:
#             new_line = line[0] + ": rgb" + short2rgb(line[2].strip())+ ";"
#         file_scss.write(new_line)

#     file_scss.close()


def scss_to_module(filename_css):  

    file_scss = open(filename_css, 'r')
    filename_python = filename_css.replace('scss', 'py')
    file_python = open(filename_python, "w") 

    content = "# this is a powerline shell theme generated automatically from an .scss file.\n\n" \
            "from powerline_shell.themes.default import DefaultColor\n" \
            "class Color(DefaultColor):\n" 

    for line in file_scss.readlines():
        line = line.split(' ')
        var_name = line[0].strip('$:')

        if (len(line) <= 1):
            pass
        elif('rgb' in line[1]):
            r, g, b = eval((line[1] + line[2] + line[3]).strip('rgb;\n'))
            content += '\t' + var_name + " = " + str(rgb2short(r, g, b))
        else:
            content += '\t' + var_name + " = " + line[1].strip(' ;:')

        content += '\n'
        
    file_python.write(content)

    return filename_python # TODO rename