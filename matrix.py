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
        row = [self.get_blank_char()] * self.width
        self._matrix = [row] * self.height

    def get_blank_char(self):
        ''' Return blank char '''
        return self.blank_char

    def __getitem__(self, *args, **kwargs):
        ''' Slices in Matrix class '''
        return self._matrix.__getitem__(*args, **kwargs)

    def __len__(self):
        ''' Matrix suports len '''
        return len(self._matrix)
