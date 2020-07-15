from tokenizer import Tokenizer
import pprint
from errors import Error

interpreter = Tokenizer()

pprint.pprint(interpreter.format('mantis.ms'))

error = Error('SyntaxError',
              {'test.py': 'line 9', 'error.py': 'line 18'},
              ['line 9: error = Error()', 'line 18: sys.exit()'],
              traceback='byeeee')
