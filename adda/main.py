# janese.adda.main.py
#Bianca
#Ada Lovelace

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://i.imgur.com/KYKStgT.png"
PERSONAGEM1 = "https://i.imgur.com/Sr5zj5S.png"
PERSONAGEM2 = "https://i.imgur.com/Jo5Ho94.png"
PERSONAGEM3 = "https://i.imgur.com/CPhpGhM.png"

STYLE["width"]=1150
STYLE["height"]=520

class inicial():

    def __init__(self):
        self.x1 = 0
        self.y1 = 460
        self.fundo = Cena(FUNDO)
        self.personagem1 = Elemento(img = PERSONAGEM1, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
        document.bind("keydown", self.andapersonagem)
    def inicio(self):
        self.x1 = 0
        self.y1 = 460
        self.fundo = Cena(FUNDO)
        self.personagem3 = Elemento(img = PERSONAGEM3, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
        document.bind("keydown", self.andapersonagem)
        
    def vai(self):
        self.fundo.vai()
        
    def andapersonagem(self, ev=None):
        teclado = ev.keyCode
        
        if teclado in [37,39]:
            teclado = (teclado - 38) * 10
            self.personagem2.x = self.personagem2.x + teclado
            
        elif teclado in [38, 40]:
            teclado = (teclado - 39) * 10
            self.personagem2.y = self.personagem2.y + teclado
        
        
if __name__ == "__main__":
    inicial().vai()