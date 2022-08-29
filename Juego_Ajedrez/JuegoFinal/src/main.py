# author - base : Coding With Russ Tutorial video Pygame Menu 
# Modifications: Group

import pygame
import button
import os

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crazzy Chess")

#game variables
game_paused = False
menu_state = "Login"

#define fonts
font = pygame.font.SysFont("arialblack", 50)

#define colours
TEXT_COL = (255, 255, 228)

#load button images
NU_img = pygame.image.load('PO/Imagenes/NU.png').convert_alpha()
loggin_img = pygame.image.load('PO/Imagenes/LU.png').convert_alpha()
nuevaPartida_img = pygame.image.load('PO/Imagenes/NP.png').convert_alpha()
cargarPartida_img = pygame.image.load('PO/Imagenes/CP.png').convert_alpha()
resume_img = pygame.image.load('PO/Imagenes/button_resume.png').convert_alpha()
options_img = pygame.image.load("PO/Imagenes/button_options.png").convert_alpha()
quit_img = pygame.image.load("PO/Imagenes/button_quit.png").convert_alpha()
video_img = pygame.image.load('PO/Imagenes/button_video.png').convert_alpha()
audio_img = pygame.image.load('PO/Imagenes/button_audio.png').convert_alpha()
keys_img = pygame.image.load('PO/Imagenes/button_keys.png').convert_alpha()
back_img = pygame.image.load('PO/Imagenes/button_back.png').convert_alpha()

#create button instances

nuevo_usuario = button.Button(250, 300, NU_img, 1)
loggin = button.Button(250, 150, loggin_img, 1)
nuevaPartida_button = button.Button(204, 225, nuevaPartida_img, 1)
cargarPartida_button = button.Button(197, 325, cargarPartida_img, 1)
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  if(x!=0):
    screen.blit(img, (x,y))
  else:
    screen.blit(img, img.get_rect(center = screen.get_rect().center))

#game loop
run = True
while run:

  screen.fill((174, 221, 221))

  #check if game is paused
  if game_paused == True:
    ##-----------------------------------------------------------
    ##              lOGIN
    ##-----------------------------------------------------------
    if menu_state == "Login":
      if nuevo_usuario.draw(screen):
        menu_state = "UsuarioNuevo"
      if loggin.draw(screen):
        menu_state = "Usuario"

    ##-----------------------------------------------------------
    ##              Usuario Invitado
    ##-----------------------------------------------------------
    if menu_state == "UsuarioNuevo":
      draw_text("Cargando Partida ...", font, TEXT_COL, 160, 150)
      if back_button.draw(screen):
        menu_state = "Login"
    ##-----------------------------------------------------------
    ##              Usuario Ya registrado
    ##-----------------------------------------------------------
    if menu_state == "Usuario":
      draw_text("Usuario:", font, TEXT_COL, 100, 75)
      draw_text("Constraseña:", font, TEXT_COL, 100, 125)
      #draw pause screen buttons
      if back_button.draw(screen):
        menu_state = "Login"
      if nuevaPartida_button.draw(screen):
        print("Nueva Partida")
      if cargarPartida_button.draw(screen):
        print("Cargar Partida")

    ##-----------------------------------------------------------
    ##              Usuario MAIN
    ##-----------------------------------------------------------

    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False

    ##-----------------------------------------------------------
    ##              Options
    ##-----------------------------------------------------------
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        menu_state = "Usuario"
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"

  else:
    draw_text("Crassy Chess", font, TEXT_COL, 0,0)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

