import tokens


class Tokenizer:
    @staticmethod
    def tokenize(msfile: str):
        keywords = {
            'if': tokens.IF,
            'import': tokens.IMPORT,
            'loop': tokens.LOOP,
            'function': tokens.FUNCTION
        }

    @staticmethod
    def format(msfile: str):
        # Get lines from file.
        with open(msfile, 'r') as file:
            lines = file.readlines()

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
