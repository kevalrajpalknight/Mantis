import tokens


class Tokenizer:
    @staticmethod
    def tokenize(msfile: str):
        keywords = {
            'if': tokens.IF,
            'el-if': tokens.IF,
            'else': tokens.IF,
            'import': tokens.IMPORT,
            'loop': tokens.LOOP,
            'function': tokens.FUNCTION
        }



    @staticmethod
    def format(msfile: str):
        # Get lines from file.
        with open(msfile, 'r') as file:
            lines = file.readlines()

        # Remove all comments
        for index in range(len(lines)):


        for index in range(len(lines)):
            if lines[index].startswith('//'):
                lines[index] = ''

        # Remove all empty lines from the list
        while '\n' in lines:
            lines.remove('\n')
        while '' in lines:
            lines.remove('')

        # Get the processed version of the lines.
        lines = [line.split() for line in lines]

        return lines
