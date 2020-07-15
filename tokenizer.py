import tokens as tkns
import json


class Tokenizer:
    @staticmethod
    def tokenize(ms_file: str):
        """Formatted file"""
        ff = Tokenizer.format(ms_file)

        tokens = []

        for line_num in range(len(ff)):
            components = ff[line_num].split()
            tokens.append(Tokenizer.tokenize_line(lines=components))

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
                clumped_lines.append(line_holder.replace('    ',
                                                         '~'
                                                         ).replace("\n",
                                                                   " \n "
                                                                   ).replace(')',
                                                                             ' ) '
                                                                             ).replace('(',
                                                                                       ' ( '
                                                                                       ).replace(',',
                                                                                                 ' , '))
                line_holder = ''

        return clumped_lines

    @staticmethod
    def is_variable_reference(file_globals):
        pass

    @staticmethod
    def find_ops(ops, segment):
        separated = []
        char_holder = ''
        for char in segment:
            if char in ops:
                if char_holder:
                    separated.append(char_holder)
                    char_holder = ''
                separated.append(char)
            else:
                char_holder += char
        if char_holder:
            separated.append(char_holder)

        return separated

    @staticmethod
    def is_variable_definition(line):
        line = Tokenizer.find_ops('=', line)
        if '=' in line:
            name_index = line.index('=') - 1
            name = line[name_index].split()[-1]
            value = line[name_index+2].split()[0]
            return {name: value}
        else:
            return False

    @staticmethod
    def tokenize_line(lines):
        with open('keywords.json', 'r') as FileData:
            keywords = json.load(FileData)
        tokenized_line = ''
        for line in lines:
            pass

        return tokenized_line
