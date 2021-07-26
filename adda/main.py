# janese.adda.main.py
#Bianca
#Ada Lovelace

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document

FUNDO = "https://i.imgur.com/KYKStgT.png"
PERSONAGEM = "https://imgur.com/E6lSl7l.gif"
FOLHA = "https://i.imgur.com/upAN1GX.png"
PENA = "https://i.imgur.com/916QFLA.png"
MARCADOR_X = "https://imgur.com/kJ2MkuK.png"
MARCADOR_DIREITA = "https://imgur.com/GTnLEnS.png"
MARCADOR_ESQUERDA = "https://imgur.com/Nl7Qy9h.png"
MARCADOR_CIMA = "https://imgur.com/f2zfcvx.png"
MARCADOR_BAIXO = "https://imgur.com/QDx4zgx.png"


STYLE["width"]=1350
STYLE["height"]=720

def teste():
    fundo = Cena(FUNDO) 
    fundo.vai()
    bonequinha = Persona_control( fundo) 
        
class Persona_control:
    """ Cria um elemento que anda a partir do clique no joystick
    
        self.nome_do_elemento = Persona_control( nome_do_fundo)
        
        :param nome_do_fundo: Insere o personagem em um fundo pré-criado
        
    """
    def __init__(self, nome_do_fundo):
        self.x = 10 # valor pré-estabelecido do x
        self.y = 430 # valor pré-estabelecido do y
        
        #self.persona.x = self.x
        #self.persona.y = self.y
        
        """self.joystickfalso = Elemento(JOYSTICK_FALSO, h=100 , w=100, x=750, y=440) #cria um elemento posicionado 'acima' no joystick
        self.joystickfalso.entra(nome_do_fundo)"""
        
        self.marcadorx = Elemento(MARCADOR_X, h=70 , w=70, x=80, y=450) #cria um elemento posicionado 'acima' no joystick
        self.marcadorx.entra(nome_do_fundo)
        
        self.cima = Elemento(MARCADOR_CIMA, h=80 , w=80, x=1180, y=410, vai=self.anda_cima) #cria um elemento posicionado 'acima' no joystick
        self.cima.entra(nome_do_fundo)
        
        self.baixo = Elemento(MARCADOR_BAIXO, h=80 , w=80, x=1180, y=560, vai=self.anda_baixo) #cria um elemento posicionado 'abaixo' no joystick
        self.baixo.entra(nome_do_fundo)
        
        self.direita = Elemento(MARCADOR_DIREITA, h=80 , w=80, x=1100, y=490,vai=self.anda_direita) #cria um elemento posicionado 'à direita' no joystick
        self.direita.entra(nome_do_fundo)
        
        self.esquerda = Elemento(MARCADOR_ESQUERDA, h=80 , w=80, x=1200, y=490, vai=self.anda_esquerda) #cria um elemento posicionado 'à esquerda' no joystick
        self.esquerda.entra(nome_do_fundo)
        
        self.persona = Elemento(PERSONAGEM, h=170 , w=190, x=self.x, y=self.y) # cria Elemento 
        self.persona.entra(nome_do_fundo) # utiliza o método entra() da classe Elemento para não ter que criar um atributo cena para a classe persona_control 
        



    def anda_direita(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'direita' é clicado.
        """
        self.persona.x = self.x = self.x - 10
        #self.persona.x = self.x - 10 > Deixar para averiguações posteriores
        #self.persona.x = self.x -= 10 > Deixar para averiguações posteriores
        
    def anda_esquerda(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'esquerda' é clicado.
        """
        self.persona.x = self.x = self.x + 10
        
    def anda_cima(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'em cima' é clicado.
        """
        self.persona.y = self.y = self.y - 10
        
    def anda_baixo(self,*_):
        """Este método guarda a expressão de movimentação do elemento quando o botão 'embaixo' é clicado.
        """
        self.persona.y = self.y = self.y + 10

if __name__ == "__main__":  
    teste()


