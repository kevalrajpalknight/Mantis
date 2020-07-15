from tokenizer import Tokenizer
import pprint
from errors import Error
import tokenizer

interpreter = Tokenizer()

interpreter.tokenize('mantis.ms')

print(Tokenizer.is_variable_definition('Hello=Floof Hallo'))

error = Error('ByeeeeeError',
              {'test.py': 'line 9', 'error.py': 'line 18'},
              ['line 9: error = Error()', 'line 18: sys.exit()'],
              'byeeeee')
