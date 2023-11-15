from getkey import getkey, keys
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_text_logo(version, hub_version):
    print(
        f""" ______   __  __     ______   ______     __  __     __  __     ______    
/\  == \ /\ \_\ \   /\__  _\ /\  __ \   /\ \_\ \   /\ \/\ \   /\  == \   
\ \  _-/ \ \____ \  \/_/\ \/ \ \ \/\ \  \ \  __ \  \ \ \_\ \  \ \  __<   
 \ \_\    \/\_____\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_/     \/_____/     \/_/   \/_____/   \/_/\/_/   \/_____/   \/_____/
  
            (Version: {version}, Hub Version: {hub_version})
                                                                        
"""
    )


class textcolors:
    HEADER = "\033[95m"
    BACKGROUND = "\033[107m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def main_menu(g1, g2):
    sel = 0

    selects = ["Disconnect", "Upload", "Manage modules"]

    while True:
        clear()
        print_text_logo(g1, g2)
        print()
        for i in selects:
            if i == selects[sel]:
                print(textcolors.BACKGROUND + i + textcolors.END)
            else:
                print(i)
        print("\nUse UP/DOWN arrows to navagate")
        key = getkey()
        if key == keys.DOWN:
            if not sel == len(selects) - 1:
                sel += 1
        elif key == keys.UP:
            if not sel == 0:
                sel -= 1
        elif key == keys.ENTER:
            clear()
            return (selects[sel], sel)
        else:
            pass


def second_menu(menuname: str, options=[]):
    sel = 0
    options.append("Back")
    while True:
        clear()
        print(menuname)
        print()
        for i in options:
            if i == options[sel]:
                print(textcolors.BACKGROUND + i + textcolors.END)
            else:
                print(i)
        print()
        print("\nUse UP/DOWN arrows to navagate")
        key = getkey()
        if key == keys.DOWN:
            if not sel == len(options) - 1:
                sel += 1
        elif key == keys.UP:
            if not sel == 0:
                sel -= 1
        elif key == keys.ENTER:
            clear()
            return (options[sel], sel)
        else:
            pass


def options_menu(menuname: str, options=[], desc=None, include_exit=False, exitfn=exit):
    sel = 0
    while True:
        clear()
        print(menuname)
        print()
        if not desc == None:
            print(desc)
        print()
        for i in options:
            if i == options[sel]:
                print(textcolors.BACKGROUND + i + textcolors.END)
            else:
                print(i)
        if include_exit == True:
            print('\nUse UP/DOWN arrows to navagate or press "Q" to exit')
        else:
            print("\nUse UP/DOWN arrows to navagate")
        key = getkey()
        if key == keys.DOWN:
            if not sel == len(options) - 1:
                sel += 1
        elif key == keys.UP:
            if not sel == 0:
                sel -= 1
        elif key == "q" and include_exit:
            exitfn()
        elif key == keys.ENTER:
            clear()
            return (options[sel], sel)
        else:
            pass
