# janese.adda.main.py
#Bianca
#Ada Lovelace

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://i.imgur.com/KYKStgT.png"
PERSONAGEM = "https://i.imgur.com/Jo5Ho94.png"
FOLHA = "https://i.imgur.com/upAN1GX.png"

STYLE["width"]=1150
STYLE["height"]=520

class inicial():

    def __init__(self):
        self.x1 = 0
        self.y1 = 460
        self.fundo = Cena(FUNDO)
        self.folha()
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
        document.bind("keydown", self.andapersonagem)
    def folha(self):    
        self.x2 = 0
        self.y2 = 500
        self.fundo = Cena(FUNDO)
        self.folha = Elemento(img = FOLHA, cena = self.fundo, h=80, w=80)
        
        
    def vai(self):
        self.fundo.vai()
        
    def andapersonagem(self, ev=None):
        teclado = ev.keyCode
        
        if teclado in [37,39]:
            teclado = (teclado - 38) * 10
            self.personagem.x = self.personagem.x + teclado
            
        elif teclado in [38, 40]:
            teclado = (teclado - 39) * 10
            self.personagem.y = self.personagem.y + teclado
        
        
if __name__ == "__main__":
    inicial().vai()