class GameState():

    def __init__(self) -> None:
        self.piezas = [
        ["TD","CD","AD","QD","KD","AD","CD","TD"], #x0
        ["PD","PD","PD","PD","PD","PD","PD","PD"], #x1
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["PB","PB","PB","PB","PB","PB","PB","PB"],
        ["TB","CB","AB","QB","KB","AB","CB","TB"],
        ]
    def imprimir_Tablero(self):
        for x in self.piezas:
            print(x)
        

class Peon():
    def __init__(self):
        self.Tipo = "PD"
        self.posiX = 0
        self.posiY = 0
        self.color = "N"
    def mover(self):
        self.posiX+=0
        self.posiY+=1
    def comer(self,Enemigo):
        if(self.color !=Enemigo.color):
            if(self.posiX+1==Enemigo.posiX or self.posiX-1==Enemigo.posiX ):
                if(self.posiY+1==Enemigo.posiY or self.posiY-1==Enemigo.posiY ):
                    self.posiX=Enemigo.posiX
                    self.posiY=Enemigo.posiY
    def getTipo(self):
        return self.posiX
    def __str__(self):
        return self.Tipo

peon1 = Peon()
print(peon1.getTipo())

juego = GameState()
juego.imprimir_Tablero()