from .main import run, download_program
from .hmd_maker import run_lmod_maker
from .logging import log
import time
import sys
import os

def show_help():
    print("""
            Pytohub command guide

    Arguements:

        --download : Loads the download menu
        --help : Loads the Pytohub command guide
        --module_maker : Loads the module_maker menu
""")

if __name__ == "__main__":
    program = sys.argv[0]
    if not len(sys.argv) == 1:
        if '--download' in sys.argv:
            download_program()
        
        elif '--module_maker' in sys.argv:
            run_lmod_maker(sys.argv)
            
        elif '--help' in sys.argv:
            show_help()
            
        else:
            log.fatul(f"Unknown arguement {sys.argv[1]} for help use \"--help\"")
    else:
        run()