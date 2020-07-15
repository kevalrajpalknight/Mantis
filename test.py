from tokenizer import Tokenizer
import pprint
from errors import Error

interpreter = Tokenizer()

pprint.pprint(interpreter.format('mantis.ms'))

error = Error('Syntax', {'errors.py': 'line 4', 'test.py': 'None'}, ['line 0', 'line -1'], traceback='bloop!')
