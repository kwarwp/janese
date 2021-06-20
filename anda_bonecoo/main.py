# janese.anda_bonecoo.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

PERSONAGEM = "https://imgur.com/gfe9a1S.png"
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
        self.bonequinha = Persona_control(self.fundo)        

        #self.cima = Elemento(PERSONAGEM, h=100 , w=100, x=10, y=430, cena= self.fundo)
        #self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, cena= self.fundo)
        #self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=530, cena= self.fundo)
        #self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490, cena= self.fundo)
        #self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, cena= self.fundo)

        
    def vai(self):
        self.fundo.vai()
        
class Persona_control:

    def __init__(self, fundo):
        self.x = 10
        self.y = 430 
        
        self.persona = Elemento(PERSONAGEM, h=100 , w=100, x=self.x, y=self.y)
        self.persona.entra(fundo)
        
        self.persona.x = self.x
        self.persona.y = self.y
        
        
        self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, vai=self.anda_cima)
        self.cima.entra(fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=530, vai=self.anda_baixo)
        self.baixo.entra(fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490,vai=self.anda_direita)
        self.direita.entra(fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, vai=self.anda_esquerda)
        self.esquerda.entra(fundo)

    def anda_direita():
        self.persona.x = self.x = self.x + 10

    def anda_esquerda():
        self.persona.x = self.x = self.x - 10
        
    def anda_cima():
        self.persona.y = self.y = self.y + 10
        
    def anda_baixo():
        self.persona.y = self.y = self.y - 10

if __name__ == "__main__":  
    Quadro().vai()