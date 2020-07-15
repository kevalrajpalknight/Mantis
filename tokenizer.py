import tokens


class Tokenizer:
    @staticmethod
    def tokenize(ms_file: str):
        """Formatted file"""
        ff = Tokenizer.format(ms_file)

        tokens= []

        for line_num in range(len(ff)):
            components = ff[line_num].split()
            tokens.append(Tokenizer.tokenize_line(components))

    @staticmethod
    def format(ms_file: str):
        # Get lines from file.
        with open(ms_file, 'r') as file:
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
            line_holder += line.replace('    ', '~').replace("\n", " \n ")
            if parentheses_counter == 0:
                clumped_lines.append(line_holder)
                line_holder = ''

        return clumped_lines

    def is_variable_definition(self, line):
        pass

    def is_variable_reference(self, file_globals):
        pass

    def tokenize_line(self, components):
        keywords = {
            'if': tokens.IF
        }

        return tokenized_line
