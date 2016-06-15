from matrix_parser import MatrixParser


if __name__ == '__main__':
    parser = MatrixParser()
    command = ''

    while command != 'X':
        command = input()
        try:
            parser.parse(command)
        except TypeError:
            print('Incorrect input')
