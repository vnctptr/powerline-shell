#! /usr/bin/env python
from .colortrans import hexstr2num, rgbstring2tuple, rgb2short, RGB2SHORT_DICT
from .utils import import_file

def short2rgb (shortstring):
    return str((list(RGB2SHORT_DICT.keys())[list(RGB2SHORT_DICT.values()).index(int(shortstring))]))

 
# file1 = open('./config/themes/soft-blue.py', 'r') # TODO change this to support ~/.config
# f = open("./config/themes/soft-blue.scss", "a")

# Lines = file1.readlines()
# # py to scss
# # TODO make this into method
# for line in Lines:
#     line = line.split(' ')
#     if (line[0] == '\n'):
#         new_line = ''
#     elif(line[2].strip() == "-1"):
#         new_line = line[0] + ": " + line[2].strip() + ";"
#     elif line[2].strip() == 'True' or line[2].strip() == 'False': # TODO change to shorter
#         new_line = line[0] + ": " + line[2].strip() + ";" 
#     else:
#         new_line = line[0] + ": rgb" + short2rgb(line[2].strip())+ ";"
#     f.write(new_line)

# f.close()


def import_scss(filename_css):  

    file_scss = open(filename_css, 'r') # TODO change this to support ~/.config
    content = "# this theme file placed in \"~/.config/powerline-shell/themes\n" \
            "# this is a powerline shell theme generated automatically from an .scss file.\n\n" \
            "from powerline_shell.themes.default import DefaultColor\n" \
            "\nclass Color(DefaultColor):\n" 


    filename_python = filename_css.replace('scss', 'py')

    import os
    if os.path.exists(filename_python):
        os.remove(filename_python)
        
    file_python = open(filename_python, "a") 
    file_python.write(content)

    # TODO cleanup
    for line in file_scss.readlines():
        line = line.split(' ')
        if (line[0] == '\n'):
            new_line = ''
        elif(line[1].strip('\n ;:') == "-1"):
            new_line = line[0].strip('$:') + " = " + line[1].strip('\n ;:')
        elif line[1].strip('\n ;:') == 'True' or line[1].strip() == 'False': # TODO change to shorter
            new_line = line[0].strip('$:') + " = " + line[1].strip('\n ;:')
        else:
            r, g, b = int(line[1].strip('rgb, (')), int(line[2].strip(', ')), int(line[3].strip(') \n;'))
            new_line = line[0].strip('$:') + " = " + str(rgb2short(r,g,b))
        
        # TODO prompt if overwrite file?
        file_python.write('\t' + new_line + '\n')

    return filename_python # TODO rename