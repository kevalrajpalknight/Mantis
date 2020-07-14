class Token:
    def __init__(self):
        pass


# Language Keywords
class IF:
    def __init__(self, statement):
        pass


class LOOP:
    def __init__(self):
        pass


class FUNCTION:
    def __init__(self):
        pass


# *+-/
class OPERATION:
    def __init__(self):
        pass


class IMPORT:
    def __init__(self, package_name):
        pass


# Define Variable functionality
class VARIABLE:
    def __init__(self):
        pass


# Define Builtin objects
class Object:
    pass


class Str(Object):
    pass


class Num(Object):
    pass


class List(Object):
    pass


class Dict(Object):
    pass


# Error System
class Error:
    def find_traceback(self):
        pass
