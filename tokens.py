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
        pass

    elif chunk[1] == '=':
        # Set Variable name {chunk[0]} to {chunk[2]}
        set_variable(chunk[0], chunk[2])

    return tokens


# Language Keywords
class IF:
    def __init__(self, boolean, tokens):
        pass


class LOOP:
    def __init__(self, iterable, tokens):
        pass

    def _exec(self):
        pass


class PASS:
    def _exec(self):
        pass


class FUNCTION:
    def __init__(self, name, params, tokens):
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
        pass

class OUTPUT:
    def __init__(self, output):
        self.output = output

    def _exec(self):
        print(self.output)

class INPUT:
    def __init__(self, query: str):
        self.query = query

    def __repr__(self):
        pass

    def _exec(self):
        pass


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



