import sys
import colorama


def error_print(msg):
    print(colorama.Fore.RED + msg)


class Error:
    def __init__(self, type_err: str, location: dict, lines: list, traceback: str):
        location_list = []
        for item in location:
            string = item + ': ' + location.get(item)
            location_list.append(string)
        location_str = ' -> '.join(location_list)
        msg = type_err + ": Found at " + location_str + "\nLines where error occurred: \n" + "\n".join(lines) + "\nAdditional information: \n" + traceback
        error_print(msg)
        sys.exit()
