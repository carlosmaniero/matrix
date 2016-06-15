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
