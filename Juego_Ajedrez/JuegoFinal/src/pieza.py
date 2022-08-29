#author: -Coding Spot video a Complete Chess Game AI With Python
# Modifications: Group

import os

class Pieza:

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
            f'Imagenes/{self.name}{self.color}.png')
        
           # PO\Imagenes\TD.png
            
    def add_move(self,move):
        self.moves.append(move)

#clases herencia ("Peon, Reina, Rey, Alfil, Torre, Caballo")    

#Peon
class Peon(Pieza):
    def __init__(self,color):
        #Selecciona direccion dependiendo de color
        if  color == 'B':
            self.dir = -1 
        else:
            self.dir = 1 
        super().__init__('P',color,1.0)

#Caballo
class Caballo(Pieza):
    def __init__(self, color):
        super().__init__('C', color, 3.0)

#Alfil
class Alfil(Pieza):
    def __init__(self, color):
        super().__init__('A', color, 3.001)

#Torre
class Torre(Pieza):

    def __init__(self, color):
        super().__init__('T', color, 5.0)

#Reina
class Reina(Pieza):

    def __init__(self, color):
        super().__init__('Q', color, 9.0)

#Rey
class Rey(Pieza):

    def __init__(self, color):
        self.izquierda_rey= None
        self.derecha_rey = None
        super().__init__('K', color, 10000.0)

                