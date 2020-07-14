class Token:
    def __init__(self):
        pass


# Language Keywords
class IF:
    def __init__(self, statement):
        pass


class ELSE:
    def __init__(self, statement):
        pass


class LOOP:
    pass


class FUNCTION:
    pass


class IMPORT:
    def __init__(self, package_name):
        pass


# Define Variable functionality
class VARIABLE:
    pass


# Define Builtin Objects
class OBJECT:
    pass


class Num(OBJECT):
    pass


class Str(OBJECT):
    pass


# Error System
class Error:
    def find_traceback(self):
        pass