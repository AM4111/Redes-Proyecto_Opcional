import pygame

from constante import *

class Dragger:

    def __init__(self):
        self.pieza = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # blit method

    def update_blit(self, surface):
        # texture
        self.pieza.set_texture(size=128)
        texture = self.pieza.texture
        # img
        img = pygame.image.load(texture)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.pieza.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.pieza.texture_rect)

    # other methods

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)

    def save_initial(self, pos):
        self.initial_row = pos[1] // TamannoCasilla
        self.initial_col = pos[0] // TamannoCasilla

    def drag_pieza(self, pieza):
        self.pieza = pieza
        self.dragging = True

    def undrag_pieza(self):
        self.pieza = None
        self.dragging = False