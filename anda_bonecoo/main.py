# janese.anda_bonecoo.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

BONEQUINHA = "https://imgur.com/gfe9a1S.png"
FUNDO = "https://imgur.com/vaUUL1h.jpg"
MARCADOR_ESQUERDA = "https://imgur.com/hEF8XPG.png"
MARCADOR_DIREITA = "https://imgur.com/hEF8XPG.png"
MARCADOR_CIMA = "https://imgur.com/hEF8XPG.png"
MARCADOR_BAIXO = "https://imgur.com/hEF8XPG.png"


STYLE["width"] = 900
STYLE["heigth"] = 900

class Quadro:
    def __init__(self,*_):   
        self.fundo = Cena(FUNDO) 
        self.bonequinha = bonequinha(self.fundo, 1)
        self.bonequinha = bonequinha(self.fundo)
        self.comeca()
        
    def comeca(self, *_):
        self.bonequinha.x = 200
        self.mais = Texto(self.fundo, txt = "Clique aqui", foi=self.foi, A="-1,3655", B="-4")
        self.mais.vai()
    
        
    def foi(self,opcao):
        self.bonequinha.a = self.cf [opcao]
        self.bonequinha.x = 200
        self.bonequinha.y = 620
        self.bonequinha.aparece()
        self.cf = dict(A = "(2,3)")

    def vai(self):
        self.fundo.vai()

class Joystick:

    def __init__(self):
        pass
        
    def anda():
        pass
        
if __name__ == "__main__":  
    Quadro().vai()