# janese.sarah.main.py
#Helena Pacheco

from_spy.vitollino.main import Cena, Elemento, STYLE
from brownser import document

FUNDO = "https://imgur.com/gallery/SJ4CR6x"
PERSONAGEM = "https://imgur.com/gallery/kiO6u4F"

STYLE["wedth"]=500
STYLE["height"]= 200

class inicial():
  def init(self):
        self.x1 = 0
        self.y1 = 500
        self.fundo = Cena(FUNDO)
self.personagem=Elemento(img=PERSONAGEM, cena=self.fundo)

  def vai(self):
  self.fundo.vai()


if __name__== "__main__":
inicial().vai()