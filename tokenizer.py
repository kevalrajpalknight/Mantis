import tokens


class Tokenizer:
    @staticmethod
    def tokenize(msfile: str):
        keywords = {
            'if': tokens.IF_STATEMENT,
            'el-if': tokens.IF_STATEMENT,
            'else': tokens.IF_STATEMENT,
            'import': tokens.IMPORT,
            'loop': tokens.LOOP,
            'function': tokens.FUNCTION,
            'func': tokens.FUNCTION,
            'raise': tokens.Error,
            'error': tokens.Error
            }

    @staticmethod
    def format(msfile: str):
        # Get lines from file.
        with open(msfile, 'r') as file:
            lines = file.readlines()

        # Remove comments from lines
        for line in lines:
            if '#' in line:
                lines[line] = line[:line.find('#')]

        is_comment = False
        for line in lines:
            if '///' in line:
                lines[line] = line[line.find('///'):]
                is_comment = -is_comment
            elif is_comment:
                lines[line] = ''

        # Remove all empty lines from the list
        while '\n' in lines:
            lines.remove('\n')

        # Get the processed version of the lines.
        lines = [line.split() for line in lines]

        action_tree = []

        for line in lines:
            action_tree += line
            action_tree += ['\n']

        return " ".join(action_tree)
