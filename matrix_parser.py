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

    def parse(self, command):
        command, *args = command.split()
        method = self._REGISTER.get(command)

        if method:
            method(self, *args)

    _REGISTER = {
        'I': init,
        'C': clean,
        'L': colorize
    }
