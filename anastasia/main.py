#Profa Gi :)

from _spy.vitolino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://imgur.com/bg1h3oD.png"
PERSONAGEM = "https://imgur.com/7qQzMJb.png"

class inicial():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo)
        
    def vai(self):
        self.fundo.vai()
        
        
if __name__ == "__manin__":
    inicial().vai()