import pygame

from constante import *
from tablero import Tablero
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Tablero()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(FILAS ):
            for col in range(COLUMNAS ):
                if (row + col) % 2 == 0:
                    color = (174, 221, 221)
                else:
                    color = (255, 255, 228)

                rect = (col * TamannoCasilla, row *TamannoCasilla, TamannoCasilla, TamannoCasilla)

                pygame.draw.rect(surface, color, rect)

    def show_piezas(self, surface):
        for row in range(FILAS ):
            for col in range(COLUMNAS ):
                #validacion de si existe pieza en el cuadrado
                if self.board.casillas[row][col].has_pieza():
                    piece = self.board.casillas[row][col].pieza

                    #crea la imagen 
                    img = pygame.image.load(piece.texture)
                    img_center = col * TamannoCasilla + TamannoCasilla // 2, row * TamannoCasilla + TamannoCasilla // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)



""" from tkinter.tix import COLUMN
import pygame

from constante import *
from tablero import Tablero
from dragger import Dragger
from configuracion import Config
from casilla import Casilla

class Game:

    def __init__(self):
        self.next_player = 'B'
        self.hovered_sqr = None
        self.tablero = Tablero()
        self.dragger = Dragger()
        self.config = Config()

    # blit methods

    def show_bg(self, surface):
        theme = self.config.theme
        
        for row in range(FILAS):
            for col in range(COLUMNAS):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # rect
                rect = (col * TamannoCasilla, row * TamannoCasilla, TamannoCasilla, TamannoCasilla)
                # blit
                pygame.draw.rect(surface, color, rect)

                # row coordinates
                if col == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(str(FILAS-row), 1, color)
                    lbl_pos = (5, 5 + row * TamannoCasilla)
                    # blit
                    surface.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    # label
                    lbl_pos = (col * TamannoCasilla+ TamannoCasilla- 20, AlturaTablero - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)

    def show_piezas(self, surface):
        for row in range(FILAS):
            for col in range(COLUMNAS):
                #validacion de si existe pieza en el cuadrado
                if self.tablero.casillas[row][col].has_pieza():
                    pieza = self.tablero.casillas[row][col].pieza

                    #crea la imagen 
                    img = pygame.image.load(pieza.texture)
                    img_center = col * TamannoCasilla + TamannoCasilla // 2, row * TamannoCasilla + TamannoCasilla // 2
                    pieza.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, pieza.texture_rect)

    def show_moves(self, surface):
        theme = self.config.theme

        if self.dragger.dragging:
            pieza = self.dragger.pieza

            # loop all valid moves
            for move in pieza.moves:
                # color
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                # rect
                rect = (move.final.col * TamannoCasilla, move.final.row * TamannoCasilla, TamannoCasilla, TamannoCasilla)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        theme = self.config.theme

        if self.tablero.last_move:
            initial = self.tablero.last_move.initial
            final = self.tablero.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.col * TamannoCasilla, pos.row * TamannoCasilla, TamannoCasilla, TamannoCasilla)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * TamannoCasilla, self.hovered_sqr.row * TamannoCasilla, TamannoCasilla, TamannoCasilla)
            # blit
            pygame.draw.rect(surface, color, rect, AnchoTablero=3)

    # other methods

    def next_turn(self):
        self.next_player = 'B' if self.next_player == 'D' else 'D'

    def set_hover(self, row, col):
        pass
        #self.hovered_sqr = self.tablero.casillas[row][col]

    def change_theme(self):
        self.config.change_theme()

    def reset(self):
        self.__init__() """