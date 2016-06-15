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
