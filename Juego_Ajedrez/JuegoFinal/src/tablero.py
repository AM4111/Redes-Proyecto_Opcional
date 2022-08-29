from constante import *
from casilla import Casilla
from pieza import *
from movimiento import Move
import copy
import os

class Tablero:

    def __init__(self):
        self.casillas = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLUMNAS)]
        self.last_move = None
        self._create()
        self._add_piezas('B')
        self._add_piezas('D')

    def move(self, pieza, move, testing=False):
        initial = move.initial
        final = move.final

        en_passant_empty = self.casillas[final.row][final.col].isempty()

        # console board move update
        self.casillas[initial.row][initial.col].pieza = None
        self.casillas[final.row][final.col].pieza = pieza

        if isinstance(pieza, Peon):
            # en passant capture
            diff = final.col - initial.col
            if diff != 0 and en_passant_empty:
                # console board move update
                self.casillas[initial.row][initial.col + diff].pieza = None
                self.casillas[final.row][final.col].pieza = pieza
            
            # Peon promotion
            else:
                self.check_promotion(pieza, final)

        # Rey castling
        if isinstance(pieza, Rey):
            if self.castling(initial, final) and not testing:
                diff = final.col - initial.col
                rook = pieza.left_rook if (diff < 0) else pieza.right_rook
                self.move(rook, rook.moves[-1])

        # move
        pieza.moved = True

        # clear valid moves
        pieza.clear_moves()

        # set last move
        self.last_move = move

    def valid_move(self, pieza, move):
        return move in pieza.moves

    def check_promotion(self, pieza, final):
        if final.row == 0 or final.row == 7:
            self.casillas[final.row][final.col].pieza = Reina(pieza.color)

    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2

    def set_true_en_passant(self, pieza):
        
        if not isinstance(pieza, Peon):
            return

        for row in range(FILAS):
            for col in range(COLUMNAS):
                if isinstance(self.casillas[row][col].pieza, Peon):
                    self.casillas[row][col].pieza.en_passant = False
        
        pieza.en_passant = True

    def in_check(self, pieza, move):
        temp_pieza = copy.deepcopy(pieza)
        temp_board = copy.deepcopy(self)
        temp_board.move(temp_pieza, move, testing=True)
        
        for row in range(FILAS):
            for col in range(COLUMNAS):
                if temp_board.casillas[row][col].has_enemy_pieza(pieza.color):
                    p = temp_board.casillas[row][col].pieza
                    temp_board.calc_moves(p, row, col, bool=False)
                    for m in p.moves:
                        if isinstance(m.final.pieza, Rey):
                            return True
        
        return False

    def calc_moves(self, pieza, row, col, bool=True):
        '''
            Calculate all the possible (valid) moves of an specific pieza on a specific position
        '''
        
        def Peon_moves():
            # steps
            steps = 1 if pieza.moved else 2

            # vertical moves
            start = row + pieza.dir
            end = row + (pieza.dir * (1 + steps))
            for possible_move_row in range(start, end, pieza.dir):
                if Casilla.in_range(possible_move_row):
                    if self.casillas[possible_move_row][col].isempty():
                        # create initial and final move casillas
                        initial = Casilla(row, col)
                        final = Casilla(possible_move_row, col)
                        # create a new move
                        move = Move(initial, final)

                        # check potencial checks
                        if bool:
                            if not self.in_check(pieza, move):
                                # append new move
                                pieza.add_move(move)
                        else:
                            # append new move
                            pieza.add_move(move)
                    # blocked
                    else: break
                # not in range
                else: break

            # diagonal moves
            possible_move_row = row + pieza.dir
            possible_move_COLUMNAS = [col-1, col+1]
            for possible_move_col in possible_move_COLUMNAS:
                if Casilla.in_range(possible_move_row, possible_move_col):
                    if self.casillas[possible_move_row][possible_move_col].has_enemy_pieza(pieza.color):
                        # create initial and final move casillas
                        initial = Casilla(row, col)
                        final_pieza = self.casillas[possible_move_row][possible_move_col].pieza
                        final = Casilla(possible_move_row, possible_move_col, final_pieza)
                        # create a new move
                        move = Move(initial, final)
                        
                        # check potencial checks
                        if bool:
                            if not self.in_check(pieza, move):
                                # append new move
                                pieza.add_move(move)
                        else:
                            # append new move
                            pieza.add_move(move)

            # en passant moves
            r = 3 if pieza.color == 'white' else 4
            fr = 2 if pieza.color == 'white' else 5
            # left en pessant
            if Casilla.in_range(col-1) and row == r:
                if self.casillas[row][col-1].has_enemy_pieza(pieza.color):
                    p = self.casillas[row][col-1].pieza
                    if isinstance(p, Peon):
                        if p.en_passant:
                            # create initial and final move casillas
                            initial = Casilla(row, col)
                            final = Casilla(fr, col-1, p)
                            # create a new move
                            move = Move(initial, final)
                            
                            # check potencial checks
                            if bool:
                                if not self.in_check(pieza, move):
                                    # append new move
                                    pieza.add_move(move)
                            else:
                                # append new move
                                pieza.add_move(move)
            
            # right en pessant
            if Casilla.in_range(col+1) and row == r:
                if self.casillas[row][col+1].has_enemy_pieza(pieza.color):
                    p = self.casillas[row][col+1].pieza
                    if isinstance(p, Peon):
                        if p.en_passant:
                            # create initial and final move casillas
                            initial = Casilla(row, col)
                            final = Casilla(fr, col+1, p)
                            # create a new move
                            move = Move(initial, final)
                            
                            # check potencial checks
                            if bool:
                                if not self.in_check(pieza, move):
                                    # append new move
                                    pieza.add_move(move)
                            else:
                                # append new move
                                pieza.add_move(move)


        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Casilla.in_range(possible_move_row, possible_move_col):
                    if self.casillas[possible_move_row][possible_move_col].isempty_or_enemy(pieza.color):
                        # create casillas of the new move
                        initial = Casilla(row, col)
                        final_pieza = self.casillas[possible_move_row][possible_move_col].pieza
                        final = Casilla(possible_move_row, possible_move_col, final_pieza)
                        # create new move
                        move = Move(initial, final)
                        
                        # check potencial checks
                        if bool:
                            if not self.in_check(pieza, move):
                                # append new move
                                pieza.add_move(move)
                            else: break
                        else:
                            # append new move
                            pieza.add_move(move)

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Casilla.in_range(possible_move_row, possible_move_col):
                        # create casillas of the possible new move
                        initial = Casilla(row, col)
                        final_pieza = self.casillas[possible_move_row][possible_move_col].pieza
                        final = Casilla(possible_move_row, possible_move_col, final_pieza)
                        # create a possible new move
                        move = Move(initial, final)

                        # empty = continue looping
                        if self.casillas[possible_move_row][possible_move_col].isempty():
                            # check potencial checks
                            if bool:
                                if not self.in_check(pieza, move):
                                    # append new move
                                    pieza.add_move(move)
                            else:
                                # append new move
                                pieza.add_move(move)

                        # has enemy pieza = add move + break
                        elif self.casillas[possible_move_row][possible_move_col].has_enemy_pieza(pieza.color):
                            # check potencial checks
                            if bool:
                                if not self.in_check(pieza, move):
                                    # append new move
                                    pieza.add_move(move)
                            else:
                                # append new move
                                pieza.add_move(move)
                            break

                        # has team pieza = break
                        elif self.casillas[possible_move_row][possible_move_col].has_team_pieza(pieza.color):
                            break
                    
                    # not in range
                    else: break

                    # incrementing incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def Rey_moves():
            adjs = [
                (row-1, col+0), # up
                (row-1, col+1), # up-right
                (row+0, col+1), # right
                (row+1, col+1), # down-right
                (row+1, col+0), # down
                (row+1, col-1), # down-left
                (row+0, col-1), # left
                (row-1, col-1), # up-left
            ]

            # normal moves
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Casilla.in_range(possible_move_row, possible_move_col):
                    if self.casillas[possible_move_row][possible_move_col].isempty_or_enemy(pieza.color):
                        # create casillas of the new move
                        initial = Casilla(row, col)
                        final = Casilla(possible_move_row, possible_move_col) # pieza=pieza
                        # create new move
                        move = Move(initial, final)
                        # check potencial checks
                        if bool:
                            if not self.in_check(pieza, move):
                                # append new move
                                pieza.add_move(move)
                            else: break
                        else:
                            # append new move
                            pieza.add_move(move)

            # castling moves
            if not pieza.moved:
                # Reina castling
                left_rook = self.casillas[row][0].pieza
                if isinstance(left_rook, Torre):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            # castling is not possible because there are piezas in between ?
                            if self.casillas[row][c].has_pieza():
                                break

                            if c == 3:
                                # adds left rook to Rey
                                pieza.left_rook = left_rook

                                # rook move
                                initial = Casilla(row, 0)
                                final = Casilla(row, 3)
                                moveR = Move(initial, final)

                                # Rey move
                                initial = Casilla(row, col)
                                final = Casilla(row, 2)
                                moveK = Move(initial, final)

                                # check potencial checks
                                if bool:
                                    if not self.in_check(pieza, moveK) and not self.in_check(left_rook, moveR):
                                        # append new move to rook
                                        left_rook.add_move(moveR)
                                        # append new move to Rey
                                        pieza.add_move(moveK)
                                else:
                                    # append new move to rook
                                    left_rook.add_move(moveR)
                                    # append new move Rey
                                    pieza.add_move(moveK)

                # Rey castling
                right_rook = self.casillas[row][7].pieza
                if isinstance(right_rook, Torre):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            # castling is not possible because there are piezas in between ?
                            if self.casillas[row][c].has_pieza():
                                break

                            if c == 6:
                                # adds right rook to Rey
                                pieza.right_rook = right_rook

                                # rook move
                                initial = Casilla(row, 7)
                                final = Casilla(row, 5)
                                moveR = Move(initial, final)

                                # Rey move
                                initial = Casilla(row, col)
                                final = Casilla(row, 6)
                                moveK = Move(initial, final)

                                # check potencial checks
                                if bool:
                                    if not self.in_check(pieza, moveK) and not self.in_check(right_rook, moveR):
                                        # append new move to rook
                                        right_rook.add_move(moveR)
                                        # append new move to Rey
                                        pieza.add_move(moveK)
                                else:
                                    # append new move to rook
                                    right_rook.add_move(moveR)
                                    # append new move Rey
                                    pieza.add_move(moveK)

        if isinstance(pieza, Peon): 
            Peon_moves()

        elif isinstance(pieza, Caballo): 
            knight_moves()

        elif isinstance(pieza, Alfil): 
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])

        elif isinstance(pieza, Torre): 
            straightline_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
            ])

        elif isinstance(pieza, Reina): 
            straightline_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1) # left
            ])

        elif isinstance(pieza, Rey): 
            Rey_moves()

    def _create(self):
        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                self.casillas[fila][columna] = Casilla(fila,columna)

    def _add_piezas(self,color):
        fila_peon, fila_Opiezas = (6,7) if color == 'B'else (1,0)
    
        #Peones
        for col in range (COLUMNAS):
            self.casillas[fila_peon][col] = Casilla(fila_peon, col, Peon(color))

        #Caballos (D = (0,1) y (0,6)) o (B = (7,1) y (7,6)) 
        self.casillas[fila_Opiezas][1] = Casilla(fila_Opiezas, 1, Caballo(color))
        self.casillas[fila_Opiezas][6] = Casilla(fila_Opiezas, 6, Caballo(color))

        #Alfil (D = (0,2) y (0,5)) o (B = (7,2) y (7,5)) 
        self.casillas[fila_Opiezas][2] = Casilla(fila_Opiezas, 2, Alfil(color))
        self.casillas[fila_Opiezas][5] = Casilla(fila_Opiezas, 5, Alfil(color))

        #Torres (D = (0,0) y (0,7)) o (B = (7,0) y (7,7)) 
        self.casillas[fila_Opiezas][0] = Casilla(fila_Opiezas, 0, Torre(color))
        self.casillas[fila_Opiezas][7] = Casilla(fila_Opiezas, 7, Torre(color))

        #Reina D = (0,3) o (B = (7,3)
        self.casillas[fila_Opiezas][3] = Casilla(fila_Opiezas, 3, Reina(color))

        #Rey D = (0,4) o (B = (7,4) 
        self.casillas[fila_Opiezas][4] = Casilla(fila_Opiezas, 4, Rey(color))
