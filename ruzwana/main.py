# janese.ruzwana.main.py
#samantha

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document 

FUNDO = "https://imgur.com/AU7K7D4.png"
PERSONAGEM = "https://imgur.com/d6FSzPZ.png"
MARCADOR_X = "https://imgur.com/kJ2MkuK.png"
MARCADOR_DIREITA = "https://imgur.com/GTnLEnS.png"
MARCADOR_ESQUERDA = "https://imgur.com/Nl7Qy9h.png"
MARCADOR_CIMA = "https://imgur.com/f2zfcvx.png"
MARCADOR_BAIXO = "https://imgur.com/QDx4zgx.png"


STYLE["width"]=1250
STYLE["height"]=720

class inicial():
    def __init__(self):
        self.x1 = 0
        self.y1 = 500
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=130, w=110)
        document.bind("keydown", self.andapersonagem)

    def vai(self):
        self.fundo.vai()

    def andapersonagem(self, ev=None):
        teclado = ev.keyCode

        if teclado in [37, 39]:
            teclado = (teclado - 38) * 10 #podem modificar o valor do 10
            self.personagem.x = self.personagem.x + teclado

        elif teclado in [38, 40]:
            teclado = (teclado - 39) * 10
            self.personagem.y = self.personagem.y + teclado



if __name__ == "__main__":
    inicial().vai()