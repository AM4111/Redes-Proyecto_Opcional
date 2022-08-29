import pygame
import sys

from constante import *
from game import Game
from casilla import Casilla
from movimiento import Move

class Partida:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (AnchoTablero, AlturaTablero) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    """ def mainloop(self):
        
        screen = self.screen
        game = self.game
        tablero = self.game.tablero
        dragger = self.game.dragger

        while True:
            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_piezas(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // TamannoCasilla
                    clicked_col = dragger.mouseX // TamannoCasilla

                    # if clicked casilla has a pieza ?
                    if tablero.casillas[clicked_row][clicked_col].has_pieza():
                        pieza = tablero.casillas[clicked_row][clicked_col].pieza
                        # valid pieza (color) ?
                        if pieza.color == game.next_player:
                            tablero.calc_moves(pieza, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_pieza(pieza)
                            # show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_piezas(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // TamannoCasilla
                    motion_col = event.pos[0] // TamannoCasilla

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_piezas(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // TamannoCasilla
                        released_col = dragger.mouseX // TamannoCasilla

                        # create possible move
                        initial = Casilla(dragger.initial_row, dragger.initial_col)
                        final = Casilla(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if tablero.valid_move(dragger.pieza, move):
                            # normal capture
                            captured = tablero.casillas[released_row][released_col].has_pieza()
                            tablero.move(dragger.pieza, move)

                            tablero.set_true_en_passant(dragger.pieza)                            

                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_piezas(screen)
                            # next turn
                            game.next_turn()
                    
                    dragger.undrag_pieza()
                
                # key press
                elif event.type == pygame.KEYDOWN:
                    
                    # changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                     # changing themes
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        tablero = self.game.tablero
                        dragger = self.game.dragger

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update() """


    def mainloop(self):
        game = self.game
        screen = self.screen
        #dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_piezas(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Partida()
main.mainloop()