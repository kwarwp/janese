# janese.anda_boneco_refact.main.py
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
        self.bonequinha = Persona_control(PERSONAGEM, self.fundo)        
        
    def vai(self):
        self.fundo.vai()
        
class Persona_control:
    """ Cria um elemento que anda a partir do clique no joystick
    
        self.nome_do_elemento = Persona_control(nome_do_fundo, movi)
        :param variavel_personagem:Requisita o nome da variável que guarda o link do personagem
        :param nome_do_fundo: Insere o personagem em um fundo pré-criado
        :param h:
        :param w:
        :param movi: Determina a quantidade de movimento do personagem. Por padrão é 10
    """
    def __init__(self, variavel_personagem, nome_do_fundo, h =100, w=100, x=10, y=430, movi= 10):
        self.x = x
        self.y = y
        self.h = h 
        self.w = w 
        
        self.movi = movi 
        self.variavel_personagem = variavel_personagem
        
        self.persona = Elemento(self.variavel_personagem, h=self.h , w=self.w, x=self.x, y=self.y)
        self.persona.entra(nome_do_fundo)
        
        #self.persona.x = self.x
        #self.persona.y = self.y
        
        
        self.cima = Elemento(MARCADOR_CIMA, h=40 , w=40, x=780, y=450, vai=self.anda_cima)
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=40 , w=40, x=780, y=530, vai=self.anda_baixo)
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=40 , w=40, x=720, y=490,vai=self.anda_direita)
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=40 , w=40, x=840, y=490, vai=self.anda_esquerda)
        self.esquerda.entra(nome_do_fundo)

    def anda_direita(self,*_):
        """
        """
        self.persona.x = self.x = self.x - self.movi
        
    def anda_esquerda(self,*_):
        self.persona.x = self.x = self.x + self.movi
        
    def anda_cima(self,*_):
        self.persona.y = self.y = self.y - self.movi
        
    def anda_baixo(self,*_):
        self.persona.y = self.y = self.y + self.movi

if __name__ == "__main__":  
    Quadro().vai()