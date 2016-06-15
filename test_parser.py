import pytest


@pytest.fixture
def parser():
    from matrix_parser import MatrixParser
    p = MatrixParser()
    p.parse('I 2 2')


def test_parse_init():
    parser = MatrixParser()
    parser.parse('I 2 2')
    assert parser.matrix.wisth == 2
    assert parser.matrix.height == 2


def test_parse_clear(parser):
    parser.matrix.colorize(0, 0, 'X')
    parser.parse('C')
    assert parser.matrix.get_blank_char() == parser.matrix[0][0]


def test_parse_colorize(parser):
    parser.parse('L 1 1 X')
    assert parser.matrix[0][0] == 'X'


def test_parse_vcolorize(parser):
    parser.parse('V 1 1 2 X')
    assert parser.matrix[0][0] == 'X'
    assert parser.matrix[0][1] == 'X'


def test_parse_hcolorize(parser):
    parser.parse('H 1 2 1 X')
    assert parser.matrix[0][0] == 'X'
    assert parser.matrix[1][0] == 'X'


def test_parse_fill(parser):
    parser = MatrixParser()
    parser.parse('I 3 3')
    parser.parse('L 2 1 x')
    parser.parse('L 2 3 X')
    parser.parse('L 1 2 X')
    parser.parse('L 3 2 X')
    parser.parse('F 2 2 X')
    assert parser.matrix[1][1] == 'X'


def test_parse_save(parser):
    parser.parse('S /tmp/matrix.bmp')
    with open('/tmp/matrix.bmp') as f:
        assert f.read() == str(parser.matrix)
