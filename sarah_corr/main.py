# janese.sarah_corr.main.py
# janese.sarah.main.py
#Helena Pacheco

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://imgur.com/DPM4HbC.png"
PERSONAGEM = "https://imgur.com/azAG8JJ.png"

STYLE["wedth"]= 40000
STYLE["height"]= 50000

class inicial():
    def _init_(self):
        self.x1 = 0
        self.y1 = 500
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=50, w=50)
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



if _name_ == "_main_":
    inicial().vai()