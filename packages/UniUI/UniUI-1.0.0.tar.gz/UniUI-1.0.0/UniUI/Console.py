import inspect
import Info
import os

class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_MAGENTA = '\033[1;35m'
    BOLD_CYAN = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'

    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    BOLD_BG_BLACK = '\033[1;40m'
    BOLD_BG_RED = '\033[1;41m'
    BOLD_BG_GREEN = '\033[1;42m'
    BOLD_BG_YELLOW = '\033[1;43m'
    BOLD_BG_BLUE = '\033[1;44m'
    BOLD_BG_MAGENTA = '\033[1;45m'
    BOLD_BG_CYAN = '\033[1;46m'
    BOLD_BG_WHITE = '\033[1;47m'

    ENDC = '\033[0m'

def Clear() -> None:
    if Info.system == "Windows": os.system("cls")
    else: os.system("clear -r")

def get_caller_info() -> (str, int):
    stack = inspect.stack()
    return stack[-1].filename, stack[-1].lineno

def Error(error: str) -> None:
    file_name, line_number = get_caller_info()
    print(Color.RED + f"UniUI Error : in file \"{file_name}\" : on line {line_number}\n{error}" + Color.ENDC)

def Warning(error: str) -> None:
    file_name, line_number = get_caller_info()
    print(Color.YELLOW + f"UniUI Warning : in file \"{file_name}\" : on line {line_number}\n{error}" + Color.ENDC)