import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'B' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        
    #Images
    def set_texture(self):
        self.texture = os.path.join(
            f'PO/Imagenes/{self.name}{self.color}.png')
           # PO\Imagenes\TD.png
            
    def add_move(self,move):
        self.moves.append(move)

#clases herencia ("Peon, Reina, Rey, Alfil, Torre, Caballo")    

#Peon
class Pawn(Piece):
    def __init__(self,color):
        self.dir = -1 if color == 'B' else 1 #Selecciona direccion dependiendo de color
        super().__init__('P',color,1.0)

#Caballo
class Knight(Piece):
    def __init__(self, color):
        super().__init__('C', color, 3.0)

#Alfil
class Bishop(Piece):
    def __init__(self, color):
        super().__init__('A', color, 3.001)

#Torre
class Rook(Piece):

    def __init__(self, color):
        super().__init__('T', color, 5.0)

#Reina
class Queen(Piece):

    def __init__(self, color):
        super().__init__('Q', color, 9.0)

#Rey
class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('K', color, 10000.0)

                