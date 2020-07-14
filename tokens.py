class Token:
    def __init__(self):
        pass


# Language Keywords
class IF:
    def __init__(self, statement):
        pass


class ELIF:
    def __init__(self, statement):
        pass


class ELSE:
    def __init__(self, statement):
        pass


class LOOP:
    def __init__(self):
        pass


class WHILE:
    def __init__(self):
        pass


class FUNCTION:
    def __init__(self):
        pass


class IMPORT:
    def __init__(self, package_name):
        pass


# Define Variable functionality
class VARIABLE:
    def __init__(self):
        pass


# Define Builtin Objects
class OBJECT:
    def __init__(self):
        pass


class Num(OBJECT):
    pass


class Str(OBJECT):
    pass


class List(OBJECT):
    pass


class Open(OBJECT):
    pass


# Error System
class Error:
    def __init__(self):
        pass

    def find_traceback(self):
        pass