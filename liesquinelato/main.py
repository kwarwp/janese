# janese.liesquinelato.main.py
# aqui é a Lilian

from _spy.vitollino.main import Cena, Elemento, STYLE

FUNDO = "https://imgur.com/7hpkeNU"
#CIMA = "https://imgur.com/9cZpb4V"
#LABIRINTO = "https://imgur.com/OkOhvxf"
BONEQUINHA = "https://imgur.com/gfe9a1S.png"


class inicial():
    def __init__(self):
        self.fundo = Cena(FUNDO)
        self.bonequinha = Elemento(BONEQUINHA, x=230, y=620)
        
if __name__ == "__main__":  
    inicial().vai()     