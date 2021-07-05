# janese.adda.main.py
#Bianca
#Ada Lovelace

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://i.imgur.com/KYKStgT.png"
PERSONAGEM = "https://imgur.com/7qQzMJb.png"

STYLE["width"]=1200
STYLE["height"]=620

class inicial():

    def __init__(self):
        self.x1 = 0
        self.y1 = 500
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=50, w=50)
        document.bind("keydown", self.andapersonagem)
        
        
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