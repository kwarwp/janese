# janese.danae.main.py
#Lilian Esquinelato

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document 

FUNDO = "https://i.imgur.com/73J8HqZ.png"
PERSONAGEM = "https://imgur.com/0Zyn3IL.png"

STYLE["width"]=500
STYLE["height"]=120

class inicial():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=0, y=100)
        
    def vai(self):
        self.fundo.vai()
        
        
        
if __name__ == "__main__":
    inicial().vai()