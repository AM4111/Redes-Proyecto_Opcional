import pygame
import sys

from const import *
from game import Game

#create game window
SCREEN_WIDTH = WIDTH+350
SCREEN_HEIGHT = HEIGHT

class Partida:

    def __init__(self):
        pygame.init()
        #self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
        pygame.display.set_caption('Chess')
        self.game = Game()


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
   

#main = Partida()
#main.mainloop()