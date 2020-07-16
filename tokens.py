from errors import SyntaxErr


def get_tokens(chunk):
    _keywords = {
        'if': IF,
        'loop': LOOP,
        'function': FUNCTION,
        'output': OUTPUT,
        'input': INPUT,
        'pass': PASS
    }

    _exts = {
        '+': OPERATION,
        '-': OPERATION,
        '*': OPERATION,
        '/': OPERATION,
        '<=': COMPARISON,
        '>=': COMPARISON,
        '==': COMPARISON,
        '!=': COMPARISON,
        '=>': COMPARISON,
        '=<': COMPARISON,
    }

    tokens = {
        'variables': {},
        'action_tree': []
    }

    def set_variable(name, value):
        tokens['variables'][name] = value

    if chunk[0] in _keywords:
        # How many values to initialize the token object with.
        req_args_count = _keywords[chunk[0]].__init__.__code__.co_argcount - 1
        # Take things from chunk and assign to initalization of the token object
        # print(chunk[0], 'takes', req_args_count, 'parameters')
        # print(chunk[1:])

    elif chunk[1] == '=':
        # Set Variable name {chunk[0]} to {chunk[2]}

        value = "".join(chunk[2:])
        for char in list(value):
            print(char)

        evaled_variable = VARIABLE(chunk[0], value)

        set_variable(chunk[0], evaled_variable)

    return tokens


def instance_to_token(instance):
    pass


# Language Keywords
class IF:
    def __init__(self, boolean, tokens):
        pass


class LOOP:
    def __init__(self, iterable, tokens):
        pass

    def _exec(self, **variables):
        return variables


class PASS:
    def _exec(self):
        pass


class FUNCTION:
    def __init__(self, name, params, tokens):
        self.name = name
        self.params = params
        self.code = tokens

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} -- {self.params} (\n{self.code}\n"

    def _exec(self, **variables):
        return variables


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

    def _exec(self, **variables):
        ops = {
            '*': '__mul__(%s)',
            '/': '__div__(%s)',
            '+': '__add__(%s)',
            '-': '__sub__(%s)'
        }


        return variables


# == >= <= < > !=
class COMPARISON:
    def __init__(self, objects, comparitor):
        if len(objects) != 2:
            SyntaxErr(f'Cannot compare {" ".join(objects)} with {comparitor}')

        self.objects = objects
        self.comparitor = comparitor

    def _exec(self, **variables):
        return variables


class OUTPUT:
    def __init__(self, output):
        self.output = output

    def _exec(self, **variables):

        return variables


class INPUT:
    def __init__(self, query: str):
        self.query = query

    def __repr__(self):
        pass

    def _exec(self, **variables):

        return variables


# Define Variable functionality
class VARIABLE:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} of value {self.value}"


# Define Mantis Object for Standard Library to utilize
class Object:
    pass


class Str(Object):
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return int(self.value)