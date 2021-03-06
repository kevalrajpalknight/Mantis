import sys
import colorama


def _error_print(msg):
    print(colorama.Fore.RED + msg)


class MantisError:
    def __init__(self, type_err: str, location: dict, lines: list, traceback: str):
        location_list = []
        for item in location:
            string = item + ': ' + location.get(item)
            location_list.append(string)
        location_str = ' -> '.join(location_list)
        msg = "\n \n" + type_err + ": Found at: " + location_str + "\nLines where error occurred: \n" + "\n".join(lines) + "\nAdditional information: \n" + traceback
        _error_print(msg)
        sys.exit()


class SyntaxErr:
    def __init__(self, cause):
        _error_print(cause)
        sys.exit()
