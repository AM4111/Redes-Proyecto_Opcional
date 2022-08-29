import pygame
import button
from partida import Partida 
import os
import sys

pygame.init()

clock=pygame.time.Clock()

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
User_img = pygame.image.load('PO/Imagenes/U.png').convert_alpha()
Pass_img = pygame.image.load('PO/Imagenes/P.png').convert_alpha()
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

usuario = button.Button(275, 47, User_img, 1)
password = button.Button(400, 125, Pass_img, 1)
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

#create input instances
user_text = ''
password_text = ''

input_recuser = pygame.Rect(200,200,140,32)
input_recpass = pygame.Rect(200,200,140,32)

def draw_input(ptext,prect_input):
  text = font.render(ptext,True,TEXT_COL)
  screen.blit(text, (prect_input.x+5,prect_input.y + 5))

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
      draw_text("Usuario:", font, TEXT_COL, 40, 50)
      draw_text("Constraseña:", font, TEXT_COL, 40, 125)

      if usuario.draw(screen):
        print("pez vol user")
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ENTER:
              user_text = user_text[:-1]
            else:
              user_text += event.unicode
        print("pez vol user", user_text)

        draw_input(user_text,input_recuser)

      if password.draw(screen):
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ENTER:
              password_text = password_text[:-1]
            else:
              password_text += event.unicode

        draw_input(password_text,input_recpass)

      #draw pause screen buttons
      if back_button.draw(screen):
        menu_state = "Login"
      if nuevaPartida_button.draw(screen):
        partida = Partida()
        partida.mainloop()
        print("nueva Partida")

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
  clock.tick(60)

pygame.quit()

