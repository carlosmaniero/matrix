class Matrix:
    '''
    Matrix Data.
    A API from the list python object
    '''
    blank_char = 'O'

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._create_matrix()

    def _create_matrix(self):
        ''' Create a blank matrix '''
        self._matrix = []
        for _ in range(0, self.height):
            self._matrix.append(['O'] * self.width)

    def get_blank_char(self):
        ''' Return blank char '''
        return self.blank_char

    def __getitem__(self, *args, **kwargs):
        ''' Slices in Matrix class '''
        return self._matrix.__getitem__(*args, **kwargs)

    def __len__(self):
        ''' Matrix suports len '''
        return len(self._matrix)

    def colorize(self, x, y, color):
        ''' colorize a pixel '''
        self._matrix[y][x] = color

    def clean(self):
        ''' reset matrix '''
        self._create_matrix()

    def hcolorize(self, y, x1, x2, color):
        ''' Put the color C horizontally in (X1-X2, Y). '''
        if x1 > x2:
            x1, x2 = x2, x1

        # inclusive x2
        x2 += 1

        # using slices (self.__getitem__) to fill matrix
        self[y][x1:x2] = [color] * (x2 - x1)

    def vcolorize(self, x, y1, y2, color):
        ''' Put the color C vertically in (X1-X2, Y). '''
        if y1 > y2:
            y1, y2 = y2, y1

        for y in range(y1, y2+1):
            self._matrix[y][x] = color

    def hfind(self, y, color):
        ''' find a color horizontally in the matrix '''
        results = []
        for x in range(0, self.width):
            if color == self._matrix[y][x]:
                results.append(x)

        return results

    def vfind(self, x, color):
        ''' find a color vertically in the matrix '''
        results = []
        for y in range(0, self.height):
            if color == self._matrix[y][x]:
                results.append(y)

        return results

    def fill(self, x, y, color):
        ''' Fill matrix colors if points exists'''
        x_indexs = self.vfind(x, color)
        y_indexs = self.hfind(y, color)

        try:
            x1 = min(x_indexs)
            x2 = max(x_indexs)

            y1 = min(y_indexs)
            y2 = max(y_indexs)
        except ValueError:
            pass
        else:
            self.vcolorize(x, y1, y2, color)
            self.hcolorize(y, x1, x2, color)

    def rect(self, x1, y1, x2, y2, color):
        ''' fill a rect in matrix '''
        for y in range(y1, y2 + 1):
            self.hcolorize(y, x1, x2, color)

    def replace(self, x, y, color, old_color=None, mapped=[]):
        if (x, y) in mapped:
            return
        mapped.append((x, y))

        if x < 0 or y < 0:
            return
        try:
            current_color = self[x][y]
        except IndexError:
            # EAFP
            return

        if old_color is None:
            old_color = current_color

        if old_color == current_color:
            self[x][y] = color

            self.replace(x - 1, y, color, old_color)
            self.replace(x + 1, y, color, old_color)
            self.replace(x, y - 1, color, old_color)
            self.replace(x, y + 1, color, old_color)

    def __str__(self):
        rows = []

        for row in self:
            rows.append(''.join(row))

        return '\n'.join(rows)

    def save(self, name):
        ''' Save matrix in the file '''
        with open(name, 'w+') as f:
            f.write(str(self))
