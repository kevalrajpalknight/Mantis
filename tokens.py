from errors import SyntaxErr

def assign_token(chunk):

    _syntax = {
        'if': IF,
        'loop': LOOP,
        'function': FUNCTION,
        '+': OPERATION,
        '-': OPERATION,
        '*': OPERATION,
        '/': OPERATION,
        'output':
    }

    for element in chunk:



# Language Keywords
class IF:
    def __init__(self, boolean, code):
        pass


class LOOP:
    def __init__(self, iterable, code):
        pass

    def _exec(self):
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
    def __init__(self, objects, operation):
        if len(objects) != 2:
            SyntaxErr(f'Cannot {operation} with {" ".join(objects)}')

        if operation not in ['*', '/', '+', '-']:
            SyntaxErr(f"{operation} isn't a valid operation.")

        self.objects = objects
        self.op = operation

    def __repr__(self):
        return f"{self.__class__.__name__} {self.op}\n"

    def _exec(self):
        ops = {
            '*': '__mul__(%s)',
            '/': '__div__(%s)',
            '+': '__add__(%s)',
            '-': '__sub__(%s)'
        }



# == >= <= < > !=
class COMPARISON:
    def __init__(self, objects, comparitor):
        if len(objects) != 2:
            Error(f'Cannot compare {" ".join(objects)} with {comparitor}')

        self.objects = objects
        self.comparitor = comparitor

    def _exec(self):

class OUTPUT:
    def __init__(self, output):
        self.output = output

    def _exec(self):
        print(self.output)


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

