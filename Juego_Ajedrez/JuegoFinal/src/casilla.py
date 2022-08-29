class Casilla:

    def __init__(self, row, col, pieza=None):
        self.row = row
        self.col = col
        self.pieza = pieza

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_pieza(self):
        return self.pieza != None

    def isempty(self):
        return not self.has_pieza()

    def has_team_pieza(self, color):
        return self.has_pieza() and self.pieza.color == color

    def has_enemy_pieza(self, color):
        return self.has_pieza() and self.pieza.color != color

    def isempty_or_enemy(self, color):
        return self.isempty() or self.has_enemy_pieza(color)

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        
        return True
