# janese.liesquinelato.main.py
# aqui é a Lilian

from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://imgur.com/7hpkeNU.png"
#CIMA = "https://imgur.com/9cZpb4V.png"
#LABIRINTO = "https://imgur.com/OkOhvxf.png"
BONEQUINHA = "https://imgur.com/gfe9a1S.png"

STYLE["width"] = 1200
STYLE["heigth"] = 900

class inicial():
    def __init__(self):
        self.x = -50
        self.y = 200
        self.fundo = Cena(FUNDO)
        self.bonequinha = Elemento(img = BONEQUINHA, cena = self.fundo, x=-50, y=200, h=200, w=200)
    def vai(self):
        self.fundo.vai()
                
if __name__ == "__main__":  
    inicial().vai()     