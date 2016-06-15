from matrix import Matrix


def test_matrix_init():
    m, n = 3, 3
    matrix = Matrix(m, n)

    for row in matrix:
        for col in row:
            assert col == Matrix.blank_char

    assert len(matrix) == m
    assert len(matrix[0]) == n


def test_matrix_colorize():
    m, n = 3, 3
    matrix = Matrix(m, n)

    matrix.colorize(0, 0, 'X')
    matrix.colorize(m - 1, n - 1, 'X')

    assert matrix[0][0] == 'X'
    assert matrix[m - 1][n - 1]

    return matrix


def test_matrix_clear():
    matrix = test_matrix_colorize()
    matrix.clean()

    for row in matrix:
        for col in row:
            assert col == Matrix.blank_char


def test_matrix_hcolorize():
    m, n = 3, 3
    matrix = Matrix(m, n)

    matrix.hcolorize(1, 1, 2, 'X')

    assert matrix[1][1] == 'X'
    assert matrix[1][2] == 'X'

    matrix.hcolorize(2, 0, 1, 'X')

    assert matrix[2][0] == 'X'
    assert matrix[2][1] == 'X'

    matrix.hcolorize(0, 0, 2, 'X')

    assert matrix[0][0] == 'X'
    assert matrix[0][1] == 'X'
    assert matrix[0][2] == 'X'


def test_matrix_vcolorize():
    m, n = 3, 3
    matrix = Matrix(m, n)

    matrix.vcolorize(1, 1, 2, 'X')

    assert matrix[1][1] == 'X'
    assert matrix[2][1] == 'X'

    matrix.vcolorize(2, 0, 1, 'X')

    assert matrix[0][2] == 'X'
    assert matrix[1][2] == 'X'

    matrix.vcolorize(0, 0, 2, 'X')

    assert matrix[0][0] == 'X'
    assert matrix[1][0] == 'X'
    assert matrix[2][0] == 'X'


def test_matrix_hfind():
    m, n = 3, 3
    matrix = Matrix(m, n)

    matrix.colorize(0, 0, 'X')
    matrix.colorize(0, 2, 'X')
    matrix.colorize(1, 2, 'X')

    assert 0 in matrix.hfind(0, 'X')
    assert 2 in matrix.hfind(0, 'X')
    assert 2 in matrix.hfind(1, 'X')


def test_matrix_vfind():
    m, n = 3, 3
    matrix = Matrix(m, n)

    matrix.colorize(0, 0, 'X')
    matrix.colorize(0, 2, 'X')
    matrix.colorize(1, 2, 'X')

    assert 0 in matrix.vfind(0, 'X')
    assert 0 in matrix.vfind(2, 'X')
    assert 1 in matrix.vfind(2, 'X')


def test_matrix_fill():
    m, n = 5, 5
    matrix = Matrix(m, n)

    matrix.colorize(2, 0, 'X')
    matrix.colorize(2, 4, 'X')

    matrix.colorize(0, 2, 'X')
    matrix.colorize(4, 2, 'X')

    matrix.fill(2, 2, 'X')

    assert ['X'] * 5 == matrix[2]

    for i in range(0, 5):
        matrix[i][2] == 'X'


def test_matrix_str():
    m, n = 2, 2
    matrix = Matrix(m, n)
    matrix.colorize(0, 1, 'X')

    assert str(matrix) == 'OX\nOO'


def test_matrix_save():
    m, n = 2, 2
    matrix = Matrix(m, n)
    matrix.colorize(0, 1, 'X')
    matrix.save('/tmp/matrix.bmp')

    with open('/tmp/matrix.bmp') as f:
        assert str(matrix) == f.read()
