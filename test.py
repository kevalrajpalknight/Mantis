from tokenizer import Tokenizer
import pprint
from errors import Error
import tokenizer

interpreter = Tokenizer()

interpreter.tokenize('mantis.ms')

print(tokenizer.find_ops(['i', 'b'], 'ibis loves to go boating'))

error = Error('ByeeeeeError',
              {'test.py': 'line 9', 'error.py': 'line 18'},
              ['line 9: error = Error()', 'line 18: sys.exit()'],
              'byeeeee')
