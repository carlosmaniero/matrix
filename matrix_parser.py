from matrix import Matrix


class MatrixParser:

    def init(self, m, n):
        m, n = int(m), int(n)
        self.matrix = Matrix(m, n)

    def clean(self):
        self.matrix.clean()

    def colorize(self, x, y, color):
        # Humanaze
        x, y = int(x), int(y)
        x, y = x - 1, y - 1
        self.matrix.colorize(x, y, color)

    def vcolorize(self, x, y1, y2, color):
        x, y1, y2 = int(x), int(y1), int(y2)
        x, y1, y2 = x - 1, y1 - 1, y2 - 1
        self.matrix.vcolorize(x, y1, y2, color)

    def hcolorize(self, x1, x2, y, color):
        y, x1, x2 = int(y), int(x1), int(x2)
        y, x1, x2 = y - 1, x1 - 1, x2 - 1
        self.matrix.hcolorize(y, x1, x2, color)

    def fill(self, x, y, color):
        x, y = int(x), int(y)
        x, y = x - 1, y - 1
        self.matrix.fill(x, y, color)

    def rect(self, x1, y1, x2, y2, color):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        self.matrix.rect(x1, y1, x2, y2, color)

    def replace(self, x, y, color):
        x, y = int(x), int(y)
        x, y = x - 1, y - 1
        self.matrix.replace(x, y, color)

    def save(self, name):
        self.matrix.save(name)

    def parse(self, command):
        command, *args = command.split()
        method = self._REGISTER.get(command)

        if method:
            method(self, *args)

    _REGISTER = {
        'I': init,
        'C': clean,
        'L': colorize,
        'V': vcolorize,
        'H': hcolorize,
        'Q': fill,
        'F': replace,
        'K': rect,
        'S': save
    }
