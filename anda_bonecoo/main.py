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
#        self.bonequinha = bonequinha(self.fundo, 1)
#        self.bonequinha = bonequinha(self.fundo)
#        self.comeca()

        #self.cima = Elemento(PERSONAGEM, h=100 , w=100, x=10, y=430, cena= self.fundo)
        #self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, cena= self.fundo)
        #self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=530, cena= self.fundo)
        #self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490, cena= self.fundo)
        #self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, cena= self.fundo)

        
    def vai(self):
        self.fundo.vai()
        
class Persona_control:

"""
Constrói um boneco que se movimenta com clique no joystick

nome_do_elemento = Elemento(MEU_ELEMENTO, 
                            h=xx , w=xx,
                            x=xx, y=xx, cena= nome_da_cena, vai=funcao)        
"""

    def __init__(self, fundo):
        self.x = 10
        self.y = 430        
        
        self.persona = Elemento(PERSONAGEM, h=100 , w=100, x=self.x, y=self.y, cena= self.fundo)
        self.persona.entra(fundo)
        self.persona.x = 10
        self.persona.y = 430
        
        
        self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, cena= self.fundo, vai=self.anda_cima)
        self.cima.entra(fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=530, cena= self.fundo, vai=self.anda_baixo)
        self.baixo.entra(fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490, cena= self.fundo,vai=self.anda_direita)
        self.direita.entra(fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, cena= self.fundo, vai=self.anda_esquerda)
        self.esquerda.entra(fundo)

    def anda_direita():
        pass
    def anda_esquerda():
        pass
    def anda_cima():
        pass
    def anda_baixo():
        pass

if __name__ == "__main__":  
    Quadro().vai()