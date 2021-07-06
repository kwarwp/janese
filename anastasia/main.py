#Profa Gi :)

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://imgur.com/bg1h3oD.png"
PERSONAGEM = "https://imgur.com/1b13SPC.png"
PERSONAGEM_ANDANDO = "https://imgur.com/KCLilyv.png"

STYLE["width"]=1150
STYLE["height"]=550

class inicial():

    def __init__(self):
        self.x1 = 1000
        self.y1 = 400
        self.fundo = Cena(FUNDO)
        self.personagem = Elemento(img = PERSONAGEM, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
        self.personagem_andando = Elemento(img = PERSONAGEM_ANDANDO, cena = self.fundo, x=self.x1, y=self.y1, h=100, w=100)
        document.bind("keydown", self.andapersonagem)

        
        
    def vai(self):
        self.fundo.vai()
        
    def andapersonagem(self, ev=None):
        teclado = ev.keyCode
        
        if teclado in [37,39]:
            teclado = (teclado - 38) * 10
            self.personagem.x = self.personagem.x + teclado
            self.personagem_andando.x = self.personagem_andando.x + teclado
            self.personagem.opacity = 0
            
        elif teclado in [38, 40]:
            teclado = (teclado - 39) * 10
            self.personagem.y = self.personagem.y + teclado
        
        
if __name__ == "__main__":
    inicial().vai()