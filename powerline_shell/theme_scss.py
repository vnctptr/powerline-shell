#! /usr/bin/env python
import importlib
from .colortrans import rgb2short, RGB2SHORT_DICT

def short2rgb (shortstring):
    return str((list(RGB2SHORT_DICT.keys())[list(RGB2SHORT_DICT.values()).index(int(shortstring))]))

# TODO add python to rgb python maybe?

def python_to_scss(filename_python):
    file_python = open(filename_python, 'r')
    filename_scss = filename_python.replace('.py', '-generated.scss')
    file_scss = open(filename_scss, 'w')

    content = ""

    for line in file_python.readlines():
        line = line.strip().split(' ')
        if line[0] == '':
            content += '\n'
        elif len(line) > 2:
            variable = '$' + line[0]
            value = line[2].strip('\n;')
            if value == "-1" or value == 'True' or value == 'False':
                content +=  variable + ": " + value + ";\n"
            elif line[2].strip().isdigit(): 
                content += variable + ": rgb" + short2rgb(value)+ ";\n"
        
        
    file_scss.write(content)
    file_scss.close()
    file_python.close()

def scss_to_python(filename_scss):  
    file_scss = open(filename_scss, 'r')
    filename_python = filename_scss.replace('.scss', '-temp.py')
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
            content += '\t' + var_name + " = " + str((r, g, b))
        else:
            content += '\t' + var_name + " = " + line[1].strip(' ;:')

        content += '\n'
        
    file_python.write(content)
    file_python.close()
    file_scss.close()

    return filename_python