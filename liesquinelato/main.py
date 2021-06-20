# janese.liesquinelato.main.py
# aqui é a Lilian

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document # importa o DOM para atribuir o evento de teclado

FUNDO = "https://imgur.com/7hpkeNU.png"
#CIMA = "https://imgur.com/9cZpb4V.png"
#LABIRINTO = "https://imgur.com/OkOhvxf.png"
BONEQUINHA = "https://imgur.com/gfe9a1S.png"

STYLE["width"] = 1200
STYLE["heigth"] = 900

class inicial():
    def __init__(self):
        self.x1 = -50
        self.y1 = 200
        self.fundo = Cena(FUNDO)
        self.bonequinha = Elemento(img = BONEQUINHA, cena = self.fundo, x=self.x1, y=self.y1, h=200, w=200)
        document.bind("keydown", self.andaboneca)  # captura o evento de teclado
    
    def vai(self):
        self.fundo.vai()
    
    def andaboneca(self, ev=None):
        teclado = ev.keyCode #chama o teclado
        
        # os códigos 37 e 38 são a seta para esquerda e para direita
        # os códigos 39 e 40 são a seta para cima e para baixo
        
        if teclado in [37, 39]:
            teclado = (teclado - 30) * 5
            self.bonequinha.x = self.bonequinha.x + teclado # muda a posição de mais um ou menos um
            
        elif teclado in [38, 40]:
            teclado = (teclado - 39) * 5
            self.bonequinha.y = self.bonequinha.y + teclado #muda a posição de mais um ou menos um

if __name__ == "__main__":  
    inicial().vai()     