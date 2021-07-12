# janese.sarah.main.py
#Helena Pacheco

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://imgur.com/DPM4HbC.png"
PERSONAGEM = "https://imgur.com/azAG8JJ.png"

STYLE["wedth"]= 1000
STYLE["height"]= 400

class inicial():
    def __init__(self):
        self.x1 = 1000
        self.y1 = 500
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
        document.bind("keydown", self.andapersonagem)

    def vai(self):
        self.fundo.vai()

    def andapersonagem(self, ev=None):
        teclado = ev.keyCode

        if teclado in [37, 39]:
            teclado = (teclado - 38) * 20 #podem modificar o valor do 10
            self.personagem.x = self.personagem.x + teclado

        elif teclado in [38, 40]:
            teclado = (teclado - 39) * 10
            self.personagem.y = self.personagem.y + teclado



if __name__ == "__main__":
    inicial().vai()