#Profa Gi :)

from _spy.vitolino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://imgur.com/bg1h3oD.png"
PERSONAGEM = "https://imgur.com/7qQzMJb.png"

#STYLE["width"]=500
#STYLE["height"]=120

class inicial():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=0, y=500)
        document.bind("keydown", self.andapersonagem)
        
        
    def vai(self):
        self.fundo.vai()
        
    #def andapersonagem(self, ev=None):
        
        
if __name__ == "__main__":
    inicial().vai()