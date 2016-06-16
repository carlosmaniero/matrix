import os
from matrix_parser import MatrixParser
DEBUG = os.environ.get('DEBUG_MATRIX', False)


if __name__ == '__main__':
    parser = MatrixParser()
    command = ''

    while command != 'X':
        command = input()
        try:
            parser.parse(command)
        except TypeError:
            print('Incorrect input')

        if DEBUG:
            print(str(parser.matrix))
