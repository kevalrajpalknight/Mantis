import tokens


class Interpeter:
    @staticmethod
    def tokenize(ms_file: str):
        """Formatted file"""
        ff = [" ".join(line.split()) for line in Interpeter.format(ms_file)]

        _memory = {
            'variables': {},
            'action_tree': []
        }

        for chunk in ff:
            chunk_tokens = tokens.get_tokens(chunk.split())
            print('Tokens',chunk_tokens)

            for key in chunk_tokens['variables']:
                _memory['variables'][key] = chunk_tokens['variables'][key]

            _memory['action_tree'] += chunk_tokens['action_tree']

        return _memory

    @staticmethod
    def format(ms_file: str):
        # Get lines from file.
        with open(ms_file, 'r') as file:
            lines = file.readlines()

        # Remove one-line comments
        for index in range(len(lines)):
            if '#' in lines[index]:
                lines[index] = lines[index][:lines[index].find('#')]

        # Remove Multi-line comments
        is_comment = False
        for index in range(len(lines)):
            if lines[index].startswith('/*') and not is_comment:
                is_comment = True

            if lines[index].endswith('*/\n') and is_comment:
                is_comment = False

            if is_comment:
                lines[index] = ''
            elif '/*' in lines[index] or '*/' in lines[index]:
                lines[index] = ''

        # Remove all empty lines from the list
        while '\n' in lines:
            lines.remove('\n')
        while '' in lines:
            lines.remove('')

        # Compress formatted file to code segments for tokenizing
        parentheses_counter, clumped_lines, line_holder = 0, [], ''
        for line in lines:
            parentheses_counter += line.count('(')
            parentheses_counter -= line.count(')')
            line_holder += line
            if parentheses_counter == 0:
                clumped_lines.append(
                    line_holder
                        .strip('\n')
                        .replace('(', ' ( ')
                        .replace(')', ' ) ')
                        .replace('    ', '... ')
                )
                line_holder = ''

        return clumped_lines

    @staticmethod
    def execute_tree(action_tree, **global_variables):
        for branch in action_tree:
            global_variables = branch._exec(**global_variables)
