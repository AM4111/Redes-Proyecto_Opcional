from const import *
from square import Square
from pieza import *

class Board:

    def __init__(self):
        #Crea cuadricula
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_piece('B')
        self._add_piece('D')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row,col)

    def _add_piece(self,color):
        fila_peon, fila_Opiezas = (6,7) if color == 'B'else (1,0)
    
        #Peones
        for col in range (COLS):
            self.squares[fila_peon][col] = Square(fila_peon, col, Pawn(color))

        #Caballos (D = (0,1) y (0,6)) o (B = (7,1) y (7,6)) 
        self.squares[fila_Opiezas][1] = Square(fila_Opiezas, 1, Knight(color))
        self.squares[fila_Opiezas][6] = Square(fila_Opiezas, 6, Knight(color))

        #Alfil (D = (0,2) y (0,5)) o (B = (7,2) y (7,5)) 
        self.squares[fila_Opiezas][2] = Square(fila_Opiezas, 2, Bishop(color))
        self.squares[fila_Opiezas][5] = Square(fila_Opiezas, 5, Bishop(color))

        #Torres (D = (0,0) y (0,7)) o (B = (7,0) y (7,7)) 
        self.squares[fila_Opiezas][0] = Square(fila_Opiezas, 0, Rook(color))
        self.squares[fila_Opiezas][7] = Square(fila_Opiezas, 7, Rook(color))

        #Reina D = (0,3) o (B = (7,3)
        self.squares[fila_Opiezas][3] = Square(fila_Opiezas, 3, Queen(color))

        #Rey D = (0,4) o (B = (7,4) 
        self.squares[fila_Opiezas][4] = Square(fila_Opiezas, 4, King(color))
