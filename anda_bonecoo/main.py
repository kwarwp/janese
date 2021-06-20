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
        self.bonequinha = bonequinha(self.fundo, 1)
        self.bonequinha = bonequinha(self.fundo)
        self.comeca()
        
    def vai(self):
        self.fundo.vai()

class Persona_control:
""" Constrói um boneco que se movimenta com clique no joystick

nome_do_elemento = Elemento(MEU_ELEMENTO, 
                            h=xx , w=xx,
                            x=xx, y=xx, cena= nome_da_cena, vai=funcao)    
    
"""
    def __init__(self, fundo, ):
        self.x = x
        self.y = y
        self.persona = Elemento(PERSONAGEM, h=250 , w=250, x=self.x, y=self.y)
        self.boneca.vai = self.equacao1
        self.persona.entra(fundo)

    def anda():
        pass
        
if __name__ == "__main__":  
    Quadro().vai()