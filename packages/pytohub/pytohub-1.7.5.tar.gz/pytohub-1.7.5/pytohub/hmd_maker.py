from .menu import *
import time
from .textcolors import textcolors
from tkinter.filedialog import *
import os
import sys
from .logging import log

file = None
premake = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def run_lmod_maker(args):
    print(
        textcolors.BOLD
        + textcolors.PURPLE
        + "PYToHub is made by @mas6y6 on github\n"
        + textcolors.END
    )
    a = args

    if a[2] == '-file':
        log.info('Asking where to store file')
        d = askdirectory()
        if d == '':
            log.error('No directory to store file')
        else:
            log.info("Creating file")
            f = open(f"{d}/setup.umd",'w+')
            f.write("#Use \"python3 -m pytohub --hmd_maker -h\" to get the help guide to use this file\n")
            f.write("#This file is needed to install your module to your hub\n")
    elif a[2] == '-guide':
        print("""How to use the module_maker

You well be given a file that pytohub will need to use to install the module to your lego hub

    Comments will be ignored #<comment>

    How to use arguments:
    After the command, you need to use a space to implement an argument
    Example: upload_file main.py
    
    File commands:
            make_module : Builds the module folder on the hub and get the hub ready (You can only run this one)
            ARGUMENTS: (<module_name>)

            return_home : Returns to the main directory of the module on the computer and hub
            ARGUMENTS: (None)
            
            upload_file : Uploads a file thats in a directory
            ARGUMENTS: (<file_directory>)
            
            mkdir : Makes a directory in the hub
            ARGUMENTS: (<new_directory>)
            
            chdir : Changes the current directory in the hub
            ARGUMENTS: (<directory>)
            
            finish : Finishs the module when its done (You can only run this one)
            ARGUMENTS: (None)
""")
    else:
        log.error("UNKNOWN ERROR")
    
    #w = sys.argv[0].split('/')
    #w.pop(len(w) - 1)
    #main_mod = '/'.join(w)
    #time.sleep(3)