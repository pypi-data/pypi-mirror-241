from .textcolors import textcolors

class log:
    def fatul(text, exitcode=1):
        print(
            textcolors.RED
            + textcolors.BOLD
            + "[FATUL] "
            + text
            + " ("
            + str(exitcode)
            + ")"
            + textcolors.END
        )
        exit(exitcode)

    def error(text):
        print(textcolors.RED + "[ERROR] " + text + textcolors.END)
    
    def question(text,is_yn=False):
        if is_yn:
            input(textcolors.PURPLE + "[QUESTION] " + textcolors.END + text + " (Y/n) " + " :")
        else:
            input(textcolors.PURPLE + "[QUESTION] " + textcolors.END + text + " :")

    def warning(text):
        print(textcolors.YELLOW + "[WARNING] " + text + textcolors.END)

    def success(text):
        print(textcolors.GREEN + "[SUCCESS] " + text + textcolors.END)

    def successblue(text):
        print(textcolors.BLUE + "[SUCCESS] " + text + textcolors.END)

    def successcyan(text):
        print(textcolors.CYAN + "[SUCCESS] " + text + textcolors.END)

    def log(text):
        print("[INFO] " + text)

    def info(text):
        print("[INFO] " + text)
