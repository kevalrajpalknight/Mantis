class Token:
    def __init__(self):
        pass


# Language Keywords
class IF:
    def __init__(self, statement):
        pass


class LOOP:
    def __init__(self, ):
        pass


class COMMA:
    def __init__(self):
        pass


class FUNCTION:
    def __init__(self, name, params, code):
        self.name = name
        self.params = params
        self.code = code

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} -- {self.params} (\n{self.code}\n"


# *+-/
class OPERATION:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return f"{self.__class__.__name__} {self.type}\n"


class IMPORT:
    def __init__(self, package_name):
        self.package_name = package_name

    def __repr__(self):
        return f"{self.__class__.__name__} {self.package_name}\n"


# Define Variable functionality
class VARIABLE:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} of value {self.value}"


# Define Builtin objects
class Object:
    pass


class Str(Object):
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"{self.__class__.__name__} {self.string}"


class Num(Object):
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"{self.__class__.__name__} {self.number}"


class List(Object):
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"{self.__class__.__name__} {self.elements}"


class Dict(Object):
    def __init__(self, items):
        self.items = items

    def __dict__(self):
        return {k: v for k, v in self.items}

    def __repr__(self):
        return f"{self.__class__.__name__} {self.__dict__()}"
