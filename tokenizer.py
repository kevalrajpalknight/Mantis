import tokens


class Tokenizer:
    @staticmethod
    def tokenize(msfile: str):
        file = Tokenizer.format(msfile)

        for file_line_number in range(len(file)):
            pass

    @staticmethod
    def format(msfile: str):
        # Get lines from file.
        with open(msfile, 'r') as file:
            lines = file.readlines()

        # Remove one-line comments
        for index in range(len(lines)):
            if lines[index].startswith('#'):
                lines[index] = ''

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
            line_holder += line.replace('    ', '~')
            if parentheses_counter == 0:
                clumped_lines.append(line_holder)
                line_holder = ''

        return clumped_lines

    def is_variable_definition(self, line):
        pass

    def is_variable_reference(self, file_globals):
        pass

    def tokenize_line(self, line):
        pass
