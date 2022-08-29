import pygame

class Main:

    def __init__(self, size_cuadrado):
        self.gs = Funcionamiento.GameState()
        self.size_cuadrado = size_cuadrado
        self.imagenes = { } 

        self.partida = tkinter.Tk()
        self.partida.title("Ventana de partida")
        self.partida.geometry(f"{str(size_cuadrado*8)}x{str(size_cuadrado*8)}" )


        self.interfaz = tkinter.Canvas(self.partida)
        self.interfaz.pack(fill="both", expand = True)