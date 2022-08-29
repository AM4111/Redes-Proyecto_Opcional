
import tkinter
import Funcionamiento
from tkinter import *

class Partida ():
    def __init__(self, size_cuadrado):
        self.gs = Funcionamiento.GameState()
        self.size_cuadrado = size_cuadrado
        self.imagenes = { } 

        self.partida = tkinter.Tk()
        self.partida.title("Ventana de partida")
        self.partida.geometry(f"{str(size_cuadrado*8)}x{str(size_cuadrado*8)}" )


        self.interfaz = tkinter.Canvas(self.partida)
        self.interfaz.pack(fill="both", expand = True)
 
    def __call__(self):
        self.partida.mainloop()

    def Tablero(self):
        for i in range (8):
            for j in range (8):
                if (i+j)%2==0:
                    self.interfaz.create_rectangle(i*self.size_cuadrado, j*self.size_cuadrado,(i+1)*self.size_cuadrado, (j+1)*self.size_cuadrado, fill='#aedddd')
                else:
                    self.interfaz.create_rectangle(i*self.size_cuadrado, j*self.size_cuadrado,(i+1)*self.size_cuadrado, (j+1)*self.size_cuadrado, fill='#FBFBE4')

    def CargarImagenes (self):
        piezas = ["AB","AD","CB","CD","TD","TB","KD","KB","QD","QB","PD","PB" ]
        for pieza in piezas:
            self.imagenes [pieza] = tkinter.PhotoImage(file = "Imagenes/"+ pieza + ".png") 

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j != "--":
                    self.interfaz.create_image(indice_j*self.size_cuadrado, indice_i*self.size_cuadrado, image = self.imagenes[j], anchor= "nw")




Ajedrez = Partida(70)
Ajedrez.Tablero()
Ajedrez.CargarImagenes()
Ajedrez.mostrarPiezas()
Ajedrez()
