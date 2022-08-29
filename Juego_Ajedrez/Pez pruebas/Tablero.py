import pygame

size_cuadrado = 70

class Game:

    def __init__(self) -> None:
        pass

    def Mostrar_Tablero(self):
        for i in range (8):
            for j in range (8):
                if (i+j)%2==0:
                    self.interfaz.create_rectangle(i*self.size_cuadrado, j*self.size_cuadrado,(i+1)*self.size_cuadrado, (j+1)*self.size_cuadrado, fill='#aedddd')
                else:
                    self.interfaz.create_rectangle(i*self.size_cuadrado, j*self.size_cuadrado,(i+1)*self.size_cuadrado, (j+1)*self.size_cuadrado, fill='#FBFBE4')