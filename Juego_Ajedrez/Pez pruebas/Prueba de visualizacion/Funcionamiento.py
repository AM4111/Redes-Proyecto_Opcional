import posix
from this import d


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
        
    def mover_Ficha(self,intx,inty,nextx,nexty):
        if()

class Peon():
    def __init__(self):
        nombre= ""
        posiX = 0
        posiY = 0
        color = "N"
    def mover(self):
        posiX+=0
        posiY+=1
    def comer(self,Enemigo):
        if(self.color !=Enemigo.color):
            if(self.posiX+1==Enemigo.posiX or self.posiX-1==Enemigo.posiX ):
                if(self.posiY+1==Enemigo.posiY or self.posiY-1==Enemigo.posiY ):
                    self.posiX=Enemigo.posiX
                    self.posiY=Enemigo.posiY



